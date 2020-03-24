# -*- coding: utf-8 -*-
import io
import sys
try:
    reload(sys)  # Python 2.7
    sys.setdefaultencoding('utf8')
except NameError:
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        from importlib import reload  # Python 3.4+
        reload(sys)
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3
        reload(sys)
from tencentcloud import __version__ as sdkVersion
from tccli import __version__
from tccli.nice_command import NiceCommand
from tccli.configure import Configure
import tccli.services as Services
import tccli.help_template as HelpTemplate
import tccli.options_define as OptionalsDefine
import tccli.error_msg as ErrorMsg


def tccli_action(argv, arglist):
    if OptionalsDefine.Help in argv:
        services = Services.service_get_list()
        services_help = "      configure\n"
        for s in services:
            services_help += "      %s\n" % s
        print(HelpTemplate.TCCLI_HELP % services_help)
    elif OptionalsDefine.CliVersion in argv:
        print(__version__)
    else:
        print(ErrorMsg.INVALID_CMD % "too few arguments")


def main():
    try:
        cli_version = __version__.rsplit(".", 1)[0]
        if sdkVersion < cli_version:
            print("Version is inconsistent, python sdk version:%s tccli version:%s"
                  % (sdkVersion, __version__))
            return
        if len(sys.argv) < 2:
            print(ErrorMsg.INVALID_CMD % "too few arguments")
            return
        services = Services.service_get_list()

        c = Configure(services)
        c.init_configures()

        command = NiceCommand("tccli", tccli_action)
        command.reg_opt(OptionalsDefine.Help, "bool")
        command.reg_opt(OptionalsDefine.CliVersion, "bool")

        if sys.argv[1] == "configure":
            config = Configure(services)
            config.register_arg(command)
        elif sys.argv[1] in services:
            Services.services_register_arg(command, sys.argv[1])

        command.parse(sys.argv[1:])

    except Exception as err:
        print("tccli: " + str(err))
