# -*- coding: utf-8 -*-

import logging
from logging import handlers

logger = logging.getLogger()

def init(filename):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    rotate = handlers.RotatingFileHandler(filename, maxBytes=10 * 1024 * 1024, backupCount=10)
    rotate.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(fmt)
    rotate.setFormatter(fmt)
    logger.addHandler(console)
    logger.addHandler(rotate)
    logger.setLevel(logging.DEBUG)

init("spider.log")
