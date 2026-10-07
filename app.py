from flask import Flask, jsonify, request
import asyncio
import aiohttp
import json
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)


# ============================================================
#  ط·آ§ط¸â€‍ط·آ­ط·آ³ط·آ§ط·آ¨ط·آ§ط·ع¾ أ¢â‚¬â€‌ ط·آ§ط¸â€‍ط·آµط¸â€ڑ ط¸â€ڑط·آ§ط·آ¦ط¸â€¦ط·ع¾ط¸ئ’ ط¸â€،ط¸â€ ط·آ§ (ط¸ئ’ط¸â€¦ط·آ§ ط¸â€،ط¸ظ¹)
# ============================================================
group_accounts = [
    {
        "8029172663": "BNGX_LVLXLRS9H"
    },
    {
        "8029172664": "BNGX_LVLSS9DQN"
    },
    {
        "8029172665": "BNGX_LVLQTAJXL"
    },
    {
        "8029172986": "BNGX_LVLPLANPL"
    },
    {
        "8029173009": "BNGX_LVLVNLSTH"
    },
    {
        "8029172996": "BNGX_LVLWRMVYP"
    },
    {
        "8029173180": "BNGX_LVL33GQVU"
    },
    {
        "8029173198": "BNGX_LVLPF2FF5"
    },
    {
        "8029173215": "BNGX_LVLJTQA3A"
    },
    {
        "8029173430": "BNGX_LVLNK2DYT"
    },
    {
        "8029173436": "BNGX_LVLGFANKP"
    },
    {
        "8029173451": "BNGX_LVL1GCE5H"
    },
    {
        "8029173652": "BNGX_LVL6ZWNQD"
    },
    {
        "8029173658": "BNGX_LVLEEJGC6"
    },
    {
        "8029173690": "BNGX_LVLHKNS2E"
    },
    {
        "8029174302": "BNGX_LVLGZYYJO"
    },
    {
        "8029174309": "BNGX_LVL7G7SW9"
    },
    {
        "8029174511": "BNGX_LVLYQ9KWX"
    },
    {
        "8029174884": "BNGX_LVLT2VYVC"
    },
    {
        "8029174933": "BNGX_LVL6JDUWE"
    },
    {
        "8029175117": "BNGX_LVLSF0FX5"
    },
    {
        "8029175430": "BNGX_LVL1CWET9"
    },
    {
        "8029175486": "BNGX_LVLD2ZH5T"
    },
    {
        "8029175644": "BNGX_LVLSMIR0J"
    },
    {
        "8029175881": "BNGX_LVL36W523"
    },
    {
        "8029175890": "BNGX_LVLLSH166"
    },
    {
        "8029176072": "BNGX_LVLQUEG0E"
    },
    {
        "8029179825": "BNGX_LVL8OFAS8"
    },
    {
        "8029180071": "BNGX_LVL3NSHIM"
    },
    {
        "8029180028": "BNGX_LVLCA5O3W"
    },
    {
        "8029180694": "BNGX_LVLS6R3F0"
    },
    {
        "8029180785": "BNGX_LVLS33BDP"
    },
    {
        "8029180804": "BNGX_LVLXM1SRP"
    },
    {
        "8029181248": "BNGX_LVL5XR4VX"
    },
    {
        "8029181330": "BNGX_LVLVAM0PL"
    },
    {
        "8029181393": "BNGX_LVLSQOZFQ"
    },
    {
        "8029184035": "BNGX_LVLDCQNUQ"
    },
    {
        "8029184108": "BNGX_LVL1T884U"
    },
    {
        "8029184069": "BNGX_LVL097P2H"
    },
    {
        "8029184082": "BNGX_LVL78KSON"
    },
    {
        "8029184111": "BNGX_LVLJH6UWP"
    },
    {
        "8029184067": "BNGX_LVL3YKWLQ"
    },
    {
        "8029184089": "BNGX_LVLTIGUV5"
    },
    {
        "8029184032": "BNGX_LVLSYC8DK"
    },
    {
        "8029184093": "BNGX_LVLPZMT5V"
    },
    {
        "8029184031": "BNGX_LVLSCO7SX"
    },
    {
        "8029184090": "BNGX_LVLRN6VCA"
    },
    {
        "8029184094": "BNGX_LVL62Z115"
    },
    {
        "8029184866": "BNGX_LVLZKLJ90"
    },
    {
        "8029184738": "BNGX_LVLHN24V2"
    },
    {
        "8029185059": "BNGX_LVLGISZJA"
    },
    {
        "8029185052": "BNGX_LVLJGYB16"
    },
    {
        "8029185119": "BNGX_LVLMVYO9Z"
    },
    {
        "8029184878": "BNGX_LVLFT0SS6"
    },
    {
        "8029185251": "BNGX_LVL8HBAW2"
    },
    {
        "8029185236": "BNGX_LVL52F6UY"
    },
    {
        "8029185267": "BNGX_LVLXYI3NJ"
    },
    {
        "8029185197": "BNGX_LVLMJPP9M"
    },
    {
        "8029185429": "BNGX_LVLCWTEN6"
    },
    {
        "8029185307": "BNGX_LVLUYPC18"
    },
    {
        "8029185355": "BNGX_LVLLQYH1I"
    },
    {
        "8029185411": "BNGX_LVLK0T8FX"
    },
    {
        "8029185370": "BNGX_LVLZOH9TJ"
    },
    {
        "8029185436": "BNGX_LVLHFTNAG"
    },
    {
        "8029185398": "BNGX_LVLJVEF2Q"
    },
    {
        "8029185335": "BNGX_LVLIWF2NR"
    },
    {
        "8029185440": "BNGX_LVLTRD35X"
    },
    {
        "8029185314": "BNGX_LVLXVF0BQ"
    },
    {
        "8029185554": "BNGX_LVLW6Y8F5"
    },
    {
        "8029185475": "BNGX_LVLPZV3NZ"
    },
    {
        "8029185521": "BNGX_LVLOLWIGD"
    },
    {
        "8029185523": "BNGX_LVLTTM9EE"
    },
    {
        "8029185574": "BNGX_LVL5AUH86"
    },
    {
        "8029185854": "BNGX_LVL1GD22X"
    },
    {
        "8029185584": "BNGX_LVL46HYED"
    },
    {
        "8029185726": "BNGX_LVLA4UB6P"
    },
    {
        "8029185795": "BNGX_LVLCOROHT"
    },
    {
        "8029185855": "BNGX_LVLTMP98B"
    },
    {
        "8029195931": "BNGX_LVLW9PVRK"
    },
    {
        "8029195929": "BNGX_LVLWZ3XKD"
    },
    {
        "8029195230": "BNGX_LVLK5GWXD"
    },
    {
        "8029195554": "BNGX_LVLMQTM09"
    },
    {
        "8029195422": "BNGX_LVL2E0OK0"
    },
    {
        "8029195940": "BNGX_LVLEPBP6Y"
    },
    {
        "8029195364": "BNGX_LVLUNM8GF"
    },
    {
        "8029195509": "BNGX_LVL4EJDSC"
    },
    {
        "8029195031": "BNGX_LVL3KADO5"
    },
    {
        "8029195905": "BNGX_LVL86KJAM"
    },
    {
        "8029195911": "BNGX_LVLW5SXP9"
    },
    {
        "8029195909": "BNGX_LVL87RTWF"
    },
    {
        "8029195102": "BNGX_LVLIRLLHW"
    },
    {
        "8029195128": "BNGX_LVL0I0NN1"
    },
    {
        "8029195201": "BNGX_LVL6BZLZ9"
    },
    {
        "8029195027": "BNGX_LVLHW89YZ"
    },
    {
        "8029196003": "BNGX_LVL0SMWYK"
    },
    {
        "8029196005": "BNGX_LVLZNAV81"
    },
    {
        "8029195859": "BNGX_LVLMKREYP"
    },
    {
        "8029195927": "BNGX_LVL83G5XI"
    },
    {
        "8029195865": "BNGX_LVLCFCKYD"
    },
    {
        "8029195064": "BNGX_LVLOH8L2W"
    },
    {
        "8029195071": "BNGX_LVLOQ5P0X"
    },
    {
        "8029195534": "BNGX_LVLG102JR"
    },
    {
        "8029195960": "BNGX_LVLQOJ9B7"
    },
    {
        "8029195548": "BNGX_LVLOUBEQE"
    },
    {
        "8029195081": "BNGX_LVLRGFB9J"
    },
    {
        "8029195050": "BNGX_LVLO2E8WG"
    },
    {
        "8029195968": "BNGX_LVLBA1VX5"
    },
    {
        "8029195806": "BNGX_LVL65C9QR"
    },
    {
        "8029200054": "BNGX_LVLWJI3SC"
    },
    {
        "8029200019": "BNGX_LVLR5M53B"
    },
    {
        "8029200275": "BNGX_LVL97BLHD"
    },
    {
        "8029200016": "BNGX_LVLOMMDM0"
    },
    {
        "8029200148": "BNGX_LVLOW71GI"
    },
    {
        "8029200276": "BNGX_LVL8IMXBM"
    },
    {
        "8029200000": "BNGX_LVLNNLB6B"
    },
    {
        "8029200004": "BNGX_LVL0H4CNC"
    },
    {
        "8029200254": "BNGX_LVLQAFMMC"
    },
    {
        "8029200261": "BNGX_LVLRANNCV"
    },
    {
        "8029200351": "BNGX_LVLUF6PXE"
    },
    {
        "8029200197": "BNGX_LVL5UT9PR"
    },
    {
        "8029200308": "BNGX_LVLT5ZFVZ"
    },
    {
        "8029200455": "BNGX_LVLMSNHSP"
    },
    {
        "8029200386": "BNGX_LVLWI4YPB"
    },
    {
        "8029200416": "BNGX_LVL8U1BGM"
    },
    {
        "8029200560": "BNGX_LVL2FFL6S"
    },
    {
        "8029200467": "BNGX_LVLWD11NE"
    },
    {
        "8029200305": "BNGX_LVLNZWEUP"
    },
    {
        "8029200421": "BNGX_LVLSSHSE0"
    },
    {
        "8029200579": "BNGX_LVL27L9QP"
    },
    {
        "8029200834": "BNGX_LVLWCFH7E"
    },
    {
        "8029200765": "BNGX_LVL5MOJ27"
    },
    {
        "8029200815": "BNGX_LVLNL9RO9"
    },
    {
        "8029200786": "BNGX_LVLIVJUDN"
    },
    {
        "8029200857": "BNGX_LVLJI6WF0"
    },
    {
        "8029200861": "BNGX_LVLHV82E2"
    },
    {
        "8029200825": "BNGX_LVLE22BPG"
    },
    {
        "8029200783": "BNGX_LVL1YJSIX"
    },
    {
        "8029200972": "BNGX_LVL6CDENR"
    },
    {
        "8029214457": "BNGX_LVLLIJCM8"
    },
    {
        "8029214538": "BNGX_LVLT5Q9EN"
    },
    {
        "8029214547": "BNGX_LVLQGJ8TE"
    },
    {
        "8029214242": "BNGX_LVLK8CPZJ"
    },
    {
        "8029214519": "BNGX_LVLGH94FK"
    },
    {
        "8029214363": "BNGX_LVLG4OW7E"
    },
    {
        "8029214537": "BNGX_LVL3NM1U6"
    },
    {
        "8029214151": "BNGX_LVL329Z7Q"
    },
    {
        "8029214289": "BNGX_LVL1PDZGR"
    },
    {
        "8029214509": "BNGX_LVL8IJMEF"
    },
    {
        "8029214320": "BNGX_LVLFPMXMO"
    },
    {
        "8029214516": "BNGX_LVL316M0V"
    },
    {
        "8029214302": "BNGX_LVL40TI7G"
    },
    {
        "8029214196": "BNGX_LVL3URW0C"
    },
    {
        "8029214209": "BNGX_LVL5YDL9O"
    },
    {
        "8029214260": "BNGX_LVLHVFU3Z"
    },
    {
        "8029214206": "BNGX_LVLSHX1OH"
    },
    {
        "8029214505": "BNGX_LVLQQPW3O"
    },
    {
        "8029214306": "BNGX_LVLXHM9ET"
    },
    {
        "8029214453": "BNGX_LVLTCGKXZ"
    },
    {
        "8029214518": "BNGX_LVL64XUVR"
    },
    {
        "8029214191": "BNGX_LVLKNOWXA"
    },
    {
        "8029214399": "BNGX_LVL77STUQ"
    },
    {
        "8029214193": "BNGX_LVL9G7J9N"
    },
    {
        "8029214540": "BNGX_LVLBPAYIZ"
    },
    {
        "8029214339": "BNGX_LVLWU652K"
    },
    {
        "8029214285": "BNGX_LVL6Z8J1H"
    },
    {
        "8029214482": "BNGX_LVLTZU3RD"
    },
    {
        "8029214431": "BNGX_LVLGOCVYE"
    },
    {
        "8029214330": "BNGX_LVLT9U79Z"
    },
    {
        "8029220737": "BNGX_LVL6IGQM8"
    },
    {
        "8029220522": "BNGX_LVL9N9SZN"
    },
    {
        "8029220551": "BNGX_LVLASMUV1"
    },
    {
        "8029220749": "BNGX_LVLPI92CK"
    },
    {
        "8029220943": "BNGX_LVLM6XMJU"
    },
    {
        "8029220793": "BNGX_LVLYMO28K"
    },
    {
        "8029220880": "BNGX_LVLMIMI0R"
    },
    {
        "8029220940": "BNGX_LVL06DAUN"
    },
    {
        "8029221060": "BNGX_LVLLU7TTR"
    },
    {
        "8029220944": "BNGX_LVL62LVBC"
    },
    {
        "8029221190": "BNGX_LVL1SCS2B"
    },
    {
        "8029221262": "BNGX_LVLSIBK15"
    },
    {
        "8029221389": "BNGX_LVL0ZJNS9"
    },
    {
        "8029221305": "BNGX_LVLIS3UNM"
    },
    {
        "8029221188": "BNGX_LVLZI4PM4"
    },
    {
        "8029221334": "BNGX_LVLXYV7XZ"
    },
    {
        "8029221199": "BNGX_LVLNEQCF1"
    },
    {
        "8029221363": "BNGX_LVLAEUKP2"
    },
    {
        "8029221403": "BNGX_LVLLOYL44"
    },
    {
        "8029221590": "BNGX_LVL1F70GH"
    },
    {
        "8029221472": "BNGX_LVLNCT84T"
    },
    {
        "8029221441": "BNGX_LVL776EPM"
    },
    {
        "8029221824": "BNGX_LVLFWF40I"
    },
    {
        "8029221562": "BNGX_LVLBIZHFP"
    },
    {
        "8029221544": "BNGX_LVLSJJ1CK"
    },
    {
        "8029221692": "BNGX_LVLD1YTQ8"
    },
    {
        "8029221640": "BNGX_LVLRRBQS8"
    },
    {
        "8029221810": "BNGX_LVLDAAP59"
    },
    {
        "8029221757": "BNGX_LVLAN4OVE"
    },
    {
        "8029221588": "BNGX_LVLJCTKJP"
    }
]


