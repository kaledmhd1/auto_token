from flask import Flask, jsonify
import asyncio
import aiohttp
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)

# المجموعات الثمانية (كل مجموعة فيها 8 حسابات كحد أقصى)
group_accounts = [
    {
        "3231011844": "16CA073DB9766AC222E35C2A55EB5F36AF67235CDE9EF5F855339334A218D28D"
    },
    {
        "3231014029": "79F37904133C1AD52ED425CFE03E628FB4CDA75CB3ED3D4290E51C0F237D1444",
        "3231015105": "6D4044A81705A3DEF00DC5E95A3F4F9DD661F58548C29101A853A0596F93DF47",
        "3231015608": "0A39DB28B12A4DEB5176E700DE68D04E9FB0CA8CA00166B126B065E468EE0785",
        "3231016152": "8AD81FC469728920C8454DCB23345022470774580030A36D7CA74A194229EAE4",
        "3231006740": "8133B583B7F2B0701733C5A0586F28205C3CC8B0DB5004EC731C7BB1EB64FA9F",
        "3231018315": "C1B0AC574DA747386676FEAC0A15DB6C7DCF1CCE9EFF71AD305C329AAF44ADF9",
        "3231016672": "FAB40727917046A4C9792FC693690F21C75B48DC2432984960E31DF794B114C9"
    },
    # أضف باقي المجموعات...
]

JWT_API_TEMPLATE = "https://jwt-token-bngx.vercel.app/api/oauth_guest?uid={uid}&password={password}"

CACHE = {
    "tokens": [],
    "timestamp": 0
}

COLLECTED_TOKENS = []
GROUP_INDEX = 0  # مؤشر المجموعة الحالية

CACHE_DURATION = 3600  # ثانية (ساعة)
CONCURRENT_LIMIT = 40  # عدد الاتصالات المتزامنة

async def fetch_token(session, uid, password):
    url = JWT_API_TEMPLATE.format(uid=uid, password=password)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                token = data.get("token")
                if token:
                    return token
            return None
    except Exception as e:
        print(f"Error fetching token for uid {uid}: {e}")
        return None

async def fetch_token_with_semaphore(semaphore, session, uid, password):
    async with semaphore:
        return await fetch_token(session, uid, password)

async def fetch_tokens_for_group(group):
    tokens = []
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_token_with_semaphore(semaphore, session, uid, password)
                 for uid, password in group.items()]
        results = await asyncio.gather(*tasks)
        for t in results:
            if t:
                tokens.append(t)
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

    # جلب المجموعة الحالية فقط
    async def process_group():
        current_group = group_accounts[GROUP_INDEX]
        tokens = await fetch_tokens_for_group(current_group)
        return tokens

    new_tokens = asyncio.run(process_group())
    COLLECTED_TOKENS.extend(new_tokens)

    # إذا وصلنا لنهاية المجموعات الثمانية
    if GROUP_INDEX == len(group_accounts) - 1:
        CACHE["tokens"] = COLLECTED_TOKENS.copy()
        CACHE["timestamp"] = time.time()
        COLLECTED_TOKENS.clear()
        GROUP_INDEX = 0
    else:
        GROUP_INDEX += 1

    return jsonify({
        "count": len(COLLECTED_TOKENS) if CACHE["tokens"] == [] else len(CACHE["tokens"]),
        "last_update_vn": get_last_update_vn() if CACHE["tokens"] else None,
        "tokens": CACHE["tokens"] if CACHE["tokens"] else COLLECTED_TOKENS
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
