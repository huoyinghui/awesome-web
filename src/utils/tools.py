import hashlib
from .log import logger


def encrypted(salt, text):
    m = hashlib.md5()
    m.update("{}:{}".format(salt, text).encode('utf8'))
    data = m.hexdigest()
    logger.debug("salt:{} text:{} data:{}".format(salt, text, data))
    return data


if __name__ == '__main__':
    logger.debug(encrypted('123', '122'))
