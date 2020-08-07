from monitoramento_precos.dao import Dao
from monitoramento_precos.factory import Factory
from monitoramento_precos.helpers import get_logger

logger = get_logger()


def main():
    logger.info("Starting process...")
    datas = Dao().load_data()
    for conf in datas:
        processor = Factory(conf)
        processor.fetch_price()
        processor.compare()
        processor.update_variation()
        processor.notify()
    logger.info("Finish process.")
