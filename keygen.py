import tkinter as tk
from tkinter import messagebox
import random

KEY_BACKGROUND = 'White'

def init_gui():
    root = tk.Tk()
    return root

def init_input(fr_input):
    label_info = tk.Label(fr_input, text='Введите 6-ти значное число:')
    value_entry = tk.Entry(fr_input, width=10)
    labels = []
    def get_value(value_entry):
        value = value_entry.get()
        if len(value) == 6:
            nums = []
            letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            letters_in = []
            for i in value:
                nums.append(i)

            first_nums = nums[:3]
            second_nums = nums[3:]
            first_nums = ''.join(random.sample(first_nums, len(first_nums)))
            second_nums = ''.join(random.sample(second_nums, len(second_nums)))
            
            third_nums = int(''.join(map(str, second_nums))) + int(''.join(map(str, first_nums)))

            for i in range(2):
                letters_in.append(random.choice(letters) + random.choice(letters))
            
            if third_nums <= 999:
                text = f'{first_nums}{letters_in[0]}-{second_nums}{letters_in[1]}-0{third_nums}'
            else:
                text = f'{first_nums}{letters_in[0]}-{second_nums}{letters_in[1]}-{third_nums}'

            label_key = tk.Label(text=text, background=KEY_BACKGROUND, font='bold')
            label_key.place(relx=.5, rely=.4, anchor='c')
            labels.append(label_key)
            if len(labels) > 1:
                label = labels.pop(0)
                label.destroy()
        else:
            messagebox.showinfo('ERROR', 'Введено не 6-ти значное число.')

        
    btn_value = tk.Button(fr_input, text='Генерировать', command= lambda: get_value(value_entry))
    
    btn_value.pack(side=tk.RIGHT)
    value_entry.pack(side=tk.RIGHT)
    label_info.pack(side=tk.LEFT)

def init_frames(root):
    fr_input = tk.Frame(root)
    fr_bg = tk.Frame(root)
    fr_input.pack(side=tk.BOTTOM, anchor='se')
    fr_bg.pack()
    return fr_bg, fr_input


if __name__ == '__main__':
    root = init_gui()
    root.geometry('320x240')
    root.resizable(width=False, height=False)
    root.title('Генератор ключей Sea of Thievs')

    fr_bg, fr_input = init_frames(root)

    bg = tk.PhotoImage(file='sea_s.png')
    label_bg = tk.Label(fr_bg, image=bg)
    label_bg.pack(side=tk.TOP)

    init_input(fr_input)
    
    root.mainloop()
