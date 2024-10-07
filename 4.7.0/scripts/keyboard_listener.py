from pynput import keyboard

def on_press(key):
    print('Key %s pressed' % key)

def on_release(key):
    print('Key %s released' % key)
    if key == keyboard.Key.esc: # quit the process when input is esc
        return False
        
 # how to register a listener
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
    ) as listener:
    listener.join()
