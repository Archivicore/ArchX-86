from var import Var
from fridayubot.Configs import Config
from fridayubot.utils import friday_on_cmd

issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "3.1"
if issudousing:
    amiusingsudo = "Aktif ✅"
else:
    amiusingsudo = "Mati ❌"

if islogokay:
    logchat = "Terhubung ✅"
else:
    logchat = "Tidak Terhubung ❌"

if isherokuokay:
    riplife = "Terhubung ✅"
else:
    riplife = "Tidak Terhubung ❌"

if gdriveisshit:
    wearenoob = "Aktif ✅"
else:
    wearenoob = "Mati ❌"

if rmbg:
    gendu = "Aktif ✅"
else:
    gendu = "Mati ❌"

if wttrapi:
    starknoobs = "Aktif ✅"
else:
    starknoobs = "Mati ❌"

if hmmok:
    meiko = "Aktif ✅"
else:
    meiko = "Mati ❌"

if isdbfine:
    dbstats = "Aktif ✅"
else:
    dbstats = "Mati ❌"

inlinestats = (
    f"✘ ARCHXBOT STATS ✘\n"
    f"VERSI = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {amiusingsudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"ARCHXSERVER = {riplife} \n"
    f"G-DRIVE = {wearenoob}"
)
