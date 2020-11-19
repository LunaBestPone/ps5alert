# ps5alert
A naïve implementation of ps5 direct page auto refresher, works only for windows. Tried to use Selenium on unix but of course they have detection for that.
# Usage
1. install [Buster](https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en) chrome extension
1. Go to options of Buster, Switch to Google Cloud Speech to Text API, insert your own API key (Guide on this will not be covered). If you have the 300 dollars free credit on Google Cloud, this will be most likely free over your usage during the script.
1. Run
  ```pip install -r requirements.txt```
2. Launch chrome with [ps direct](https://direct.playstation.com/en-us/ps5) tab open on top, for ```main_1920x1080.py``` variant, you need to also open chrome settings tap, place it on the second position, in addition, copy the ps direct link to your clip board for pasting.
3. Run
  ```python main.py```
  or
  ```python main_1920x1080.py```,
  differences are listed in Behavior Section
4. Manually focus the chrome window, chrome must be in focus during the execution.
# Behavior
## main.py (deprecated, as sony place user in queue by cookie issue time)
Makes beeps if hits the queue page, requires a human to complete recaptcha even if it's not an actual queue. Exit execution by killing the program whenever you like.
## main_1920x1080.py
Makes beeps for one minute if hits an actual queue or the program just broke. Doesn't require a human to complete recaptcha if it's just bot checking. Exit execution by killing the program whenver you like. This only works for 1920x1080 resolution devices with windows task bar positioned on top because the mouse operation coordinates are hard coded. You can adjust the value, start by using ```findmouse.py``` which provides information on your mouse coordinates in real time.
### Note
1. You will most likely need adjustments for clicking coordinates for the 1920x1080 version. But it is the variant that bought me the video game machine. The comments in the script is detailed enough for localization on different environment (of course you need matching operating system).
2. Remember to deactivate your GC API key after you are done with these stuffs. I do not have responsibility for your bills.

# And good luck on the hunt for your new toy
![Loot](https://github.com/LunaBestPone/ps5alert/blob/main/Capture.PNG?raw=true)
