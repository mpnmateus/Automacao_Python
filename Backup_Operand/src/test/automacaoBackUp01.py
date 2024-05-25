import pyautogui
import time




pyautogui.alert("O código vai começar")

pyautogui.PAUSE = 1

#vai até a página operand aberta
pyautogui.hotkey('winleft', 'tab')

pyautogui.moveTo(547,212)
pyautogui.mouseDown()
pyautogui.mouseUp()

#clica na Segunda aba
pyautogui.hotkey('ctrl', '2')

for i in range (42):

    #move o cursor para o botão download
    pyautogui.moveTo(1261, 147)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
    #pressiona enter para baixar arquivo
    pyautogui.press('enter')

    #fecha aba
    pyautogui.hotkey('ctrl', 'w')
    
    #Vai para a segunda aba
    pyautogui.hotkey('ctrl', '2')

    i += 1

pyautogui.alert("O código parou de rodar")

