import time, datetime
import vlc
import signal
from gfxhat import touch, lcd, backlight, fonts

from handler import handler as h



class Handler:


    ''' When instantiate this, put functions to buttons of GFXHAT '''
    def __init__(self):

        self.initialize_button()
        self.player_stmt = False
        self.playlist = ["http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"]

        
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
        
        time.sleep(0.5)
        print("on rentre dans la fonction player_stmt:", self.player_stmt)

        if self.player_stmt == True: 
            self.player.stop()
            self.player_stmt = False
            touch.set_led(5, 0)
            print("GOOD : On arrete la lecture, player_stmt", self.player_stmt)
            return self.player_stmt
        elif self.player_stmt == False:
            self.player = vlc.MediaPlayer(self.playlist[2])
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