import time
import random
from pywinauto import Application
from pywinauto.keyboard import send_keys


def main():
    app = Application(backend='uia')
    app.connect(title_re='.*Chrome.*')
    dlg = app.top_window()
    while True:
        time.sleep(random.uniform(3, 5))
        url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
        if 'direct-queue' in url:
            while True:
                print('\a')
                time.sleep(1)
        send_keys('^{F5}')


if __name__ == '__main__':
    main()
