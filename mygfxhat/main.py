
import time, datetime, signal
import os, sys

#internal import
from display import display




def main():
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    
    # light on screen and display object list
    try: 
        screen = Screen(object_list)
        screen.start()
        screen.draw_object(object_list)
        signal.pause()

    except KeyboardInterrupt: # if exit with ctrl + c shut off the screen
        print('Interrupted')
        try:
            screen.stop()
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
   main()