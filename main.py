import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Time to do pushups",
            message = "5 pushups, 10 sqats, 10 curnches, 30 jumping jacks, neck stretch and back stretch",
            app_icon = "D:\\Python Projects\\Pushup reminder popup\\Icons8-Windows-8-Sports-Exercise.ico",
            timeout = 30
        )
        time.sleep(60*45)