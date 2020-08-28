import time
import signal

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


class DisplayObject:

        ''' Display an object list '''

        def __init__(self, object_list):
            self.object_list = object_list
            self.screen_width = lcd.dimensions()
            self.screen_height = lcd.dimensions()
            self.font = ImageFont.load_default()


        def draw_object(self, object_list):
            # for object in object_list:
            #     pass       
                text = object_list[0]
                w, h = font.getsize(text)
                x = (width - w) // 2
                y = (height - h) // 2
                draw.text((x, y), text, 1, font)


        def start(self):
            for x in range(6):
                touch.set_led(x, 1)
                time.sleep(0.1)
                touch.set_led(x, 0)

            for x in range(6):
                backlight.set_pixel(x, 0, 255, 0)
            pass

        def stop(self):
            for x in range(6):
                backlight.set_pixel(x, 0, 0, 0)
                touch.set_led(x, 0)
            backlight.show()
            lcd.clear()
            lcd.show()


if __name__ == "__main__":
    object_list = ['Hello Johan!'] 
    my_screen  = DisplayObject(object_list)
    my_screen.start()
    my_screen.draw_object(object_list)
    time.sleep(5)
    my_screen.stop()
    pass