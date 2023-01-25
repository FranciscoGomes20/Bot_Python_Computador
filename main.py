import pyautogui

pyautogui.PAUSE = 3
# Acessar arquivo
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

pyautogui.PAUSE = 3
# Preencher login
pyautogui.click(x=3051, y=263)
pyautogui.write("joao")

# Preencher senha
pyautogui.click(x=2993, y=314)
pyautogui.write("123")

# Fazer login
pyautogui.doubleClick(x=2845, y=450)
