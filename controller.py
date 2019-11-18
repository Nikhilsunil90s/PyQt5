from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QListWidgetItem
import sys
from main import Ui_firstwindow
from googlesearch import Ui_googlewindow
from utube import Ui_YoutubeWindow
from urlwindow import Ui_UrlWindow
from novel import Ui_NovelWindow
from compwindow import Ui_computerwindow
from compiler import Ui_compilerwindow
import webbrowser
#from gtts import gTTS

class CompilerClass(QMainWindow):
    def compile(self):
        inputcode = self.ui.textEdit.toPlainText()
        lang = self.ui.comboBox.currentText()
        self.ui.statusbar.showMessage('Compiling Your Code...')
        lang_dict = {'C' : 'c', 'C++':'cpp','Java':'java','Python':'python3'}
        import requests
        import json
        datadict = {'clientId':'2b6618ec421ce4f3c9cf416ae969db79','clientSecret':'e2ff5d2fefc5b558570de26a1c99353ac29970f31fefa27ba0425f52a4db844b', 'script':inputcode,'language':lang_dict.get(lang),'versionIndex':'2'}
        headers = {'content-type':'application/json'}
        response = requests.post('https://api.jdoodle.com/v1/execute',data = json.dumps(datadict), headers = headers)
        x = response.json()
        self.ui.textEdit_2.setText(x['output'])
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_compilerwindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.compile)


