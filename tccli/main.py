# -*- coding: utf-8 -*-

import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

import io
import sys
import six
from tccli.log import init
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

try:
    # cp65001 is utf-8 on windows platform
    # python2 doesn't support cp65001 codec
    if getattr(sys.stdin, 'encoding', 'utf-8') == "cp65001":
        import codecs
        codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

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
from tccli.command import CLICommand
from tencentcloud import __version__ as sdkVersion
from tccli import __version__
from tccli.exceptions import UnknownArgumentError, ConfigurationError, NoCredentialsError, NoRegionError, ClientError
from tccli.error_msg import USAGE

log = init('tccli.main')


def main():
    cli_version = __version__.rsplit(".", 1)[0]
    if int(sdkVersion.split(".")[-1]) < int(cli_version.split(".")[-1]):
        sys.stderr.write("Version is inconsistent, python sdk version:%s tccli version:%s" % (sdkVersion, __version__))
        return 255
    try:
        log.info("tccli %s" % ' '.join(sys.argv[1:]))
        CLICommand()()
        return 0
    except UnknownArgumentError as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        log.exception(e)
        return 255
    except ConfigurationError as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        log.exception(e)
        return 255
    except NoRegionError as e:
        msg = ('%s You can configure your region by running '
               '"tccli configure".' % e)
        sys.stderr.write(msg)
        sys.stderr.write('\n')
        log.exception(e)
        return 255
    except NoCredentialsError as e:
        msg = ('%s. You can configure your credentials by running '
               '"tccli configure".' % e)
        sys.stderr.write(msg)
        sys.stderr.write('\n')
        log.exception(e)
        return 255
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        return 255
    except ClientError as e:
        sys.stderr.write("\n")
        sys.stderr.write(six.text_type(e))
        sys.stderr.write("\n")
        log.exception(e)
        return 255
    except TencentCloudSDKException as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        log.error(e)
        return 255
    except Exception as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        log.exception(e)
        return 255


if __name__ == "__main__":
    main()

