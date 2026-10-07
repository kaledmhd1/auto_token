from flask import Flask, jsonify, request
import asyncio
import aiohttp
import json
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)


# ============================================================
#  ط§ظ„ط­ط³ط§ط¨ط§طھ â€” ط§ظ„طµظ‚ ظ‚ط§ط¦ظ…طھظƒ ظ‡ظ†ط§ (ظƒظ…ط§ ظ‡ظٹ)
# ============================================================
group_accounts = [
  {
    "8019121427": "AlliFF_VIPKOVKK1",
    "8019121595": "AlliFF_VIPQ0W9FN",
    "8019121600": "AlliFF_VIP8Y7VJL",
    "8019121605": "AlliFF_VIPUJ8NQ4",
    "8019121744": "AlliFF_VIPFPVHOT",
    "8019121772": "AlliFF_VIP49ZERV",
    "8019121762": "AlliFF_VIP3GG0GO",
    "8019121898": "AlliFF_VIPVX11GH",
    "8019121909": "AlliFF_VIP5EHX0Z",
    "8019121906": "AlliFF_VIPVUTD4L",
    "8019122008": "AlliFF_VIPQWHOTD",
    "8019122017": "AlliFF_VIP3GEZFX",
    "8019122037": "AlliFF_VIPIL2FFG",
    "8019122386": "AlliFF_VIPPMKIM8",
    "8019122404": "AlliFF_VIPD1X7OX",
    "8019122424": "AlliFF_VIPLOHXCS",
    "8019122585": "AlliFF_VIPNYIDJX",
    "8019122607": "AlliFF_VIP418JMJ",
    "8019122618": "AlliFF_VIP87W6XM",
    "8019122747": "AlliFF_VIP3CIVNY",
    "8019122789": "AlliFF_VIPVKTNU4",
    "8019122786": "AlliFF_VIP9PAA0Q",
    "8019122947": "AlliFF_VIPSVXBSK",
    "8019122957": "AlliFF_VIPTSGLBD",
    "8019123035": "AlliFF_VIPWLKTAU",
    "8019123107": "AlliFF_VIPQ3P29X",
    "8019123125": "AlliFF_VIPOVE17X",
    "8019123147": "AlliFF_VIPTOMZUI",
    "8019123202": "AlliFF_VIPA0AWD5",
    "8019123225": "AlliFF_VIP7953ZE",
    "8019123258": "AlliFF_VIPN7I028",
    "8019123335": "AlliFF_VIPN0JP4S",
    "8019123363": "AlliFF_VIPO3BQPF",
    "8019123384": "AlliFF_VIP8YDILZ",
    "8019123471": "AlliFF_VIPEMQB2B",
    "8019123531": "AlliFF_VIP7PYYH8",
    "8019123560": "AlliFF_VIP1NH7Z7",
    "8019123618": "AlliFF_VIPC2LN7I",
    "8019123717": "AlliFF_VIPOU5YPN",
    "8019123736": "AlliFF_VIPRMWU1L",
    "8019123948": "AlliFF_VIPISI4IZ",
    "8019124058": "AlliFF_VIPS5QQQ9",
    "8019124084": "AlliFF_VIPU6Q36H",
    "8019124371": "AlliFF_VIPMT8ORE",
    "8019124422": "AlliFF_VIPOTLHJ8",
    "8019124473": "AlliFF_VIPH54BSZ",
    "8019124662": "AlliFF_VIPH0MLIT",
    "8019124691": "AlliFF_VIPDGPHN9",
    "8019124725": "AlliFF_VIP1UQQAA",
    "8019124886": "AlliFF_VIPP4O9ZX",
    "8019124942": "AlliFF_VIPNH9N31",
    "8019124949": "AlliFF_VIPL06Z1Z",
    "8019125026": "AlliFF_VIPW7X6UV",
    "8019125076": "AlliFF_VIPAS5PO6",
    "8019125071": "AlliFF_VIPGR1SQM",
    "8019125156": "AlliFF_VIP36NJFF",
    "8019125194": "AlliFF_VIP95S9SQ",
    "8019125192": "AlliFF_VIPSIQI7G",
    "8019125276": "AlliFF_VIPWOS80P",
    "8019125307": "AlliFF_VIPUT3F68",
    "8019125314": "AlliFF_VIP09C8ID",
    "8019125383": "AlliFF_VIPQ12XAP",
    "8019125423": "AlliFF_VIPYX15C5",
    "8019125424": "AlliFF_VIPFQ2NRZ",
    "8019125509": "AlliFF_VIPU7LRC2",
    "8019125556": "AlliFF_VIPRSHFB3",
    "8019125592": "AlliFF_VIPBUBDDQ",
    "8019125671": "AlliFF_VIPKDXXYO",
    "8019125756": "AlliFF_VIPZXXHA4",
    "8019125882": "AlliFF_VIPEC2LRQ",
    "8019126073": "AlliFF_VIP2WG9QF",
    "8019126150": "AlliFF_VIP5U70IC",
    "8019126176": "AlliFF_VIPXRCXBP",
    "8019126257": "AlliFF_VIPTDX5MM",
    "8019126312": "AlliFF_VIPZVAHEJ",
    "8019126310": "AlliFF_VIPYDWPMQ",
    "8019126388": "AlliFF_VIPB9556R",
    "8019126430": "AlliFF_VIPUHK7JW",
    "8019126428": "AlliFF_VIPWISMV2",
    "8019126499": "AlliFF_VIP3W51KO",
    "8019126557": "AlliFF_VIPBN9WGU",
    "8019126554": "AlliFF_VIPLTQE46",
    "8019126636": "AlliFF_VIP2GE0XW",
    "8019126697": "AlliFF_VIPYE5Z07",
    "8019126705": "AlliFF_VIPO9NNDQ",
    "8019126741": "AlliFF_VIPZK92EW",
    "8019126818": "AlliFF_VIPWO2D2K",
    "8019126829": "AlliFF_VIPNQ70BM"
  }
]

