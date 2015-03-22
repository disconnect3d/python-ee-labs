import logging

FORMAT = '%(asctime)-10s %(module)s-10s %(funcName)-10s %(message)s'
logging.basicConfig(format=FORMAT)


def logger_injector(cls):
    def wrap(*args, **kwargs):
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.setLevel(logging.INFO)
        return cls(*args, **kwargs)

    return wrap
