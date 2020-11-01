import display
import time
from display import DisplayedObject

if __name__ == "__main__":
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    screen = Screen(object_list)
    screen.start()
    screen.draw_object(object_list)
    time.sleep(5)
    screen.stop()
    pass