JWT_API_TEMPLATE = "http://us-az-phx.hostbu.com:5022/login?uid={uid}&password={password}"

# ============================================================
#  ط§ظ„ط¥ط¹ط¯ط§ط¯ط§طھ
# ============================================================
TIMEOUT_PER_REQUEST = 20.0   # â†گ 20 ط«ط§ظ†ظٹط© ظ„ظƒظ„ ط­ط³ط§ط¨
REQUEST_DELAY = 0.0
CACHE_DURATION = 10000

# âœ… ظ„ط§ ط¯ظپط¹ط§طھ â€” ظپظ‚ط· 5 ط­ط³ط§ط¨ط§طھ ظ…طھط²ط§ظ…ظ†ط© ظپظٹ ظ†ظپط³ ط§ظ„ظ„ط­ط¸ط© (5 ط¨ظ€ 5)
MAX_CONCURRENT = 5


CACHE = {
    "tokens": {},
    "timestamp": 0
}

COLLECTED_TOKENS = {}
IS_FETCHING = False


# ============================================================
#  ط¬ظ„ط¨ طھظˆظƒظ† ط­ط³ط§ط¨ ظˆط§ط­ط¯ â€” timeout 20s
# ============================================================
async def fetch_one_token(session, uid, password, semaphore):
    """
    ط¬ظ„ط¨ طھظˆظƒظ† ظˆط§ط­ط¯ ظ…ط¹ timeout 20 ط«ط§ظ†ظٹط©.
    ظٹط³طھط®ط¯ظ… semaphore ظ„ظ„طھط­ظƒظ… ظپظٹ ط§ظ„طھظˆط§ط²ظٹ.
    """
    url = JWT_API_TEMPLATE.format(uid=uid, password=password)
    timeout = aiohttp.ClientTimeout(total=TIMEOUT_PER_REQUEST)
    started = time.time()

    async with semaphore:
        try:
            async with session.get(url, timeout=timeout) as resp:
                elapsed = time.time() - started

                if resp.status != 200:
                    print(f"[{uid}] HTTP {resp.status} ({elapsed:.2f}s)")
                    return uid, None, None, None, f"http_{resp.status}"

                text = await resp.text()

                # â”€â”€â”€ ظ…ط­ط§ظˆظ„ط© JSON â”€â”€â”€
                try:
                    data = json.loads(text)
                    if isinstance(data, dict):
                        if data.get("ok") and data.get("token"):
                            print(f"[{uid}] âœ… OK ({elapsed:.2f}s) | "
                                  f"acc={data.get('account_id')} | "
                                  f"region={data.get('region')}")
                            return (
                                uid,
                                data["token"],
                                str(data.get("account_id", "")),
                                data.get("region", ""),
                                None
                            )
                        return uid, None, None, None, data.get("error", "not_ok")
                except json.JSONDecodeError:
                    pass

                # â”€â”€â”€ fallback: ظ†طµ ظ…ط¨ط§ط´ط± â”€â”€â”€
                token = text.strip()
                if len(token) > 20:
                    print(f"[{uid}] âœ… OK raw ({elapsed:.2f}s)")
                    return uid, token, None, None, None

                return uid, None, None, None, "empty_response"

        except asyncio.TimeoutError:
            print(f"[{uid}] âڈ± timeout after {TIMEOUT_PER_REQUEST}s")
            return uid, None, None, None, "timeout"
        except aiohttp.ClientError as e:
            print(f"[{uid}] â‌Œ connection error: {e}")
            return uid, None, None, None, f"conn_error"
        except Exception as e:
            print(f"[{uid}] â‌Œ {type(e).__name__}: {e}")
            return uid, None, None, None, "exception"


