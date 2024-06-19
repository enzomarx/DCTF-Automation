import pyautogui
import time
import DominioWeb

DominioWeb()
def enviar_dctf(cnpj, periodo):
    start_time = time.time()
    
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('edge\n', interval=0.1)
    time.sleep(2)
    
    pyautogui.typewrite('https://dominio-web.thomsonreuters.com\n', interval=0.1)
    time.sleep(5)
    
    pyautogui.click(x=400, y=300)
    pyautogui.typewrite('usuario\n', interval=0.1)
    pyautogui.typewrite('senha\n', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)
    
    pyautogui.click(x=400, y=400)
    time.sleep(3)
    
    pyautogui.click(x=400, y=500)
    pyautogui.typewrite(cnpj, interval=0.1)
    pyautogui.click(x=400, y=600)
    pyautogui.typewrite(periodo, interval=0.1)
    
    pyautogui.click(x=500, y=700)
    time.sleep(5)
    
    pyautogui.hotkey('alt', 'f4')
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")

if __name__ == '__main__':
    enviar_dctf()
    DominioWeb()