import keyboard, pyautogui

while True:
    if keyboard.read_key() == 'right':
        print('Go right')
        pyautogui.move(20, 0)
    elif keyboard.read_key() == 'left':
        print('Go left')
        pyautogui.move(-20, 0)
    elif keyboard.read_key() == 'up':
        print('Go up')
        pyautogui.move(0, -20)
    elif keyboard.read_key() == 'down':
        print('Go down')
        pyautogui.move(0, 20)
    elif keyboard.read_key() == 'enter':#left click
        print('Clicked')
        pyautogui.leftClick()
    elif keyboard.read_key() == 'shift':
        print('RT click')
        pyautogui.rightClick()
        