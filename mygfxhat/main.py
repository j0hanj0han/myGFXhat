
import time, datetime, signal
import os, sys
from gfxhat import lcd
#internal import
from screen import screen







def main():
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    # light on screen and display object list
    myscreen = screen.Screen(object_list)
    while True: 
        try: 
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            object_list = [now, "Hello Johan !", "Hello Nina !", "Go to Nice!"]
            myscreen.draw_object(object_list)
            time.sleep(1)
            lcd.clear()
            lcd.show()
        except KeyboardInterrupt: # if exit with ctrl + c shut off the screen
            print('Interrupted')
            try:
                myscreen.stop()
                sys.exit(0)
            except SystemExit:
                os._exit(0)

if __name__ == '__main__':
   main()