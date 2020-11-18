import sys
import time
import random
from pywinauto import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from pywinauto.mouse import press, release


def main():
    app = Application(backend='uia')
    app.connect(title_re='.*Chrome.*')
    dlg = app.top_window()
    encounter = False
    roll = True

    while True:
        time.sleep(random.uniform(3, 5))
        url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
        if 'direct-queue' in url:
            # consecutive hits on queue means either failed execution or hittin an actual queue
            if encounter:
                for i in range(60):
                    print('\a')
                    time.sleep(1)
                sys.exit('Alerting done, shutting down.')

                    
            randx = int(random.uniform(430,453))
            randy = int(random.uniform(628,649))
            click(button='left', coords=(randx,randy))
            encounter = True
            roll = True
            continue

        encounter = False
        if roll:
            press(button='left', coords=(1910,419))
            time.sleep(0.2)
            release(button='left', coords=(1910,419))
            roll = False
            
        send_keys('^{F5}')



if __name__ == '__main__':
    main()
