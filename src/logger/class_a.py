import logging


class ClassA:
    __logger = logging.getLogger('other')

    def __init__(self, value: str):
        self.value = value

    def execute(self):
        ClassA.__logger.debug('DEBUG Execute method %s', self.value)
        ClassA.__logger.info('INFO Execute method %s', self.value)
        ClassA.__logger.warning('WARN Execute method %s', self.value)
        ClassA.__logger.error('ERROR Execute method %s', self.value)
        ClassA.__logger.critical('CRITICAL Execute method %s', self.value)
