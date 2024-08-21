import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        self.input_box = TextInput(multiline=False, readonly=True, halign='right', font_size=30)
        main_layout.add_widget(self.input_box)

        button_grid = GridLayout(cols=4, spacing=10, padding=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=30)
            button.bind(on_press=self.button_press)
            button_grid.add_widget(button)

        main_layout.add_widget(button_grid)

        return main_layout

    def button_press(self, instance):
        button_text = instance.text
        if button_text == '=':
            try:
                result = eval(self.input_box.text)
                self.input_box.text = str(result)
            except:
                self.input_box.text = 'Error'
        elif button_text == 'C':
            self.input_box.text = ''
        else:
            self.input_box.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
