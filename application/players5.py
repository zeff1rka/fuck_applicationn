from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class players5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        bl.add_widget(Label(text= "Название команды"))
        self.name_team = TextInput(hint_text= "Приморский край", multiline=False)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры"))
        self.name_game = TextInput(hint_text= "Первенство россии среди кого и какого возраста", multiline=False)
        bl.add_widget(self.name_game)
        
        bl.add_widget(Label(text="Дата игры"))
        self.date = TextInput(hint_text= "дд.мм.гггг", multiline=False)
        bl.add_widget(self.date)
        
        end = Button(text= "Рассчёт")
        end.bind(on_release=self.math_operation)
        bl.add_widget(end)
        
        match_plus = Button(text= "Назад")
        match_plus.bind(on_release=self.switch_match_plus)
        bl.add_widget(match_plus)
        
        self.add_widget(bl)
    
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"

    def math_operation(self, *args):
        pass