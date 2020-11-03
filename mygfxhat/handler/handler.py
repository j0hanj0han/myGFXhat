from gfxhat import touch
import handler_function as f


class Handler:
    ''' When instantiate this, put functions to buttons of GFXHAT '''
    def __init__(self):
        self.buttons = self.initialize_button()

        
    def initialize_button(self):
        touch.on(0, f.handler)
        touch.on(1, f.handler)
        touch.on(2, f.handler)
        touch.on(3, f.handler)
        touch.on(4, f.display_time)
        player = touch.on(5, f.launch_radio)


