from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from llama_caller import LlamaCaller
from prompt_builder import PromptBuilder

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.text_input = TextInput(hint_text="Enter your goals (separated by commas)")
        button = Button(text="Generate Affirmations")
        button.bind(on_press=self.on_button_click)

        layout.add_widget(self.text_input)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        goals = [goal.strip() for goal in self.text_input.text.split(",")]
        prompt_builder = PromptBuilder()
        prompt = prompt_builder.build_prompt(goals)
        llama_caller = LlamaCaller()
        output_file_name = llama_caller.chat_with_llama_3(prompt)
        self.text_input.text = ""

if __name__ == '__main__':
    MainApp().run()