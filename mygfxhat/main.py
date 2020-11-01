
import time, datetime, signal
import os, sys
from gfxhat import touch


#internal import
from display import Screen


# handler for touch
def handler(channel, event):
    print("Got {} on channel {}".format(event, channel))

def display_time(channel, event):
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    
    #activate handler
    for x in range(6):
        touch.on(x, handler)

    touch.on(4, display_time)
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