import os
import re
import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout)

AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'

def qualifiedpath(filename, pathdir=None):
    return os.path.join(basepath(pathdir), filename)


def basepath(pathdir: str):
    return os.path.join(os.getcwd(), pathdir)


def safe_element_value(elements: list):
    return elements[0].text if elements else '0.0'


def sanitize_price(price: str, brazillian_currency=False):
    only_float = re.sub(r'[^0-9,.]', '', price)
    if brazillian_currency:
        only_float = only_float.replace('.', '')
        only_float = only_float.replace(',', '.')
    return float(only_float)


def safe_float(price, default=None):
    try:
        return float(price)
    except (ValueError, TypeError):
        return default


def get_logger(module=None):
    return logger