# ============================================================
#  ط¬ظ„ط¨ ظƒظ„ ط§ظ„ط­ط³ط§ط¨ط§طھ â€” 5 ظپظٹ ظ†ظپط³ ط§ظ„ظˆظ‚طھ ظپظ‚ط· (ط¨ط¯ظˆظ† ط¯ظپط¹ط§طھ)
# ============================================================
async def fetch_all(accounts: dict, max_concurrent: int = 5):
    """
    ظٹط±ط³ظ„ ظƒظ„ ط§ظ„ط­ط³ط§ط¨ط§طھ ظ…ط±ط© ظˆط§ط­ط¯ط© ظ„ظ€ asyncioطŒ
    ظ„ظƒظ† Semaphore(max_concurrent) ظٹط¶ظ…ظ† طھط´ط؛ظٹظ„ 5 ظپظ‚ط· ط¨ط§ظ„طھظˆط§ط²ظٹ.
    ط§ظ„ط¨ط§ظ‚ظٹ ظٹظ†طھط¸ط±ظˆظ† ط¯ظˆط±ظ‡ظ… طھظ„ظ‚ط§ط¦ظٹط§ظ‹ (5 ط¨ظ€ 5) ط¨ط¯ظˆظ† ط¯ظپط¹ط§طھ.
    """
    total = len(accounts)
    print(f"\n{'='*60}")
    print(f"ًں“ٹ Total accounts   : {total}")
    print(f"ًں“ٹ Concurrent limit : {max_concurrent} (5 by 5)")
    print(f"ًں“ٹ Timeout/req      : {TIMEOUT_PER_REQUEST}s")
    print(f"{'='*60}\n")

    semaphore = asyncio.Semaphore(max_concurrent)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_one_token(session, uid, password, semaphore)
            for uid, password in accounts.items()
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # طھط¬ظ…ظٹط¹ ط§ظ„ظ†طھط§ط¦ط¬
    tokens = {}
    failed = []
    for result in results:
        if isinstance(result, Exception):
            failed.append(("unknown", str(result)))
            continue
        uid, token, acc_id, region, error = result
        if token:
            tokens[uid] = token
        else:
            failed.append((uid, error))

    print(f"\n{'='*60}")
    print(f"âœ… ALL DONE: {len(tokens)}/{total} succeeded | {len(failed)} failed")
    print(f"{'='*60}\n")

    return tokens, failed


# ============================================================
#  ظ…ط³ط§ط¹ط¯ط§طھ
# ============================================================
def is_cache_valid():
    return (time.time() - CACHE["timestamp"]) < CACHE_DURATION and len(CACHE["tokens"]) > 0


def get_last_update_vn():
    utc_time = datetime.fromtimestamp(CACHE["timestamp"], tz=timezone.utc)
    vn_time = utc_time + timedelta(hours=7)
    return vn_time.strftime("%Y-%m-%d %H:%M:%S")


