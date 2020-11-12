
#!/usr/bin/env python
import time
import sys
import atexit

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

class Menu:
    current_choice_index = 1
    def __init__(self, choices):
        self.choices = choices
        self.current_choice_index = 0
        self.init_screen()
        self.handler()
        self.draw_object(self.choices)
        

    def init_screen(self):
        self.start()
        self.screen_width = lcd.dimensions()[0]
        self.screen_height = lcd.dimensions()[1]
        self.image = Image.new("P", (self.screen_width, self.screen_height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        


    def handler(self):
        ''' assignate functions to buttons '''
        touch.on(0, self.previous)
        touch.on(1, self.next)
        touch.on(2, self.play)

    def previous(self, event, channel):
        if self.current_choice_index > 0:
            self.current_choice_index -= 1
            time.sleep(1)
        elif self.current_choice_index == 0:
            self.current_choice_index = len(self.choices) - 1 
        
        print("index:", self.current_choice_index)

    def next(self, event, channel):
        if self.current_choice_index < len(self.choices) - 1:
            self.current_choice_index += 1 
            time.sleep(1)
        if self.current_choice_index == len(self.choices) - 1:
            self.current_choice_index = 0
            time.sleep(1)
        print("index", self.current_choice_index)

    def play(self, channel, event):
        radio_to_play = self.choices[self.current_choice_index]
        print("radio to play:", radio_to_play)



    def draw_object(self, object_list):
        padding = 2
        for object in object_list:
            text = object
            print("you are in the function draw")
            print(text)
            w, h = self.font.getsize(text)
            x = 2
            y = (self.screen_height - h) // 2 + padding
            print(
                "screen height", self.screen_height, "screen width", self.screen_width
            )
            print(x, y, text)
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


if __name__ == "__main__":
    radios = ["radio1", "radio2", "radio3", "radio4"]
    menu = Menu(radios)
    time.sleep(30)
    menu.stop()
    sys.exit(0)
    print("exited successfully")