JWT_API_TEMPLATE = "http://us-az-phx.hostbu.com:5022/login?uid={uid}&password={password}"

# ============================================================
#  ط·آ§ط¸â€‍ط·آ¥ط·آ¹ط·آ¯ط·آ§ط·آ¯ط·آ§ط·ع¾
# ============================================================
TIMEOUT_PER_REQUEST = 20.0   # أ¢â€ ع¯ 20 ط·آ«ط·آ§ط¸â€ ط¸ظ¹ط·آ© ط¸â€‍ط¸ئ’ط¸â€‍ ط·آ­ط·آ³ط·آ§ط·آ¨
REQUEST_DELAY = 0.0
CACHE_DURATION = 10000

# أ¢إ“â€¦ ط¸â€‍ط·آ§ ط·آ¯ط¸ظ¾ط·آ¹ط·آ§ط·ع¾ أ¢â‚¬â€‌ ط¸ظ¾ط¸â€ڑط·آ· 5 ط·آ­ط·آ³ط·آ§ط·آ¨ط·آ§ط·ع¾ ط¸â€¦ط·ع¾ط·آ²ط·آ§ط¸â€¦ط¸â€ ط·آ© ط¸ظ¾ط¸ظ¹ ط¸â€ ط¸ظ¾ط·آ³ ط·آ§ط¸â€‍ط¸â€‍ط·آ­ط·آ¸ط·آ© (5 ط·آ¨ط¸â‚¬ 5)
MAX_CONCURRENT = 5


