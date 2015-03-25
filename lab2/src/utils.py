import logging

FORMAT = '%(asctime)-10s %(levelname)7s %(module)-15s | %(funcName)-15s | (%(lineno)d) | %(message)s'
logging.basicConfig(format=FORMAT)


def logger_injector(cls):
    cls.logger = logging.getLogger(cls.__name__)
    cls.logger.setLevel(logging.DEBUG)

    return cls
