from API import *
from tkinter import*

tk = Tk()
tk.geometry("400x400")


sudokuTable = createSudokuTable("hard")
##Bàn cờ sudoku được tạo ra ngẫu nhiên theo độ khó (easy,medium,hard)
##Các phần tử không phải là đề mang giá trị bằng 0


arr = [] ## Tạo một mảng hai chiều để quản lý các StringVar tương ứng với (i,j) của bàn cờ sudoku

##Duyệt bàn cờ 9x9 để gắn các Entry lên GUI
for i in range(0,9):
    col = []
    for j in range(0,9):
        entry_text = StringVar()
        entry = Entry(tk,width = 5,textvariable = entry_text,justify = "center")
        if(sudokuTable[i][j] != 0): ##Nếu phần tử không phải là đề bài (tức là bằng 0)
            entry_text.set(str(sudokuTable[i][j])) ##Set giá trị mặc định cho Entry (gắn đề bài vào)
            entry.configure(state = DISABLED,disabledbackground="#89CFF0") ##Disable không cho phép Entry nhập được
        entry.place(x =50 + j*30,y = 10+ i*20)
        col.append(entry_text) ## Gắn StringVar tương ứng của Entry vào cột
    arr.append(col)


tk.mainloop()
