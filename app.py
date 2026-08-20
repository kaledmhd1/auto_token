from flask import Flask, jsonify
import asyncio
import aiohttp
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)


group_accounts = [
{
      "6820365753": "H4RDIXx-BCEJ02-S_3_0_3",
  "6820365682": "H4RDIXx-LCJ0OZ-S_3_0_3",
  "6820365665": "H4RDIXx-MXNGJS-S_3_0_3",
  "6820365553": "H4RDIXx-0Z08KE-S_3_0_3",
  "6820365756": "H4RDIXx-CFTHEP-S_3_0_3",
  "6820365722": "H4RDIXx-J7CMZN-S_3_0_3",
  "6820365633": "H4RDIXx-DSVWOQ-S_3_0_3",
  "6820365758": "H4RDIXx-2WIZLW-S_3_0_3",
  "6820365747": "H4RDIXx-9UOH40-S_3_0_3",
  "6820365847": "H4RDIXx-CSUD2Z-S_3_0_3",
  "6820365549": "H4RDIXx-1LDIN6-S_3_0_3",
  "6820365797": "H4RDIXx-TUMDNF-S_3_0_3",
  "6820365686": "H4RDIXx-FA7R1N-S_3_0_3",
  "6820365922": "H4RDIXx-GAN04J-S_3_0_3",
  "6820365962": "H4RDIXx-GEODBN-S_3_0_3",
  "6820365947": "H4RDIXx-Y2IQIC-S_3_0_3",
  "6820366808": "H4RDIXx-K9D5UK-S_3_0_3",
  "6820366794": "H4RDIXx-6LPMAX-S_3_0_3",
  "6820366858": "H4RDIXx-SNZXTW-S_3_0_3",
  "6820366828": "H4RDIXx-IH6PXS-S_3_0_3",
  "6820366901": "H4RDIXx-RDOX4Y-S_3_0_3",
  "6820366842": "H4RDIXx-URVLHQ-S_3_0_3",
  "6820366937": "H4RDIXx-HYGLMV-S_3_0_3",
  "6820366954": "H4RDIXx-V96TMH-S_3_0_3",
  "6820366932": "H4RDIXx-IKKMLO-S_3_0_3",
  "6820366975": "H4RDIXx-5JPM1Q-S_3_0_3",
  "6820366886": "H4RDIXx-ZCPY6Q-S_3_0_3",
  "6820366998": "H4RDIXx-AJ3UZX-S_3_0_3",
  "6820367001": "H4RDIXx-GNMP3I-S_3_0_3",
  "6820366911": "H4RDIXx-5SMMFD-S_3_0_3",
  "6820366957": "H4RDIXx-SRKHEJ-S_3_0_3",
  "6820367094": "H4RDIXx-TSHIXH-S_3_0_3",
  "6820367015": "H4RDIXx-WE3DAT-S_3_0_3",
  "6820367046": "H4RDIXx-TET4AL-S_3_0_3",
  "6820366992": "H4RDIXx-PRGXEQ-S_3_0_3",
  "6820366931": "H4RDIXx-FQXI4H-S_3_0_3",
  "6820366848": "H4RDIXx-W4MLCZ-S_3_0_3",
  "6820367005": "H4RDIXx-4D8IPS-S_3_0_3",
  "6820367151": "H4RDIXx-SV2YBH-S_3_0_3",
  "6820367108": "H4RDIXx-U8XPXD-S_3_0_3",
  "6820366972": "H4RDIXx-CYT00B-S_3_0_3",
  "6820363717": "H4RDIXx-YPFYUL-S_3_0_3",
  "6820363733": "H4RDIXx-U7BFST-S_3_0_3",
  "6820363716": "H4RDIXx-FQE8GZ-S_3_0_3",
  "6820363744": "H4RDIXx-SZBBQX-S_3_0_3",
  "6820363791": "H4RDIXx-QK3SPO-S_3_0_3",
  "6820363688": "H4RDIXx-HG8WLO-S_3_0_3",
  "6820363694": "H4RDIXx-YYQUKR-S_3_0_3",
  "6820363704": "H4RDIXx-L4AFWU-S_3_0_3",
  "6820363722": "H4RDIXx-SOQOW0-S_3_0_3",
  "6820363686": "H4RDIXx-3MQZQR-S_3_0_3",
  "6820363720": "H4RDIXx-J6PAHF-S_3_0_3",
  "6820363809": "H4RDIXx-THABYA-S_3_0_3",
  "6820363739": "H4RDIXx-VTMSCD-S_3_0_3",
  "6820363727": "H4RDIXx-BTNHYE-S_3_0_3",
  "6820363730": "H4RDIXx-W4UNFZ-S_3_0_3",
  "6820363816": "H4RDIXx-NR0YHT-S_3_0_3",
  "6820363738": "H4RDIXx-EFRMNH-S_3_0_3",
  "6820363736": "H4RDIXx-TN7WAK-S_3_0_3",
  "6820363712": "H4RDIXx-QOSQER-S_3_0_3",
  "6820363745": "H4RDIXx-P2S7RJ-S_3_0_3",
  "6820363789": "H4RDIXx-ZJINYY-S_3_0_3",
  "6820363702": "H4RDIXx-CXDGAA-S_3_0_3",
  "6820363755": "H4RDIXx-TYG3B9-S_3_0_3",
  "6820363795": "H4RDIXx-HBXECK-S_3_0_3",
  "6820363697": "H4RDIXx-JUVMOL-S_3_0_3",
  "6820363723": "H4RDIXx-26ODO2-S_3_0_3",
  "6820363732": "H4RDIXx-BEWPP2-S_3_0_3",
  "6820363748": "H4RDIXx-4AUC2Y-S_3_0_3",
  "6820363699": "H4RDIXx-WHCU61-S_3_0_3",
  "6820363747": "H4RDIXx-AM2HB0-S_3_0_3",
  "6820365512": "H4RDIXx-0GCGYO-S_3_0_3",
  "6820365516": "H4RDIXx-Z0UYIZ-S_3_0_3",
  "6820365583": "H4RDIXx-QY4F4G-S_3_0_3",
  "6820365605": "H4RDIXx-LGMTSA-S_3_0_3",
  "6820365543": "H4RDIXx-NHZATH-S_3_0_3",
  "6820365635": "H4RDIXx-T8DIS2-S_3_0_3",
  "6820365505": "H4RDIXx-SREHYP-S_3_0_3",
  "6820365563": "H4RDIXx-0RFLMU-S_3_0_3",
  "6820365474": "H4RDIXx-TJPXDS-S_3_0_3",
  "6820365537": "H4RDIXx-WZLQGH-S_3_0_3"
}
]
JWT_API_TEMPLATE = "http://78.154.103.18:11844/get?uid={uid}&pw={password}"

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
