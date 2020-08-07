from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from monitoramento_precos.helpers import get_logger


logger = get_logger()

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=5)
def print_data():
    data = datetime.now()
    logger.warning(f'JOB CHAMADA {data}')


scheduler.start()
