
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
    if 'player_stmt' in locals():
        pass
    else:
        self.player_stmt = False

    print("coucou dans le bouton!")
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

    
    
    
    
    
    # if player.is__playing(): 
    #     if locals()["player"] == True:
                
    #             player.stop()
    #             locals()["player"] = False
    #     else:
    #         print("On relance la lecture")
    #         player.play()
    #         locals()["player"] = True
    # else:
    #     try:
    #         print("On lance la lecture...")
    #         player = vlc.MediaPlayer(playlist[0])
    #         radio = player.play()
    #         locals()["player"] = True
    #     except Exception as e:
    #         print(e)

