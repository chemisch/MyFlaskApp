from flask import Flask, render_template, url_for, redirect, request
from Word_List import New_Word_func
import os

app = Flask(__name__)
dir_Path = os.path.dirname(os.path.abspath(__file__))
Wordfile = os.path.join(dir_Path, 'words.txt')
Word = New_Word_func(Wordfile)
Length_Word = len(Word)
Hidden_Word = list(Word)
Blank = []
for i in Hidden_Word:
    Blank.append('_')

Guess_String = ''.join(Blank)
User_Input = ""
DisplayMSG = ''

@app.route("/",)
def index():
    return render_template('index.html',
    Length_Word = Length_Word,
    User_Input = User_Input,
    Guess_String = Guess_String)



@app.route('/', methods=['POST'])
def Word_Game():

    User_Input = request.form['Guess']
    global DisplayMSG
    global Word
    global Hidden_Word
    global Length_Word
    global Blank
    global Guess_String

    if User_Input == "reset":
        for i in range(len(Blank)):
            if Blank[i] != '_':
                Blank[i] = '_'
        Guess_String = ''.join(Blank)

    elif User_Input == Word:
        DisplayMSG = 'You Solved the Puzzle!'

    elif User_Input == 'New_Word':
        Word = New_Word_func(Wordfile)
        Length_Word = len(Word)
        Hidden_Word = list(Word)
        Blank = []
        for i in Hidden_Word:
            Blank.append('_')

    for i in range(len(Hidden_Word)):
        if Hidden_Word[i] == User_Input:
            Blank[i] = User_Input
            Guess_String = ''.join(Blank)
        else:
            Guess_String = ''.join(Blank)
            

    return render_template('index.html', 
    User_Input = User_Input,
    Word = Word,
    Hidden_Word = Hidden_Word,
    Length_Word = Length_Word,
    Guess_String = Guess_String,
    DisplayMSG = DisplayMSG)

if __name__ == "__main__":
    app.run(debug=True)

