from API import *
from tkinter import*
from SudokuChecking import *
import sys
import time
import threading

sys.setrecursionlimit(999999999)

tk = Tk()
tk.geometry("400x400")


sudokuTable = createSudokuTable("easy")
##Bàn cờ sudoku được tạo ra ngẫu nhiên theo độ khó (easy,medium,hard)
##Các phần tử không phải là đề mang giá trị bằng 0
arr = [] ## Tạo một mảng hai chiều để quản lý các StringVar tương ứng với (i,j) của bàn cờ sudoku
arr_entry = [] ##Tạo một mảng hai chiều để quản lý các Entry

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def solveSudoku():
    find = find_empty(sudokuTable)
    if(find == None):
        return True
    row,col = find[0],find[1]
    for num in range(1,10):
        if(isSafe(sudokuTable,num,(row,col))):
            sudokuTable[row][col] = num
            arr[row][col].set(str(num))
            time.sleep(0.005/99999999)
            arr_entry[row][col].configure(background = "#90EE90")
            if(solveSudoku()):
                return True
            sudokuTable[row][col] = 0
            time.sleep(0.005/99999999)
            arr[row][col].set(str(0))
            arr_entry[row][col].configure(background = "#FF7F7F")
    return False


def solveSudoku_command():
    solveSudoku_threading = threading.Thread(target = solveSudoku)
    solveSudoku_threading.start()
    return


def main():
    ##Duyệt bàn cờ 9x9 để gắn các Entry lên GUI
    for i in range(0,9):
        col = []
        col_entry = []
        for j in range(0,9):
            entry_text = StringVar()
            entry = Entry(tk,width = 5,textvariable = entry_text,justify = "center")
            if(sudokuTable[i][j] != 0): ##Nếu phần tử không phải là đề bài (tức là bằng 0)
                entry_text.set(str(sudokuTable[i][j])) ##Set giá trị mặc định cho Entry (gắn đề bài vào)
                entry.configure(state = DISABLED,disabledbackground="#89CFF0") ##Disable không cho phép Entry nhập được
            entry.place(x =50 + j*30,y = 10+ i*20)
            col.append(entry_text) ## Gắn StringVar tương ứng của Entry vào cột
            col_entry.append(entry)
        arr.append(col)
        arr_entry.append(col_entry)

main()
solve_button = Button(tk,text = "Auto Solve", command = solveSudoku_command)
solve_button.place(x = 150, y = 300)

tk.mainloop()
