from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            check(i)
            player = "O"
            button["bg"] = "yellow"
      else :
            check(i)
            player = "X"
            button["bg"] = "lightgreen"



window = Tk()
player = "X"
list= []


for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

def check(i) :
      r = i//3
      c = i%3

      if list[r*3]["text"] == list[r*3+1]["text"] == list[r*3+2]["text"] :
            win()
      elif list[c]["text"] == list[c+3]["text"] == list[c+6]["text"] :
            win()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " or list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
            win()

def win() :
      if player=="X":
            msg = Message(window, text="X Win")
            msg.grid(row=3, column=0)

            
      else :
            msg = Message(window, text="O Win")
            msg.grid(row=3, column=0)

            

window.mainloop()


