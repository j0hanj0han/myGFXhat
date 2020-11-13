
import time, datetime, signal
import os, sys
from gfxhat import lcd
#internal import
from screen import screen

def main():

        
        try: 
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            object_list = [now, "Hello Johan !", "Hello Nina !", "Go to Nice!"]
            myscreen = screen.Screen(object_list)
            myscreen.draw_object(object_list)
            signal.pause()
        except KeyboardInterrupt: # if exit with ctrl + c shut off the screen
            print('Interrupted')
            try:
                myscreen.stop()
                sys.exit(0)
            except SystemExit:
                os._exit(0)

if __name__ == '__main__':
   main()