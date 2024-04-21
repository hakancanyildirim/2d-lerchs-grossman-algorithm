from tkinter import *

master = Tk()

master.title("2D Lerchs-Grossman Algorithm")

def enterbtn():
    global total_number_of_blocks
    number_of_blocks_in_X_dimension = X.get()
    number_of_blocks_in_Y_dimension = Y.get()
    total_number_of_blocks = int(number_of_blocks_in_X_dimension) + int(number_of_blocks_in_Y_dimension)
    messageVar.configure(text="Total number of blocks:" + str(total_number_of_blocks))

Label(master, text="Enter the number of blocks for the X dimension:").grid(row=0)
X = Entry(master)

Label(master, text="Enter the number of blocks for the Y dimension:").grid(row=1)
Y = Entry(master)

X.grid(row=0, column=1)
Y.grid(row=1, column=1)

button1 = Button(text = "Enter", font = ("Calibri", 10), command = enterbtn)
button1.grid(column = 0, row = 3, columnspan = 2)

messageVar = Message(master)
messageVar.grid(column = 0, row = 4, columnspan = 2)

mainloop()

'''block_dimension_x = input()
block_dimension_y = input()

costs = float(input("Costs in dollars: "))
revenues = float(input("Revenues in dollars: "))

profit = e1 - e2

print("Here is your net profit: " + "$" + str(profit))'''