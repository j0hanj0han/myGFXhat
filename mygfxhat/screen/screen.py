import time, datetime
import signal
import vlc


from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

from handler import handler as h


class Screen:

    """ Display an object list """

    def __init__(self, object_list):
        self.init_screen()
        self.object_list = object_list
        self.handler = h.Handler()
        

    def init_screen(self):
        self.screen_width = lcd.dimensions()[0]
        self.screen_height = lcd.dimensions()[1]
        self.image = Image.new("P", (self.screen_width, self.screen_height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        self.backlight = True
        self.start()


    def draw_object(self, object_list):
        padding = 2
        for object in object_list:
            text = object

            # print(text)
            w, h = self.font.getsize(text)
            x = 2
            y = (self.screen_height - h) // 2 + padding
            # print(
            #     "screen height", self.screen_height, "screen width", self.screen_width
            # )
            # print(x, y, text)
            self.draw.text((x, y), text, 1, self.font)
            for x in range(128):
                for y in range(64):
                    pixel = self.image.getpixel((x, y))
                    lcd.set_pixel(x, y, pixel)
            padding += 10
        lcd.show()

    def start(self):
        for x in range(6):
            touch.set_led(x, 1)
            time.sleep(0.1)
            touch.set_led(x, 0)

        for x in range(6):
            backlight.set_pixel(x, 255, 79, 193)
        backlight.show()

    def stop(self):
        for x in range(6):
            backlight.set_pixel(x, 0, 0, 0)
            touch.set_led(x, 0)
        backlight.show()
        lcd.clear()
        lcd.show()

    

        
