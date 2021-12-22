import logging
import logging.handlers
import os


def init(name):
    logdir = '~/.tccli/log'
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    fn = os.path.join(logdir, "tccli.log")
    FMT = '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s'
    mb = 1024 * 1024
    handler = logging.handlers.RotatingFileHandler(fn, maxBytes=512*mb, backupCount=10)
    handler.setFormatter(logging.Formatter(FMT))
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    return log