class CompClass(QMainWindow):
    def opensett(self):
        self.ui.statusbar.showMessage('Opening Your Computer Settings...')
        import os
        os.chdir('C:/Users/net sol')
        os.startfile('ms-settings:')
        self.ui.statusbar.showMessage('Settings Opened!')

    def showExplorer(self):
        self.ui.statusbar.showMessage('Opening Your Computer Explorer...')
        import os
        os.chdir('C:/Windows')
        os.startfile('explorer.exe')
        self.ui.statusbar.showMessage('Explorer Opened!')

    def showWord(self):
        self.ui.statusbar.showMessage('Opening MS Word...')
        import os
        os.chdir('C:/Program Files (x86)/Microsoft Office/Office12')
        os.startfile('WINWORD.exe')
        self.ui.statusbar.showMessage('MS Word Opened!')

    def showWinamp(self):
        self.ui.statusbar.showMessage('Opening MS Winamp...')
        import os
        os.chdir('C:/Program Files/Windows Media Player')
        os.startfile('wmplayer.exe')
        self.ui.statusbar.showMessage('MS Winamp Opened!')
        
    def showCalendar(self):
        self.ui.statusbar.showMessage('Opening MS Winamp...')
        import os
        os.chdir('C:/Program Files/Windows Media Player')
        os.startfile('wmplayer.exe')
        self.ui.statusbar.showMessage('MS Winamp Opened!')
        
    def showCalc(self):
        self.ui.statusbar.showMessage('Opening Calculator...')
        import os
        os.chdir('C:/Windows/System32')
        os.startfile('calc.exe')
        self.ui.statusbar.showMessage('MS Calculator Opened!')

    def fetchcommand(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.statusbar.showMessage('Speak Something: ')
            audio = self.recognizer.listen(source,phrase_time_limit = 5)
        try:
            self.ui.statusbar.showMessage('Processing Audio...')
            text = self.recognizer.recognize_google(audio)
            print(text)
            self.ui.statusbar.showMessage('Speech Captured!')
            self.ui.statusbar.showMessage('Preparing Your Results...')
        except sr.UnknownValueError:
            self.ui.statusbar.showMessage('Couldn\'t Understand What You Said!')
        except sr.RequestError:
            self.ui.statusbar.showMessage('Check Your Internet Connection...')
        if text == 'open settings':
            self.opensett()
        elif text == 'open calculator':
            self.showCalc()
        elif text == 'open explorer' or text == 'open computer explorer':
            self.showExplorer()
        elif text == 'open Microsoft Word' or text == 'open MS Word':
            print(text)
            self.showWord()
        elif text == 'open media player' or text == 'open winamp':
            self.showWinamp()
        else:
            pass
        
        
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_computerwindow()
        self.ui.setupUi(self)
        self.ui.commandLinkButton_2.clicked.connect(self.opensett)
        self.ui.commandLinkButton.clicked.connect(self.showExplorer)
        self.ui.commandLinkButton_3.clicked.connect(self.showWord)
        self.ui.commandLinkButton_4.clicked.connect(self.showWinamp)
        self.ui.commandLinkButton_5.clicked.connect(self.showCalc)
        self.ui.commandLinkButton_6.clicked.connect(self.showCalendar)
        self.ui.pushButton.clicked.connect(self.fetchcommand)
'''class NovelClass(QMainWindow):
    def loadnovels(self):
        file = QFileDialog.getOpenFileName(self,'Select A Text Novel: ')
        #print(file)
        self.ui.listWidget.addItem(f"Novel_Path: {file[0]}")

    def readNovel(self):
        import os
        from gtts import gTTS
        x = self.ui.listWidget.currentItem().text()
        print(x)
        filepath = x.split(' ',1)[1]
        #os.startfile(filepath)
        print(filepath)
        with open(filepath,'r') as self.filedata:
            print('File Opened!')
            maintext = self.filedata.read()
        print("Read Data: ",maintext)
        print('Data Read!')
        self.ui.statusbar.showMessage('Reading Your Novel...')
        try:
            self.tts = gTTS(maintext)
            self.tts.save('mynovel.mp3')
            os.startfile('mynovel.mp3')
        except ModuleNotFoundError:
            print("Module Error!")
        self.ui.statusbar.showMessage('Worked!')

            
        
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_NovelWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadnovels)
        self.ui.listWidget.itemDoubleClicked.connect(self.readNovel)
'''

class UrlClass(QMainWindow):
    def urlsearch(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.statusbar.showMessage('Speak Something: ')
            audio = self.recognizer.listen(source,phrase_time_limit = 5)
        try:
            self.ui.statusbar.showMessage('Processing Audio...')
            text = self.recognizer.recognize_google(audio)
            print(text)
            self.ui.statusbar.showMessage('Speech Captured!')
            self.ui.statusbar.showMessage('Preparing Your Results...')
        except sr.UnknownValueError:
            self.ui.statusbar.showMessage('Couldn\'t Understand What You Said!')
        except sr.RequestError:
            self.ui.statusbar.showMessage('Check Your Internet Connection...')
        webbrowser.open(f"www.{text.split(' ',1)[1]}.com")
        self.ui.statusbar.showMessage("Click And Speak Again!")

    def gotomain(self):
        self.fc = FirstClass()
        self.fc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_UrlWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.urlsearch)
        self.ui.actionMain_Window.triggered.connect(self.gotomain)
    
class FirstClass(QMainWindow):
    def showgoogle(self):
        self.gc = GoogleClass()
        self.gc.show()
        self.hide()

    def showutube(self):
        self.uc = YoutubeClass()
        self.uc.show()
        self.hide()

    def searchanurl(self):
        self.uc = UrlClass()
        self.uc.show()
        self.hide()

    def getmenus(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.statusbar.showMessage('Speak Something: ')
            audio = self.recognizer.listen(source,phrase_time_limit = 5)
        try:
            self.ui.statusbar.showMessage('Processing Audio...')
            text = self.recognizer.recognize_google(audio)
            print(text)
            self.ui.statusbar.showMessage('Speech Captured!')
            self.ui.statusbar.showMessage('Preparing Your Results...')
        except sr.UnknownValueError:
            self.ui.statusbar.showMessage('Couldn\'t Understand What You Said!')
        except sr.RequestError:
            self.ui.statusbar.showMessage('Check Your Internet Connection...')
        if text == 'play music on YouTube':
            self.yc = YoutubeClass()
            self.yc.show()
            self.hide()
        elif text == 'search on Google':
            self.gc = GoogleClass()
            self.gc.show()
            self.hide()
        elif text == 'search a URL':
            self.uc = UrlClass()
            self.uc.show()
            self.hide()
        elif text == 'compile code' or text == 'open compiler':
            self.nc = CompilerClass()
            self.nc.show()
            self.hide()
        elif text == 'commands to the computer' or text == 'commands to computer':
            self.cc = CompClass()
            self.cc.show()
            self.hide()
            print(text)

    def shownovel(self):
        self.nc = NovelClass()
        self.nc.show()
        self.hide()

    def compwin(self):
        self.obj = CompClass()
        self.obj.show()
        self.hide()
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_firstwindow()
        self.ui.setupUi(self)
        self.ui.commandLinkButton_2.clicked.connect(self.showgoogle)
        self.ui.commandLinkButton.clicked.connect(self.showutube)
        self.ui.commandLinkButton_4.clicked.connect(self.searchanurl)
        self.ui.pushButton.clicked.connect(self.getmenus)
        self.ui.commandLinkButton_5.clicked.connect(self.shownovel)
        self.ui.commandLinkButton_3.clicked.connect(self.compwin)

class GoogleClass(QMainWindow):
    def searchgoogle(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.statusbar.showMessage('Speak Something: ')
            audio = self.recognizer.listen(source,phrase_time_limit = 5)
        try:
            self.ui.statusbar.showMessage('Processing Audio...')
            text = self.recognizer.recognize_google(audio)
            print(text)
            self.ui.statusbar.showMessage('Speech Captured!')
            self.ui.statusbar.showMessage('Preparing Your Results...')
        except sr.UnknownValueError:
            self.ui.statusbar.showMessage('Couldn\'t Understand What You Said!')
        except sr.RequestError:
            self.ui.statusbar.showMessage('Check Your Internet Connection...')
        webbrowser.open(f"www.google.com/search?source=hp&ei=9ZghXeubEpa6rQH4kaSgDg&q={text.split(' ',1)[1]}")
        self.ui.statusbar.showMessage("Click And Speak Again!")
        
    def gotomain(self):
        self.fc = FirstClass()
        self.fc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_googlewindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.searchgoogle)
        self.ui.actionmain.triggered.connect(self.gotomain)

class YoutubeClass(QMainWindow):
    def playonutube(self):
        import speech_recognition as sr
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ui.statusbar.showMessage('Speak Something: ')
            audio = self.recognizer.listen(source,phrase_time_limit = 5)
        try:
            self.ui.statusbar.showMessage('Processing Audio...')
            text = self.recognizer.recognize_google(audio)
            print(text)
            self.ui.statusbar.showMessage('Speech Captured!')
            self.ui.statusbar.showMessage('Preparing Your Results...')
        except sr.UnknownValueError:
            self.ui.statusbar.showMessage('Couldn\'t Understand What You Said!')
        except sr.RequestError:
            self.ui.statusbar.showMessage('Check Your Internet Connection...')
        webbrowser.open(f"www.youtube.com/results?search_query={text.split(' ',1)[1]}")
        self.ui.statusbar.showMessage("Click And Speak Again!")

    def gotomain(self):
        self.fc = FirstClass()
        self.fc.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_YoutubeWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.playonutube)
        self.ui.actionMain_Window.triggered.connect(self.gotomain)

class Control:
    def __init__(self):
        pass

    def showFirst(self):
        self.fc = FirstClass()
        self.fc.show()

def main():
    app = QApplication(sys.argv)
    con = Control()
    con.showFirst()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
