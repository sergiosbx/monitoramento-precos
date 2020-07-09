import os
import re
import sys
from functools import singledispatch

from loguru import logger
from lxml.etree import _Element

logger.remove()
logger.add(sys.stdout)

AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'


def qualifiedpath(filename, pathdir=None):
    return os.path.join(basepath(pathdir), filename)


def basepath(pathdir: str):
    return os.path.join(os.getcwd(), pathdir)


@singledispatch
def safe_element_value(element):
    raise NotImplementedError


@safe_element_value.register(list)
def safe_elements(elements):
    return elements[0].attrib.get('content', elements[0].text) if elements else '0,0'


@safe_element_value.register(_Element)
def safe_element(element):
    return element.attrib.get('content', element.text) if element is not None else '0,0'


def sanitize_price(price: str, brazillian_currency):
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
