import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

from monitoramento_precos.dao import Dao
from monitoramento_precos.factory import Factory
from monitoramento_precos.helpers import get_logger

pool = ThreadPool(8)

logger = get_logger()


def main():
    print(multiprocessing.cpu_count())
    logger.info("Starting process...")
    datas = Dao().load_data()
    pool.map(process, datas)
    logger.info("Finish process.")


def process(conf):
    processor = Factory(conf)
    processor.fetch_price()
    processor.compare()
    processor.update_variation()
    processor.notify()


if __name__ == "__main__":
    main()
