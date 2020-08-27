import time
import signal

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


class DisplayObject:

        def __init__(self, object_list):
            self.object_list = object_list
            self.screen_width = lcd.dimensions()
            self.screen_height = lcd.dimensions()
            self.font = ImageFont.truetype(fonts.AmaticSCBold, 38)


        def draw_object(self, object_list):
            for object in object_list:
                text = "Hello World"
                w, h = font.getsize(text)
                x = (width - w) // 2
                y = (height - h) // 2
                draw.text((x, y), text, 1, font)
                pass


        def start(self):
            for x in range(6):
                touch.set_led(x, 1)
                time.sleep(0.1)
                touch.set_led(x, 0)

            for x in range(6):
                backlight.set_pixel(x, 0, 255, 0)
                touch.on(x, handler)
            pass

        def stop(self):
            for x in range(6):
                backlight.set_pixel(x, 0, 0, 0)
                touch.set_led(x, 0)
            backlight.show()
            lcd.clear()
            lcd.show()


if __name__ == "__main__":
    prices = [ price1, price2] 
    my_screen  = DisplayObject(object_list)
    my_screen.start()
    time.sleep(5)
    my_screen.stop()
    pass