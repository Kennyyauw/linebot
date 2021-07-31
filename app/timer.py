from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

scheduleEvent = BlockingScheduler()

@scheduleEvent.scheduled_job('cron',day_of_week='mon-fri',minute='*/20')
def scheduled_job():
    website = "" #輸入你的heroku的網頁
    connection = urllib.request.urlopen(website)

    for i, value in connection.getheaders():
        print(i,value)

scheduleEvent.start()