import datetime
import time
from plyer import notification

prev_hour = datetime.datetime.now().hour

while True:
    current_hour = datetime.datetime.now().hour
    if(prev_hour != current_hour):
        notification.notify(
            title=f"It's {current_hour} o'clock",
            message=f"This is made by Bishal to remind himself of time",
            timeout = 10
        )
        prev_hour = datetime.datetime.now().hour
    time.sleep(1) 