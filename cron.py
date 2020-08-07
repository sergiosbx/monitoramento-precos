from apscheduler.schedulers.blocking import BlockingScheduler

from app import main

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=5)
def print_data():
    main()


scheduler.start()
