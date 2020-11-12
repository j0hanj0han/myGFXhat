
import time, datetime, signal
import os, sys

#internal import
from screen import screen




def main():
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    
    while True: 
    # light on screen and display object list

        myscreen = screen.Screen(object_list)
        try: 
            
            myscreen.draw_object(object_list)

        except KeyboardInterrupt: # if exit with ctrl + c shut off the screen
            print('Interrupted')
            try:
                myscreen.stop()
                sys.exit(0)
            except SystemExit:
                os._exit(0)

if __name__ == '__main__':
   main()