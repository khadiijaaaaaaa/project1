from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        #screen
        main_Layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white",multiline = False, halign='right', font_size = 65 , readonly = True)#multiline=false: to stay in the same line no matter what is the screen width

        main_Layout.add_widget(self.solution)
        buttons = [
            ["7", "8" ,"9" ,"/"],
            ["4", "5" ,"6" ,"*"],
            ["1", "2" ,"3" ,"+"],
            [".", "0" ,"C" ,"-"],
        ]

        #insert the buttons inside the screen
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color="grey", #to center the buttons:
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                #everytime we press a btn , we call a fct named :on_button_press
                button.bind(on_press=self.on_button_press)

                #insert buttons inside h_layout 
                h_layout.add_widget(button)
            #insert h_layout inside main_Layout
            main_Layout.add_widget(h_layout)

        equal_button = Button(
                    text = "=", font_size=30, background_color="grey", #to center the buttons:
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_Layout.add_widget(equal_button)

        return main_Layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        #for the clear button C:
        if button_text == 'C':
            self.solution.text = ""
        else:
            #if we type an operator ad then we try to type another op, we won't show anyything inside the screen
            if current and (
                self.last_was_operator and button_text in self.operators):
                return 
            #if we start with an operator well show nothing on screen
            elif current =="" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        #clear variables
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


#run the app
if __name__ == "__main__":
    app = MainApp()
    app.run()