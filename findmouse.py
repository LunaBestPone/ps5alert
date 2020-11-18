import time
import pyautogui


def main():
    while True:
        print(pyautogui.position())
        time.sleep(1)


if __name__ == '__main__':
    main()