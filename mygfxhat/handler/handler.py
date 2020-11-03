from gfxhat import touch
import handler_function as f


class Handler:
    ''' When instantiate this, put functions to buttons of GFXHAT '''
    def __init__(self):
        self.buttons = self.initialize_button()
        self.player_stmt = False

        
    def initialize_button(self):
        touch.on(0, f.handler)
        touch.on(1, f.handler)
        touch.on(2, f.handler)
        touch.on(3, f.handler)
        touch.on(4, f.display_time)
        touch.on(5, launch_radio)


    def launch_radio(self, channel, event): 
        import pdb; pdb.set_trace()
        if self.player_stmt == True: 
            print("On arrete la lecture")
            player.stop()
            self.player_stmt = False
            return self.player_stmt
        elif player_stmt == False:
            print("On lance la lecture...")
            player = vlc.MediaPlayer(playlist[0])
            radio = player.play()
            self.player_stmt == True
            return self.player_stmt