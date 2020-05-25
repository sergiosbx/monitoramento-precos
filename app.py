from monitor_precos.dao import Dao
from monitor_precos.factory import Factory


def main():
    datas = Dao().load_data()
    for conf in datas:
        processor = Factory(conf)
        processor.fetch_price()
        processor.compare()
        processor.update_variation()
        processor.notify()


if __name__ == "__main__":
    main()
