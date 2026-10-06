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
group_accounts = [{
    "8007695996": "BNGX_LVL#3HFO19",
    "8007695896": "BNGX_LVL#99EPFK",
    "8007696130": "BNGX_LVL#OE2P7G",
    "8007695864": "BNGX_LVL#3ZX7AT",
    "8007696010": "BNGX_LVL#BI9A87",
    "8007700511": "BNGX_LVL#S9O5NV",
    "8007700599": "BNGX_LVL#E17XZ2",
    "8007700509": "BNGX_LVL#TO8L27",
    "8007700679": "BNGX_LVL#NTG3WE",
    "8007700575": "BNGX_LVL#AV7SJN",
    "8007700688": "BNGX_LVL#QRB83L",
    "8007700809": "BNGX_LVL#19ADRM",
    "8007707137": "BNGX_LVL#DAQZIF",
    "8007707403": "BNGX_LVL#KO3195",
    "8007707224": "BNGX_LVL#SW1WBS",
    "8007707435": "BNGX_LVL#O5MEIM",
    "8007707660": "BNGX_LVL#W1JO08",
    "8007707721": "BNGX_LVL#ND5UBW",
    "8007707624": "BNGX_LVL#45K9UO",
    "8007712125": "BNGX_LVL#AITQDN",
    "8007712264": "BNGX_LVL#7E15Y3",
    "8007712113": "BNGX_LVL#REG04G",
    "8007712274": "BNGX_LVL#KWG12T",
    "8007712321": "BNGX_LVL#42531N",
    "8007712168": "BNGX_LVL#EPDC4E",
    "8007652507": "BNGX_LVL#WAQVZ0",
    "8007652436": "BNGX_LVL#O4Q25J",
    "8007652445": "BNGX_LVL#KZVU1O",
    "8007652548": "BNGX_LVL#0KHQCV",
    "8007652433": "BNGX_LVL#V8OWPT",
    "8007652500": "BNGX_LVL#C4ITP8",
    "8007652432": "BNGX_LVL#YO2QYV",
    "8007652528": "BNGX_LVL#N2PV6E",
    "8007652429": "BNGX_LVL#CMRMVS",
    "8007652419": "BNGX_LVL#5PEOHL",
    "8007652446": "BNGX_LVL#8B1UPM",
    "8007652477": "BNGX_LVL#ADSUOE",
    "8007652450": "BNGX_LVL#KF4SDH",
    "8007652449": "BNGX_LVL#I2CRLL",
    "8007652451": "BNGX_LVL#A3DTOG",
    "8007652541": "BNGX_LVL#52EGXG",
    "8007652539": "BNGX_LVL#GR8OI0",
    "8007652472": "BNGX_LVL#2CQ64K",
    "8007652547": "BNGX_LVL#GQZN44",
    "8007652431": "BNGX_LVL#27BOIB",
    "8007652540": "BNGX_LVL#XVAGY9",
    "8007652448": "BNGX_LVL#Y5QW6Z",
    "8007652467": "BNGX_LVL#POZALY",
    "8007652535": "BNGX_LVL#II8VSC",
    "8007652428": "BNGX_LVL#9UKBJ7",
    "8007652497": "BNGX_LVL#0TTPRI",
    "8007652538": "BNGX_LVL#JF1AJW",
    "8007652452": "BNGX_LVL#N3Z0G2",
    "8007652370": "BNGX_LVL#BWGM5R",
    "8007652522": "BNGX_LVL#JCYWW3",
    "8007655941": "BNGX_LVL#GN9I3F",
    "8007656093": "BNGX_LVL#5PUK4Q",
    "8007655805": "BNGX_LVL#2406OG",
    "8007655924": "BNGX_LVL#M0LQUG",
    "8007655813": "BNGX_LVL#BG09PR",
    "8007656199": "BNGX_LVL#MNNGJT",
    "8007655913": "BNGX_LVL#ZIHRQT",
    "8007656143": "BNGX_LVL#DVSOOB",
    "8007655911": "BNGX_LVL#QUFTQG",
    "8007655986": "BNGX_LVL#HTJSQT",
    "8007655951": "BNGX_LVL#HGROE7",
    "8007655964": "BNGX_LVL#OMVZJ3",
    "8007656254": "BNGX_LVL#ND4JRF",
    "8007655940": "BNGX_LVL#SA4U50",
    "8007656060": "BNGX_LVL#GR2EA0",
    "8007656023": "BNGX_LVL#JCJ8AS",
    "8007655977": "BNGX_LVL#FKPTR3",
    "8007656065": "BNGX_LVL#K4QEZ3",
    "8007656079": "BNGX_LVL#LOVO22",
    "8007656161": "BNGX_LVL#VNXM23",
    "8007656141": "BNGX_LVL#MF1QH3",
    "8007656052": "BNGX_LVL#51XX9R",
    "8007656130": "BNGX_LVL#L2OVGJ",
    "8007656140": "BNGX_LVL#Z0APKQ",
    "8007656224": "BNGX_LVL#TMYC7K",
    "8007656160": "BNGX_LVL#8MGQSK",
    "8007656226": "BNGX_LVL#QO8P68",
    "8007656225": "BNGX_LVL#8EWWF2",
    "8007656249": "BNGX_LVL#2ZIQ0B",
    "8007656229": "BNGX_LVL#SYQD7H",
    "8007660143": "BNGX_LVL#2OQZAW",
    "8007660467": "BNGX_LVL#7KKBBO",
    "8007660471": "BNGX_LVL#5OAPM3",
    "8007660149": "BNGX_LVL#NQKP47",
    "8007660058": "BNGX_LVL#DZFJRA",
    "8007660146": "BNGX_LVL#2L7RVI",
    "8007660182": "BNGX_LVL#BX4JI7",
    "8007660543": "BNGX_LVL#24XQAE",
    "8007660273": "BNGX_LVL#VVXEUU",
    "8007660219": "BNGX_LVL#AT34EM",
    "8007660296": "BNGX_LVL#IW7ZRF",
    "8007660358": "BNGX_LVL#LLUHEC",
    "8007660355": "BNGX_LVL#LCMS65",
    "8007660426": "BNGX_LVL#GZ173G",
    "8007660342": "BNGX_LVL#WEV5Z2",
    "8007660311": "BNGX_LVL#Y2FVGK",
    "8007660504": "BNGX_LVL#TKA14P",
    "8007660491": "BNGX_LVL#WR373R",
    "8007660440": "BNGX_LVL#YGI9DL",
    "8007660607": "BNGX_LVL#C3EHXY",
    "8007660572": "BNGX_LVL#IM8XBD",
    "8007660451": "BNGX_LVL#SXJ00T",
    "8007660703": "BNGX_LVL#H1PUI3",
    "8007660688": "BNGX_LVL#T0UE6S",
    "8007660686": "BNGX_LVL#OMK4JP",
    "8007661000": "BNGX_LVL#JX2CY3",
    "8007661001": "BNGX_LVL#2CDRNN",
    "8007660916": "BNGX_LVL#Q88DU6",
    "8007660931": "BNGX_LVL#JO1DWJ",
    "8007660967": "BNGX_LVL#EEOXE6",
    "8007664274": "BNGX_LVL#BCOAYD",
    "8007664263": "BNGX_LVL#XRH00O",
    "8007664298": "BNGX_LVL#I7IC69",
    "8007664343": "BNGX_LVL#MV9RW2",
    "8007664292": "BNGX_LVL#Z8I545",
    "8007664383": "BNGX_LVL#DR3JUX",
    "8007664548": "BNGX_LVL#1EG552",
    "8007664312": "BNGX_LVL#AQY8JL",
    "8007664358": "BNGX_LVL#8XWW38",
    "8007664393": "BNGX_LVL#6TNWC2",
    "8007664359": "BNGX_LVL#EQ27UB",
    "8007664392": "BNGX_LVL#57P03V",
    "8007664398": "BNGX_LVL#M8FFMU",
    "8007664479": "BNGX_LVL#N5J6UV",
    "8007664434": "BNGX_LVL#41S8Q3",
    "8007664453": "BNGX_LVL#27CD5M",
    "8007664534": "BNGX_LVL#YFKQQ5",
    "8007664602": "BNGX_LVL#D13UJZ",
    "8007664555": "BNGX_LVL#DTY14U",
    "8007664601": "BNGX_LVL#R55W3D",
    "8007664598": "BNGX_LVL#DHDBHL",
    "8007664625": "BNGX_LVL#RB1SD3",
    "8007664696": "BNGX_LVL#P2H94E",
    "8007664707": "BNGX_LVL#8C537S",
    "8007664720": "BNGX_LVL#0L82LN",
    "8007664780": "BNGX_LVL#67YV44",
    "8007664789": "BNGX_LVL#CMR7SP",
    "8007664821": "BNGX_LVL#8PPAUV",
    "8007664768": "BNGX_LVL#1UK9CO",
    "8007664870": "BNGX_LVL#KUILJY",
    "8011209874": "BNGX_LVL8YHQFA",
    "8011209876": "BNGX_LVLWWE4MN",
    "8011209887": "BNGX_LVLD47RHK",
    "8011209913": "BNGX_LVLHRKDDI",
    "8011209905": "BNGX_LVLWC39LA",
    "8011209916": "BNGX_LVL46G51R",
    "8011209918": "BNGX_LVLRO2EHE",
    "8011209931": "BNGX_LVLURW502",
    "8011209911": "BNGX_LVLDLSV9M",
    "8011209924": "BNGX_LVLJCY2HG",
    "8011209917": "BNGX_LVLSKG4M7",
    "8011209932": "BNGX_LVL5RZI26",
    "8011210040": "BNGX_LVLZR4KO6",
    "8011210064": "BNGX_LVLAW4AJ6",
    "8011210106": "BNGX_LVLWPCAQB",
    "8011210056": "BNGX_LVLNMV4PA",
    "8011209928": "BNGX_LVL4FRQRX",
    "8011210093": "BNGX_LVLBEM1RA",
    "8011209920": "BNGX_LVL5NHLBT",
    "8011209923": "BNGX_LVLR291RU",
    "8011209878": "BNGX_LVLA9CJ0X",
    "8011209877": "BNGX_LVLM6M9RD",
    "8011209930": "BNGX_LVLIJ983P",
    "8011209910": "BNGX_LVLY2YVKP",
    "8011209991": "BNGX_LVLGS66WW",
    "8011210034": "BNGX_LVL24HWJD",
    "8011210036": "BNGX_LVLYLAHGG",
    "8011210086": "BNGX_LVLBY8KOC",
    "8011210071": "BNGX_LVLROIC82",
    "8011210112": "BNGX_LVL6OT7JY",
    "8011211998": "BNGX_LVLZZD3CQ",
    "8011212484": "BNGX_LVL22CWA5",
    "8011212532": "BNGX_LVL9AUU9O",
    "8011212563": "BNGX_LVLV55QYI",
    "8011212550": "BNGX_LVLMDPFLH",
    "8011212443": "BNGX_LVLYU1XEK",
    "8011212565": "BNGX_LVL8KF4B3",
    "8011212738": "BNGX_LVLC2NJUF",
    "8011212755": "BNGX_LVL412GHC",
    "8011212776": "BNGX_LVLJGURJ8",
    "8011212737": "BNGX_LVLO9XFG7",
    "8011212800": "BNGX_LVLXDFTFR",
    "8011212792": "BNGX_LVL6WVR60",
    "8011212806": "BNGX_LVLTTEGUC",
    "8011212819": "BNGX_LVLG5B77X",
    "8011212682": "BNGX_LVL9B2V9R",
    "8011212699": "BNGX_LVL3FXZ6R",
    "8011212910": "BNGX_LVL781EZD",
    "8011212770": "BNGX_LVL39R3Z3",
    "8011212978": "BNGX_LVLQFGXIC",
    "8011212772": "BNGX_LVLPB79NI",
    "8011212795": "BNGX_LVLQSTKQW",
    "8011212844": "BNGX_LVL20JUK6",
    "8011212797": "BNGX_LVLAHU4LP",
    "8011212790": "BNGX_LVLOZPEL3",
    "8011213069": "BNGX_LVLYG4268",
    "8011212989": "BNGX_LVLJSX9J8",
    "8011213014": "BNGX_LVL4L1GBJ",
    "8011213115": "BNGX_LVL26GN43",
    "8011213104": "BNGX_LVLHDDEHP",
    "8011215336": "BNGX_LVLR8NM8Q",
    "8011215350": "BNGX_LVLY004ST",
    "8011215473": "BNGX_LVLLXO26Z",
    "8011215422": "BNGX_LVLGL90E6",
    "8011215483": "BNGX_LVLCWIWSM",
    "8011215443": "BNGX_LVL50TTH9",
    "8011215526": "BNGX_LVL8AOEG8",
    "8011215329": "BNGX_LVLI2APAC",
    "8011215306": "BNGX_LVLJ5K8G6",
    "8011215562": "BNGX_LVLMK70U1",
    "8011215388": "BNGX_LVLY5WX1Z",
    "8011215582": "BNGX_LVLHCQPXV",
    "8011215404": "BNGX_LVLTRL11P",
    "8011215339": "BNGX_LVL6TUBKA",
    "8011215405": "BNGX_LVL3WB1X7",
    "8011215721": "BNGX_LVLDT53VX",
    "8011215510": "BNGX_LVLZTBOJT",
    "8011215811": "BNGX_LVLRNQXYL",
    "8011215821": "BNGX_LVL78UYLK",
    "8011215831": "BNGX_LVLVE8M6T",
    "8011215678": "BNGX_LVLEDA7GB",
    "8011215843": "BNGX_LVLZG2RVB",
    "8011215879": "BNGX_LVL77V1WB",
    "8011215905": "BNGX_LVLI28A7G",
    "8011215876": "BNGX_LVLQZGP5U",
    "8011215783": "BNGX_LVLMTKO15",
    "8011215768": "BNGX_LVLLOA1PU",
    "8011215809": "BNGX_LVLZF65QR",
    "8011215847": "BNGX_LVL7UAC34",
    "8011215840": "BNGX_LVLSYMLCD",
    "8011219316": "BNGX_LVLWKFWZO",
    "8011219086": "BNGX_LVL8G9Y8D",
    "8011219300": "BNGX_LVLOBOG8E",
    "8011219360": "BNGX_LVL8CTXIV",
    "8011219377": "BNGX_LVL07E9AT",
    "8011219295": "BNGX_LVLBYBAY8",
    "8011219476": "BNGX_LVL9VWX9A",
    "8011219447": "BNGX_LVLCR96VZ",
    "8011219479": "BNGX_LVL9QT4DD",
    "8011219478": "BNGX_LVLM1Y0UX",
    "8011219501": "BNGX_LVLS7DKPA",
    "8011219511": "BNGX_LVL74C498",
    "8011219544": "BNGX_LVLUCIBAM",
    "8011219568": "BNGX_LVLRH6NDD",
    "8011219430": "BNGX_LVLP2KB65",
    "8011219591": "BNGX_LVLMOTQT2",
    "8011219495": "BNGX_LVLV0UTDX",
    "8011219466": "BNGX_LVLIFS44P",
    "8011219664": "BNGX_LVLX9161Y",
    "8011219524": "BNGX_LVLPTUP8Q",
    "8011219485": "BNGX_LVLMV22AS",
    "8011219578": "BNGX_LVLECPUMV",
    "8011219706": "BNGX_LVL23W1LV",
    "8011219696": "BNGX_LVL83ILJW",
    "8011219628": "BNGX_LVLGV01NW",
    "8011219682": "BNGX_LVLDNDALY",
    "8011219656": "BNGX_LVLE9NK7Y",
    "8011219718": "BNGX_LVLFXVUFF",
    "8011219695": "BNGX_LVLKU3BVL",
    "8011219726": "BNGX_LVLTPSWSM",
    "8011223005": "BNGX_LVL3TEL4Q",
    "8011223094": "BNGX_LVLP07SO8",
    "8011223156": "BNGX_LVLM2KACI",
    "8011223109": "BNGX_LVLKJRCSG",
    "8011223451": "BNGX_LVLTWWJVW",
    "8011223141": "BNGX_LVLVVEEZ5",
    "8011223598": "BNGX_LVLY8B9LG",
    "8011223586": "BNGX_LVLRW2AKZ",
    "8011223639": "BNGX_LVL884D74",
    "8011223656": "BNGX_LVLAM398C",
    "8011223422": "BNGX_LVL3ICWC7",
    "8011223761": "BNGX_LVLMU0B44",
    "8011223725": "BNGX_LVL0BSBA8",
    "8011223822": "BNGX_LVLLQV2MC",
    "8011223497": "BNGX_LVLRBO2RE",
    "8011223943": "BNGX_LVLE88UY0",
    "8011223982": "BNGX_LVL6OSLCX",
    "8011223978": "BNGX_LVLA7S6GN",
    "8011224040": "BNGX_LVLARGPQT",
    "8011223990": "BNGX_LVLB4RWK3",
    "8011224028": "BNGX_LVL4NMMR4",
    "8011224074": "BNGX_LVLI641V4",
    "8011224084": "BNGX_LVL07XTOU",
    "8011223848": "BNGX_LVLJGXJJ3",
    "8011224075": "BNGX_LVLXNZMXZ",
    "8011224127": "BNGX_LVLXIXVLW",
    "8011224158": "BNGX_LVL5JEU0H",
    "8011224106": "BNGX_LVLYPMZ0Y",
    "8011224154": "BNGX_LVLEETEJT",
    "8011224196": "BNGX_LVLDOJNMR",
    "8011227162": "BNGX_LVLZGHLYQ",
    "8011227326": "BNGX_LVL03WZL3",
    "8011227366": "BNGX_LVLN0CWZJ",
    "8011227479": "BNGX_LVL4HN0AO",
    "8011227503": "BNGX_LVLK5IMGQ",
    "8011227625": "BNGX_LVLCTSE7K",
    "8011227643": "BNGX_LVLP3P88H",
    "8011227419": "BNGX_LVLE7G6H8",
    "8011227672": "BNGX_LVL9NI90X",
    "8011227737": "BNGX_LVLQBAEAH",
    "8011227738": "BNGX_LVLK8T5OO",
    "8011227789": "BNGX_LVLZ9CDU0",
    "8011227614": "BNGX_LVLZ29XPV",
    "8011227843": "BNGX_LVLOOMNGM",
    "8011227848": "BNGX_LVLZE4SC0",
    "8011227687": "BNGX_LVL5KMUXX",
    "8011227907": "BNGX_LVLOVGJFG",
    "8011227845": "BNGX_LVLPFYPHG",
    "8011227911": "BNGX_LVLNB3Z61",
    "8011227914": "BNGX_LVLTKD4O0",
    "8011227941": "BNGX_LVL6UJWOE",
    "8011227962": "BNGX_LVL5ZSX2I",
    "8011227824": "BNGX_LVLDGACOF",
    "8011227834": "BNGX_LVLHERQFJ",
    "8011227886": "BNGX_LVL309K7Q",
    "8011227847": "BNGX_LVLNM6UBW",
    "8011227842": "BNGX_LVL6ZUNSB",
    "8011227869": "BNGX_LVL2RZGFJ",
    "8011227975": "BNGX_LVLVQKSBO",
    "8011228017": "BNGX_LVLWV109U",
    "8011231274": "BNGX_LVLIM5NYH",
    "8011231333": "BNGX_LVL5O9I6A",
    "8011231410": "BNGX_LVLLYDUN6",
    "8011231300": "BNGX_LVL3DAL0P",
    "8011231248": "BNGX_LVLA2QO5U",
    "8011231636": "BNGX_LVLMAXD36",
    "8011231469": "BNGX_LVLAVMYAD",
    "8011231673": "BNGX_LVL7S8DWE",
    "8011231729": "BNGX_LVLEWZ4WL",
    "8011231789": "BNGX_LVLBIG9NQ",
    "8011231792": "BNGX_LVLMWLQTU",
    "8011231942": "BNGX_LVLCRYC65",
    "8011231970": "BNGX_LVLKJ2NR4",
    "8011231987": "BNGX_LVLQEXR2A",
    "8011231990": "BNGX_LVLKHW197",
    "8011232005": "BNGX_LVLS7EU90",
    "8011232089": "BNGX_LVL8W7E9Q",
    "8011232091": "BNGX_LVL6U8RLU",
    "8011232082": "BNGX_LVL2F0MNB",
    "8011232128": "BNGX_LVLXQ841L",
    "8011232192": "BNGX_LVLMOVTRR",
    "8011231932": "BNGX_LVLMM378I",
    "8011232030": "BNGX_LVLLHKY8A",
    "8011232018": "BNGX_LVL3FWERU",
    "8011232303": "BNGX_LVLRQKU5R",
    "8011232271": "BNGX_LVL3ENGKQ",
    "8011232160": "BNGX_LVLSW2ZWX",
    "8011232223": "BNGX_LVLJ2H6QQ",
    "8011232273": "BNGX_LVLE9WISC",
    "8011232312": "BNGX_LVLQZ36U5",
    "8011235726": "BNGX_LVLFG90TK",
    "8011235803": "BNGX_LVLFVHX0A",
    "8011235711": "BNGX_LVLHGKPS5",
    "8011236151": "BNGX_LVL761VLG",
    "8011236214": "BNGX_LVLFYGRU7",
    "8011236270": "BNGX_LVLEG462J",
    "8011236269": "BNGX_LVL80RDWK",
    "8011236120": "BNGX_LVLG2G8FT",
    "8011236349": "BNGX_LVLPM0ETW",
    "8011236211": "BNGX_LVLSG6XFJ",
    "8011236554": "BNGX_LVLO5S6CN",
    "8011236594": "BNGX_LVL42XX3T",
    "8011236497": "BNGX_LVL6H8SB2",
    "8011236504": "BNGX_LVLXZLU63",
    "8011236465": "BNGX_LVLLDZNN0",
    "8011236591": "BNGX_LVLOTSC5O",
    "8011236605": "BNGX_LVLM80MKP",
    "8011236585": "BNGX_LVL7GLM0Z",
    "8011239660": "BNGX_LVLPSWQAD",
    "8011239696": "BNGX_LVL9ITNR4",
    "8011239710": "BNGX_LVLTPBGKX",
    "8011239956": "BNGX_LVL3TM88G",
    "8011239958": "BNGX_LVL93C0OE",
    "8011239998": "BNGX_LVLYRB273",
    "8011240085": "BNGX_LVLH5AUNK",
    "8011239896": "BNGX_LVLCGIF9V",
    "8011239959": "BNGX_LVLPMJWK0",
    "8011240193": "BNGX_LVL01SGL5",
    "8011240184": "BNGX_LVL5U04CZ",
    "8011239996": "BNGX_LVL2KRQZ7",
    "8011240208": "BNGX_LVLB86H7U",
    "8011240067": "BNGX_LVLKRHCTM",
    "8011240209": "BNGX_LVLQN6582",
    "8011240099": "BNGX_LVLJPF4CM",
    "8011240233": "BNGX_LVLDLVQTZ",
    "8011240253": "BNGX_LVL93BU3M",
    "8011240284": "BNGX_LVLIH5AJT",
    "8011240329": "BNGX_LVLW6ZOXI",
    "8011240195": "BNGX_LVLSEBKQC",
    "8011240401": "BNGX_LVLDOE9A6",
    "8011240374": "BNGX_LVLZN2PMO",
    "8011240441": "BNGX_LVLQA5IG4",
    "8011240210": "BNGX_LVLD1RR1A",
    "8011240454": "BNGX_LVLDD06BO",
    "8011240471": "BNGX_LVL7G5M7M",
    "8011240476": "BNGX_LVLDOLBOZ",
    "8011240330": "BNGX_LVLTNMNPS",
    "8011240386": "BNGX_LVLCDKLCX",
    "8011243649": "BNGX_LVLCFNDUB",
    "8011243923": "BNGX_LVLBXJJ0P",
    "8011243957": "BNGX_LVLFJX6RB",
    "8011243982": "BNGX_LVLB45K8A",
    "8011243823": "BNGX_LVLHX6U6Y",
    "8011244054": "BNGX_LVL4OYKC1",
    "8011243797": "BNGX_LVL0ZDW9V",
    "8011244201": "BNGX_LVLWBKKYJ",
    "8011244252": "BNGX_LVL6103UW",
    "8011244068": "BNGX_LVLHH8U7F",
    "8011244230": "BNGX_LVLTYEJE9",
    "8011244301": "BNGX_LVLBIN9O6",
    "8011244306": "BNGX_LVLXSWEWW",
    "8011244328": "BNGX_LVLPSOJIG",
    "8011244368": "BNGX_LVLZ30QXB",
    "8011244208": "BNGX_LVLPD6A48",
    "8011244267": "BNGX_LVLNA6Y1R",
    "8011244518": "BNGX_LVLM9PI1L",
    "8011244282": "BNGX_LVLARH1U5",
    "8011244283": "BNGX_LVLEZPFAN",
    "8011244552": "BNGX_LVL537VLW",
    "8011244507": "BNGX_LVLBE9KPN",
    "8011244561": "BNGX_LVLBYBIB9",
    "8011244329": "BNGX_LVLA6O4Q2",
    "8011244490": "BNGX_LVL2PLHLD",
    "8011244545": "BNGX_LVLI3DP4T",
    "8011244524": "BNGX_LVLEEDJTS",
    "8011244547": "BNGX_LVLR47FSZ",
    "8011244544": "BNGX_LVLOC4E0X",
    "8011244534": "BNGX_LVL2H7HOS",
    "8011247313": "BNGX_LVLQB5SMA",
    "8011247344": "BNGX_LVL1O03BL",
    "8011247458": "BNGX_LVLM9SCB6",
    "8011247287": "BNGX_LVLQEKK72",
    "8011247499": "BNGX_LVL455565",
    "8011247280": "BNGX_LVL9AH41M",
    "8011247662": "BNGX_LVLH0LOM0",
    "8011247637": "BNGX_LVLFAKPLP",
    "8011247659": "BNGX_LVL5D8YZG",
    "8011247512": "BNGX_LVLA52LGL",
    "8011247754": "BNGX_LVLCWCNM2",
    "8011247853": "BNGX_LVL0425Z6",
    "8011247844": "BNGX_LVL6VM852",
    "8011247759": "BNGX_LVL6YUQAX",
    "8011247783": "BNGX_LVLQX6GC0",
    "8011247921": "BNGX_LVLKQRZT4",
    "8011247775": "BNGX_LVLIYMV97",
    "8011247823": "BNGX_LVLINQSC1",
    "8011247976": "BNGX_LVL9TPYUP",
    "8011247848": "BNGX_LVLFZLLRI",
    "8011248002": "BNGX_LVLO82SV1",
    "8011248011": "BNGX_LVLBRY2OT",
    "8011248020": "BNGX_LVL4B0F87",
    "8011247894": "BNGX_LVLQXCR0S",
    "8011248105": "BNGX_LVLHM1XAP",
    "8011248090": "BNGX_LVLAU67AD",
    "8011247953": "BNGX_LVLUXMZV6",
    "8011247947": "BNGX_LVLB15I1O",
    "8011248037": "BNGX_LVLCTGF7W",
    "8011248077": "BNGX_LVLO81RLR",
    "8011251661": "BNGX_LVLJRE78S",
    "8011251664": "BNGX_LVLTSHHAX",
    "8011251828": "BNGX_LVL7KZRSO",
    "8011251878": "BNGX_LVLU9G030",
    "8011251991": "BNGX_LVLV8WMBQ",
    "8011252030": "BNGX_LVL8UMK4B",
    "8011251887": "BNGX_LVLZV9KNZ",
    "8011252155": "BNGX_LVLT2E4BZ",
    "8011252125": "BNGX_LVL5R1L77",
    "8011252092": "BNGX_LVLHFTTXU",
    "8011252299": "BNGX_LVL0FFP82",
    "8011252285": "BNGX_LVLP0FYUW",
    "8011252365": "BNGX_LVLYR8SWZ",
    "8011252387": "BNGX_LVLTVB59L",
    "8011252400": "BNGX_LVL9CEVPR",
    "8011252407": "BNGX_LVLYLG5RA",
    "8011252426": "BNGX_LVLW1AX8P",
    "8011252242": "BNGX_LVL1RULW7",
    "8011252330": "BNGX_LVLDG90R9",
    "8011252529": "BNGX_LVLGGKW3R",
    "8011252547": "BNGX_LVLODLFOW",
    "8011252397": "BNGX_LVLWEU3IP",
    "8011252519": "BNGX_LVLQGPGOO",
    "8011252393": "BNGX_LVLWPCEX2",
    "8011252432": "BNGX_LVLFC3O9X",
    "8011252410": "BNGX_LVLFNC3M9",
    "8011252423": "BNGX_LVL9KI6JY",
    "8011252488": "BNGX_LVLGUR12C",
    "8011252537": "BNGX_LVLGXQNKS",
    "8011252546": "BNGX_LVL5OPJZT"
}]
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
