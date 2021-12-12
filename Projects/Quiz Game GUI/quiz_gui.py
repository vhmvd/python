import tkinter as tk
import readquiz
import random

questions = readquiz.loadQuestions()
total = 0
correct = 0

def get_new_question():
  current_question = questions[random.randint(0, len(questions))]
  question_label_text_widget.config(text=current_question[0])
  if current_question[1] == True:
    true_button.config(command=good_answer)
    false_button.config(command=bad_answer)
  else:
    true_button.config(command=bad_answer)
    false_button.config(command=good_answer)


def good_answer():
  global total
  global correct
  total += 1
  correct += 1
  status_label.config(bg="light green", text="Your answer was correct")
  score_label.config(text= "Score: " + str(correct) + "/" + str(total))
  get_new_question()

def bad_answer():
  global total
  global correct
  total += 1
  status_label.config(bg="pink", text="Your answer was incorrect")
  score_label.config(text= "Score: " + str(correct) + "/" + str(total))
  get_new_question()

root = tk.Tk()
root.title("Quiz")

button_frame = tk.Frame(root)
status_and_score_frame = tk.Frame(root)

question_label_widget = tk.Label(root, text="Question:", font="bold")
question_label_widget.pack()

question_label_text_widget = tk.Message(root, width=200)
question_label_text_widget.pack()

true_button = tk.Button(root, text="Yes", width=10, height=1)
false_button = tk.Button(root, text="No", width=10, height=1)
true_button.pack(side=tk.LEFT, in_=button_frame)
false_button.pack(side=tk.RIGHT, in_=button_frame)
button_frame.pack()

status_label = tk.Label(root, text="Status")
score_label = tk.Label(root, text="Score: " + str(correct) + "/" + str(total))
status_label.pack(side=tk.LEFT, in_=status_and_score_frame)
score_label.pack(side=tk.RIGHT, in_=status_and_score_frame)
status_and_score_frame.pack(fill="both")

get_new_question()
root.mainloop()

