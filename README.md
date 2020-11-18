# ps5alert
A naïve implementation of ps5 direct page auto refresher, works only for windows. Tried to use Selenium on unix but of course they have detection for that.
# Usage
1. Run
  ```pip install -r requirements.txt```
2. Launch chrome with ps direct tab open on top
3. Run
  ```python main.py```
  or
  ```python main_1920x1080.py```,
  differences are listed in Behavior Section
4. Manually focus the chrome window, chrome must be in focus during the execution.
# Behavior
## main.py
Makes beeps if hits the queue page, requires a human to complete recaptcha even if it's not an actual queue. Exit execution by killing the program whenever you like.
## main_1920x1080.py
Makes beeps for one minute if hits an actual queue or the program just broke. Doesn't require a human to complete recaptcha if it's just bot checking. Also scrolls to a position where you can confirm the stock status after redirections. Exit execution by killing the program whenver you like. This only works for 1920x1080 resolution devices with windows task bar positioned on top because the mouse operation coordinates are hard coded. You can adjust the value, start by using ```findmouse.py``` which provides information on your mouse coordinates in real time.
