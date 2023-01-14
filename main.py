import tkinter

window = tkinter.Tk()
window.title("First Replit Programm")
window.minsize(width=800, height=600)


def button_click():
  print("button test")
  pass


button01 = tkinter.Button(text="Click Me", command=button_click)
button01.pack()

window.mainloop()
