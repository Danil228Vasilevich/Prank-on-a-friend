from pickle import TRUE
from pril import *
from game import *
from turtle import delay
import pyautogui as pag
import sys,random,webbrowser,time,pyglet,os
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
b = 0
ui.label_4.setText("BETA Функции только одну!")
def check_Steam():
    global b
    check = ui.radioButton.isChecked()
    Login = ui.textLogin.toPlainText()
    Pass = ui.textPass.toPlainText()
    if check == True:
        if Login == "Login" or Pass == "Password":
            ui.Dannie.setText("Не введены данные!")
            ui.Dannie.setStyleSheet('QLabel { color: #FF0000}')
            ui.infoLoading.setText("error! обратитесь разрабочику TRIBUTE")
            ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
            
        else:
            ui.Dannie.setText("Данные приняты!")
            ui.Dannie.setStyleSheet('QLabel { color: #00FF00}')
            ui.infoLoading.setText("Нет ответа ")
            ui.infoLoading.setStyleSheet('QLabel { color: #fc0}')
            b = 1
            
        

    else:
        ui.Dannie.setText("Не выполнено условие соглашения")
        ui.Dannie.setStyleSheet('QLabel { color: #FF0000}')
        ui.infoLoading.setText("error! обратитесь разрабочику TRIBUTE")
        ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
        print()
ui.ButPOTVERD.clicked.connect(check_Steam)
def genSt():
    ui.infoLoading.setText("Нет ответа ")
    ui.infoLoading.setStyleSheet('QLabel { color: #fc0}')
    check = ui.gal4.isChecked()
    kay = {0: '9Y3YI-I02EC-FYYDL',1:'WMP3V-JFZCV-TMMFK',2:'EMR3V-JPZCV-TOMFK',3:'GKHV-JFZCV-TMMFK',4:'EMTTV-JPYYV-TPPFK',5:'Иди в баню!',6:'https://youtu.be/7dXRCMYls1Q ',7:'WMP3V-JFZCV-TMMFK',8:'https://youtu.be/HsFVUNk5tY0'}
    gen = random.randint(0, 8)  # Генерируем
    player_name = kay[gen] 
    if check == True:
        ui.randomkay.setText("Проверка...")
        ui.randomkay.setStyleSheet('QTextBrowser { color: #FF0000}')
        ui.infoLoading.setText("error! Ti slishok mnogo hochesh")
        ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
    else:
        if gen == 6 or gen == 8:
            ui.randomkay.setText(player_name) 
            ui.randomkay.setStyleSheet('QTextBrowser { color: #FF0000}')
            webbrowser.open (player_name, new=2)
        else:
            ui.randomkay.setText(player_name)# Преобразуем в название
            ui.randomkay.setStyleSheet('QTextBrowser { color: #fc0}')
     

ui.generation.clicked.connect(genSt)

def BETA():
    g1 = ui.gal1.isChecked()
    g2 = ui.gal2.isChecked()
    g3 = ui.gal3.isChecked()

    if g1 == True:
        ui.label_4.setText("BETA Функция октивированна!") 
        webbrowser.open ("https://youtu.be/tGuV6xOc6qI", new=2)
        ui.label_4.setStyleSheet('QLabel { color: #FF0000}')
    elif g2 == True:
        ui.label_4.setText("BETA Функция октивированна!") 
        ui.infoLoading.setText("error! Ti slishok mnogo hochesh")
        ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
        ui.label_4.setStyleSheet('QLabel { color: #FF0000}')
    elif g3 == True:
        ui.label_4.setText("BETA Функция октивированна!") 
        ui.label_4.setStyleSheet('QLabel { color: #FF0000}')
        play()
    else:
        ui.label_4.setText("BETA Функции только одну!")
        ui.label_4.setStyleSheet('QLabel { color: #fc0}')
        ui.infoLoading.setText("Нет ответа ")
        ui.infoLoading.setStyleSheet('QLabel { color: #fc0}')
        

ui.gal1.clicked.connect(BETA)
ui.gal2.clicked.connect(BETA)
ui.gal3.clicked.connect(BETA)

