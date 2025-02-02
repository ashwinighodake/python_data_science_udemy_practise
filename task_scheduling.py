import schedule
import time
import datetime

def fun_minute():
    print("Current time is:",datetime.datetime.now())
    print("schedular executed after minute")

def fun_hour():
    print("Current time is:",datetime.datetime.now())
    print("schedular executed after hour")

def fun_day():
    print("Current time is:",datetime.datetime.now())
    print("schedular executed after a day")

def fun_Afternoon():
    print("Current time is:",datetime.datetime.now())
    print("schedular executed at 12")

def main():
    print("Python job schedular")
    print(datetime.datetime.now())
    schedule.every(1).minutes.do(fun_minute)
    schedule.every().hours.do(fun_hour)
    schedule.every().days.at("00:00").do(fun_Afternoon)
    schedule.every().sunday.do(fun_day)
    schedule.every().saturday.at("18:30").do(fun_day)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
    
    
    
    