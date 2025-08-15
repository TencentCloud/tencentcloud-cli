import contextlib
import functools
import os
import subprocess
import sys


def shell(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()

    if sys.version_info.major >= 3:
        return p.stdout.read(409600).decode("utf-8")

    return p.stdout.read(409600)


def recover_profile(prof="default"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with recover_profile_ctx(prof):
                return func(*args, **kwargs)

        return wrapper

    return decorator


@contextlib.contextmanager
def recover_profile_ctx(prof="default"):
    cred_path = os.path.expanduser("~/.tccli/%s.credential" % prof)
    conf_path = os.path.expanduser("~/.tccli/%s.configure" % prof)

    cred_backup = None
    conf_backup = None

    if os.path.exists(cred_path):
        with open(cred_path, "r") as cred_f:
            cred_backup = cred_f.readlines()

    if os.path.exists(conf_path):
        with open(conf_path, "r") as conf_f:
            conf_backup = conf_f.readlines()

    yield

    if sys.version_info.major == 2:
        FileNotFound = OSError
    else:
        FileNotFound = FileNotFoundError

    if cred_backup:
        with open(cred_path, "w") as cred_f:
            cred_f.writelines(cred_backup)
    else:
        try:
            os.remove(cred_path)
        except FileNotFound:
            pass

    if conf_backup:
        with open(conf_path, "w") as conf_f:
            conf_f.writelines(conf_backup)
    else:
        try:
            os.remove(conf_path)
        except FileNotFound:
            pass
