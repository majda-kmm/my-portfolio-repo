import tkinter as tk
from typing import List, Tuple
from PIL import Image,ImageTk
from .tk_init import *

#pyglet.font.add_file('S6_project/src/SinglyLinkedRegular-vmoRL.otf')
class Button:
    def __init__(self, master: tk.Tk, pos: Tuple[int, int], text: str, width: int = 100, height: int = 30,
                 color: str = RED, textcolor: str = RED) -> None:
        """
        :param master: Tkinter master widget
        :param pos: specifies the top left corner of the button (x, y)
        :param text: text to be displayed on the button
        :param width: width of the button
        :param height: height of the button
        :param color: background color of the button
        :param textcolor: color of the text
        """
        self.master = master
        self.text = text
        self.color = color
        self.textcolor = textcolor

        self.button = tk.Button(master, text=text, bg=color, fg=textcolor, width=width, height=height)
        self.button.place(x=pos[0], y=pos[1])

    def set_text(self, text: str) -> None:
        self.text = text
        self.button.config(text=text)

    def set_color(self, color: str) -> None:
        self.color = color
        self.button.config(bg=color)

    def set_text_color(self, textcolor: str) -> None:
        self.textcolor = textcolor
        self.button.config(fg=textcolor)

    def bind_click(self, callback) -> None:
        self.button.config(command=callback)

    def pack(self) -> None:
        self.button.pack()

class GameOptionButton(Button):
    """Each option in the GameOptions menu. Extends Button class"""

    def __init__(self, master: tk.Tk, pos: Tuple[int, int], text: str) -> None:
        super().__init__(master, pos, text, width=100, height=50)

class GameOptions:
    """Kind of like a drop down menu that's always down, cause I'm too lazy to make an actual drop down menu. User
    selects one of the options, which sets the mode. When a new game is started, the mode will determine the game setup,
    i.e. 2-player vs AI difficulty, or determining who goes first."""

    def __init__(self, master: tk.Tk, pos: Tuple[int, int], default: str, *options: str) -> None:
        """
        :param master: Tkinter master widget
        :param pos: position of the first button
        :param default: button selected by default
        :param options: the text to be displayed on each button (also the mode that the button will dictate)
        """
        self.master = master
        self.current_option = None
        self.options = []

        for i, option in enumerate(options):
            btn = GameOptionButton(master, (pos[0], pos[1] + i * 50), option)
            btn.bind_click(lambda o=option: self.select_option(o))
            self.options.append(btn)

            if option == default:
                self.current_option = btn
                self.current_option.set_color('lightblue')

    def select_option(self, option: str) -> None:
        for btn in self.options:
            btn.set_color('gray')

        self.current_option = next(btn for btn in self.options if btn.text == option)
        self.current_option.set_color('lightblue')

    def pack(self) -> None:
        for btn in self.options:
            btn.pack()

    def get_option(self) -> str:
        """Returns the text of the selected option"""
        return self.current_option.text

class TextArea:
    """White area that can print two lines of text. Used for printing the turn/winner"""

    def __init__(self, master: tk.Tk, pos: Tuple[int, int]) -> None:
        self.master = master
        self.textarea = tk.Frame(master, bg=GRAY, width=300, height=100)
        self.textarea.place(x=pos[0], y=pos[1])

        self.top_text = tk.Label(self.textarea, text="", bg=RED, fg='black',font= ('Singly Linked',14),borderwidth=0,highlightthickness=0)
        self.top_text.pack(side='top', pady=20)

        self.bot_text = tk.Label(self.textarea, text="", bg=RED, fg='black', ffont= ('Singly Linked',14),borderwidth=0,highlightthickness=0)
        self.bot_text.pack(side='bottom', pady=10)

    def set_text(self, top_text: str, bot_text: str) -> None:
        self.top_text.config(text=top_text)
        self.bot_text.config(text=bot_text)

class RulesScreen:
    """Prints the rules of the game on the screen"""

    def __init__(self, master: tk.Tk, pos: Tuple[int, int]) -> None:
        self.master = master
        self.rules_screen = tk.Frame(master, bg=GRAY, width=200, height=200,highlightthickness=0,borderwidth=0)
        self.rules_screen.place(x=pos[0], y=pos[1])
        
        self.rules_text = tk.Text(self.rules_screen, spacing1=5, wrap='word', bg=BLUE, fg=WHITE, font= ('Singly Linked',19),highlightthickness=0,borderwidth=0)
        self.rules_text.pack(expand=True, fill='both',anchor='center')

        self.ok_button = tk.Button(self.rules_screen, text='UNDERSTOOD', bg=BLUE, fg=WHITE, width=10, height=2, font= ('Singly Linked',19), command=self.close_rules,highlightthickness=0,borderwidth=0)
        #ok = Image.open('S6_project/src/Screenshot 2024-02-15 at 21.01.01.png')
        #ph_ok = ImageTk.PhotoImage(ok)
        #self.ok_button.config(ph_ok)
        self.ok_button.pack()

        # Get the rules from rules.txt, and save each line in a list. File must end with a newline
        with open("/Users/majdakemmou/EURECOM/S6_project/src/gui/rules.txt", 'r') as file:
            self.lines_of_text = file.readlines()

        self.write_rules()  # draw each line on the surface

    def write_rules(self) -> None:
        for line in self.lines_of_text:
            self.rules_text.insert('end', line)

    def show_rules(self) -> None:
        self.master.wait_window(self.rules_screen)

    def close_rules(self) -> None:
        self.rules_screen.destroy()
        
