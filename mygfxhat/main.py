import display


if __name__ == "__main__":
    object_list = ["Hello Johan !", "Hello Nina !", "Go to Nice!"]
    my_screen = DisplayedObject(object_list)
    my_screen.start()
    my_screen.draw_object(object_list)
    time.sleep(5)
    my_screen.stop()
    pass
