from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#Create application
class MainApp(App):
    #Define  Initialise the application, It called only once
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]   #Initialise operators
        self.last_was_operator = None
        self.last_button = None

        #Create box layout in vertical
        main_layout = BoxLayout(orientation = "vertical")

        #Create input field to display value and solution value
        self.solution = TextInput(background_color = "black", foreground_color = "white",
                                  multiline = False, halign = "right", font_size = 55, readonly = True)

        main_layout.add_widget(self.solution)
        #Create list calculatr buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        #Set label and formating to the buttons
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        #Create equal button
        equal_button = Button(
            text = "=", font_size = 30, background_color = "grey",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    #Define functions to process the button press and equal button
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        #Condition to clear screen
        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            #If screen is empty dont allow user to press operator before button
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    #Create function to fine solution
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))    #Evaluate the expression and Convert value into string
            self.solution.text = solution

#Run Application
if __name__ == "__main__":
    app = MainApp()
    app.run()   #Launches the application in standAlone mode