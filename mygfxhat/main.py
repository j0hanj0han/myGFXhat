
import time, datetime, signal
import os, sys

import vlc
from gfxhat import touch


#internal import
from display import Screen


# handler for touch
def handler(channel, event):
    print("Got {} on channel {}".format(event, channel))

def display_time(channel, event):
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))


# radio section
playlist = ["http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"]
    
def launch_radio(channel, event):
    print("coucou dans le bouton!")
    player = vlc.MediaPlayer(playlist[0])
    if player.is_playing() == 1:
            print("Lecture en cours...")
            print("On arrete la lecture")
            player.stop()
    else:
        try:
            print("On lance la lecture...")
            radio = player.play()
        except Exception as e:
            print(e)




def main():
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    
    #activate handler
    for x in range(5):
        touch.on(x, handler)

    touch.on(4, display_time)

    touch.on(5, launch_radio)
    # light on screen and display object list
    try: 
        screen = Screen(object_list)
        screen.start()
        screen.draw_object(object_list)

        signal.pause()


    except KeyboardInterrupt: # if exit with ctrl + c shut off the screen
        print('Interrupted')
        try:
            screen.stop()
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
   main()