def chislo():
    chis = ui.nacrutka.toPlainText()
    if chis == "Введите число для накрутки " or "":
        ui.infoLoading.setText(f"Введите число!")
        ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
    else:
        ui.infoLoading.setText(f"Добавлено число накрутки!:{chis}")
        ui.infoLoading.setStyleSheet('QLabel { color: #00FF00}')
ui.butnak.clicked.connect(chislo)

def start():
    ui.infoLoading.setText("Нет ответа ")
    ui.infoLoading.setStyleSheet('QLabel { color: #fc0}')
    if b == 0:
        ui.infoLoading.setText(f"Введите данные аккаунта")
        ui.infoLoading.setStyleSheet('QLabel { color: #FF0000}')
    else:
        
        ui.progressBarLod.setValue(100)
        ui.infoLoading.setText(f"Готово!")
        while True:
            pag.typewrite("frwagfragarggaagrgrgrgrrg")
            pag.moveTo(600, 600)   # перемещение мыши на X 600, Y 600
            pag.moveTo(100, 200, 2)   # перемещение мыши на X 100, Y 200 в течение 2 секунд

            pag.move(0, 50)       # перемещение мыши на 50 пикселей относительно ее предыдущего расположения

            pag.dragTo(100, 200, button='left')     # перемещение мыши на X 100, Y 200 с удержанием левой кнопки

            pag.dragTo(300, 400, 2, button='left')  # перемещение мыши на X 300, Y 400 в течение 2 секунд с удержанием левой кнопки

            pag.click()    #  щелчок мыши
            pag.click(x=100, y=200)  # перемещение на 100, 200, а затем нажатие левой кнопкой

            pag.click(button='right')  # щелчок правой кнопкой мыши
            pag.doubleClick()  # двойной щелчок левой кнопкой
            pag.click(clicks=2)  # двойной щелчок левой кнопкой мыши
            pag.click(clicks=2, interval=0.25)  # двойной щелчок левой кнопкой мыши с паузой в четверть секунды между щелчками

            pag.scroll(10)   # прокрутка на 10 "кликов" вверх
            pag.scroll(-10)   # прокрутка на 10 "кликов" вниз

            pag.hscroll(10)   # прокрутка на 10 "кликов" вправо
            pag.hscroll(-10)   # прокрутка на 10 "кликов" влево
            os.startfile(r"C:/WINDOWS/System32/calc.exe")
            delay(100)
            sound = pyglet.media.load('MORGENSHTERN - БЕБЕБЕ (remix).mp3', streaming=False)
            sound.play()
            webbrowser.open ("https://youtu.be/tGuV6xOc6qI", new=2)
            os.startfile(r"D:/nedohaker/icons8-hack-100.png")
            os.startfile(r"D:/nedohaker/fish.png")
            pag.typewrite("frwagfragarggaagrgrgrgrrg")
            pag.moveTo(600, 600)   # перемещение мыши на X 600, Y 600
            pag.moveTo(100, 200, 2)   # перемещение мыши на X 100, Y 200 в течение 2 секунд

            pag.move(0, 50)       # перемещение мыши на 50 пикселей относительно ее предыдущего расположения

            pag.dragTo(100, 200, button='left')     # перемещение мыши на X 100, Y 200 с удержанием левой кнопки

            pag.dragTo(300, 400, 2, button='left')  # перемещение мыши на X 300, Y 400 в течение 2 секунд с удержанием левой кнопки

            pag.click()    #  щелчок мыши
            pag.click(x=100, y=200)  # перемещение на 100, 200, а затем нажатие левой кнопкой

            pag.click(button='right')  # щелчок правой кнопкой мыши
            pag.doubleClick()  # двойной щелчок левой кнопкой
            pag.click(clicks=2)  # двойной щелчок левой кнопкой мыши
            pag.click(clicks=2, interval=0.25)  # двойной щелчок левой кнопкой мыши с паузой в четверть секунды между щелчками

            pag.scroll(10)   # прокрутка на 10 "кликов" вверх
            pag.scroll(-10)   # прокрутка на 10 "кликов" вниз

            pag.hscroll(10)   # прокрутка на 10 "кликов" вправо
            pag.hscroll(-10)   # прокрутка на 10 "кликов" влево
            
        
        


    
            
    

            

            

            
            
        

ui.Start.clicked.connect(start)
#ui.Start.clicked.connect(pizda)

sys.exit(app.exec_())