from flask import Flask, jsonify
import asyncio
import aiohttp
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)


group_accounts = [
    {
      "6768403837": "AC8127538162E8F1FE13B64BC4AFC12CAE89A4091FE493F402BF83E9FE3D9AC1",
  "6768399558": "BC1642AA9674A50298D69D15117AC6E6A8F77FE4C0E382568145D5656DC9B725",
  "6768397802": "DC9DFB28A6FD0F3ED2CAB73AC8EA7C424CF10696FE8CE1E7AD50B5CDB70C6222",
  "6768371110": "8EED1456DA85F3DDD57CF91A7F00D7441BD345DF3028417D76068A365259C1F5",
  "6768369927": "EE2A40C67C91C8126C46E5A732182A909061DA84614918B418292A8DD095BB3B",
  "6768369420": "D0ED27713D729DABA28CACBE0A7683508ABDD54F19D4AADB45D5F8AFACC64893",
  "6768369315": "7E7C5E40BB28CBFADA8C88165A5C807D42507F0BFE2647C73846BD75EAC40D08",
  "6768523851": "19C8E4CC1259A346892D2C1F19CB5F1CCF96B131A1DABDCCBAE736DEBF2F5CAC",
  "6768523557": "335C52D571BD15AF6D52084387EA1D21BB3B53BE62B6E37CBDE18BF154B1E392",
  "6768520202": "EB3E978845A45BF0019DBC9DADBDD67E509C72086847BCCD710AACFC79637357",
  "6768521030": "3CC76F2E98198A57F8AA2E0860379BA4751597F540EE7B33768BE02329FF0EB4",
  "6179324155": "998F2071F098CB251ADD9BA1CFA4F09F31610890134781363FEEDE0C0132FBBF",
  "6179324479": "A5BDF12403FEC1031B38D960C32FEED214A63CD3086399332476291EB2B7DD12",
  "6179324446": "F7ABEEE466926B21DDC9658D53472CE016C5B9EE469051B908E47C26CA899DB5",
  "6179324434": "179EB150E8AB5C1F2079E13001A4B804BF7A2791E0407B7FF8A9094FBFD62A36",
  "5878090909": "857AC2F27E5A859F72A78F73FF05232EBE8236C933EABB33C60D1165658FB411",
  "5878089256": "8E4115B39FB2D3203712DC2F385AD1D47117099F6C00961C0E8A9C81A979B236",
  "5878089267": "3FA178FFF0C9D4A76736023EAB761C3036BDE6D2FE022C51E4B8985169F3EB4C",
  "5878089107": "B52C2277833F82EEBDD2574D8E409A5332D0B2BA25C350759D7C70DDB68AC8F9",
  "5695280395": "36D641370335C33124815AD9446D671761E22B0CEDDFC0B2CDF23AFE9FC613C0",
  "5695280350": "75F45C150842A602ECE27E9A223AC484192D1487EA00E422C14B8EEB81E4AC60",
  "5695280311": "5DB656AA2FC58845E272970C419DCD8F4BC54A0ABC8C4E0535FD4AA6D114D5F3",
  "5695280268": "7C08F234DB328FEDBDBE41521017940391D48E8D7B35A0C4CFD92135A38545E1",
  "5681192008": "395CB4D2B230C4BC89F706A0C0B8932AC45DE2C73737BEEBC7C05FE8E5874A0D",
  "5681191838": "1E54E7225595090C2CE130C6BBECCA4A8AAB8C976563BE62ACD1A64C783D88C3",
  "5681191901": "3B1468D20742829F146492EB625ED354AFBA50450D7F6C8AF37FBDB5073299DE",
  "5681191746": "956C24CD3B29932072AA444141F808D29E24F2DAF2ABFB6BE1BD3E79331C816B",
  "5673568400": "893E0CAE88B5285B167CEB5DD91FCFA0778A91A9556B28A5777B9153DEAA1D2D",
  "5673568409": "C9AD333C9D0FCC88B689F62B7AE4438D661C09CBF61D434DDF6F9CCDD0302D30",
  "5673568391": "E3C729412F72F573145CCB778FB2AACA0E801181146CF2132096AD2A26DE6D80",
  "5673568393": "85817FD21DFDAA5D19182E4C17FEA0471709FDC5FB4BE0BF6967354F51CA6EB4"          }
]
JWT_API_TEMPLATE = "https://jwt-tmk.vercel.app/GeneRate-Jwt?uid={uid}&password={password}"

CACHE = {
    "tokens": {},   # dict {uid: token}
    "timestamp": 0
}

COLLECTED_TOKENS = {}
GROUP_INDEX = 0  # مؤشر المجموعة الحالية

CACHE_DURATION = 10000  # ثانية
CONCURRENT_LIMIT = 50  # عدد الاتصالات المتزامنة

async def fetch_token(session, uid, password):
    url = JWT_API_TEMPLATE.format(uid=uid, password=password)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                token = data.get("token")
                if token:
                    return uid, token
            return uid, None
    except Exception as e:
        print(f"Error fetching token for uid {uid}: {e}")
        return uid, None

async def fetch_token_with_semaphore(semaphore, session, uid, password):
    async with semaphore:
        return await fetch_token(session, uid, password)

async def fetch_tokens_for_group(group):
    tokens = {}
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_token_with_semaphore(semaphore, session, uid, password)
                 for uid, password in group.items()]
        results = await asyncio.gather(*tasks)
        for uid, token in results:
            if token:
                tokens[uid] = token
    return tokens

def is_cache_valid():
    return (time.time() - CACHE["timestamp"]) < CACHE_DURATION and len(CACHE["tokens"]) > 0

def get_last_update_vn():
    utc_time = datetime.fromtimestamp(CACHE["timestamp"], tz=timezone.utc)
    vn_time = utc_time + timedelta(hours=7)
    return vn_time.strftime("%Y-%m-%d %H:%M:%S")

@app.route("/api/get_jwt", methods=["GET"])
def get_jwt_tokens():
    global GROUP_INDEX, COLLECTED_TOKENS

    if is_cache_valid():
        return jsonify({
            "count": len(CACHE["tokens"]),
            "last_update_vn": get_last_update_vn(),
            "tokens": CACHE["tokens"]
        })

    async def process_groups():
        global GROUP_INDEX
        groups_to_fetch = []

        # جلب الجروب الحالي
        groups_to_fetch.append(group_accounts[GROUP_INDEX])

        # جلب الجروب اللي بعده
        next_index = (GROUP_INDEX + 1) % len(group_accounts)
        if next_index != GROUP_INDEX:
            groups_to_fetch.append(group_accounts[next_index])

        all_tokens = {}
        for group in groups_to_fetch:
            tokens = await fetch_tokens_for_group(group)
            all_tokens.update(tokens)

        # تحديث المؤشر (+2 كل مرة)
        GROUP_INDEX = (GROUP_INDEX + 2) % len(group_accounts)

        return all_tokens

    new_tokens = asyncio.run(process_groups())
    COLLECTED_TOKENS.update(new_tokens)

    if GROUP_INDEX == 0:  # يعني خلصنا دورة كاملة
        CACHE["tokens"] = COLLECTED_TOKENS.copy()
        CACHE["timestamp"] = time.time()
        COLLECTED_TOKENS.clear()

    return jsonify({
        "count": len(COLLECTED_TOKENS) if not CACHE["tokens"] else len(CACHE["tokens"]),
        "last_update_vn": get_last_update_vn() if CACHE["tokens"] else None,
        "tokens": CACHE["tokens"] if CACHE["tokens"] else COLLECTED_TOKENS
    })
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
