# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.mouse_jiggler import MouseJiggler
from kmk.extensions.media_keys import MediaKeys
# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
layer = Layers()
keyboard.modules.append(layer)
keyboard.modules.append(MouseJiggler())
keyboard.modules.append(MediaKeys())
# Define your pins here!
PINS = [board.GP6, board.GP7, board.GP0, board.GP4, board.GP2, board.GP1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.F1, KC.F2, KC.F3,
     KC.F4, KC.F5, KC.TG(1)],

    [KC.trns, KC.up, KC.TG(0),
     KC.left, KC.down, KC.right],

    [KC.MJ_TOGGLE, KC.MEDIA_PLAY_PAUSE, KC.trns,
     KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.NO] 
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
