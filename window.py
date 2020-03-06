from tkinter import *
import converter as c

def openTranslator() :
    #Window Title and size
    window = Tk()
    window.title("Pig Latin Translator")
    window.geometry('300x200')

    #Labels
    lbl_welcome = Label(window, text = "Welcome to Jose Luis's Pig Latin Translator!", font = ("Arial Bold", 10))
    lbl_welcome.grid(column=0,  row=0)

    lbl_instructions = Label(window, text = "Enter the word you'd like translated:", font = ("Arial Bold", 10))
    lbl_instructions.grid(column=0, row = 2)

    #Box to Enter word to be translated
    entry = Entry(window, width=20)
    entry.grid(column = 0, row = 3)

    def translate():
        word = entry.get()
        translatedWord = c.toPigLatin(word)
        translationLabel.configure(text = translatedWord)
        translationLabel.grid(column=0, row=5)

    #Translation Label
    translationLabel = Label(window, font = ("Arial Bold", 16))

    #Translate Button
    translate_btn = Button(window, text = "Translate!", command = translate)
    translate_btn.grid(column=0, row = 4)

    window.mainloop()