from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Set black theme
Window.clearcolor = (0, 0, 0, 1)

# Dictionary mapping English letters to Braille characters
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': '⠀'
}

# Font supporting Braille Unicode characters
braille_font = 'DejaVuSans.ttf'  # You may need to change this to a font that supports Braille characters

class BrailleConverter(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Text input for English text
        self.input_text = TextInput(hint_text='Enter English text', size_hint=(1, 0.5))
        
        # Button to trigger conversion
        self.convert_button = Button(text='Convert', size_hint=(1, 0.1))
        self.convert_button.bind(on_press=self.convert_text)
        
        # Label to display Braille text
        self.output_label = Label(text='', halign='center', valign='middle', size_hint=(1, 0.5), font_name=braille_font)
        
        layout.add_widget(self.input_text)
        layout.add_widget(self.convert_button)
        layout.add_widget(self.output_label)
        return layout

    def convert_text(self, instance):
        braille_text = self.to_braille(self.input_text.text.lower())
        self.output_label.text = braille_text

    def to_braille(self, text):
        braille_text = ''
        for char in text:
            if char in braille_dict:
                braille_text += braille_dict[char]
        return braille_text

if __name__ == '__main__':
    BrailleConverter().run()
