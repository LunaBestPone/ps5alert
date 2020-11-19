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

    while True:
        # how long you want the refresh interval? set it here
        time.sleep(20)
        url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
        if 'direct-queue' in url:
            # x and y positions for BOT CHECKING recaptcha check box, modify this if you have different screen config
            randx = int(random.uniform(430,453))
            randy = int(random.uniform(628,649))
            click(button='left', coords=(randx,randy))
            # wait for captcha box to appear, or redirect directly to ps direct
            time.sleep(2)
            url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
            if 'direct-queue' in url:
                # Buster extension kicks in, this is the box for buster button after recaptcha box appears
                click(button='left', coords=(606,930))
                # wait for verification, and potential redirect
                time.sleep(3)
                # if still on the direct queue page, it means either 1. current captcha failed 2. google detected you are a bot
                url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
                if 'direct-queue' in url:
                    # attemp to click on 'get new challenge'
                    click(button='left', coords=(501,771))
                    time.sleep(0.5)
                    # this position overlaps both buster button position, and refresh captcha box button if google detects the botting
                    click(button='left', coords=(630,771))
                    time.sleep(3)
                    
                    # if google detection happened and bot clicked refresh, need to open up the recaptcha box again
                    # x and y positions for bot checking recaptcha check box, modify this if you have different screen config
                    randx = int(random.uniform(430,453))
                    randy = int(random.uniform(628,649))
                    click(button='left', coords=(randx,randy))

                    # Buster kicks in again
                    time.sleep(1)
                    click(button='left', coords=(606,930))
                    time.sleep(3)

                    # click on first tap addres bar and paste in ps5 direct link
                    click(button='left', coords=(385,90))
                    send_keys('^v')
                    send_keys('{ENTER}')
                    time.sleep(3)
                # if passed bot checking, still meet direct queue page afterwards, that means you hit the queue
                time.sleep(2)
                url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
                if 'direct-queue' in url:
                    # try to queue the queue before alert happens
                    randx = int(random.uniform(430,453))
                    randy = int(random.uniform(409,429))
                    click(button='left', coords=(randx, randy))
                    # alert for 1 min
                    for i in range(60):
                        print('\a')
                        time.sleep(1)
                    sys.exit('Alerting done, shutting down.')
            # move on to next cycle if recaptcha didn't appear at all (restart from top of while loop)
            continue

        # add a step for clearing cache, since sony's site queue users based on their cookie time stamp, doing this gets you the newest cookies
        # click on second tap which is chrome setting
        click(button='left', coords=(388,56))
        time.sleep(0.1)
        # click on clear browser data sub-section
        click(button='left', coords=(784,1009))
        time.sleep(0.1)
        # click on clear cache button
        click(button='left', coords=(1198,749))
        time.sleep(0.1)
        # click on first tap
        click(button='left',coords=(181,59))
        
        # address bar pasting
        click(button='left', coords=(385,90))
        send_keys('^v')
        send_keys('{ENTER}')



if __name__ == '__main__':
    main()
