import pyautogui, time
time.sleep(6)
f= open("spam.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


