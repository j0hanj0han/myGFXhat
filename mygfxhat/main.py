import display
import time
from display import Screen
import signal
from gfxhat import touch

def handler(channel, event):
    print("Got {} on channel {}".format(event, channel))




if __name__ == "__main__":
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    for x in range(6):
        touch.on(x, handler)

    screen = Screen(object_list)
    screen.start()
    screen.draw_object(object_list)
    signal.pause()
    screen.stop()
    pass
