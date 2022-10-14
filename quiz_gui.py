from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.withdraw()

questions = [ "What is the capital of Germany?",
              "Who is the president of the US?",
              "What is the capital of France?",
              "What is the capital of Spain?" ]

answer = [ "Berlin", 
           "Biden",
           "Paris",
           "Madrid" ]

score = 0

for i in range(0, len(questions)):
    print(questions[i])
    user_answer = simpledialog.askstring(questions[i], "Answer: ")

    if user_answer == answer[i]:
        messagebox.showinfo("Correct", "Correct")
        score = score + 1
    else:
        messagebox.showinfo("Wrong", "Wrong")

messagebox.showinfo("Score", str(score))