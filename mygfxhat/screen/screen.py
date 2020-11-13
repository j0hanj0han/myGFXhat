import time, datetime
import signal
import vlc


from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw



class Screen:

    """ Display an object list """

    def __init__(self):
        self.init_screen()
        self.init_handler()

        
    def init_screen(self):
        self.screen_width = lcd.dimensions()[0]
        self.screen_height = lcd.dimensions()[1]
        self.font = ImageFont.load_default()
        self.backlight = True
        self.start()
        # draw 
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.initial_list = [now, "Hello Johan !", "Hello Nina !", "Go to Nice!"]
        self.object_list = self.initial_list
        self.draw_object(self.object_list)

        

    def init_handler(self):
        self.player_stmt = False
        self.backlight = True
        self.data = {"NRJ": "http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","France Info": "http://direct.franceinfo.fr/live/franceinfo-midfi.mp3", "Voltage":"http://start-voltage.ice.infomaniak.ch/start-voltage-high.mp3"}
        self.choices = list(self.data.values())
        self.radios =  list(self.data.keys())
        self.current_choice_index = 0
        touch.on(0, self.previous)
        touch.on(1, self.next)
        touch.on(2, self.backlight_screen)
        touch.on(3, self.illuminate)
        touch.on(4, self.actual_choice)
        touch.on(5, self.launch_radio)


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


    def draw_object(self, object_list):
        padding = 2
        lcd.clear()
        self.image = Image.new("P", (self.screen_width, self.screen_height))
        self.draw = ImageDraw.Draw(self.image)
        

        for object in object_list:
            text = object

            # print(text)
            w, h = self.font.getsize(text)
            x = 2
            y = (self.screen_height - h) // 6 + padding
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

    # handler for touch
    def handler(self, channel, event):
        print("Got {} on channel {}".format(event, channel))

    def previous(self, event, channel):
        if self.current_choice_index > 0:
            self.current_choice_index -= 1
            time.sleep(0.5)
        elif self.current_choice_index == 0:
            self.current_choice_index = len(self.choices) - 1 
            time.sleep(0.5)
        
        print("index:", self.current_choice_index)
        display_list = self.initial_list.append(self.radios[self.current_choice_index])
        self.draw_object(display_list)
        

    def next(self, event, channel):
        if self.current_choice_index < len(self.choices):
            self.current_choice_index += 1 
            time.sleep(0.5)
        if self.current_choice_index == len(self.choices):
            self.current_choice_index = 0
            time.sleep(0.5)
        print("index", self.current_choice_index)
        display_list = self.initial_list.append(self.radios[self.current_choice_index])
        import pdb; pdb.set_trace()
        self.draw_object(display_list)

    def actual_choice(self, event, channel):
        print("Current choice index", self.current_choice_index)
        print("Current radio selected:", self.choices[self.current_choice_index])


    def launch_radio(self, channel, event): 
        #import pdb; pdb.set_trace()
        
        time.sleep(0.5)
        print("on rentre dans la fonction player_stmt:", self.player_stmt)

        if self.player_stmt == True: 
            self.player.stop()
            self.player_stmt = False
            touch.set_led(5, 0)
            print("GOOD : On arrete la lecture, player_stmt", self.player_stmt)
            return self.player_stmt
        elif self.player_stmt == False:
            self.player = vlc.MediaPlayer(self.choices[2])
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

    def backlight_screen(self, channel, event):
        
        time.sleep(0.5)
        if self.backlight == True: 
            for x in range(6):
                backlight.set_pixel(x, 0, 0, 0)            
            
            backlight.show()
            self.backlight = False
            touch.set_led(2, 0)
            print("Backlight status: ", self.backlight)
            return self.backlight
        else: 
            for x in range(6):
                backlight.set_pixel(x, 255, 79, 193)
            backlight.show()
            self.backlight = True
            touch.set_led(2, 1)
            print("Backlight status: ", self.backlight)
            return self.backlight


    

        
