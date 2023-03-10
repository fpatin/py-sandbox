import logging


class ClassB:
    __logger = logging.getLogger('other')

    def __init__(self):
        pass

    def execute(self, value: str):
        ClassB.__logger.debug('DEBUG Execute method %s', value)
        ClassB.__logger.info('INFO Execute method %s', value)
        ClassB.__logger.warning('WARN Execute method %s', value)
        ClassB.__logger.error('ERROR Execute method %s', value)
        ClassB.__logger.critical('CRITICAL Execute method %s', value)
