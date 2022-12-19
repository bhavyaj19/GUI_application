from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore
from urllib.request import urlopen
import json
import pandas as pd
import random

# API for questions 'https://opentdb.com/api.php?amount=50&category=29&type=multiple'
with urlopen("https://opentdb.com/api.php?amount=50&category=29&type=multiple") as webpage:
    data = json.loads(webpage.read().decode())
    df = pd.DataFrame(data["results"])  # storing data in a data frame
    # print(df.columns)


def preload_data(idx):
    question = df["question"][idx]
    correct_ans = df["correct_answer"][idx]
    wrong_ans = df["incorrect_answers"][idx]

    # formaatting questions
    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "less than SYMBOL"),
        ("&gt;", "greater than SYMBOL"),
        ("&amp;",",")
    ]

    for tuple in formatting:
        question = question.replace(tuple[0], tuple[1])
        correct_ans = correct_ans.replace(tuple[0], tuple[1])

    for tuple in formatting:
        wrong_ans = [char.replace(tuple[0], tuple[1]) for char in wrong_ans]

    parameters["question"].append(question)
    parameters["correct_ans"].append(correct_ans)

    # [] will convert single data to a list
    all_ans = wrong_ans + [correct_ans]
    random.shuffle(all_ans)

    parameters["answer1"].append(all_ans[0])
    parameters["answer2"].append(all_ans[1])
    parameters["answer3"].append(all_ans[2])
    parameters["answer4"].append(all_ans[3])

    # print(parameters["correct_ans"][-1]) #to print answers


parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct_ans": [],
    "score": [],
    "index": []
}

widgets = {
    "profile_pic": [],  # initialising global widgets
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "message": [],
    "message2": []
}

grid = QGridLayout()


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def clear_parameters():
    for parameter in parameters:
        if parameters[parameter] != []:
            for i in range(0, len(parameters[parameter])):
                parameters[parameter].pop()
    
    parameters["index"].append(random.randint(0,49))
    parameters["score"].append(0)

def show_frame1():
    clear_widgets()
    frame1()


def start_game():
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    frame2()


def create_buttons(answer, l_margin, r_margin, v_padding, h_padding):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(450)
    button.setStyleSheet(
        "*{border: 4px solid '#fb6667';" +
        "border-radius: 20px;" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "font-size: 30px;" +
        "padding:" + str(v_padding) + "px" + str(h_padding) + "px;"
        "color: '#fb6667';" +
        "font-family: Courier New;" +
        "font-weight: bold; }" +
        "*:hover{background: '#fb6667';" +
        "color: #251B37}"
    )
    button.clicked.connect(lambda x: is_correct(button))
    return button


def is_correct(btn):
    # print('i was clicked')
    if btn.text() == parameters["correct_ans"][-1]:
        print(btn.text() + ' is correct answer')

        temp_score = parameters["score"][-1]
        parameters["score"].pop()
        parameters["score"].append(temp_score + 10)

        parameters["index"].pop()
        parameters["index"].append(random.randint(0, 49))

        preload_data(parameters["index"][-1])

        widgets["score"][-1].setText(str(parameters["score"][-1]))
        widgets["question"][0].setText(parameters["question"][-1])
        widgets["answer1"][0].setText(parameters["answer1"][-1])
        widgets["answer2"][0].setText(parameters["answer2"][-1])
        widgets["answer3"][0].setText(parameters["answer3"][-1])
        widgets["answer4"][0].setText(parameters["answer4"][-1])

        if parameters["score"][-1]==50:
            clear_widgets()
            frame3()
    else:
        print("Correct answer is: "+parameters["correct_ans"][-1])
        clear_widgets()
        frame4()


