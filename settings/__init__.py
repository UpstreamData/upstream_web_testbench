import toml
import os
from pyasic.settings import PyasicSettings

settings_keys = {}

try:
    with open(
        os.path.join(os.path.dirname(__file__), "settings.toml"), "r"
    ) as settings_file:
        settings = toml.loads(settings_file.read())
    settings_keys = settings.keys()
except:
    pass

if "ping_retries" in settings_keys:
    PyasicSettings().network_ping_retries = settings["ping_retries"]
if "ping_timeout" in settings_keys:
    PyasicSettings().network_ping_timeout = settings["ping_timeout"]
if "scan_threads" in settings_keys:
    PyasicSettings().network_scan_threads = settings["scan_threads"]

if "get_version_retries" in settings_keys:
    PyasicSettings().miner_factory_get_version_retries = settings["get_version_retries"]


if "whatsminer_pwd" in settings_keys:
    PyasicSettings().global_whatsminer_password = settings["whatsminer_pwd"]

if "debug" in settings_keys:
    PyasicSettings().debug = settings["debug"]

if "logfile" in settings_keys:
    PyasicSettings().logfile = settings["logfile"]
