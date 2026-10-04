from flask import Flask, jsonify
import asyncio
import aiohttp
import json
import time
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)


group_accounts = [
  {
    "8003192873": "BNGX_LVL~LQ63Q7",
    "8003192911": "BNGX_LVL~CQRXG1",
    "8003192821": "BNGX_LVL~APCCRK",
    "8003192936": "BNGX_LVL~40535V",
    "8003192921": "BNGX_LVL~GLD60M",
    "8003192974": "BNGX_LVL~ZLMQXG",
    "8003192957": "BNGX_LVL~XKBU39",
    "8003192961": "BNGX_LVL~SCEDHX",
    "8003192878": "BNGX_LVL~265ADT",
    "8003192860": "BNGX_LVL~M6HW5W",
    "8003192896": "BNGX_LVL~KSJH8V",
    "8003192903": "BNGX_LVL~IOPI8T",
    "8003192838": "BNGX_LVL~S01DS9",
    "8003192853": "BNGX_LVL~EXLDC7",
    "8003192931": "BNGX_LVL~G61W27",
    "8003192923": "BNGX_LVL~4M5POU",
    "8003192862": "BNGX_LVL~I9X6MR",
    "8003192884": "BNGX_LVL~W4PFWR",
    "8003192934": "BNGX_LVL~GWHEUT",
    "8003192872": "BNGX_LVL~LCR7VO",
    "8003192920": "BNGX_LVL~F1HCP8",
    "8003192844": "BNGX_LVL~GVIXT9",
    "8003192943": "BNGX_LVL~7ZNMAP",
    "8003192839": "BNGX_LVL~DSAS56",
    "8003192926": "BNGX_LVL~EQ1FTC",
    "8003192922": "BNGX_LVL~9IRY87",
    "8003192874": "BNGX_LVL~KZV8SI",
    "8003192835": "BNGX_LVL~8BP4ID",
    "8003192953": "BNGX_LVL~8GHH3C",
    "8003196090": "BNGX_LVL~I2A5VQ",
    "8003194342": "BNGX_LVL~DDV78I",
    "8003194394": "BNGX_LVL~VAK8CS",
    "8003195879": "BNGX_LVL~CZ4HPE",
    "8003195752": "BNGX_LVL~QXR81S",
    "8003194260": "BNGX_LVL~N50YDV",
    "8003195755": "BNGX_LVL~BKX9UF",
    "8003195833": "BNGX_LVL~VVIPCL",
    "8003195642": "BNGX_LVL~8LHH39",
    "8003196055": "BNGX_LVL~MHUW1O",
    "8003195920": "BNGX_LVL~5WWBMG",
    "8003195970": "BNGX_LVL~QL9W8Y",
    "8003196049": "BNGX_LVL~RTE9O0",
    "8003195851": "BNGX_LVL~LQJI13",
    "8003195958": "BNGX_LVL~OXCH62",
    "8003196063": "BNGX_LVL~0AVYX3",
    "8003196078": "BNGX_LVL~75XN05",
    "8003195999": "BNGX_LVL~LM8IXN",
    "8003195876": "BNGX_LVL~68H1AH",
    "8003196016": "BNGX_LVL~0ID74A",
    "8003195775": "BNGX_LVL~X808GX",
    "8003195710": "BNGX_LVL~V8Y9OX",
    "8003195850": "BNGX_LVL~T94384",
    "8003196005": "BNGX_LVL~5U26KO",
    "8003196044": "BNGX_LVL~S5BETY",
    "8003195932": "BNGX_LVL~N4FOAO",
    "8003196056": "BNGX_LVL~UZTNP0",
    "8003195580": "BNGX_LVL~LXYYMM",
    "8003195964": "BNGX_LVL~SSOXKN",
    "8003195921": "BNGX_LVL~90PLUP",
    "8003199752": "BNGX_LVL~OAE44N",
    "8003199671": "BNGX_LVL~KLNHR4",
    "8003199778": "BNGX_LVL~KYCXAE",
    "8003199660": "BNGX_LVL~U3PKTN",
    "8003200057": "BNGX_LVL~BYX2SK",
    "8003199638": "BNGX_LVL~3WVB9Q",
    "8003200050": "BNGX_LVL~HPB0R6",
    "8003199909": "BNGX_LVL~DV56T8",
    "8003200041": "BNGX_LVL~611VRK",
    "8003199929": "BNGX_LVL~54C9ZV",
    "8003199658": "BNGX_LVL~W9NPYT",
    "8003199665": "BNGX_LVL~E32DZS",
    "8003200163": "BNGX_LVL~CK5RRC",
    "8003200204": "BNGX_LVL~Z6DSQN",
    "8003200182": "BNGX_LVL~SPOEZ6",
    "8003200296": "BNGX_LVL~B12YGM",
    "8003200181": "BNGX_LVL~HWDPWS",
    "8003200495": "BNGX_LVL~25Y03W",
    "8003200541": "BNGX_LVL~11VHJ1",
    "8003200584": "BNGX_LVL~SC1COO",
    "8003200802": "BNGX_LVL~4Y812D",
    "8003200159": "BNGX_LVL~6YN2ZY",
    "8003200699": "BNGX_LVL~SIHC6I",
    "8003201155": "BNGX_LVL~T7AGKV",
    "8003200968": "BNGX_LVL~S9M3HX",
    "8003201187": "BNGX_LVL~Y7KETY",
    "8003200976": "BNGX_LVL~BMKZFA",
    "8003201150": "BNGX_LVL~VP4Q4F",
    "8003200990": "BNGX_LVL~X7M23F",
    "8003201185": "BNGX_LVL~CAP1O2",
    "8003205291": "BNGX_LVL~HW9555",
    "8003205469": "BNGX_LVL~7L2LHT",
    "8003205643": "BNGX_LVL~2HPGZV",
    "8003205657": "BNGX_LVL~IGN3SY",
    "8003205522": "BNGX_LVL~KWYKQF",
    "8003205630": "BNGX_LVL~6ZF9LT",
    "8003205951": "BNGX_LVL~PDOEUA",
    "8003205786": "BNGX_LVL~BA7T8J",
    "8003205892": "BNGX_LVL~FSEV6A",
    "8003205638": "BNGX_LVL~Q0LGUK",
    "8003205721": "BNGX_LVL~QEPMZX",
    "8003205532": "BNGX_LVL~6W1A5U",
    "8003205695": "BNGX_LVL~NKW0VC",
    "8003206264": "BNGX_LVL~8PNHJR",
    "8003205690": "BNGX_LVL~DOH6IQ",
    "8003205641": "BNGX_LVL~T29HOH",
    "8003206296": "BNGX_LVL~PJB2B7",
    "8003205874": "BNGX_LVL~4JPSU2",
    "8003206192": "BNGX_LVL~FZW95W",
    "8003205991": "BNGX_LVL~D8CC07",
    "8003206128": "BNGX_LVL~X8VZV3",
    "8003206289": "BNGX_LVL~VLCHDT",
    "8003206247": "BNGX_LVL~ECOQ0V",
    "8003206226": "BNGX_LVL~5ZRAI9",
    "8003206278": "BNGX_LVL~DB0VLF",
    "8003206194": "BNGX_LVL~52C2LB",
    "8003206216": "BNGX_LVL~IP0433",
    "8003206336": "BNGX_LVL~BSUMNM",
    "8003206398": "BNGX_LVL~V9JPAZ",
    "8003206444": "BNGX_LVL~DEEC4V",
    "8003211135": "BNGX_LVL~PMVWRO",
    "8003210665": "BNGX_LVL~8A3I5D",
    "8003210469": "BNGX_LVL~3W1F5D",
    "8003210691": "BNGX_LVL~4P9XEO",
    "8003210353": "BNGX_LVL~CQMX18",
    "8003211007": "BNGX_LVL~UIRPUT",
    "8003211163": "BNGX_LVL~7FT8JR",
    "8003210863": "BNGX_LVL~VFCJLT",
    "8003210987": "BNGX_LVL~PZY1VC",
    "8003210271": "BNGX_LVL~EIMKWS",
    "8003211152": "BNGX_LVL~7ZN9MP",
    "8003210666": "BNGX_LVL~V7M7GP",
    "8003211385": "BNGX_LVL~STP9EC",
    "8003210968": "BNGX_LVL~RROQE7",
    "8003211006": "BNGX_LVL~N730TB",
    "8003210515": "BNGX_LVL~5MO0MS",
    "8003211354": "BNGX_LVL~EU4GVE",
    "8003211201": "BNGX_LVL~C7KXAH",
    "8003211147": "BNGX_LVL~BZCW70",
    "8003211245": "BNGX_LVL~35ISN5",
    "8003211361": "BNGX_LVL~AW2Y11",
    "8003211106": "BNGX_LVL~1IK8R8",
    "8003211186": "BNGX_LVL~0WBR6A",
    "8003211145": "BNGX_LVL~DO4ET0",
    "8003211307": "BNGX_LVL~4RS819",
    "8003211451": "BNGX_LVL~YIEI0N",
    "8003211191": "BNGX_LVL~V83EYT",
    "8003211452": "BNGX_LVL~EXFGH4",
    "8003211168": "BNGX_LVL~3JJUFY",
    "8003211415": "BNGX_LVL~GILDEY",
    "8003214862": "BNGX_LVL~K4DWP4",
    "8003214887": "BNGX_LVL~2F4ZM3",
    "8003214946": "BNGX_LVL~08CO97",
    "8003215024": "BNGX_LVL~W31245",
    "8003214982": "BNGX_LVL~JB7PTN",
    "8003215559": "BNGX_LVL~7B7ZLS",
    "8003215026": "BNGX_LVL~B48NVB",
    "8003215216": "BNGX_LVL~RJFSFM",
    "8003215127": "BNGX_LVL~KDDZW4",
    "8003215102": "BNGX_LVL~G9UIIH",
    "8003215265": "BNGX_LVL~Y7S57A",
    "8003214949": "BNGX_LVL~5SX2OC",
    "8003215258": "BNGX_LVL~QAY74Y",
    "8003215708": "BNGX_LVL~DBFM3U",
    "8003215540": "BNGX_LVL~0CYT7N",
    "8003215383": "BNGX_LVL~FHW2XD",
    "8003215091": "BNGX_LVL~EADI69",
    "8003215072": "BNGX_LVL~GDEE6A",
    "8003215561": "BNGX_LVL~DNK31D",
    "8003215185": "BNGX_LVL~FNA5T2",
    "8003215629": "BNGX_LVL~78GKMP",
    "8003215581": "BNGX_LVL~C5D43X",
    "8003215120": "BNGX_LVL~775DLZ",
    "8003215234": "BNGX_LVL~8GZCRG",
    "8003215541": "BNGX_LVL~5HSAZW",
    "8003215181": "BNGX_LVL~IK8ND7",
    "8003215421": "BNGX_LVL~PTVXTQ",
    "8003215562": "BNGX_LVL~42UY05",
    "8003215721": "BNGX_LVL~9SPC6P",
    "8003215525": "BNGX_LVL~3DY1K3",
    "8003220183": "BNGX_LVL~D2WWU3",
    "8003219780": "BNGX_LVL~QOEEZE",
    "8003219308": "BNGX_LVL~NQ2LRX",
    "8003220326": "BNGX_LVL~N5ITY6",
    "8003220451": "BNGX_LVL~MNROMR",
    "8003219505": "BNGX_LVL~LLRGMQ",
    "8003219901": "BNGX_LVL~YZJSK9",
    "8003219449": "BNGX_LVL~54WD7L",
    "8003219451": "BNGX_LVL~IJCR8X",
    "8003219297": "BNGX_LVL~10T69R",
    "8003219755": "BNGX_LVL~WDRHV5",
    "8003220034": "BNGX_LVL~PI0ISJ",
    "8003219915": "BNGX_LVL~SE1HQX",
    "8003219863": "BNGX_LVL~8LKAWO",
    "8003219329": "BNGX_LVL~KFEOJP",
    "8003220142": "BNGX_LVL~S1JQOU",
    "8003220397": "BNGX_LVL~9Q9QHN",
    "8003219509": "BNGX_LVL~IV028L",
    "8003220449": "BNGX_LVL~NEYRFK",
    "8003220210": "BNGX_LVL~ZO6JMD",
    "8003220266": "BNGX_LVL~WZCIYN",
    "8003220134": "BNGX_LVL~QCOJRK",
    "8003219520": "BNGX_LVL~4GP8ZA",
    "8003220235": "BNGX_LVL~D8CFSI",
    "8003219943": "BNGX_LVL~7TKNF2",
    "8003220073": "BNGX_LVL~6GPS9T",
    "8003220409": "BNGX_LVL~U593UD",
    "8003220185": "BNGX_LVL~8L1X91",
    "8003219992": "BNGX_LVL~8C5FDF",
    "8003220120": "BNGX_LVL~UQUTBZ",
    "8003223620": "BNGX_LVL~1Z65XP",
    "8003223650": "BNGX_LVL~5AHS0E",
    "8003223770": "BNGX_LVL~WQ8J4R",
    "8003223853": "BNGX_LVL~H5BE1P",
    "8003223968": "BNGX_LVL~LUUUSI",
    "8003223905": "BNGX_LVL~VYW6WA",
    "8003223818": "BNGX_LVL~ITY9ZO",
    "8003223779": "BNGX_LVL~IGGYL0",
    "8003223940": "BNGX_LVL~T8S5B2",
    "8003223875": "BNGX_LVL~AQWQ21",
    "8003223996": "BNGX_LVL~RICYWV",
    "8003223900": "BNGX_LVL~CZQSNP",
    "8003223784": "BNGX_LVL~8ACAXR",
    "8003224145": "BNGX_LVL~PRXDC6",
    "8003223980": "BNGX_LVL~6ZR0XH",
    "8003223911": "BNGX_LVL~AEVI14",
    "8003224274": "BNGX_LVL~7KVJS8",
    "8003224231": "BNGX_LVL~R9NVQM",
    "8003223838": "BNGX_LVL~CLZI7E",
    "8003224136": "BNGX_LVL~H7H9LE",
    "8003224268": "BNGX_LVL~4NEE4K",
    "8003224218": "BNGX_LVL~Y62TW0",
    "8003224381": "BNGX_LVL~BU3G3W",
    "8003223953": "BNGX_LVL~SNJULM",
    "8003224388": "BNGX_LVL~10FBFY",
    "8003224232": "BNGX_LVL~BWTB1J",
    "8003223941": "BNGX_LVL~A02JDI",
    "8003224373": "BNGX_LVL~9DH1BC",
    "8003224394": "BNGX_LVL~83JT4M",
    "8003224304": "BNGX_LVL~XS3ZXA",
    "8003228496": "BNGX_LVL~9OJE6D",
    "8003228756": "BNGX_LVL~4LZQUL",
    "8003228749": "BNGX_LVL~BWSXI1",
    "8003228574": "BNGX_LVL~UOX300",
    "8003229647": "BNGX_LVL~R3KEU9",
    "8003228742": "BNGX_LVL~5EA0VA",
    "8003228895": "BNGX_LVL~RJHB49",
    "8003229645": "BNGX_LVL~WXF71Z",
    "8003228810": "BNGX_LVL~NFW1PB",
    "8003228999": "BNGX_LVL~H9PJOO",
    "8003228953": "BNGX_LVL~V6OECU",
    "8003229027": "BNGX_LVL~LGRF5R",
    "8003229195": "BNGX_LVL~14SBWB",
    "8003229018": "BNGX_LVL~S8667N",
    "8003228998": "BNGX_LVL~ZBGNNI",
    "8003229033": "BNGX_LVL~5WZRU9",
    "8003229146": "BNGX_LVL~LEHC8U",
    "8003229183": "BNGX_LVL~H2I430",
    "8003228995": "BNGX_LVL~3CIHGL",
    "8003229169": "BNGX_LVL~9JE8JE",
    "8003229398": "BNGX_LVL~LBYTC4",
    "8003229390": "BNGX_LVL~KUS4XZ",
    "8003229244": "BNGX_LVL~US1I4L",
    "8003229200": "BNGX_LVL~8JSSMI",
    "8003229392": "BNGX_LVL~02PU5R",
    "8003229219": "BNGX_LVL~P9HZGP",
    "8003229540": "BNGX_LVL~5S2KDL",
    "8003229569": "BNGX_LVL~232QXW",
    "8003229650": "BNGX_LVL~L22ESZ",
    "8003229544": "BNGX_LVL~OILH7G",
    "8003233097": "BNGX_LVL~XIS6D0",
    "8003233000": "BNGX_LVL~S0LZD6",
    "8003233092": "BNGX_LVL~ZBUS9U",
    "8003233037": "BNGX_LVL~E14BY3",
    "8003233236": "BNGX_LVL~W6T5M2",
    "8003233059": "BNGX_LVL~4XQ6L5",
    "8003233443": "BNGX_LVL~VW8BDS",
    "8003233789": "BNGX_LVL~0E939I",
    "8003233848": "BNGX_LVL~W3I6WZ",
    "8003233654": "BNGX_LVL~LZ8S7P",
    "8003233744": "BNGX_LVL~D95J4M",
    "8003233357": "BNGX_LVL~WC97FX",
    "8003233769": "BNGX_LVL~A3N6B4",
    "8003233792": "BNGX_LVL~86U7YS",
    "8003233802": "BNGX_LVL~9OC4NH",
    "8003233717": "BNGX_LVL~J2HVO0",
    "8003233925": "BNGX_LVL~AE4HJX",
    "8003233239": "BNGX_LVL~P8KK1G",
    "8003233440": "BNGX_LVL~GPOYER",
    "8003233968": "BNGX_LVL~0CK5UB",
    "8003233873": "BNGX_LVL~T8AZ4M",
    "8003233962": "BNGX_LVL~JZ4X17",
    "8003234062": "BNGX_LVL~T3A4AI",
    "8003233849": "BNGX_LVL~L0A3DM",
    "8003234000": "BNGX_LVL~DDNOV9",
    "8003233963": "BNGX_LVL~JYYZXI",
    "8003234115": "BNGX_LVL~DS9BL5",
    "8003233857": "BNGX_LVL~3JE9F5",
    "8003234088": "BNGX_LVL~FQ98V4",
    "8003234050": "BNGX_LVL~MKECB8",
    "8003237630": "BNGX_LVL~F0PD12",
    "8003237522": "BNGX_LVL~CCDSD6",
    "8003237897": "BNGX_LVL~QK064B",
    "8003237775": "BNGX_LVL~OPHM48",
    "8003237693": "BNGX_LVL~BD1XRZ",
    "8003237698": "BNGX_LVL~IOO43R",
    "8003237925": "BNGX_LVL~66NEDN",
    "8003237727": "BNGX_LVL~8RAI8M",
    "8003237748": "BNGX_LVL~ZT6M5S",
    "8003237978": "BNGX_LVL~N1UWSS",
    "8003237701": "BNGX_LVL~FDX5GI",
    "8003238092": "BNGX_LVL~5S89XS",
    "8003237658": "BNGX_LVL~N5S8Z1",
    "8003237568": "BNGX_LVL~G8UTXI",
    "8003238160": "BNGX_LVL~44JD8A",
    "8003238114": "BNGX_LVL~TSBSHS",
    "8003237936": "BNGX_LVL~BSP0HV",
    "8003238148": "BNGX_LVL~AAMMZU",
    "8003238372": "BNGX_LVL~RL2SYT",
    "8003238267": "BNGX_LVL~9U7M0N",
    "8003237539": "BNGX_LVL~A8XXRL",
    "8003238447": "BNGX_LVL~K4BEJ0",
    "8003238262": "BNGX_LVL~T0KXL6",
    "8003238209": "BNGX_LVL~5NVUJ8",
    "8003238270": "BNGX_LVL~F37K0U",
    "8003238223": "BNGX_LVL~X51E43",
    "8003238218": "BNGX_LVL~5CKLIE",
    "8003238463": "BNGX_LVL~TEEU22",
    "8003238461": "BNGX_LVL~4R8S4Z",
    "8003238396": "BNGX_LVL~T7EVTB",
    "8003241921": "BNGX_LVL~GJRFL5",
    "8003242338": "BNGX_LVL~QLAHUW",
    "8003241915": "BNGX_LVL~Y4RXA4",
    "8003242185": "BNGX_LVL~7DDWVB",
    "8003242766": "BNGX_LVL~ZS35KU",
    "8003241975": "BNGX_LVL~FDERV5",
    "8003242183": "BNGX_LVL~D43DL8",
    "8003242336": "BNGX_LVL~ECLFG8",
    "8003242286": "BNGX_LVL~QHHOOO",
    "8003242440": "BNGX_LVL~2Q3TF8",
    "8003242576": "BNGX_LVL~GCQZGF",
    "8003242446": "BNGX_LVL~WVKDN8",
    "8003242349": "BNGX_LVL~DJRH3I",
    "8003242277": "BNGX_LVL~XIPCNZ",
    "8003242229": "BNGX_LVL~QWAHUG",
    "8003242345": "BNGX_LVL~T2HRGA",
    "8003242368": "BNGX_LVL~P001JT",
    "8003242697": "BNGX_LVL~BTTKJY",
    "8003242680": "BNGX_LVL~DAB50P",
    "8003242383": "BNGX_LVL~JYZ96V",
    "8003242341": "BNGX_LVL~1V8D7B",
    "8003242511": "BNGX_LVL~YM2LF6",
    "8003242421": "BNGX_LVL~Q9DRC9",
    "8003242599": "BNGX_LVL~DB58AC",
    "8003242598": "BNGX_LVL~GJJJWC",
    "8003242740": "BNGX_LVL~QP3FU5",
    "8003242761": "BNGX_LVL~NYDH94",
    "8003242762": "BNGX_LVL~DZ7I8D",
    "8003242824": "BNGX_LVL~KJZ1FP",
    "8003242641": "BNGX_LVL~LMXWP1"
}


]