def frame1():
    clear_widgets()
    # display image
    image = QPixmap('GUI_application\pyqt5-app\profile-pic (2).png')
    image = image.scaledToHeight(300)  # set height
    profile_pic = QLabel()  # initialising label
    profile_pic.setPixmap(image)
    profile_pic.setAlignment(QtCore.Qt.AlignCenter)
    profile_pic.setStyleSheet("margin: 30px;")
    widgets["profile_pic"].append(profile_pic)  # storing to global variables

    # Button

    button = QPushButton('Start Game')
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(500)
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#fb6667';
            border-radius: 24px;
            font-size: 35px;
            padding: 0 10px;
            color: '#fb6667';
            font-family: Courier New;
            font-weight: bold; 
            
        }
        :hover
        {
            background: '#fb6667';
            color: #251B37
        }
        '''
    )

    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["profile_pic"][-1], 0, 0, 1, 2)  # row, column
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2, QtCore.Qt.AlignCenter)


def frame2():
    clear_widgets()
    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignLeft)
    score.setFixedHeight(130)
    score.setFixedWidth(130)
    score.setStyleSheet(
        '''
        font-family: Courier New;
        font-size: 35px;
        font-weight: bold;
        color: '#fb6667';
        padding: 25px;
        border: 4px solid '#fb6667';
        border-radius: 65px;
        '''
    )

    widgets["score"].append(score)

    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)  # to wrap string in new lines
    question.setStyleSheet(
        '''
        color: '#fb6667';
        font-size: 40px;
        font-family: Courier New;
        margin: 10px;
        padding: 10px;
        font-weight: bold;
        '''
    )

    widgets["question"].append(question)

    button1 = create_buttons(parameters["answer1"][-1], 10, 10, 15, 0)
    button2 = create_buttons(parameters["answer2"][-1], 10, 10, 15, 0)
    button3 = create_buttons(parameters["answer3"][-1], 10, 10, 15, 0)
    button4 = create_buttons(parameters["answer4"][-1], 10, 10, 15, 0)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    # 1,2 are row span and column span
    grid.addWidget(widgets["score"][-1], 0, 0)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)


def frame3():
    # congradulations widget
    message = QLabel("Congradulations!\n Your score is:")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        """
        font-family: 'Courier New';
        font-size: 35px;
        color: '#fb6667';
        font-weight: bold;
        margin: 100px 0px;
        """
    )
    widgets["message"].append(message)

    # score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet(
        """
        font-family: Courier New;
        font-weight: bold;
        font-size: 100px;
        color: #fb6667;
        margin: 0 75px;
        """
    )
    widgets["score"].append(score)

    # button widget
    button = QPushButton('TRY AGAIN')
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(500)
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#fb6667';
            border-radius: 24px;
            font-size: 35px;
            padding: 0 10px;
            color: '#fb6667';
            font-family: Courier New;
            font-weight: bold; 
            
        }
        :hover
        {
            background: '#fb6667';
            color: #251B37
        }
        '''
    )

    button.clicked.connect(frame1)

    widgets["button"].append(button)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2, QtCore.Qt.AlignCenter)


def frame4():
    # sorry widget
    message = QLabel("Sorry, this answer \nwas wrong\n your score is:")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        """
        font-family: 'Courier New';
        font-size: 35px;
        color: '#fb6667';
        font-weight: bold;
        margin: 100px 0px;
        """
    )
    widgets["message"].append(message)

    # score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet(
        """
        font-family: Courier New;
        font-weight: bold;
        font-size: 100px;
        color: #fb6667;
        margin: 0 75px;
        """
    )
    widgets["score"].append(score)

    # button widget
    button = QPushButton('TRY AGAIN')
    button.setFixedWidth(500)
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#fb6667';
            border-radius: 24px;
            font-size: 35px;
            padding: 0 10px;
            color: '#fb6667';
            font-family: Courier New;
            font-weight: bold; 
            
        }
        :hover
        {
            background: '#fb6667';
            color: #251B37
        }
        '''
    )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    button.clicked.connect(frame1)

    widgets["button"].append(button)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2, QtCore.Qt.AlignCenter)
