# -*- coding: utf-8 -*-

import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

import io
import os
import sys
import tccli.six as six
import signal
import logging
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base)
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
from tccli.command import CLICommand
from tencentcloud import __version__ as sdkVersion
from tccli import __version__
from tccli.exceptions import UnknownArgumentError, ConfigurationError, NoCredentialsError, NoRegionError, ClientError
from tccli.error_msg import USAGE

LOG = logging.getLogger('tccli.main')
LOG_FORMAT = ('%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')


def main():
    cli_version = __version__.rsplit(".", 1)[0]
    if sdkVersion < cli_version:
        sys.stderr.write("Version is inconsistent, python sdk version:%s tccli version:%s" % (sdkVersion, __version__))
        return
    try:
        LOG.debug("begin cli command")
        CLICommand()()
    except UnknownArgumentError as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return
    except ConfigurationError as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return
    except NoRegionError as e:
        msg = ('%s You can configure your region by running '
               '"tccli configure".' % e)
        sys.stderr.write(msg)
        sys.stderr.write('\n')
        return
    except NoCredentialsError as e:
        msg = ('%s. You can configure your credentials by running '
               '"tccli configure".' % e)
        sys.stderr.write(msg)
        sys.stderr.write('\n')
        return
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        return
    except ClientError as e:
        sys.stderr.write("\n")
        sys.stderr.write(six.text_type(e))
        sys.stderr.write("\n")
        return
    except Exception as e:
        sys.stderr.write("usage: %s\n" % USAGE)
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return


if __name__ == "__main__":
    main()

