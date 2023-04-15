DOMAIN = "browser_mod"

FRONTEND_SCRIPT_URL = "/browser_mod.js"

DATA_EXTRA_MODULE_URL = 'frontend_extra_module_url'

DATA_DEVICES = "devices"
DATA_ALIASES = "aliases"
DATA_ADDERS = "adders"
DATA_CONFIG = "config"

CONFIG_DEVICES = "devices"
CONFIG_PREFIX = "prefix"
CONFIG_DISABLE = "disable"
CONFIG_DISABLE_ALL = "all"

WS_ROOT = DOMAIN
WS_CONNECT = f"{WS_ROOT}/connect"
WS_UPDATE = f"{WS_ROOT}/update"
WS_CAMERA = f"{WS_ROOT}/camera"

USER_COMMANDS = [
        "debug",
        "popup",
        "close-popup",
        "navigate",
        "more-info",
        "set-theme",
        "lovelace-reload",
        "blackout",
        "no-blackout",
        "toast",
        ]
