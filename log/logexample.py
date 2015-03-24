import logging
import os


def setup_log(filename=False):
    source = os.uname()[1]
    format_string = '%(asctime)s {}: %(levelname)8s - %(message)s'.format(source)
    if filename:
        logging.basicConfig(filename=filename, format=format_string,
                            datefmt='%m/%d/%y %I:%M:%S %p')
    else:
        logging.basicConfig(format=format_string, datefmt='%m/%d/%y %I:%M:%S %p')


setup_log()
logging.info('Hello')
logging.error('Oops')
logging.warning('A quick warning')
