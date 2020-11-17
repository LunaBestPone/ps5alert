# ps5alert
A naïve implementation of ps5 direct page auto refresher, works only for windows. Tried to use Selenium on unix but of course they have detection for that.
# Usage
1. Run
  ```
  pip install -r requirements.txt
  ```
2. Launch chrome with ps direct tab open on top
3. Run
  ```
  python main.py
  ```
4. Manually focus the chrome window
# Behavior
Makes beeps if hit a queue, requires a human to complete recaptcha. Directly kill the program whenever you like.
