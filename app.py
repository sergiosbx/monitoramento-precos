import multiprocessing.dummy

from monitoramento_precos.dao import Dao
from monitoramento_precos.factory import Factory
from monitoramento_precos.helpers import get_logger


logger = get_logger()


def main():
    logger.info("Starting process...")
    datas = Dao().load_data()
    with multiprocessing.Pool(8) as threadPool:
        threadPool.map(process, datas)
    logger.info("Finish process.")


def singlemain():
    logger.info("Starting process...")
    datas = Dao().load_data()
    for conf in datas:
        process(conf=conf)
    logger.info("Finish process.")


def process(conf):
    processor = Factory(conf)
    processor.fetch_price()
    processor.compare()
    processor.update_variation()
    processor.notify()


if __name__ == "__main__":
    main()
