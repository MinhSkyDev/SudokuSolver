from API import *
from tkinter import*

tk = Tk()
tk.geometry("400x400")
sudokuTable = createSudokuTable("hard")

arr = []
for i in range(0,9):
    col = []
    for j in range(0,9):
        entry_text = StringVar()
        entry = Entry(tk,width = 5,textvariable = entry_text,justify = "center")
        if(sudokuTable[i][j] != 0):
            entry_text.set(str(sudokuTable[i][j]))
            entry.configure(state = DISABLED,disabledbackground="#89CFF0")
        entry.place(x =50 + j*30,y = 10+ i*20)
        col.append(entry_text)
    arr.append(col)


tk.mainloop()
