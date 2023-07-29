from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

for files in os.listdir('data/english/'):
     data=open('data/english/'+files,'r',encoding='utf-8').readlines()

     trainer.train(data)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    questionField.delete(0,END)



root=Tk()

root.geometry('500x570+100+30')
root.title('ChatBot created by Rahul')
root.config(bg='#303030')

logoPic=PhotoImage(file='pic.png')

logoPicLabel=Label(root,image=logoPic,bg='#303030')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',15),bg='#4F4F4F',fg='white',height=14,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('Arial',15),bg='#4F4F4F',fg='white')
questionField.pack(pady=16,fill=X)

askPic=PhotoImage(file='ask.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()


root.bind('<Return>',click)

root.mainloop()