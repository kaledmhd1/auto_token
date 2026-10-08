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
    "8034798870": "BNGX_LVLUFNSIG",
    "8034798885": "BNGX_LVLZ9M1Z9",
    "8034798869": "BNGX_LVLMXOEB7",
    "8034799191": "BNGX_LVLA5CKL3",
    "8034799215": "BNGX_LVLYBVIG0",
    "8034799198": "BNGX_LVLVTZ0RW",
    "8034799480": "BNGX_LVLJBLAZZ",
    "8034799486": "BNGX_LVLIJGD07",
    "8034799492": "BNGX_LVLUHMC7L",
    "8034799735": "BNGX_LVLRQP9YK",
    "8034799738": "BNGX_LVL82P1N9",
    "8034799742": "BNGX_LVLTAHXEE",
    "8034800141": "BNGX_LVLZ29GMC",
    "8034800153": "BNGX_LVLDW3G8E",
    "8034800204": "BNGX_LVLJMHJY5",
    "8034800521": "BNGX_LVL5MLGWA",
    "8034800556": "BNGX_LVL8YNGQO",
    "8034800581": "BNGX_LVLW12Q5W",
    "8034800894": "BNGX_LVLRVPKOZ",
    "8034800865": "BNGX_LVL7NGBWE",
    "8034800937": "BNGX_LVL9D4BNL",
    "8034801262": "BNGX_LVL0O4PHR",
    "8034801306": "BNGX_LVLOWK17P",
    "8034801291": "BNGX_LVLSR8N4A",
    "8034801590": "BNGX_LVLQTFAUE",
    "8034801672": "BNGX_LVLPDSYMI",
    "8034801655": "BNGX_LVLM5FK0Z",
    "8034801936": "BNGX_LVLZBT9SB",
    "8034802065": "BNGX_LVLN74D6A",
    "8034802089": "BNGX_LVL2TKGUS",
    "8034802384": "BNGX_LVL5Y9PHF",
    "8034802420": "BNGX_LVLVLYPAG",
    "8034802425": "BNGX_LVLXHUEOP",
    "8034802683": "BNGX_LVLIK10XR",
    "8034802714": "BNGX_LVLICOSXU",
    "8034802717": "BNGX_LVL842DZU",
    "8034803012": "BNGX_LVL8Q83A9",
    "8034803060": "BNGX_LVLA4IWB2",
    "8034803092": "BNGX_LVLJJMJ1I",
    "8034803309": "BNGX_LVLRK90ID",
    "8034803451": "BNGX_LVL8C6Y8L",
    "8034803476": "BNGX_LVL5EAWR8",
    "8034804343": "BNGX_LVL4J4O9T",
    "8034804445": "BNGX_LVLR8WIUX",
    "8034804479": "BNGX_LVLWJDL5J",
    "8034804759": "BNGX_LVLDQ0CHS",
    "8034804837": "BNGX_LVLVCQ9FY",
    "8034804850": "BNGX_LVLDAON7Q",
    "8034805212": "BNGX_LVLM80VBH",
    "8034805238": "BNGX_LVLVAPXAR",
    "8034805307": "BNGX_LVLCAK8K8",
    "8034805583": "BNGX_LVLXQHEX7",
    "8034805581": "BNGX_LVLTWRL9W",
    "8034805712": "BNGX_LVLYHG8CK",
    "8034805910": "BNGX_LVLKU6X0O",
    "8034805928": "BNGX_LVLZFBJ4Y",
    "8034806046": "BNGX_LVL91ONM4",
    "8034806247": "BNGX_LVLROAS2G",
    "8034806282": "BNGX_LVLWH813Z",
    "8034806367": "BNGX_LVLKWAQ34",
    "8034806579": "BNGX_LVLBOFGE3",
    "8034806657": "BNGX_LVLNK7XVB",
    "8034806737": "BNGX_LVLQ6KG3Q",
    "8034806900": "BNGX_LVLWPMKAL",
    "8034806975": "BNGX_LVL2ODWYT",
    "8034807054": "BNGX_LVLZXD3K4",
    "8034807227": "BNGX_LVLFIZORJ",
    "8034807371": "BNGX_LVLEYTT25",
    "8034807464": "BNGX_LVLEHXOEG",
    "8034807591": "BNGX_LVLW4RGZE",
    "8034807677": "BNGX_LVLQXCZ1V",
    "8034807870": "BNGX_LVLW4AHLG",
    "8034808448": "BNGX_LVLCVBVL7",
    "8034808531": "BNGX_LVL6VROIU",
    "8034808713": "BNGX_LVLEOIHZB",
    "8034808868": "BNGX_LVLVZ0C8S",
    "8034808960": "BNGX_LVLMT48BE",
    "8034809061": "BNGX_LVLRQ8COV",
    "8034809221": "BNGX_LVL0661JK",
    "8034809298": "BNGX_LVLA8SAH7",
    "8034809403": "BNGX_LVLBXWKO5",
    "8034809550": "BNGX_LVLOE5981",
    "8034809624": "BNGX_LVLECA1VK",
    "8034809746": "BNGX_LVLMN3NEM",
    "8034809861": "BNGX_LVL72ID0A",
    "8034809981": "BNGX_LVLOWDSYY",
    "8034810139": "BNGX_LVLHA3IWJ",
    "8034810225": "BNGX_LVLEDTI5I",
    "8034810330": "BNGX_LVLCM3G87",
    "8034810464": "BNGX_LVLQ8VWXA",
    "8034810560": "BNGX_LVL6K7XUX",
    "8034810659": "BNGX_LVLE9X8XR",
    "8034810773": "BNGX_LVLRJSF26",
    "8034810902": "BNGX_LVLYFA85A",
    "8034810973": "BNGX_LVLEKQXA6",
    "8034811099": "BNGX_LVL40RHC3",
    "8034811283": "BNGX_LVLXD5XOJ",
    "8034811279": "BNGX_LVLXQD34G",
    "8034811411": "BNGX_LVLRXMHEZ",
    "8034811592": "BNGX_LVLG7F4YY",
    "8034811572": "BNGX_LVL2BJRNZ",
    "8034811687": "BNGX_LVL244RCH",
    "8034812679": "BNGX_LVLDN65JS",
    "8034812712": "BNGX_LVL6LQ17L",
    "8034812877": "BNGX_LVL2HAOBN",
    
    "8038817206": "BNGX_LVLK8C1HS",
    "8038817473": "BNGX_LVLHS8PDQ",
    "8038817374": "BNGX_LVLCP8S9B",
    "8038818756": "BNGX_LVLFMOVYB",
    "8038818787": "BNGX_LVLQT81Z9",
    "8038825326": "BNGX_LVL9P8KFY",
    "8038826865": "BNGX_LVLYKAQPZ",
    "8038834608": "BNGX_LVLXWIK4L",
    "8038834764": "BNGX_LVLZ7DC9V",
    "8038835518": "BNGX_LVLX3J2TE",
    "8038842902": "BNGX_LVLE75162",
    "8038843637": "BNGX_LVL9I8K41",
    "8038844363": "BNGX_LVLPEBQHB",
    "8038844608": "BNGX_LVL6D9BBP",
    "8038844768": "BNGX_LVLFHTVBL",
    "8038845224": "BNGX_LVLZDO5O3",
    "8038851538": "BNGX_LVLA7PIYM",
    "8038851881": "BNGX_LVLY10KR2",
    "8038851882": "BNGX_LVLTMY13Y",
    "8038852437": "BNGX_LVLA7YW6F",
    "8038852638": "BNGX_LVLMPMRO2",
    "8038852646": "BNGX_LVLJE6YBC",
    "8038853039": "BNGX_LVLP0KYAG",
    "8038853211": "BNGX_LVLG462HZ",
    "8038853208": "BNGX_LVLJRAADL",
    "8038853677": "BNGX_LVLC6D6L4",
    "8038853806": "BNGX_LVLPTN2RV",
    "8038853945": "BNGX_LVLZRV4EE",
    "8038854276": "BNGX_LVLDUV389",
    "8038854384": "BNGX_LVLFC40QI",
    "8038854459": "BNGX_LVLCEX9RH",
    "8038854862": "BNGX_LVLWXZIA2",
    "8038854975": "BNGX_LVL6ZAEF2",
    "8038855125": "BNGX_LVL7827KK",
    "8038858331": "BNGX_LVL0VDCY2",
    "8038858950": "BNGX_LVLVAAGOH",
    "8038859175": "BNGX_LVLEVC54G",
    "8038859608": "BNGX_LVL93UMWQ",
    "8038859994": "BNGX_LVLFQT228",
    "8038860146": "BNGX_LVLG5CWJI",
    "8038860443": "BNGX_LVLQ5A2GF",
    "8038860656": "BNGX_LVL6215G1",
    "8038860777": "BNGX_LVL5RDJK2",
    "8038860946": "BNGX_LVL1WYVCG",
    "8038861139": "BNGX_LVLUSVR6J",
    "8038861294": "BNGX_LVLVD4C6T",
    "8038861433": "BNGX_LVLM7NEQW",
    "8038861580": "BNGX_LVLL5BOJI",
    "8038861698": "BNGX_LVLCN6OBB",
    "8038861882": "BNGX_LVLW1HA4S",
    "8038862044": "BNGX_LVL2U5VO9",
    "8038862188": "BNGX_LVLN5AC6S",
    "8038862397": "BNGX_LVL3KFT4X",
    "8038862547": "BNGX_LVLXB63FZ",
    "8038862636": "BNGX_LVL3FT5OK",
    "8038862761": "BNGX_LVLRTCM6H",
    "8038862893": "BNGX_LVL8HFBTW",
    "8038862988": "BNGX_LVL61AGA3",
    "8038863233": "BNGX_LVLC2AF0R",
    "8038863277": "BNGX_LVLH355VI",
    "8038863368": "BNGX_LVLU49YWK",
    "8038863562": "BNGX_LVL4MS5I7",
    "8038863609": "BNGX_LVLG26A4A",
    "8038865880": "BNGX_LVLP3P36L",
    "8038865797": "BNGX_LVLIM8P8A",
    "8038866411": "BNGX_LVL10NPNB",
    "8038866942": "BNGX_LVLQYQYSU",
    "8038866924": "BNGX_LVLSEFG32",
    "8038867169": "BNGX_LVLGAWDXZ",
    "8038867830": "BNGX_LVLJ5VOPS",
    "8038867894": "BNGX_LVL8UQYUJ",
    "8038868009": "BNGX_LVLYLFWCX",
    "8038868445": "BNGX_LVLMMXRYQ",
    "8038868576": "BNGX_LVL8EBSVE",
    "8038868649": "BNGX_LVLB11EL4",
    "8038869016": "BNGX_LVLZT976X",
    "8038869123": "BNGX_LVL9M4OR8",
    "8038869177": "BNGX_LVLDH10R4",
    "8038869475": "BNGX_LVLRJU58N",
    "8038869615": "BNGX_LVL3MVTL6",
    "8038869668": "BNGX_LVLA0F4NI",
    "8038870081": "BNGX_LVLSRL8ZO",
    "8038870126": "BNGX_LVLU41A7Y",
    "8038870229": "BNGX_LVL6YWV39",
    "8038870749": "BNGX_LVLDZKVUK",
    "8038870804": "BNGX_LVL2N5EH0",
    "8038870964": "BNGX_LVLUTJPM3",
    "8038871361": "BNGX_LVLPWE155",
    "8038871366": "BNGX_LVLGVILXK",
    "8038871608": "BNGX_LVLAKEROP",
    "8038871822": "BNGX_LVL797U00",
    "8038871821": "BNGX_LVLITU70R",
    "8038872081": "BNGX_LVLVN8GE2",
    "8038873664": "BNGX_LVLFXZBWX",
    "8038873924": "BNGX_LVLGKUM8I",
    "8038874594": "BNGX_LVLRY6BMS",
    "8038874902": "BNGX_LVLDMGBJV",
    "8038874951": "BNGX_LVL940OJ3",
    "8038875247": "BNGX_LVL1VT7JA",
    "8038875466": "BNGX_LVL1E055Z",
    "8038875535": "BNGX_LVLGMLNVN",
    "8038875888": "BNGX_LVLVBRKLX",
    "8038875988": "BNGX_LVLLV2BK1",
    "8038876083": "BNGX_LVLDZJS7T",
    "8038876382": "BNGX_LVL5ZIRER",
    "8038876527": "BNGX_LVLY6ISV2",
    "8038876706": "BNGX_LVLBS2R6C",
    "8038877142": "BNGX_LVLW4381I",
    "8038877193": "BNGX_LVL4BIG1D",
    "8038877311": "BNGX_LVLKV6V7O",
    "8038877672": "BNGX_LVLD7HV4L",
    "8038877728": "BNGX_LVLIU7UTH",
    "8038877838": "BNGX_LVL2SRBTA",
    "8038878178": "BNGX_LVL465CMA",
    "8038878270": "BNGX_LVLT3HB0L",
    "8038878548": "BNGX_LVLKA6ATE",
    "8038878952": "BNGX_LVLN1567F",
    "8038879111": "BNGX_LVLX3X8LR",
    
    "8040827411": "BNGX_LVLTAE7XD",
    "8040827361": "BNGX_LVLX94EAD",
    "8040827362": "BNGX_LVL7RY2SB",
    "8040828143": "BNGX_LVLGUXOKR",
    "8040828180": "BNGX_LVL77ICAO",
    "8040828234": "BNGX_LVLL592YU",
    "8040828821": "BNGX_LVLSZHNDB",
    "8040828848": "BNGX_LVLNPUH0U",
    "8040833273": "BNGX_LVLXHLAZU",
    "8040834144": "BNGX_LVLLYVEV9",
    "8040835272": "BNGX_LVLY8FMO0",
    "8040835905": "BNGX_LVLZQUKFO",
    "8040835992": "BNGX_LVLY1TVMG",
    "8040836481": "BNGX_LVLQ2MY4A",
    "8040836911": "BNGX_LVL3BTHV2",
    "8040836931": "BNGX_LVLF5N80P",
    "8040837442": "BNGX_LVLSEEPP7",
    "8040844172": "BNGX_LVLSKDUKE",
    "8040844686": "BNGX_LVL0V17GX",
    "8040845183": "BNGX_LVL0RV8LW",
    "8040845968": "BNGX_LVLP3KB97",
    "8040846340": "BNGX_LVLZJG5T1",
    "8040846564": "BNGX_LVLPMQP19",
    "8040847153": "BNGX_LVLLDPXBC",
    "8040847510": "BNGX_LVLDPM9LO",
    "8040847558": "BNGX_LVL8N9BRN",
    "8040848232": "BNGX_LVLPE6LDS",
    "8040855157": "BNGX_LVL2DMSA4",
    "8040855255": "BNGX_LVL13CY27",
    "8040855751": "BNGX_LVL3KSJEP",
    "8040856935": "BNGX_LVL1PE4IQ",
    "8040857003": "BNGX_LVLQ9A9ET",
    "8040856909": "BNGX_LVLRNSQ6Z",
    "8040857823": "BNGX_LVL22QHER",
    "8040857826": "BNGX_LVLTT4Y9O",
    "8040857760": "BNGX_LVLKLMG6M",
    "8040864401": "BNGX_LVL80HK4L",
    "8040864558": "BNGX_LVLRWRIZQ",
    "8040865096": "BNGX_LVLHIWRDJ",
    "8040866318": "BNGX_LVLRJQAZ1",
    "8040866548": "BNGX_LVLFC2U0J",
    "8040866501": "BNGX_LVL70CXXS",
    "8040867328": "BNGX_LVLKDUIUC",
    "8040867461": "BNGX_LVL7AUS5D",
    "8040867513": "BNGX_LVLFNGGM0",
    "8040873508": "BNGX_LVLNWTIKU",
    "8040873406": "BNGX_LVLT70CAW",
    "8040874640": "BNGX_LVL0KVK6I",
    "8040876048": "BNGX_LVLSVSRQ7",
    "8040876123": "BNGX_LVLDTK831"
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
