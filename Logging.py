import logging   #Logging module using. 

logging.basicConfig(filename="exampleLogging.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")