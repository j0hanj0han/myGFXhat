from gfxhat import touch
import handler_function as f
import vlc


class Handler:


    ''' When instantiate this, put functions to buttons of GFXHAT '''
    def __init__(self):

        self.buttons = self.initialize_button()
        self.player_stmt = False
        # radio section
        self.playlist = ["http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"]

        
    def initialize_button(self):
        touch.on(0, f.handler)
        touch.on(1, f.handler)
        touch.on(2, f.handler)
        touch.on(3, f.handler)
        touch.on(4, f.display_time)
        touch.on(5, self.launch_radio)


    def launch_radio(self, channel, event): 
        import pdb; pdb.set_trace()
        print("on rentre dans la fonction player_stmt:", self.player_stmt)
        if self.player_stmt == True: 
            print("GOOD : On arrete la lecture")
            self.player.stop()
            self.player_stmt = False
            return self.player_stmt
        elif self.player_stmt == False:
            print("On lance la lecture...")
            self.player = vlc.MediaPlayer(self.playlist[0])
            radio = self.player.play()
            self.player_stmt = True
            print("1ere lecture on a un player stmt:", self.player_stmt)
            return self.player_stmt