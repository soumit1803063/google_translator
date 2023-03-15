import os
import sys
from functools import partial
from tkinter import *
from googletrans import Translator,LANGUAGES



class TranslatorClass:
    def __init__(self, root):
        self.from_lang='d'
        self.to_lang="en"

        self.languages=LANGUAGES
        root.geometry("704x593")
        master_frame = Frame(root, bg="#FAFAFA")
        master_frame.place(height=593, width=704)

        #from label
        from_label = Label(master_frame, text="From", bg="#FAFAFA")
        from_label.place(x=2, y=2, width=95, height=25)

                 
        #select_from_language_button
        from_lang_button=Button(master_frame, text="detect language", bg="#0A0A0A", fg="#FAFAFA", font=("Helvetica 9 italic", 8, "bold"))
        from_lang_button.place(x=150, y=2, width=300, height=30)
        from_lang_button['command']=partial(self.show_languages,master_frame,from_lang_button,0)


        # from_Textbox
        from_textbox = Text(master_frame)
        from_textbox.place(x=2, y=30, width=700, height=250)

        #to label
        to_label = Label(master_frame, text="To", bg="#FAFAFA")
        to_label.place(x=2, y=282, width=95, height=25)

        #select_from_language_button
        to_lang_button=Button(master_frame, text="english", bg="#0A0A0A", fg="#FAFAFA", font=("Helvetica 9 italic", 8, "bold"))
        to_lang_button.place(x=150, y=282, width=300, height=30)
        to_lang_button['command']=partial(self.show_languages,master_frame,to_lang_button,1)

        # to_Textbox
        to_textbox = Text(master_frame)
        to_textbox.place(x=2, y=309, width=700, height=250)

        # Translate Button
        Button(master_frame, text="Translate", bg="#0A0A0A", fg="#FAFAFA", font=("Helvetica 9 italic", 8, "bold"),
               command=partial(self.do_translation, from_textbox,to_textbox)).place(x=2, y=561, width=700, height=30)

    
    def do_translation(self,from_Textbox,to_textbox):
        source=self.from_lang
        destination=self.to_lang

        t=Translator()
        from_text =from_Textbox.get("1.0", 'end')
        to_text=""
        if source == 'd':
            # print(1,"-->",end="")
            to_text=t.translate(from_text,dest=destination).text
        else:
            # print(2,"-->",end="")
            to_text=t.translate(from_text,src=source,dest=destination).text    
        # print(source,",",destination)
        to_textbox.delete("1.0",'end')
        to_textbox.insert('1.0', to_text)

    def show_languages(self,master_frame,selected_lang_button,Type):
        languages_options=[]
        if Type == 0:
           languages_options.append('detect language')

        for k, v in self.languages.items():
            languages_options.append(v)

        #language_frame
        lang_frame = Frame(master_frame, bg="#FAFAFA")
        lang_frame.place(height=593, width=704)

        #back_button
        Button(lang_frame, text="X", bg="#FF0B0A", fg="#FAFAFA", font=("Helvetica 9 italic", 8, "bold"),
               command=partial(self.back,lang_frame)).place(x=2, y=2, width=30, height=30)
    
    

        try:
            canvas = Canvas(lang_frame, bg="#EAFAFA")
            canvas.place(x=0, y=35, width=704, height=557)

            y = 0
            for language in languages_options:
                language_button = Button(canvas, text=language, bg="#00000F", fg="#FAFAFA")
                language_button['command'] = partial(self.select_language,selected_lang_button,language_button['text'],lang_frame,Type)
                canvas.create_window(1, y, window=language_button, anchor=NW, height=26)
                y += 30

            scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
        except Exception:
            pass    
    def back(self,lang_frame):
        lang_frame.destroy()
    def select_language(self,selected_lang_button,selected_lang,lang_frame,Type):
        selected_lang_button['text']=selected_lang

        temp=selected_lang
        selected_lang='d'
        for k, v in self.languages.items():
                if v == temp:
                    selected_lang=k
                    break
   

        if Type == 0:
            self.from_lang=selected_lang
        else:
            self.to_lang=selected_lang    
        self.back(lang_frame)           
        









#main_driver
root = Tk()
root.title("Translator")
root.geometry("400x378")
# root.wm_iconbitmap(os.path.dirname(os.path.realpath(sys.argv[0])) + "\icons" + '\RUETERS_ICON.ico')
root.resizable(0, 0)
TranslatorClass(root)
root.mainloop()
