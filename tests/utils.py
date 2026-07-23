import contextlib
import functools
import os
import subprocess
import sys


def shell(cmd):
    if isinstance(cmd, str):
        args = cmd
        use_shell = True
    else:
        args = cmd
        use_shell = False
    p = subprocess.Popen(args, shell=use_shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = p.communicate()

    if sys.version_info.major >= 3:
        return stdout.decode("utf-8")

    return stdout


_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_TCCLI_RUNNER = (
    "{py} -c \"import sys; sys.path.insert(0, '{repo}'); "
    "from tccli.main import main; sys.exit(main())\""
).format(py=sys.executable, repo=_REPO_ROOT)


def shell_with_stderr(cmd, clean_cred_env=False):
    """执行命令，返回 (stdout, stderr, returncode)。
    将命令中的 tccli 替换为当前源码入口，确保测试当前分支代码。
    clean_cred_env=True 时从 env 中移除 AK/SK，用于测试无凭证场景。
    """
    cmd = cmd.replace("tccli ", _TCCLI_RUNNER + " ", 1)
    env = os.environ.copy()
    if clean_cred_env:
        env.pop("TENCENTCLOUD_SECRET_ID", None)
        env.pop("TENCENTCLOUD_SECRET_KEY", None)
        env.pop("TENCENTCLOUD_SECRET_TOKEN", None)
    p = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=env,
    )
    stdout, stderr = p.communicate()
    if sys.version_info.major >= 3:
        return stdout.decode("utf-8"), stderr.decode("utf-8"), p.returncode
    return stdout, stderr, p.returncode


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


class TestCli(object):
    """保留国内站原有的 TestCli 风格入口，供既有测试沿用。"""

    def run_cmd(self, cmd):
        result = os.popen(cmd)
        return result

    def equal(self, cmd, expect):
        run = self.run_cmd(cmd)
        result = run.read()
        assert result.find(expect) >= 0
