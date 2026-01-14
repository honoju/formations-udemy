import logging

logging.basicConfig(level=logging.DEBUG,
                    format ='%(asctime)s - %(levelname)s - %(message)s',
                    filename="test.log",
                    filemode="w")

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")