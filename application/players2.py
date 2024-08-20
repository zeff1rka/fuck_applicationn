from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class players2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        gl = GridLayout(cols= 2)
        gl2 = GridLayout(cols=3, rows=39, spacing= 10, padding= 50, size_hint_y=None)
        bl2 = BoxLayout()
        main_bl = BoxLayout()
        
        bl.add_widget(Label(text= "Название команды"))
        self.name_team = TextInput(multiline=False)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры"))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False)
        bl.add_widget(self.name_match)
        
        bl.add_widget(Label(text= "дата игры"))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False)
        bl.add_widget(self.date_match)
        
        end = Button(text= "Рассчёт")
        end.bind(on_release=self.math_operation)
        bl2.add_widget(end)
        
        match_plus = Button(text= "Назад")
        match_plus.bind(on_release=self.switch_match_plus)
        bl2.add_widget(match_plus)
        
        main_bl.add_widget(bl)
        main_bl.add_widget(gl)
        main_bl.add_widget(gl2)
        main_bl.add_widget(bl2)
        
        scroll = ScrollView()
        scroll.add_widget(main_bl)
        
        self.add_widget(scroll)
    
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"

    def math_operation(self, *args):
        pass