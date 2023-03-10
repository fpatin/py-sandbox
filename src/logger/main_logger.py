import logging

from src.logger.class_a import ClassA
from src.logger.logger_configurator import LoggerConfigurator
from src.logger.sub.class_b import ClassB


def main():
    logger = logging.getLogger()
    logger.debug('DEBUG Started')
    logger.info('INFO Started')
    logger.warning('WARN Started')
    logger.error('ERROR Started')
    logger.critical('CRITICAL Started')
    ClassA('value A').execute()
    ClassB().execute('value B')
    logger.debug('DEBUG Finished')
    logger.info('INFO Finished')
    logger.warning('WARN Finished')
    logger.error('ERROR Finished')
    logger.critical('CRITICAL Finished')


if __name__ == '__main__':
    LoggerConfigurator.configure()
    main()