# ✅ الرابط الجديد
JWT_API_TEMPLATE = "http://us-az-phx.hostbu.com:5022/login?uid={uid}&password={password}"

CACHE = {
    "tokens": {},
    "timestamp": 0
}

COLLECTED_TOKENS = {}
GROUP_INDEX = 0

CACHE_DURATION = 10000
CONCURRENT_LIMIT = 20   # خفّضناها لأن الـ API الجديد قد يكون أبطأ


async def fetch_token(session, uid, password):
    """
    يقرأ JSON من الـ API الجديد ويستخرج:
      - token
      - account_id (مفيد للفرز)
      - region
    """
    url = JWT_API_TEMPLATE.format(uid=uid, password=password)
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=45)) as resp:
            if resp.status != 200:
                return uid, None, None, None

            text = await resp.text()
            if not text:
                return uid, None, None, None

            # ─── محاولة JSON أولاً ───
            try:
                data = json.loads(text)
                if isinstance(data, dict):
                    if data.get("ok") and data.get("token"):
                        return (
                            uid,
                            data["token"],
                            str(data.get("account_id", "")),
                            data.get("region", ""),
                        )
                    return uid, None, None, None
            except json.JSONDecodeError:
                pass

            # ─── fallback: نص مباشر ───
            token = text.strip()
            if len(token) > 20:
                return uid, token, None, None
            return uid, None, None, None

    except asyncio.TimeoutError:
        print(f"[timeout] uid {uid}")
        return uid, None, None, None
    except Exception as e:
        print(f"[error] uid {uid}: {e}")
        return uid, None, None, None


