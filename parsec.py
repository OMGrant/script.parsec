import xbmc
import xbmcaddon
import xbmcgui

PLUGIN_ID = "script.parsec"
SPECIAL_PATH = "special://home/addons/{0}/resources/".format(PLUGIN_ID)

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')

OS_USER = ADDON.getSetting('os_user')
RESOURCE_PATH = xbmc.translatePath(SPECIAL_PATH)
SERVER_ID = ADDON.getSetting('server_id')

HEADLESS_MODE = ADDON.getSetting('headless_mode')

if ADDON.getSetting('client_overlay') != "true":
    PARSEC_BUTTON = "client_overlay=0"
else:
    PARSEC_BUTTON = "client_overlay=1"

if ADDON.getSetting('client_immersive') != "true":
    KEYBOARD_PASSTHROUGH = "client_immersive=0"
else:
    KEYBOARD_PASSTHROUGH = "client_immersive=1"  

if ADDON.getSetting('wan_quality') == "Performance":
    WAN_QUALITY = "app_wan_quality=1"
else:
    if ADDON.getSetting('wan_quality') == "Balanced":
        WAN_QUALITY = "app_wan_quality=2"
    else:
        if ADDON.getSetting('wan_quality') == "Quality":
            WAN_QUALITY = "app_wan_quality=3"
        else:
            WAN_QUALITY = "app_wan_quality=1"

if ADDON.getSetting('lan_quality') == "Performance":
    LAN_QUALITY = "app_lan_quality=1"
else:
    if ADDON.getSetting('lan_quality') == "Balanced":
        LAN_QUALITY = "app_lan_quality=2"
    else:
        if ADDON.getSetting('lan_quality') == "Quality":
            LAN_QUALITY = "app_lan_quality=3"
        else:
            LAN_QUALITY = "app_lan_quality=1"

if ADDON.getSetting('force_lan') != "true":
    FORCE_LAN = "network_try_lan=0"
else:
    FORCE_LAN = "network_try_lan=1"

ENCODER_BITRATE = "encoder_bitrate=" + ADDON.getSetting('encoder_bitrate')

if ADDON.getSetting('encoder_fps') == "Client Display":
    ENCODER_FPS = "encoder_fps=0"
else:
    if ADDON.getSetting('encoder_fps') == "30":
        ENCODER_FPS = "encoder_fps=30"
    else:
        if ADDON.getSetting('encoder_fps') == "60":
            ENCODER_FPS = "encoder_fps=60"
        else:
            ENCODER_FPS = "encoder_fps=0"

ENCODER_FIDELITY = "encoder_min_qp=" + ADDON.getSetting('encoder_fidelity')

HOST_WIDTH = "server_resolution_x=" + ADDON.getSetting('server_resolution_width')

HOST_HEIGHT = "server_resolution_y=" + ADDON.getSetting('server_resolution_height')

HOST_REFRESH_RATE = "server_refresh_rate=" + ADDON.getSetting('server_refresh_rate')

if ADDON.getSetting('client_vsync') != "true":
    CLIENT_VSYNC = "client_vsync=0"
else:
    CLIENT_VSYNC = "client_vsync=1"

CLIENT_AUDIO_BUFFER = "client_audio_buffer=" + ADDON.getSetting('client_audio_buffer')

if ADDON.getSetting('echo_cancel') != "true":
    ECHO_CANCEL = "server_audio_cancel=0"
else:
    ECHO_CANCEL = "server_audio_cancel=1"

if ADDON.getSetting('server_admin_mute') != "true":
    HOST_MUTE = "server_admin_mute=0"
else:
    HOST_MUTE = "server_admin_mute=1"


PARSEC_ARGS = PARSEC_BUTTON + ":" + KEYBOARD_PASSTHROUGH + ":" + WAN_QUALITY + ":" + LAN_QUALITY + ":" + FORCE_LAN + ":" + ENCODER_BITRATE + ":" + ENCODER_FPS + ":" + ENCODER_FIDELITY + ":" + HOST_WIDTH + ":" + HOST_HEIGHT + ":" + HOST_REFRESH_RATE + ":" + CLIENT_VSYNC + ":" + CLIENT_AUDIO_BUFFER + ":" + ECHO_CANCEL + ":" + HOST_MUTE


if HEADLESS_MODE == "true":
    PARSEC_LAUNCHER = RESOURCE_PATH + "parsec-launcher.sh " + OS_USER + " " + RESOURCE_PATH + " server_id='" + SERVER_ID + "':" + PARSEC_ARGS
else:
    PARSEC_LAUNCHER = RESOURCE_PATH + "parsec-launcher.sh " + OS_USER + " " + RESOURCE_PATH + " " + PARSEC_ARGS


import subprocess
subprocess.call(PARSEC_LAUNCHER, shell=True)
