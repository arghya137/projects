import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Heyy!!! Drink Water",
            message = "About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "C:\\Users\\KIIT\\Desktop\\projects\\drink reminder\\icon.ico",
            timeout=10
        )
        time.sleep(60*60)