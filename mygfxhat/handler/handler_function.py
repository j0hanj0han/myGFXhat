
import datetime
import vlc


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
    import pdb; pdb.set_trace()
    if 'player' in locals(): 
        if player.is_playing() == 1:
                print("Lecture en cours...")
                print("On arrete la lecture")
                player.stop()
        else:
            print("On relance la lecture")
            player.play()
            return player
    else:
        try:
            print("On lance la lecture...")
            player = vlc.MediaPlayer(playlist[0])
            radio = player.play()
            return player
        except Exception as e:
            print(e)

