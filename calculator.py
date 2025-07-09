from  tkinter import *
import math

# all the needed values
# entry_box_bg = "#A6AC9F"
# entry_box_fg = "white"
# equal_btn_bg = "#0D519E"
# all_clear_btn_bg = "#9059E7"
# delete_btn_icon = '⌫'
# delete_btn_bg = "#EE4049"
# operations_btn_bg = "#8ED8FA"
# num_btn_bg = "#676D61"


# ________________________________________CALCULATOR MECHANISM________________________________________
# some initial values
num1 = 0
num2 = 0
extra_number = 0
operation = None
result = 0
ERROR = "Cannot Divide By Zero"

def choose_operation(op):
    global operation, num1

    # makes sure only one operation is selected at a time expect square/square root
    if operation == None or operation in ['x²', '√x']:
        operation = op

        # prevent non numeric number input
        try:
            num1 = float(entry.get())
        except ValueError:
            entry.delete(0, END)
            entry.insert(END, "Error: Invalid Input")
            return      
        entry.delete(0, END)

        if operation == 'x²':
            entry.insert(END, num1**2)
        elif operation == '√x':
            entry.insert(END, math.sqrt(num1))


def calculate():
    global operation, num2, result, ERROR
    
    # prevent non numeric number input
    try:
        num2 = float(entry.get())
    except ValueError:
            entry.delete(0, END)
            entry.insert(END, "ERROR: Invalid Input")
            return
    
    entry.delete(0, END)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            entry.insert(END, ERROR)
            operation = None
            return
        
    entry.insert(END, result)
    operation = None

# ________________________________________DISPLAY INPUT________________________________________
def display_num(num):
    global ERROR
    # avoid more than one decimal points
    if num == "." and num in entry.get():
        return
    
    # delete the ERROR if displayed
    if ERROR in entry.get() or "Error: Invalid Input" in entry.get():
        entry.delete(0, END)
        

    # display a zero if decimal point is entered at first place
    if len(entry.get()) == 1 and "." in entry.get():
        entry.insert(0, 0)

    # delete the leading zero when num1 number is entered
    if len(entry.get()) ==1 and '0' in entry.get():
        entry.delete(0, END)

    # display number
    entry.insert(END, num)

def all_clear():
    global num1, num2, operation
    entry.delete(0,END)
    # display num1 0 if nothing in there
    if len(entry.get()) == 0:
        entry.insert(END, 0)
    num1 = 0
    num2 = 0
    operation = None

def backspace():
    entry.delete(len(entry.get())-1)
    # display num1 0 if nothing in there
    if len(entry.get()) == 0:
        entry.insert(END, 0)
# ________________________________________UI SETUP________________________________________
wn = Tk()
wn.minsize(width=600, height=600)
wn.title("Basic Calculator")

# entry box
entry = Entry(bg="#A6AC9F", borderwidth=10, font=("Arial", 40, "normal"))
entry.focus()
entry.insert(END, 0)
entry.grid(row=0, column=0, columnspan=4, sticky=("news"))

# number buttons
btn_7 = Button(text="7", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(7))
btn_8 = Button(text="8", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(8))
btn_9 = Button(text="9", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(9))
btn_4 = Button(text="4", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(4))
btn_5 = Button(text="5", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(5))
btn_6 = Button(text="6", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(6))
btn_1 = Button(text="1", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(1))
btn_2 = Button(text="2", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(2))
btn_3 = Button(text="3", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(3))
btn_0 = Button(text="0", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:display_num(0))

# number buttons positions
btn_7.grid(row=2, column=0, sticky="news", padx=1, pady=1)
btn_8.grid(row=2, column=1, sticky="news", padx=1, pady=1)
btn_9.grid(row=2, column=2, sticky="news", padx=1, pady=1)
btn_4.grid(row=3, column=0, sticky="news", padx=1, pady=1)
btn_5.grid(row=3, column=1, sticky="news", padx=1, pady=1)
btn_6.grid(row=3, column=2, sticky="news", padx=1, pady=1)
btn_1.grid(row=4, column=0, sticky="news", padx=1, pady=1)
btn_2.grid(row=4, column=1, sticky="news", padx=1, pady=1)
btn_3.grid(row=4, column=2, sticky="news", padx=1, pady=1)
btn_0.grid(row=5, column=0, sticky="news", padx=1, pady=1)

# operation buttons
btn_add = Button(text="+", bg="#8ED8FA", font=("Arial", 20, "bold"), command=lambda:choose_operation("+"))
btn_sub = Button(text="-", bg="#8ED8FA", font=("Arial", 20, "bold"), command=lambda:choose_operation("-"))
btn_multi = Button(text="✕", bg="#8ED8FA", font=("Arial", 15, "bold"), command=lambda:choose_operation("*"))
btn_divide = Button(text="÷", bg="#8ED8FA", font=("Arial", 25, "normal"), command=lambda:choose_operation("/"))
btn_square = Button(text="x²", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:choose_operation("x²"))
btn_square_root = Button(text="√x", bg="#676D61", font=("Arial", 20, "normal"), command=lambda:choose_operation("√x"))
btn_equal = Button(text="=", bg="#0D519E", font=("Arial", 20, "normal"), fg="white", command=calculate)
btn_point = Button(text=".", bg="#676D61", font=("Arial", 20, "bold"), command=lambda:display_num("."))

# other buttons
btn_backspace = Button(text="⌫", bg="#EE4049", font=("Arial", 20, "normal"), fg="white", command=backspace)
btn_all_clear = Button(text="AC", bg="#9059E7", font=("Arial", 20, "normal"), fg="white", command=all_clear)

# operation buttons positions
btn_add.grid(row=1, column=3, sticky="news", padx=1, pady=1)
btn_sub.grid(row=2, column=3, sticky="news", padx=1, pady=1)
btn_multi.grid(row=3, column=3, sticky="news", padx=1, pady=1)
btn_divide.grid(row=4, column=3, sticky="news", padx=1, pady=1)
btn_equal.grid(row=5, column=3, sticky="news", padx=1, pady=1)
btn_square.grid(row=5, column=2, sticky="news", padx=1, pady=1)
btn_point.grid(row=5, column=1, sticky="news", padx=1, pady=1)

# other buttons positions
btn_all_clear.grid(row=1, column=0, sticky="news", padx=1, pady=1)
btn_backspace.grid(row=1, column=1, sticky="news", padx=1, pady=1)
btn_square_root.grid(row=1, column=2, sticky="news", padx=1, pady=1)


# adjust all rows and column according to main window size
for row in range(6):
    wn.rowconfigure(row, weight=1)
for column in range(4):
    wn.columnconfigure(column, weight=1)

wn.mainloop()