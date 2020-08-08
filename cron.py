from apscheduler.schedulers.blocking import BlockingScheduler

from app import main

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=5, max_instances=3)
def print_data():
    main()


scheduler.start()
