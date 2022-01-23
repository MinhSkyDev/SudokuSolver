from API import *
from tkinter import*
from SudokuChecking import *
import sys
import time
import threading

sys.setrecursionlimit(999999999)

tk = Tk()
tk.geometry("450x400")

global sudokuTable
##Bàn cờ sudoku được tạo ra ngẫu nhiên theo độ khó (easy,medium,hard)
##Các phần tử không phải là đề mang giá trị bằng 0
arr = [] ## Tạo một mảng hai chiều để quản lý các StringVar tương ứng với (i,j) của bàn cờ sudoku
arr_entry = [] ##Tạo một mảng hai chiều để quản lý các Entry

global timeSleep


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
            time.sleep(timeSleep)
            arr_entry[row][col].configure(background = "#90EE90")
            if(solveSudoku()):
                return True
            sudokuTable[row][col] = 0
            time.sleep(timeSleep)
            arr[row][col].set(str(0))
            arr_entry[row][col].configure(background = "#FF7F7F")
    return False


def chooseSpeed_command():
    global chooseSpeed_StringVar,timeSleep
    timeSleep =  10**-int(chooseSpeed_StringVar.get())
    solveSudoku_threading = threading.Thread(target = solveSudoku)
    solveSudoku_threading.start()

def chooseSpeed():
    top = Toplevel()
    top.title("Choose Speed")
    top.geometry("200x200")
    chooseSpeed_label = Label(top,text = "Choose Speed - 10^-x ")
    global chooseSpeed_StringVar
    chooseSpeed_StringVar = StringVar()
    chooseSpeed_entry = Entry(top,textvariable=chooseSpeed_StringVar,justify = "center")
    chooseSpeed_button = Button(top, text = "Confirm",command = chooseSpeed_command)
    chooseSpeed_label.pack()
    chooseSpeed_entry.pack()
    chooseSpeed_button.pack()

def solveSudoku_command():
    chooseSpeed()
    return

def getSudokuTable_entry():
    sudokuTable_entry = [] ##2D matrix get from the currentEntry
    for i in range(0,9):
        col = []
        for j in range(0,9):
            num = arr[i][j].get()
            if(num != ''):
                num = int(num)
            else:
                num = 0
            col.append(num)
        sudokuTable_entry.append(col)
    return sudokuTable_entry

def checkSudoku():
    sudokuTable_entry = getSudokuTable_entry()
    for i in range(0,9):
        for j in range(0,9):
            if(isSafe(sudokuTable_entry,sudokuTable_entry[i][j],(i,j)) and isValueValid(sudokuTable_entry[i][j])):
                ##Change the color to green
                arr_entry[i][j].configure(background = "#90EE90")
            else:
                ##Change the color to red
                arr_entry[i][j].configure(background = "#FF7F7F")
            time.sleep(0.005)



def checkSudoku_command():
    checkSudoku_threading = threading.Thread(target=checkSudoku)
    checkSudoku_threading.start()
    return


def changeEntryBorderColor():
    for i in range(0,9):
        for j in range(0,9):
            i_box = i // 3
            j_box = j // 3
            if(i_box == 0 and j_box == 0):
                arr_entry[i][j].config(highlightbackground = "#EE4B2B",highlightcolor = "#EE4B2B")
            elif(i_box == 0 and j_box == 1):
                arr_entry[i][j].config(highlightbackground = "#A52A2A",highlightcolor = "#A52A2A")
            elif(i_box == 0 and j_box == 2):
                arr_entry[i][j].config(highlightbackground = "#800020",highlightcolor = "#800020")
            elif(i_box == 1 and j_box == 0):
                arr_entry[i][j].config(highlightbackground = "#FFBF00",highlightcolor = "#FFBF00")
            elif(i_box == 1 and j_box == 1):
                arr_entry[i][j].config(highlightbackground = "#CD7F32",highlightcolor = "#CD7F32")
            elif(i_box == 1 and j_box == 2):
                arr_entry[i][j].config(highlightbackground = "#CC5500",highlightcolor = "#CC5500")
            elif(i_box == 2 and j_box == 0):
                arr_entry[i][j].config(highlightbackground = "#0096FF",highlightcolor = "#0096FF")
            elif(i_box == 2 and j_box == 1):
                arr_entry[i][j].config(highlightbackground = "#0047AB",highlightcolor = "#0047AB")
            elif(i_box == 2 and j_box == 2):
                arr_entry[i][j].config(highlightbackground = "#6F8FAF",highlightcolor = "#6F8FAF")

def displayTable():
    ##Duyệt bàn cờ 9x9 để gắn các Entry lên GUI
    for i in range(0,9):
        col = []
        col_entry = []
        for j in range(0,9):
            entry_text = StringVar()
            entry = Entry(tk,width = 5,textvariable = entry_text,justify = "center",highlightthickness = 4)
            if(sudokuTable[i][j] != 0): ##Nếu phần tử không phải là đề bài (tức là bằng 0)
                entry_text.set(str(sudokuTable[i][j])) ##Set giá trị mặc định cho Entry (gắn đề bài vào)
                entry.configure(state = DISABLED,disabledbackground="#89CFF0") ##Disable không cho phép Entry nhập được
            entry.place(x =50 + j*40,y = 10+ i*24)
            col.append(entry_text) ## Gắn StringVar tương ứng của Entry vào cột
            col_entry.append(entry)
        arr.append(col)
        arr_entry.append(col_entry)
    solve_button = Button(tk,text = "Auto Solve", command = solveSudoku_command)
    solve_button.place(x = 190, y = 230)
    check_button =  Button(tk,text = "Checking", command = checkSudoku_command)
    check_button.place(x=195,y=260)
    changeEntryBorderColor()


def clearMain():
    global headerLabel,easyButton,mediumButton,hardButton,randomButton
    headerLabel.pack_forget()
    easyButton.pack_forget()
    mediumButton.pack_forget()
    hardButton.pack_forget()
    randomButton.pack_forget()


def easyMode():
    global sudokuTable
    clearMain()
    sudokuTable = createSudokuTable("easy")
    displayTable()

def mediumMode():
    global sudokuTable
    clearMain()
    sudokuTable = createSudokuTable("medium")
    displayTable()

def hardMode():
    global sudokuTable
    clearMain()
    sudokuTable = createSudokuTable("hard")
    displayTable()

def randomMode():
    global sudokuTable
    clearMain()
    sudokuTable = createSudokuTable("random")
    displayTable()

def main():
    global headerLabel,easyButton,mediumButton,hardButton
    headerLabel = Label(tk, text = "Choose difficulty !!!")
    easyButton = Button(tk,text = "Easy",command = easyMode)
    mediumButton = Button(tk,text = "Medium",command = mediumMode)
    hardButton = Button(tk,text= "Hard",command = hardMode)
    randomButton = Button(tk,text = "Random", command = randomMode)
    headerLabel.pack()
    easyButton.pack()
    mediumButton.pack()
    hardButton.pack()
    randomButton.pack()


main()
tk.mainloop()
