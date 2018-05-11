"""Main script file: Detection and translation of keypresses"""

import pyperclip
from time import sleep
from sneakysnek.recorder import Recorder
from translations import detect_translate

key_status = {
    'CTRL': None
}
copy_keys = ('KEY_X', 'KEY_C')


def key_event(event):
    """Called with the key event argument on each event."""
    key_value = ''
    if hasattr(event, 'keyboard_key'):
        key_value = event.keyboard_key.value
    if 'CTRL' in key_value:
        key_status['CTRL'] = event.event.value
    elif (
        key_value in copy_keys and
        event.event.value == 'DOWN' and
        key_status['CTRL'] == 'DOWN'
    ):
        sleep(0.1)
        copied = pyperclip.paste()
        translated = detect_translate(copied)
        pyperclip.copy(translated)

recorder = Recorder.record(key_event)

while True:
    sleep(0.1)
