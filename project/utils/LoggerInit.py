# -*- coding: utf-8 -*-
# __author__: bicycle

import logging.config
import logging
import time
import os
import re

from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler


class LoggerInit(object):
    """

    """

    def __init__(self, *args):
        self.args = args if args else None
        dir_path = "log"
        for arg in args:
            dir_path = os.path.join(dir_path, arg)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        self.log_file_path = os.path.join(dir_path, "{0}_{1}.log".format(__name__, time.strftime("%Y_%m_%d")))

    def rotating_init(self):
        logger = logging.getLogger("main")
        timeLogHandler = RotatingFileHandler(self.log_file_path, maxBytes=1024 * 1024 * 5, backupCount=5, encoding="UTF-8")
        logger.setLevel(logging.DEBUG)
        timeLogHandler.setLevel(logging.DEBUG)
        consoleLogHandler = logging.StreamHandler()
        consoleLogHandler.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        timeLogHandler.setFormatter(formatter)
        consoleLogHandler.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(timeLogHandler)
        logger.addHandler(consoleLogHandler)
        return logger

