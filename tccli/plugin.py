import importlib
import logging
import pkgutil

import tccli.plugins as plugins

_plugins = {}
_imported = False


def import_plugins():
    global _imported

    if not _imported:
        _reimport_plugins()
        _imported = True

    return _plugins


def _reimport_plugins():
    for _, name, _ in pkgutil.iter_modules(plugins.__path__, plugins.__name__ + "."):
        mod = importlib.import_module(name)
        register_service = getattr(mod, "register_service", None)
        if not register_service:
            logging.warning("invalid module %s" % name)
            continue
        register_service(_plugins)

    return _plugins
