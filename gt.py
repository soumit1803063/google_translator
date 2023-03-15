import csv
import datetime
import json
import os
import sys
from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from googletrans import Translator,LANGUAGES



class TranslatorClass:
    def __init__(self, root):
        self.languages=LANGUAGES
        print(self.languages)
        languages_options=[]
        for k, v in self.languages.items():
            languages_options.append(v)


        root.geometry("400x593")
        master_frame = Frame(root, bg="#FAFAFA")
        master_frame.place(height=593, width=400)

        #from label
        from_label = Label(master_frame, text="From", bg="#FAFAFA")
        from_label.place(x=2, y=2, width=95, height=25)

                 
        # datatype of menu text
        to_lang = StringVar()
                 
        # initial menu text
        to_lang.set(languages_options[0])
                 
        # language options Dropdown menu
        drop = OptionMenu( master_frame , to_lang , *languages_options )
        drop.place(x=97, y=2, width=150, height=25)

        # from_Textbox
        from_textbox = Text(master_frame)
        from_textbox.place(x=2, y=30, width=396, height=250)

        #to label
        to_label = Label(master_frame, text="To", bg="#FAFAFA")
        to_label.place(x=2, y=282, width=95, height=25)

        # from_Textbox
        to_textbox = Text(master_frame)
        to_textbox.place(x=2, y=309, width=396, height=250)

        # Translate Button
        Button(master_frame, text="Translate", bg="#0A0A0A", fg="#FAFAFA", font=("Helvetica 9 italic", 8, "bold"),
               command=partial(self.do_translation, from_textbox,to_textbox)).place(x=2, y=561, width=396, height=30)

    
    def do_translation(self,from_Textbox,to_textbox):
        t=Translator()
        from_text =from_Textbox.get("1.0", 'end')
        to_text=t.translate(from_text,dest="en").text

        to_textbox.insert(1.0, to_text)
           
        









#main_driver
root = Tk()
root.title("Translator")
root.geometry("400x378")
# root.wm_iconbitmap(os.path.dirname(os.path.realpath(sys.argv[0])) + "\icons" + '\RUETERS_ICON.ico')
root.resizable(0, 0)
TranslatorClass(root)
root.mainloop()
