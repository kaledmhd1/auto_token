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
    "8079699291": "BNGX_LVLPR08JF",
    "8066999907": "BNGX_LVLSX0G2W",
    "8066992911": "BNGX_LVL4RCFTX",
    "8066982672": "BNGX_LVLHY0F1C",
    "8066996063": "BNGX_LVLBLDKCD",
    "8038877311": "BNGX_LVLKV6V7O",
    "8066999035": "BNGX_LVLPXTVB3",
    "8038877728": "BNGX_LVLIU7UTH",
    "8034804445": "BNGX_LVLR8WIUX",
    "8034806367": "BNGX_LVLKWAQ34",
    "8038862761": "BNGX_LVLRTCM6H",
    "8038863233": "BNGX_LVLC2AF0R",
    "8034810902": "BNGX_LVLYFA85A",
    "8066982592": "BNGX_LVL1H4GTU",
    "8038869475": "BNGX_LVLRJU58N",
    "8038854276": "BNGX_LVLDUV389",
    "8038860946": "BNGX_LVL1WYVCG",
    "8038853208": "BNGX_LVLJRAADL",
    "8034811279": "BNGX_LVLXQD34G",
    "8034810973": "BNGX_LVLEKQXA6",
    "8034801291": "BNGX_LVLSR8N4A",
    "8034800521": "BNGX_LVL5MLGWA",
    "8038834608": "BNGX_LVLXWIK4L",
    "8038853945": "BNGX_LVLZRV4EE",
    "8038859994": "BNGX_LVLFQT228",
    "8055651048": "BNGX_LVL4DG0MT",
    "8038859608": "BNGX_LVL93UMWQ",
    "8034799198": "BNGX_LVLVTZ0RW",
    "8038879111": "BNGX_LVLX3X8LR",
    "8038876706": "BNGX_LVLBS2R6C",
    "8034802384": "BNGX_LVL5Y9PHF",
    "8038873664": "BNGX_LVLFXZBWX",
    "8038877142": "BNGX_LVLW4381I",
    "8038862636": "BNGX_LVL3FT5OK",
    "8038862547": "BNGX_LVLXB63FZ",
    "8079727876": "BNGX_LVLJ390EV",
    "8079723360": "BNGX_LVLV7HDBW",
    "8038861882": "BNGX_LVLW1HA4S",
    "8038844608": "BNGX_LVL6D9BBP",
    "8079657969": "BNGX_LVL4PMTCA",
    "8034804343": "BNGX_LVL4J4O9T",
    "8079683964": "BNGX_LVLTW7YOV",
    "8079701762": "BNGX_LVLYSR6JC",
    "8079735082": "BNGX_LVLF41JQ9",
    "8079712649": "BNGX_LVL4VRLKN",
    "8079722442": "BNGX_LVL07FRW4",
    "8079700661": "BNGX_LVLNW8TG3",
    "8079716143": "BNGX_LVL4M549A",
    "8079654158": "BNGX_LVL2GQS6Y",
    "8003219308": "BNGX_LVL#NQ2LRX",
    "8003196049": "BNGX_LVL#RTE9O0",
    "8079743692": "BNGX_LVL5WJLO2",
    "8079738807": "BNGX_LVLMSRC5N",
    "8079707575": "BNGX_LVLAOR4S8",
    "8038860777": "BNGX_LVL5RDJK2",
    "8034810560": "BNGX_LVL6K7XUX",
    "8003211163": "BNGX_LVL#7FT8JR",
    "8034799735": "BNGX_LVLRQP9YK",
    "8038862988": "BNGX_LVL61AGA3",
    "8003192838": "BNGX_LVL#S01DS9",
    "8079769555": "BNGX_LVLABFXGT",
    "8003196055": "BNGX_LVL#MHUW1O",
    "8003199660": "BNGX_LVL#U3PKTN",
    "8003192903": "BNGX_LVL#IOPI8T",
    "8003223900": "BNGX_LVL#CZQSNP",
    "8003223968": "BNGX_LVL#LUUUSI",
    "8003200990": "BNGX_LVL#X7M23F",
    "8003205657": "BNGX_LVL#IGN3SY",
    "8003242599": "BNGX_LVL#DB58AC",
    "8021724666": "BNGX_LVL4QU990",
    "8003242341": "BNGX_LVL#1V8D7B",
    "8021764427": "BNGX_LVLX2TVYT",
    "8003205695": "BNGX_LVL#NKW0VC",
    "8003242421": "BNGX_LVL#Q9DRC9",
    "8003233769": "BNGX_LVL#A3N6B4",
    "7990615450": "BNGX_LVL#YKJG3Y",
    "8021764495": "BNGX_LVLCPT59Y",
    "8021723323": "BNGX_LVLBKA4LQ",
    "8003194342": "BNGX_LVL#DDV78I",
    "7990624805": "BNGX_LVL#D120BQ",
    "7990624853": "BNGX_LVL#W07VV2",
    "8021755732": "BNGX_LVLNFVCMP",
    "7990631689": "BNGX_LVL#AKSDSM",
    "8021731979": "BNGX_LVLJFJOC2",
    "8021716581": "BNGX_LVL7EPEF2",
    "8021732322": "BNGX_LVLW6JUC0",
    "8003223779": "BNGX_LVL#IGGYL0",
    "8021689044": "BNGX_LVL0MQV4T",
    "8021708121": "BNGX_LVL16EKRA",
    "8021701835": "BNGX_LVLCTZNY4",
    "8034805212": "BNGX_LVLM80VBH",
    "7990625004": "BNGX_LVL#J55Y2D",
    "7990615434": "BNGX_LVL#YO1M5G",
    "8021707361": "BNGX_LVLFJD6AQ",
    "8021715660": "BNGX_LVLHUSX50",
    "8034803012": "BNGX_LVL8Q83A9",
    "8021709481": "BNGX_LVL35KQIV",
    "8021687403": "BNGX_LVLPZ771Q",
    "8034809746": "BNGX_LVLMN3NEM",
    "8021701760": "BNGX_LVLUVLA3K",
    "8021716126": "BNGX_LVLHKTEUR",
    "8003206289": "BNGX_LVL#VLCHDT",
    "8079758854": "BNGX_LVLTILZHF",
    "8003192936": "BNGX_LVL#40535V",
    "8079696591": "BNGX_LVLM98CLT",
    "8003192974": "BNGX_LVL#ZLMQXG",
    "8079709012": "BNGX_LVL5K5V47",
    "8003192931": "BNGX_LVL#G61W27",
    "8003195755": "BNGX_LVL#BKX9UF",
    "8003200041": "BNGX_LVL#611VRK",
    "8079748998": "BNGX_LVLJTYMFF",
    "8003205522": "BNGX_LVL#KWYKQF",
    "8003206194": "BNGX_LVL#52C2LB",
    "8003210968": "BNGX_LVL#RROQE7",
    "8003211415": "BNGX_LVL#GILDEY",
    "8003200204": "BNGX_LVL#Z6DSQN",
    "8003219505": "BNGX_LVL#LLRGMQ",
    "8003215421": "BNGX_LVL#PTVXTQ",
    "8003219755": "BNGX_LVL#WDRHV5",
    "8066984151": "BNGX_LVLHSEUFX",
    "8003196056": "BNGX_LVL#UZTNP0",
    "8003220266": "BNGX_LVL#WZCIYN",
    "8003219943": "BNGX_LVL#7TKNF2",
    "8003220134": "BNGX_LVL#QCOJRK",
    "8003223875": "BNGX_LVL#AQWQ21",
    "8003220120": "BNGX_LVL#UQUTBZ",
    "8003224231": "BNGX_LVL#R9NVQM",
    "8003224232": "BNGX_LVL#BWTB1J",
    "8003229200": "BNGX_LVL#8JSSMI",
    "8003229219": "BNGX_LVL#P9HZGP",
    "8003206336": "BNGX_LVL#BSUMNM",
    "8003201185": "BNGX_LVL#CAP1O2",
    "8003229650": "BNGX_LVL#L22ESZ",
    "8003233000": "BNGX_LVL#S0LZD6",
    "8003233037": "BNGX_LVL#E14BY3",
    "8003219329": "BNGX_LVL#KFEOJP",
    "8003237701": "BNGX_LVL#FDX5GI",
    "8003192873": "BNGX_LVL#LQ63Q7",
    "8003238114": "BNGX_LVL#TSBSHS",
    "7990617337": "BNGX_LVL#RE342T",
    "7990617276": "BNGX_LVL#6XH8XT",
    "7990617485": "BNGX_LVL#8X846I",
    "7990617558": "BNGX_LVL#WRLMIT",
    "7990624716": "BNGX_LVL#2IPW7E",
    "7990616875": "BNGX_LVL#BLHZ3D",
    "7990624635": "BNGX_LVL#1LW41G",
    "8003210691": "BNGX_LVL#4P9XEO",
    "8003242697": "BNGX_LVL#BTTKJY",
    "7990617489": "BNGX_LVL#C3Q2SV",
    "7990617152": "BNGX_LVL#QHNQAB",
    "8003237925": "BNGX_LVL#66NEDN",
    "7990624354": "BNGX_LVL#FTUV92",
    "7990617468": "BNGX_LVL#DMUE3B",
    "7990617351": "BNGX_LVL#0Y5NQ6",
    "7990624745": "BNGX_LVL#N4O7CI",
    "7990624521": "BNGX_LVL#0CF32W",
    "8021700721": "BNGX_LVLCMQ0GB",
    "8021700867": "BNGX_LVLAVHC27",
    "8034805928": "BNGX_LVLZFBJ4Y",
    "8021700632": "BNGX_LVLP0RW0M",
    "8021701014": "BNGX_LVLN5WB2D",
    "8021715806": "BNGX_LVLNLIZL2",
    "8021716218": "BNGX_LVLVMJ4XF",
    "8021716144": "BNGX_LVLNO4VIZ",
    "8021701692": "BNGX_LVLT9J034",
    "8021701782": "BNGX_LVLVX253F",
    "8034811099": "BNGX_LVL40RHC3",
    "8021716351": "BNGX_LVLQRTGF9",
    "8021699791": "BNGX_LVL4NZQ9T",
    "8021706595": "BNGX_LVL4HTLWU",
    "8021701544": "BNGX_LVLBJULT6",
    "8021716913": "BNGX_LVL5C2DKN",
    "8021715268": "BNGX_LVLGB89DC",
    "8021709274": "BNGX_LVLMA0FV6",
    "8021732278": "BNGX_LVLHKW1HQ",
    "8021731905": "BNGX_LVLIES3QD",
    "8021724277": "BNGX_LVLHFM56A",
    "8021729844": "BNGX_LVLWGSLFA",
    "8021731971": "BNGX_LVLIG6LBC",
    "8021731214": "BNGX_LVLN2LXZL",
    "8021709225": "BNGX_LVLY1N224",
    "7990632168": "BNGX_LVL#RYGVTA",
    "8003211201": "BNGX_LVL#C7KXAH",
    "8021708194": "BNGX_LVLX1QAH6",
    "7990631662": "BNGX_LVL#JDLNE9",
    "8021708741": "BNGX_LVL86XQDV",
    "8021708806": "BNGX_LVL4BMTAN",
    "8003211245": "BNGX_LVL#35ISN5",
    "8059059064": "BNGX_LVL5OZ9ML",
    "8003233789": "BNGX_LVL#0E939I",
    "7990615392": "BNGX_LVL#E0PQTB",
    "7990624255": "BNGX_LVL#BBO8DT",
    "8034801655": "BNGX_LVLM5FK0Z",
    "8021691855": "BNGX_LVLB1BABB",
    "8021694300": "BNGX_LVL2QEMKF",
    "8021700829": "BNGX_LVLHYG7QN",
    "8003192920": "BNGX_LVL#F1HCP8",
    "8003194394": "BNGX_LVL#VAK8CS",
    "8003229018": "BNGX_LVL#S8667N",
    "8021729465": "BNGX_LVLGG1AOA",
    "8003229027": "BNGX_LVL#LGRF5R",
    "7990615376": "BNGX_LVL#J7ABX9",
    "7990631702": "BNGX_LVL#HUSB3C",
    "8003228742": "BNGX_LVL#5EA0VA",
    "8021747186": "BNGX_LVLNN3KO9",
    "8003211186": "BNGX_LVL#0WBR6A",
    "8003228895": "BNGX_LVL#RJHB49",
    "7990632110": "BNGX_LVL#5J3T9T",
    "8021730455": "BNGX_LVL1OH5ZE",
    "8003229033": "BNGX_LVL#5WZRU9",
    "8021708905": "BNGX_LVL0UGJ67",
    "8021708789": "BNGX_LVLDJGAX7",
    "7990615451": "BNGX_LVL#36GWHU",
    "8003242762": "BNGX_LVL#DZ7I8D",
    "8021687385": "BNGX_LVLVZ8S9G",
    "8003215629": "BNGX_LVL#78GKMP",
    "8003210665": "BNGX_LVL#8A3I5D",
    "8003237897": "BNGX_LVL#QK064B",
    "8003224145": "BNGX_LVL#PRXDC6",
    "8003220397": "BNGX_LVL#9Q9QHN",
    "8003237522": "BNGX_LVL#CCDSD6",
    "8003237748": "BNGX_LVL#ZT6M5S",
    "8003242345": "BNGX_LVL#T2HRGA",
    "8003233968": "BNGX_LVL#0CK5UB",
    "8003224304": "BNGX_LVL#XS3ZXA",
    "8021694281": "BNGX_LVL9WZEBN",
    "7990631429": "BNGX_LVL#4ZI0GB",
    "8003211147": "BNGX_LVL#BZCW70",
    "7990625165": "BNGX_LVL#IMNHDY",
    "7990624959": "BNGX_LVL#N1W8EO",
    "8021687399": "BNGX_LVLD57QUI",
    "8003229195": "BNGX_LVL#14SBWB",
    "8003219509": "BNGX_LVL#IV028L",
    "8003234088": "BNGX_LVL#FQ98V4",
    "8003241915": "BNGX_LVL#Y4RXA4",
    "8003192835": "BNGX_LVL#8BP4ID",
    "8003237658": "BNGX_LVL#N5S8Z1",
    "8003228496": "BNGX_LVL#9OJE6D",
    "7990617561": "BNGX_LVL#TG079D",
    "8003220185": "BNGX_LVL#8L1X91",
    "7990624434": "BNGX_LVL#SLWEOY",
    "8003210515": "BNGX_LVL#5MO0MS",
    "7990624570": "BNGX_LVL#0OD7C0",
    "8003211354": "BNGX_LVL#EU4GVE",
    "8021756093": "BNGX_LVLQORKX7",
    "8038817374": "BNGX_LVLCP8S9B",
    "8003196063": "BNGX_LVL#0AVYX3",
    "8061623365": "BNGX_LVLEREZBO",
    "8079673300": "BNGX_LVL2NWMNN",
    "8051311758": "BNGX_LVLIIF5SY",
    "8003241975": "BNGX_LVL#FDERV5",
    "8003220409": "BNGX_LVL#U593UD",
    "8003234000": "BNGX_LVL#DDNOV9",
    "8021688770": "BNGX_LVLFXE47I",
    "8079770200": "BNGX_LVLISSPR7",
    "8003206398": "BNGX_LVL#V9JPAZ",
    "8034806247": "BNGX_LVLROAS2G",
    "8003224373": "BNGX_LVL#9DH1BC",
    "8003220235": "BNGX_LVL#D8CFSI",
    "8003195876": "BNGX_LVL#68H1AH",
    "8003229183": "BNGX_LVL#H2I430",
    "8003223784": "BNGX_LVL#8ACAXR",
    "8034798870": "BNGX_LVLUFNSIG",
    "8079689631": "BNGX_LVL53HZR9",
    "8038860146": "BNGX_LVLG5CWJI",
    "8079705688": "BNGX_LVLM899J4",
    "8061632772": "BNGX_LVLZDEXLR",
    "8055649231": "BNGX_LVL77REFK",
    "8038868445": "BNGX_LVLMMXRYQ",
    "8034804837": "BNGX_LVLVCQ9FY",
    "8061617971": "BNGX_LVL0ZVM8N",
    "8079708996": "BNGX_LVLOWN95M",
    "8079669697": "BNGX_LVLOCK8RM",
    "8034809298": "BNGX_LVLA8SAH7",
    "8038852646": "BNGX_LVLJE6YBC",
    "8066998319": "BNGX_LVL9J51K4",
    "8034798869": "BNGX_LVLMXOEB7",
    "8079699616": "BNGX_LVLOYY6PX",
    "8079654351": "BNGX_LVLM64WWZ",
    "8079695684": "BNGX_LVL1I8Y37",
    "8038818756": "BNGX_LVLFMOVYB",
    "8051310247": "BNGX_LVLSOUL5W",
    "8034800556": "BNGX_LVL8YNGQO",
    "8060796730": "BNGX_LVL3VO1A6",
    "8060795630": "BNGX_LVLIF6TXO",
    "8060795546": "BNGX_LVLFZNSOA",
    "8060794493": "BNGX_LVLIUGITD",
    "8060793357": "BNGX_LVL0Y5AJ9",
    "8060800066": "BNGX_LVLJTN727",
    "8060791799": "BNGX_LVL3AMWRD",
    "8060800308": "BNGX_LVL30NZ9O",
    "8060802849": "BNGX_LVL9BKKIQ",
    "8060798148": "BNGX_LVL95UNIE",
    "8060792840": "BNGX_LVLZVNARM",
    "8060791793": "BNGX_LVLU48R0H",
    "8060798760": "BNGX_LVLOP45UO",
    "8060796581": "BNGX_LVLFPVRNV",
    "8060794442": "BNGX_LVL50CD9G",
    "8060800210": "BNGX_LVLD18UZP",
    "8060804168": "BNGX_LVLRW39KG",
    "8060802807": "BNGX_LVLWLVBB5",
    "8060799480": "BNGX_LVLEVEJHE",
    "8060804157": "BNGX_LVLY2O5C2",
    "8060797035": "BNGX_LVLI7L2IK",
    "8060805480": "BNGX_LVLF9O140",
    "8060798829": "BNGX_LVLCCVHBG",
    "8060798510": "BNGX_LVLPZKZCR",
    "8060805395": "BNGX_LVLQY5027",
    "8060806014": "BNGX_LVLJ1R0QU",
    "8060793365": "BNGX_LVL9LIO39",
    "8060790163": "BNGX_LVLJN188F",
    "8060808257": "BNGX_LVLBW51P2",
    "8060807630": "BNGX_LVLNHIDTT",
    "8060800638": "BNGX_LVLF94HOG",
    "8060808725": "BNGX_LVLLFR1FU",
    "8060809467": "BNGX_LVLN4QD9L",
    "8060803181": "BNGX_LVL79I3ST",
    "8060807367": "BNGX_LVLC5HN20",
    "8060807040": "BNGX_LVLW1WU0M",
    "8060809286": "BNGX_LVLXDZBTS",
    "8038817206": "BNGX_LVLK8C1HS",
    "8060810683": "BNGX_LVL8104K7",
    "8038878952": "BNGX_LVLN1567F",
    "8060810325": "BNGX_LVL1OQHJU",
    "8060811372": "BNGX_LVLCVNZJJ",
    "8060811424": "BNGX_LVLOQMQP3",
    "8051304277": "BNGX_LVLBTMK4B",
    "8038875466": "BNGX_LVL1E055Z",
    "8051304292": "BNGX_LVLPXZJ3M"
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
