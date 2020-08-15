from apscheduler.schedulers.blocking import BlockingScheduler

from app import main

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=7, max_instances=3)
def execution():
    main()


scheduler.start()
