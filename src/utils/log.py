import logging


logging.basicConfig(
    filename='web_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s:%(funcName)15s:%(lineno)5s%(levelname)8s:%(name)10s:%(message)s',
    datefmt='%Y/%m/%d %I:%M:%S'
)

logger = logging.getLogger('root')
logger_db = logging.getLogger('db')
logger_conf = logging.getLogger('db')


if __name__ == '__main__':
    logger.debug("test")
    logger_db.error("db err")