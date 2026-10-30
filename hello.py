import webbrowser
import time

URL = input("Enter URL: ")
Duration = int(input("Enter Duration: "))
Times = int(input("How many times would you like to view the video: "))

for i in range(Times):
    webbrowser.open_new(URL)
    time.sleep(Duration)
