import logging

def test_loggingDemo():
    Logger = logging.getLogger(__name__)

    fileHandler=logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    Logger.addHandler(fileHandler)

    Logger.setLevel(logging.CRITICAL)
    Logger.debug("A debug statement")
    Logger.info("information")
    Logger.warning("something is in wrong mode")
    Logger.error("major error is happened")
    Logger.critical("critical issue")
