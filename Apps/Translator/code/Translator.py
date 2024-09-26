from tkinter import *
from tkinter import messagebox
import  customtkinter
import googletrans
from googletrans import Translator


#Global Variiates
language=['Arabic', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Dutch', 'English', 'French', 'Kazakh', 'Persian', 'Russian', 'Uzbek', 'Turkish']
languagekey=['ar', 'zh-cn', 'zh-tw', 'nl', 'en', 'fr', 'kk', 'fa', 'ru', 'uz', 'tr']

class Word():
    def __init__(self,flang,tlang):
        self.flang=flang
        self.tlang=tlang

def setflang(lang):
    Word.flang=languagekey[language.index(lang)]
def settlang(lang):
    Word.tlang = languagekey[language.index(lang)]



def LanguageTranslator(flang,tolang,text):
    translator = Translator()
    translation = translator.translate(text,src=flang, dest=tolang)
    pronunciation=translation.pronunciation
    translation = translation.text
    return translation,pronunciation

def Translate():
    try:
        text=ftext.get('0.0','end').strip('\n')
        translation=LanguageTranslator(Word.flang,Word.tlang,text)
        translationtext=f"\n{translation[0]}"
        ttext.insert('0.0',text=translationtext)

    except:
        messagebox.showinfo("Xatolik","Xatolik yuz berdi\nTilni tog'ri kiriting..")
def Clearer():
    ftext.delete("0.0",'end')
    ttext.delete("0.0",'end')
    print(tlang)

windows=customtkinter.CTk()
windows.title("Translator")
windows.geometry("1000x500")



#Set from language
flabel=customtkinter.CTkLabel(windows,text='From',text_color="#464645",fg_color="white",width=200,height=25,font=('Bold',20))
flabel.place(x=100,y=20)

fcombo=customtkinter.CTkComboBox(windows,values=language,command=setflang,width=200,height=30,font=('Bold',20))
fcombo.place(x=100,y=60)


#Set to language
tlabel=customtkinter.CTkLabel(windows,text='To',text_color="#464645",fg_color="white",width=200,height=25,font=('Bold',20))
tlabel.place(x=600,y=20)

tcombo=customtkinter.CTkComboBox(windows,values=language,command=settlang,width=200,height=30,font=('Bold',20))
tcombo.place(x=600,y=60)


#Frame
ftext=customtkinter.CTkTextbox(windows,width=300,height=300,font=('Bold',20),text_color="white",fg_color="#767676")
ftext.place(x=70,y=100)
ftext.configure(state='normal')

#Frame
ttext=customtkinter.CTkTextbox(windows,width=300,height=300,font=('Bold',20),text_color="white",fg_color="#767676")
ttext.place(x=570,y=100)
ttext.configure(state='normal')


#Button
TranslateButton=customtkinter.CTkButton(windows,command=Translate,
                                        text="Translate",
                                        height=60,
                                        width=150,
                                        text_color='white',
                                        fg_color='#767676',
                                        bg_color='white',
                                        hover_color='#BBBBBB',
                                        corner_radius=50,
                                        border_color='grey',
                                        border_width=5,
                                        font=('Bold',20)
                                        )
TranslateButton.place(x=400,y=170)

ClearButtuon=customtkinter.CTkButton(windows,text="CLEAR",command=Clearer,
                                        height=60,
                                        width=150,
                                        text_color='white',
                                        fg_color='#767676',
                                        bg_color='white',
                                        hover_color='#BBBBBB',
                                        corner_radius=50,
                                        border_color='grey',
                                        border_width=5,
                                        font=('Bold',20)
                                        )
ClearButtuon.place(x=400,y=250)



muallif=customtkinter.CTkLabel(windows,text="Developer:Mr Ton",text_color="#464645",fg_color="white",width=200,height=25,font=('Bold',14))
muallif.place(x=800,y=450)
windows.config(bg='white')
windows.mainloop()