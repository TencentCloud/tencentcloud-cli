import logging
import logging.handlers
import os


def init(name):
    logdir = os.path.join(os.path.expanduser("~"), '.tccli', 'log')
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    fn = os.path.join(logdir, "tccli.log")
    FMT = '[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s'
    mb = 1024 * 1024
    handler = logging.handlers.RotatingFileHandler(fn, maxBytes=10*mb, backupCount=10)
    handler.setFormatter(logging.Formatter(FMT))
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    return log
