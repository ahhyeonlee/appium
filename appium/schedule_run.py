import schedule, time
import runs as r

###batch file###
def job():
    r.run()

schedule.every(120).seconds.do(job)
#schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)