async def fetch_token_with_semaphore(semaphore, session, uid, password):
    async with semaphore:
        return await fetch_token(session, uid, password)


async def fetch_tokens_for_group(group):
    tokens = {}
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_token_with_semaphore(semaphore, session, uid, password)
            for uid, password in group.items()
        ]
        results = await asyncio.gather(*tasks)
        for uid, token, acc_id, region in results:
            if token:
                tokens[uid] = token
    return tokens


def is_cache_valid():
    return (time.time() - CACHE["timestamp"]) < CACHE_DURATION and len(CACHE["tokens"]) > 0


def get_last_update_vn():
    utc_time = datetime.fromtimestamp(CACHE["timestamp"], tz=timezone.utc)
    vn_time = utc_time + timedelta(hours=7)
    return vn_time.strftime("%Y-%m-%d %H:%M:%S")


# ==================== ENDPOINTS ====================
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

        groups_to_fetch.append(group_accounts[GROUP_INDEX])

        next_index = (GROUP_INDEX + 1) % len(group_accounts)
        if next_index != GROUP_INDEX:
            groups_to_fetch.append(group_accounts[next_index])

        all_tokens = {}
        for group in groups_to_fetch:
            tokens = await fetch_tokens_for_group(group)
            all_tokens.update(tokens)

        GROUP_INDEX = (GROUP_INDEX + 2) % len(group_accounts)

        return all_tokens

    new_tokens = asyncio.run(process_groups())
    COLLECTED_TOKENS.update(new_tokens)

    if GROUP_INDEX == 0:
        CACHE["tokens"] = COLLECTED_TOKENS.copy()
        CACHE["timestamp"] = time.time()
        COLLECTED_TOKENS.clear()

    return jsonify({
        "count": len(COLLECTED_TOKENS) if not CACHE["tokens"] else len(CACHE["tokens"]),
        "last_update_vn": get_last_update_vn() if CACHE["tokens"] else None,
        "tokens": CACHE["tokens"] if CACHE["tokens"] else COLLECTED_TOKENS
    })


