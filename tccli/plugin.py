import importlib
import logging
import pkgutil
import plugins

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
        reg_cls = getattr(mod, "ServiceRegister", None)
        if not reg_cls:
            logging.warning("invalid module %s" % name)
            continue
        reg = reg_cls()
        reg.register(_plugins)

    return _plugins
