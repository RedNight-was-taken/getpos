import pyautogui
import time
from delphivcl import *

class GUIApp(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "Position Getter")
        self.SetBounds(20, 20, 450, 100)

        self.lblHello = Label(self)
        self.lblHello.SetBounds(20, 5, 20, 20)
        self.lblHello.SetProps(
            Parent=self,
            Caption="Apres avoir cliquer sur commencer, vous avez 3 secondes pour vous placer.")

        self.add_task_btn = Button(self)
        self.add_task_btn.Parent = self
        self.add_task_btn.SetBounds(15, 25,100,30)
        self.add_task_btn.Caption = "Commencer"
        self.add_task_btn.OnClick = self.getpos

    def getpos(self, Sender):
        time.sleep(3)
        self.lblHello.Caption = pyautogui.position()

def main():
    Application.Initialize()
    Application.MainFormOnTaskBar = True   
    Application.Title = "Position Getter"
    app = GUIApp(Application)
    app.Show()
    FreeConsole()
    Application.Run()
    app.Destroy()

main()