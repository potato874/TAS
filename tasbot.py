import keyboard

# The button you press to make a new macro
record_macro_key = "esc"

# The button you press to play the existing macro
play_macro_key = "ctrl+esc"

def record_macro():
    recorded=keyboard.record(until=record_macro_key)

def play_macro():
    keyboard.play(recorded)

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# keyboard.press_and_release('shift+s, space')

# keyboard.write('The quick brown fox jumps over the lazy dog.')

# keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# # Press PAGE UP then PAGE DOWN to type "foobar".
# keyboard.add_hotkey('page up+page down', lambda: keyboard.write('foobar'))

# # Blocks until you press esc.
# keyboard.wait('esc')

# # Record events until 'esc' is pressed.
# recorded = keyboard.record(until='esc')
# # Then replay back at three times the speed.
# keyboard.play(recorded, speed_factor=3)

# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# # Block forever, like `while True`.
# keyboard.wait()