# ─── اختبار اتصال مباشر بـ API واحد ───
@app.route("/api/test_one", methods=["GET"])
def test_one():
    """
    Usage: /api/test_one?uid=8003192873&password=BNGX_LVL~LQ63Q7
    """
    uid = request.args.get("uid", "").strip()
    password = request.args.get("password", "").strip()
    if not uid or not password:
        return jsonify({"ok": False, "error": "provide uid & password"}), 400

    async def run():
        async with aiohttp.ClientSession() as session:
            return await fetch_token(session, uid, password)

    u, token, acc_id, region = asyncio.run(run())
    return jsonify({
        "ok": bool(token),
        "uid": u,
        "account_id": acc_id,
        "region": region,
        "token_preview": (token[:80] + "...") if token else None,
        "token_length": len(token) if token else 0,
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True, "status": "alive"})


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "JWT Group Fetcher",
        "upstream_api": JWT_API_TEMPLATE,
        "endpoints": {
            "GET /api/get_jwt": "Returns tokens batch by batch",
            "GET /api/test_one?uid=&password=": "Test one account",
            "GET /health": "Health check"
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print("=" * 60)
    print("   JWT Group Fetcher")
    print("=" * 60)
    print(f"[i] Listening    : http://0.0.0.0:{port}")
    print(f"[i] Upstream API : {JWT_API_TEMPLATE}")
    print(f"[i] Endpoint     : http://localhost:{port}/api/get_jwt")
    print(f"[i] Test one     : http://localhost:{port}/api/test_one?uid=8003192873&password=BNGX_LVL~LQ63Q7")
    print(f"[i] Health       : http://localhost:{port}/health")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, threaded=True, debug=False)