# ============================================================
#  Endpoints
# ============================================================
@app.route("/api/get_jwt", methods=["GET"])
def get_jwt_tokens():
    """
    ظٹط¬ظ„ط¨ ظƒظ„ ط§ظ„طھظˆظƒظ†ط§طھ â€” 5 ط­ط³ط§ط¨ط§طھ ظپظ‚ط· ظپظٹ ظ†ظپط³ ط§ظ„ظ„ط­ط¸ط© (5 ط¨ظ€ 5).
    """
    global IS_FETCHING

    # optional query param ظ„ظ„طھط­ظƒظ… ظپظٹ ط§ظ„طھظˆط§ط²ظٹ (ط§ظپطھط±ط§ط¶ظٹ 5)
    max_concurrent = int(request.args.get("concurrent", MAX_CONCURRENT))
    max_concurrent = max(1, min(max_concurrent, 50))

    # 1) ظƒط§ط´ ط´ط؛ط§ظ„ â†’ ط±ط¬ظ‘ط¹ ظپظˆط±ط§ظ‹
    if is_cache_valid():
        return jsonify({
            "ok": True,
            "source": "cache",
            "count": len(CACHE["tokens"]),
            "last_update_vn": get_last_update_vn(),
            "tokens": CACHE["tokens"]
        })

    # 2) ط·ظ„ط¨ ط¢ط®ط± ط´ط؛ط§ظ„ â†’ ظ„ط§ طھظƒط±ط±
    if IS_FETCHING:
        return jsonify({
            "ok": False,
            "error": "fetch_in_progress",
            "message": "Fetch already running. Wait and retry.",
        }), 429

    # 3) ط§ط¨ط¯ط£ ط§ظ„ط¬ظ„ط¨
    IS_FETCHING = True
    try:
        all_accounts = group_accounts[0]

        tokens, failed = asyncio.run(
            fetch_all(all_accounts, max_concurrent=max_concurrent)
        )

        # ط­ظپط¸ ظپظٹ ط§ظ„ظƒط§ط´
        CACHE["tokens"] = tokens
        CACHE["timestamp"] = time.time()

        return jsonify({
            "ok": True,
            "source": "fresh",
            "count": len(tokens),
            "failed_count": len(failed),
            "concurrent": max_concurrent,
            "timeout_per_request": TIMEOUT_PER_REQUEST,
            "failed": [{"uid": u, "error": e} for u, e in failed],
            "last_update_vn": get_last_update_vn(),
            "tokens": tokens
        })
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": "server_error",
            "detail": str(e)
        }), 500
    finally:
        IS_FETCHING = False


@app.route("/api/test_one", methods=["GET"])
def test_one():
    """ط§ط®طھط¨ط§ط± ط­ط³ط§ط¨ ظˆط§ط­ط¯."""
    uid = request.args.get("uid", "").strip()
    password = request.args.get("password", "").strip()

    if not uid or not password:
        return jsonify({"ok": False, "error": "provide uid & password"}), 400

    async def run():
        sem = asyncio.Semaphore(1)
        async with aiohttp.ClientSession() as session:
            return await fetch_one_token(session, uid, password, sem)

    uid_r, token, acc_id, region, error = asyncio.run(run())

    return jsonify({
        "ok": bool(token),
        "uid": uid_r,
        "account_id": acc_id,
        "region": region,
        "error": error,
        "token_preview": (token[:80] + "...") if token else None,
        "token_length": len(token) if token else 0,
    })


@app.route("/api/status", methods=["GET"])
def status():
    """ط­ط§ظ„ط© ط§ظ„ط¬ظ„ط¨ ط§ظ„ط­ط§ظ„ظٹط©."""
    return jsonify({
        "is_fetching": IS_FETCHING,
        "cache_valid": is_cache_valid(),
        "cache_count": len(CACHE["tokens"]),
        "cache_age_seconds": (time.time() - CACHE["timestamp"]) if CACHE["timestamp"] else None,
        "config": {
            "concurrent": MAX_CONCURRENT,
            "timeout_per_request": TIMEOUT_PER_REQUEST,
            "cache_duration": CACHE_DURATION,
        }
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True, "status": "alive"})


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "JWT Fetcher (5 concurrent, no batches)",
        "upstream_api": JWT_API_TEMPLATE,
        "config": {
            "concurrent": MAX_CONCURRENT,
            "timeout_per_request": TIMEOUT_PER_REQUEST,
            "cache_duration": CACHE_DURATION,
            "mode": "5 accounts at a time, continuously (no batches)"
        },
        "endpoints": {
            "GET /api/get_jwt": "Fetch all tokens (5 concurrent)",
            "GET /api/get_jwt?concurrent=10": "Control concurrency (default 5)",
            "GET /api/test_one?uid=&password=": "Test one account",
            "GET /api/status": "Fetch status",
            "GET /health": "Health check"
        }
    })


# ============================================================
#  ط§ظ„طھط´ط؛ظٹظ„
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print("=" * 60)
    print("   JWT Fetcher â€” 5 accounts at a time (no batches)")
    print("=" * 60)
    print(f"[i] Listening      : http://0.0.0.0:{port}")
    print(f"[i] Upstream       : {JWT_API_TEMPLATE}")
    print(f"[i] Concurrency    : {MAX_CONCURRENT} (5 by 5)")
    print(f"[i] Timeout/req    : {TIMEOUT_PER_REQUEST}s")
    print(f"[i] Cache          : {CACHE_DURATION}s")
    print(f"[i] Endpoint       : http://localhost:{port}/api/get_jwt")
    print(f"[i] With conc.     : http://localhost:{port}/api/get_jwt?concurrent=10")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, threaded=True, debug=False)
