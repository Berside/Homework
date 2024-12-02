from tkinter import *
root = Tk()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n
def Prime_NUmbers():
    clear_text()
    bd = []
    if minentry.get().isdigit() and maxentry.get().isdigit():
        min = int(minentry.get())
        max = int(maxentry.get())

        if (min >= 0) and (max > 0) and (type(min) is int) and (type(max) is int):
            for i in range(min,max):
                a = is_prime(i)
                if a > 2:
                    bd.append(a)
            for i in range(len(bd)):
                result.insert(END, f'{(str(bd[i]))} ')
            c['text'] = f'Найдено чисел:{(str(len(bd)))}'
    else:
        result.insert(END, 'Нужно вводить только целые положительные числа')

def is_harshad(num):
    sum_of_digits = sum(int(digit) for digit in str(num))
    return num % sum_of_digits == 0

def find_harshad_numbers():
    clear_text()
    harshad_numbers = []
    if minentry.get().isdigit() and maxentry.get().isdigit():
        min = int(minentry.get())
        max = int(maxentry.get())

        if (min_val >= 0) and (max_val > 0) and (type(min_val) is int) and (type(max_val) is int):
            for num in range(min_val, max_val):
                if is_harshad(num):
                    harshad_numbers.append(num)
            for i in range(len(harshad_numbers)):
                result.insert(END, f'{str(harshad_numbers[i])} ')
            c['text'] = f'Найдено чисел: {str(len(harshad_numbers))}'
    else:
        result.insert(END, 'Нужно вводить только целые положительные числа')
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return a

def find_fibonacci_numbers():
    clear_text()
    fib_numbers = []
    if minentry.get().isdigit() and maxentry.get().isdigit():
        min = int(minentry.get())
        max = int(maxentry.get())
        if ( min >= 0) and ( max > 0) and (type(min) is int) and (type(max) is int):
            while fibonacci(min) <= max:
                fib_numbers.append(fibonacci(min))
                min += 1
            fib_numbers.pop(0)
            for i in range(len(fib_numbers)):
                result.insert(END, f'{str(fib_numbers[i])} ')
            c['text'] = f'Найдено чисел: {str(len(fib_numbers))}'
    else:
        result.insert(END, 'Нужно вводить только целые положительные числа')

root.geometry('640x480')
root.resizable(width=False, height=False)

minlabel = Label(root, text = "Min Value:")
minlabel.pack()
minentry = Entry(root)
minentry.pack()

maxlabel = Label(root, text = "Max Value:")
maxlabel.pack()
maxentry = Entry(root)
maxentry.pack()

btn = Button(root, text="Find Numbers", command=Prime_NUmbers)
btn.pack()

c = Label(root, text="Найдено чисел:")
c.pack()
result = Text(root,wrap=WORD)
result.pack()

def clear_text():
    result.delete(1.0, END)

def update_command(*args):
    if (radio.get() == 1):
        btn['command'] = Prime_NUmbers
    elif (radio.get() == 2):
        btn['command'] = find_fibonacci_numbers
    elif (radio.get() == 3):
        btn['command'] = find_harshad_numbers

radio = IntVar()
radio.set("1")
radio.trace('w', update_command)

menu = Menu(root)
submenu = Menu(menu, tearoff=0)
submenu.add_radiobutton(label="Простые числа", value="1", variable=radio)
submenu.add_radiobutton(label="Числа Фибоначчи", value="2", variable=radio)
submenu.add_radiobutton(label="Числа Харшада", value="3", variable=radio)

menu.add_cascade(label="Поиск", menu=submenu)

root.config(menu=menu)

root.mainloop()