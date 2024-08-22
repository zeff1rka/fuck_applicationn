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
        gl2 = GridLayout(cols=3, rows=39, spacing= 5, padding= 1, size_hint_y=None, height= 1200)
        bl2 = BoxLayout()
        main_bl = BoxLayout(size_hint=(1, None), height=2000)
        
        bl.add_widget(Label(text= "Название команды" , color = "#02034e", size_hint_y=None, height= 28))
        self.name_team = TextInput(hint_text= "Приморкий край" , multiline=False, size_hint_y=None, height= 28)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры" , color = "#02034e", size_hint_y=None, height= 28))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False, size_hint_y=None, height= 28)
        bl.add_widget(self.name_match)
        
        bl.add_widget(Label(text= "дата игры" , color = "#02034e", size_hint_y=None, height= 28))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 28)
        bl.add_widget(self.date_match)
        
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 28))
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 28))
        self.name_1 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 28)
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 28)
        gl.add_widget(self.name_2)
        
        gl2.add_widget(Label(text="1" , color = "#02034e", size_hint=(None, 1) , size = (20 , 10)))
        self.one_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_1)
        self.one_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_2)
        
        gl2.add_widget(Label(text="2" , color = "#02034e"))
        self.two_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_1)
        self.two_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_2)
        
        gl2.add_widget(Label(text="3" , color = "#02034e"))
        self.three_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.three_1)
        self.three_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.three_2)
        
        gl2.add_widget(Label(text="4" , color = "#02034e"))
        self.four_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.four_1)
        self.four_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.four_2)
        
        gl2.add_widget(Label(text="5" , color = "#02034e"))
        self.five_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.five_1)
        self.five_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.five_2)
        
        gl2.add_widget(Label(text="6" , color = "#02034e"))
        self.six_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.six_1)
        self.six_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.six_2)
        
        gl2.add_widget(Label(text="7" , color = "#02034e"))
        self.seven_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.seven_1)
        self.seven_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.seven_2)
        
        gl2.add_widget(Label(text="8" , color = "#02034e"))
        self.eight_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.eight_1)
        self.eight_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.eight_2)
        
        gl2.add_widget(Label(text="9" , color = "#02034e"))
        self.nine_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.nine_1)
        self.nine_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.nine_2)
        
        gl2.add_widget(Label(text="10" , color = "#02034e"))
        self.one_zero_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_zero_1)
        self.one_zero_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_zero_2)
        
        gl2.add_widget(Label(text="11" , color = "#02034e"))
        self.one_one_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_one_1)
        self.one_one_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_one_2)
        
        gl2.add_widget(Label(text="12" , color = "#02034e"))
        self.one_two_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_two_1)
        self.one_two_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_two_2)
        
        gl2.add_widget(Label(text="13" , color = "#02034e"))
        self.one_three_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_three_1)
        self.one_three_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_three_2)
        
        gl2.add_widget(Label(text="14" , color = "#02034e"))
        self.one_four_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_four_1)
        self.one_four_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_four_2)
        
        gl2.add_widget(Label(text="15" , color = "#02034e"))
        self.one_five_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_five_1)
        self.one_five_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_five_2)
        
        gl2.add_widget(Label(text="16" , color = "#02034e"))
        self.one_six_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_six_1)
        self.one_six_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_six_2)
        
        gl2.add_widget(Label(text="17" , color = "#02034e"))
        self.one_seven_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_seven_1)
        self.one_seven_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_seven_2)
        
        gl2.add_widget(Label(text="18" , color = "#02034e"))
        self.one_eight_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_eight_1)
        self.one_eight_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_eight_2)
        
        gl2.add_widget(Label(text="19" , color = "#02034e"))
        self.one_nine_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_nine_1)
        self.one_nine_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.one_nine_2)
        
        gl2.add_widget(Label(text="20" , color = "#02034e"))
        self.two_zero_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_zero_1)
        self.two_zero_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_zero_2)
        
        gl2.add_widget(Label(text="21" , color = "#02034e"))
        self.two_one_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_one_1)
        self.two_one_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_one_2)
        
        gl2.add_widget(Label(text="22" , color = "#02034e"))
        self.two_two_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_two_1)
        self.two_two_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_two_2)
        
        gl2.add_widget(Label(text="23" , color = "#02034e"))
        self.two_three_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_three_1)
        self.two_three_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_three_2)
        
        gl2.add_widget(Label(text="24" , color = "#02034e"))
        self.two_four_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_four_1)
        self.two_four_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_four_2)
        
        gl2.add_widget(Label(text="25" , color = "#02034e"))
        self.two_five_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_five_1)
        self.two_five_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_five_2)
        
        gl2.add_widget(Label(text="26" , color = "#02034e"))
        self.two_six_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_six_1)
        self.two_six_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_six_2)
        
        gl2.add_widget(Label(text="27" , color = "#02034e"))
        self.two_seven_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_seven_1)
        self.two_seven_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_seven_2)
        
        gl2.add_widget(Label(text="28" , color = "#02034e"))
        self.two_eight_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_eight_1)
        self.two_eight_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_eight_2)
        
        gl2.add_widget(Label(text="29" , color = "#02034e"))
        self.two_nine_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_nine_1)
        self.two_nine_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.two_nine_2)
        
        gl2.add_widget(Label(text="30" , color = "#02034e"))
        self.three_zero_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.three_zero_1)
        self.three_zero_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.three_zero_2)
        
        gl2.add_widget(Label(text="extra-1" , color = "#02034e"))
        self.extra_one_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_one_1)
        self.extra_one_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_one_2)
        
        gl2.add_widget(Label(text="extra-2" , color = "#02034e"))
        self.extra_two_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_two_1)
        self.extra_two_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_two_2)
        
        gl2.add_widget(Label(text="extra-3" , color = "#02034e"))
        self.extra_three_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_three_1)
        self.extra_three_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_three_2)
        
        gl2.add_widget(Label(text="extra-4" , color = "#02034e"))
        self.extra_four_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_four_1)
        self.extra_four_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_four_2)
        
        gl2.add_widget(Label(text="extra-5" , color = "#02034e"))
        self.extra_five_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_five_1)
        self.extra_five_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_five_2)
        
        gl2.add_widget(Label(text="extra-6" , color = "#02034e"))
        self.extra_six_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_six_1)
        self.extra_six_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_six_2)
        
        gl2.add_widget(Label(text="extra-7" , color = "#02034e"))
        self.extra_seven_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_seven_1)
        self.extra_seven_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_seven_2)
        
        gl2.add_widget(Label(text="extra-8" , color = "#02034e"))
        self.extra_eight_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_eight_1)
        self.extra_eight_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_eight_2)
        
        gl2.add_widget(Label(text="extra-9" , color = "#02034e"))
        self.extra_nine_1 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_nine_1)
        self.extra_nine_2 = TextInput(hint_text= "0/1/2")
        gl2.add_widget(self.extra_nine_2)
        
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