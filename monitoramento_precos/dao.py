from pydbwrapper import Database as Datasource, Config

import variables as var
from .helpers import qualifiedpath


class Dao():
    def connect(self):
        return Datasource(Config(config_dict={
            "host": var.DATABASE_BASE_URL,
            "port": var.DATABASE_PORT,
            "dbname": var.DATABASE_NAME,
            "user": var.DATABASE_USERNAME,
            "password": var.DATABASE_PASSWORD,
            "connect_timeout": int(var.DATABASE_CONNECT_TIMEOUT),
            "maxconnections": int(var.DATABASE_MAX_CONNECTIONS)
        }))

    def load_data(self):
        with open(qualifiedpath("datas.sql", var.QUERYS_DIR), "r") as sqlfile:
            with self.connect() as db:
                datas = db.execute(sqlfile.read(), skip_load_query=True).fetchall()
                return datas

    def insert_price_varation(self, stores_products_id, price):
        with self.connect() as db:
            db.insert(table='variations') \
                .set(field='value', value=price) \
                .where(field='stores_products_id', value=stores_products_id) \
                .execute()
