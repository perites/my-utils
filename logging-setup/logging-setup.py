import logging


logging.basicConfig(
    format='%(asctime)s [%(levelname)s] : %(message)s  ||[LOGGER:%(name)s] [FUNC:%(funcName)s] [FILE:%(filename)s]',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(PATH_TO_LOGS, mode='a', encoding='utf-8', ) # or mode 'w' 
    ]
)

logging.getLogger("requests").setLevel(logging.ERROR)
