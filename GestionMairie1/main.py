from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.core.window import Window

#Builder.load_file('AccueilMaire.kv')
#Builder.load_file('ActesMaire.kv')
#Builder.load_file('ActesNaissanceMaire.kv')
#Builder.load_file('ActesDécèsMaire.kv')
#Builder.load_file('ActesMariageMairie.kv')
#Builder.load_file('BancsMaire.kv')
#Builder.load_file('DocumentsMaire.kv')
#Builder.load_file('EmployésMaire.kv')
#Builder.load_file('ProjetsMaire.kv')
#Builder.load_file('RDVMaire.kv')
#Builder.load_file('PersonneMaire.kv')
#Builder.load_file('Comptabilité.kv')
#Builder.load_file('ActesSS.kv')
Builder.load_file('ActesNaissanceSS.kv')
#Builder.load_file('ActesMariageSS.kv')
#Builder.load_file('ActesDécèsSS.kv')





class myGrid(Widget) :
    pass

class myApp(App):
    def build(self):
        Window.clearcolor="#FFFFFF"


        return myGrid()


myApp().run()
