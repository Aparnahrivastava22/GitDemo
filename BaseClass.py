import inspect
import logging


class  BaseClass:

    def getlogger(self):
        loggerName= inspect.stack()[1][3]
        Logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        Logger.addHandler(fileHandler)

        Logger.setLevel(logging.DEBUG)
        return Logger
