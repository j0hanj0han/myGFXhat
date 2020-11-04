import time, datetime
import signal
import vlc


from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

from handler import handler as h


class Screen:

    """ Display an object list """

    def __init__(self, object_list):
        self.object_list = object_list
        self.screen_width = lcd.dimensions()[0]
        self.screen_height = lcd.dimensions()[1]
        self.image = Image.new("P", (self.screen_width, self.screen_height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        self.player_stmt = False
        self.buttons = self.initialize_button()
        self.playlist = ["http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"]
        self.backlight = True


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

    
    
    def initialize_button(self):
        touch.on(0, self.handler)
        touch.on(1, self.handler)
        touch.on(2, self.backlight_screen)
        touch.on(3, self.illuminate)
        touch.on(4, self.display_time)
        touch.on(5, self.launch_radio)

    # handler for touch
    def handler(self, channel, event):
        print("Got {} on channel {}".format(event, channel))

    def display_time(self, channel, event):
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

    def launch_radio(self, channel, event): 
        #import pdb; pdb.set_trace()
        print("on rentre dans la fonction player_stmt:", self.player_stmt)
        if self.player_stmt == True: 
            self.player.stop()
            self.player_stmt = False
            touch.set_led(5, 0)
            print("GOOD : On arrete la lecture, player_stmt", self.player_stmt)
            return self.player_stmt
        elif self.player_stmt == False:
            self.player = vlc.MediaPlayer(self.playlist[0])
            radio = self.player.play()
            self.player_stmt = True
            touch.set_led(5, 1)
            print("on lance la lecture, player_stmt:", self.player_stmt)
            return self.player_stmt

    def illuminate(self, channel, event):
        for x in range(6):
            touch.set_led(x, 1)
            time.sleep(0.1)
            touch.set_led(x, 0)

    def backlight_screen(self):
        if self.backlight == True: 
            for x in range(6):
                backlight.set_pixel(x, 0, 0, 0)            
            print(self.backlight)
            self.backlight == False
        else: 
            for x in range(6):
                backlight.set_pixel(x, 255, 79, 193)
            print(self.backlight)
            self.backlight == True
        backlight.show()
