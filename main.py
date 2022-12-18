import pyautogui as pya 
import datetime
import time
startHour = int(input("hora:"))
startMin = int(input("Minuto:"))
startTime = startHour, startMin

def iniciar():
    print("inicando a inicialização")
    startButton = 'startButton.png'
    locateOfStartButtton = pya.locateCenterOnScreen(startButton, confidence = 0.9)
    pya.click(locateOfStartButtton)

while True:
    dataReal = datetime.datetime.now()
    hourReal = dataReal.hour
    minReal = dataReal.minute
    hourMinReal = hourReal, minReal
    time.sleep(3)
    print(startTime)
    print(hourMinReal)
    if startTime == hourMinReal:
        iniciar()
        time.sleep(60)