CACHE = {
    "tokens": {},
    "timestamp": 0
}

COLLECTED_TOKENS = {}
IS_FETCHING = False


# ============================================================
#  ط·آ¬ط¸â€‍ط·آ¨ ط·ع¾ط¸ث†ط¸ئ’ط¸â€  ط·آ­ط·آ³ط·آ§ط·آ¨ ط¸ث†ط·آ§ط·آ­ط·آ¯ أ¢â‚¬â€‌ timeout 20s
# ============================================================
async def fetch_one_token(session, uid, password, semaphore):
    """
    ط·آ¬ط¸â€‍ط·آ¨ ط·ع¾ط¸ث†ط¸ئ’ط¸â€  ط¸ث†ط·آ§ط·آ­ط·آ¯ ط¸â€¦ط·آ¹ timeout 20 ط·آ«ط·آ§ط¸â€ ط¸ظ¹ط·آ©.
    ط¸ظ¹ط·آ³ط·ع¾ط·آ®ط·آ¯ط¸â€¦ semaphore ط¸â€‍ط¸â€‍ط·ع¾ط·آ­ط¸ئ’ط¸â€¦ ط¸ظ¾ط¸ظ¹ ط·آ§ط¸â€‍ط·ع¾ط¸ث†ط·آ§ط·آ²ط¸ظ¹.
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

                # أ¢â€‌â‚¬أ¢â€‌â‚¬أ¢â€‌â‚¬ ط¸â€¦ط·آ­ط·آ§ط¸ث†ط¸â€‍ط·آ© JSON أ¢â€‌â‚¬أ¢â€‌â‚¬أ¢â€‌â‚¬
                try:
                    data = json.loads(text)
                    if isinstance(data, dict):
                        if data.get("ok") and data.get("token"):
                            print(f"[{uid}] أ¢إ“â€¦ OK ({elapsed:.2f}s) | "
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

                # أ¢â€‌â‚¬أ¢â€‌â‚¬أ¢â€‌â‚¬ fallback: ط¸â€ ط·آµ ط¸â€¦ط·آ¨ط·آ§ط·آ´ط·آ± أ¢â€‌â‚¬أ¢â€‌â‚¬أ¢â€‌â‚¬
                token = text.strip()
                if len(token) > 20:
                    print(f"[{uid}] أ¢إ“â€¦ OK raw ({elapsed:.2f}s)")
                    return uid, token, None, None, None

                return uid, None, None, None, "empty_response"

        except asyncio.TimeoutError:
            print(f"[{uid}] أ¢عˆآ± timeout after {TIMEOUT_PER_REQUEST}s")
            return uid, None, None, None, "timeout"
        except aiohttp.ClientError as e:
            print(f"[{uid}] أ¢â€Œإ’ connection error: {e}")
            return uid, None, None, None, f"conn_error"
        except Exception as e:
            print(f"[{uid}] أ¢â€Œإ’ {type(e).__name__}: {e}")
            return uid, None, None, None, "exception"


# ============================================================
#  ط·آ¬ط¸â€‍ط·آ¨ ط¸ئ’ط¸â€‍ ط·آ§ط¸â€‍ط·آ­ط·آ³ط·آ§ط·آ¨ط·آ§ط·ع¾ أ¢â‚¬â€‌ 5 ط¸ظ¾ط¸ظ¹ ط¸â€ ط¸ظ¾ط·آ³ ط·آ§ط¸â€‍ط¸ث†ط¸â€ڑط·ع¾ ط¸ظ¾ط¸â€ڑط·آ· (ط·آ¨ط·آ¯ط¸ث†ط¸â€  ط·آ¯ط¸ظ¾ط·آ¹ط·آ§ط·ع¾)
# ============================================================
async def fetch_all(accounts: dict, max_concurrent: int = 5):
    """
    ط¸ظ¹ط·آ±ط·آ³ط¸â€‍ ط¸ئ’ط¸â€‍ ط·آ§ط¸â€‍ط·آ­ط·آ³ط·آ§ط·آ¨ط·آ§ط·ع¾ ط¸â€¦ط·آ±ط·آ© ط¸ث†ط·آ§ط·آ­ط·آ¯ط·آ© ط¸â€‍ط¸â‚¬ asyncioط·إ’
    ط¸â€‍ط¸ئ’ط¸â€  Semaphore(max_concurrent) ط¸ظ¹ط·آ¶ط¸â€¦ط¸â€  ط·ع¾ط·آ´ط·ط›ط¸ظ¹ط¸â€‍ 5 ط¸ظ¾ط¸â€ڑط·آ· ط·آ¨ط·آ§ط¸â€‍ط·ع¾ط¸ث†ط·آ§ط·آ²ط¸ظ¹.
    ط·آ§ط¸â€‍ط·آ¨ط·آ§ط¸â€ڑط¸ظ¹ ط¸ظ¹ط¸â€ ط·ع¾ط·آ¸ط·آ±ط¸ث†ط¸â€  ط·آ¯ط¸ث†ط·آ±ط¸â€،ط¸â€¦ ط·ع¾ط¸â€‍ط¸â€ڑط·آ§ط·آ¦ط¸ظ¹ط·آ§ط¸â€¹ (5 ط·آ¨ط¸â‚¬ 5) ط·آ¨ط·آ¯ط¸ث†ط¸â€  ط·آ¯ط¸ظ¾ط·آ¹ط·آ§ط·ع¾.
    """
    total = len(accounts)
    print(f"\n{'='*60}")
    print(f"ظ‹ع؛â€œظ¹ Total accounts   : {total}")
    print(f"ظ‹ع؛â€œظ¹ Concurrent limit : {max_concurrent} (5 by 5)")
    print(f"ظ‹ع؛â€œظ¹ Timeout/req      : {TIMEOUT_PER_REQUEST}s")
    print(f"{'='*60}\n")

    semaphore = asyncio.Semaphore(max_concurrent)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_one_token(session, uid, password, semaphore)
            for uid, password in accounts.items()
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # ط·ع¾ط·آ¬ط¸â€¦ط¸ظ¹ط·آ¹ ط·آ§ط¸â€‍ط¸â€ ط·ع¾ط·آ§ط·آ¦ط·آ¬
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
    print(f"أ¢إ“â€¦ ALL DONE: {len(tokens)}/{total} succeeded | {len(failed)} failed")
    print(f"{'='*60}\n")

    return tokens, failed


# ============================================================
#  ط¸â€¦ط·آ³ط·آ§ط·آ¹ط·آ¯ط·آ§ط·ع¾
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
    ط¸ظ¹ط·آ¬ط¸â€‍ط·آ¨ ط¸ئ’ط¸â€‍ ط·آ§ط¸â€‍ط·ع¾ط¸ث†ط¸ئ’ط¸â€ ط·آ§ط·ع¾ أ¢â‚¬â€‌ 5 ط·آ­ط·آ³ط·آ§ط·آ¨ط·آ§ط·ع¾ ط¸ظ¾ط¸â€ڑط·آ· ط¸ظ¾ط¸ظ¹ ط¸â€ ط¸ظ¾ط·آ³ ط·آ§ط¸â€‍ط¸â€‍ط·آ­ط·آ¸ط·آ© (5 ط·آ¨ط¸â‚¬ 5).
    """
    global IS_FETCHING

    # optional query param ط¸â€‍ط¸â€‍ط·ع¾ط·آ­ط¸ئ’ط¸â€¦ ط¸ظ¾ط¸ظ¹ ط·آ§ط¸â€‍ط·ع¾ط¸ث†ط·آ§ط·آ²ط¸ظ¹ (ط·آ§ط¸ظ¾ط·ع¾ط·آ±ط·آ§ط·آ¶ط¸ظ¹ 5)
    max_concurrent = int(request.args.get("concurrent", MAX_CONCURRENT))
    max_concurrent = max(1, min(max_concurrent, 50))

    # 1) ط¸ئ’ط·آ§ط·آ´ ط·آ´ط·ط›ط·آ§ط¸â€‍ أ¢â€ â€™ ط·آ±ط·آ¬ط¸â€کط·آ¹ ط¸ظ¾ط¸ث†ط·آ±ط·آ§ط¸â€¹
    if is_cache_valid():
        return jsonify({
            "ok": True,
            "source": "cache",
            "count": len(CACHE["tokens"]),
            "last_update_vn": get_last_update_vn(),
            "tokens": CACHE["tokens"]
        })

    # 2) ط·آ·ط¸â€‍ط·آ¨ ط·آ¢ط·آ®ط·آ± ط·آ´ط·ط›ط·آ§ط¸â€‍ أ¢â€ â€™ ط¸â€‍ط·آ§ ط·ع¾ط¸ئ’ط·آ±ط·آ±
    if IS_FETCHING:
        return jsonify({
            "ok": False,
            "error": "fetch_in_progress",
            "message": "Fetch already running. Wait and retry.",
        }), 429

    # 3) ط·آ§ط·آ¨ط·آ¯ط·آ£ ط·آ§ط¸â€‍ط·آ¬ط¸â€‍ط·آ¨
    IS_FETCHING = True
    try:
        all_accounts = group_accounts[0]

        tokens, failed = asyncio.run(
            fetch_all(all_accounts, max_concurrent=max_concurrent)
        )

        # ط·آ­ط¸ظ¾ط·آ¸ ط¸ظ¾ط¸ظ¹ ط·آ§ط¸â€‍ط¸ئ’ط·آ§ط·آ´
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
    """ط·آ§ط·آ®ط·ع¾ط·آ¨ط·آ§ط·آ± ط·آ­ط·آ³ط·آ§ط·آ¨ ط¸ث†ط·آ§ط·آ­ط·آ¯."""
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
    """ط·آ­ط·آ§ط¸â€‍ط·آ© ط·آ§ط¸â€‍ط·آ¬ط¸â€‍ط·آ¨ ط·آ§ط¸â€‍ط·آ­ط·آ§ط¸â€‍ط¸ظ¹ط·آ©."""
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
#  ط·آ§ط¸â€‍ط·ع¾ط·آ´ط·ط›ط¸ظ¹ط¸â€‍
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print("=" * 60)
    print("   JWT Fetcher أ¢â‚¬â€‌ 5 accounts at a time (no batches)")
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
