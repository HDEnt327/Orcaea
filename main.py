import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
from PIL import Image
import os
from arc import arc
import json
import tracemalloc

tracemalloc.start()

# CODE WISE TODO: Organize with classes

# TODO: Organize interface, add table view of play data
# TODO: Support multi-profile/users
# TODO: Output as image (b30)
# TODO: Take in manual data when OCR fails
# TODO: Add more screen position and ratios
# TODO: Fix error outputting
# TODO: Pyinstaller windows EXE tetss
# TODO: requirements.txt generation

window = tk.Tk()
window.title('Orcaea')
window.geometry('400x300')

fr_title = ttk.Frame(window, border=50)

lb_title = ttk.Label(fr_title, text='Orcaea', anchor=tk.CENTER, font=('Arial', 20))
lb_subtitle = ttk.Label(fr_title, text="Start by choosing files below!")
lb_title.pack()
lb_subtitle.pack() 

fr_title.pack()

lb_res = ttk.Label(text='')
btn_save = ttk.Button(text='')

def selectImage():
    global lb_res
    global btn_save
    lb_res.destroy()
    btn_save.destroy()
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image', filetypes=(('PNG Files', '*.png'), ('JPG Files', '*.jpg'), ('JPEG Files', '*.jpeg')))
    try:
        print(filename)
        img = Image.open(filename)
        res = arc(img)
        msg = f'Name: {res.name}\nScore: {res.score}\nDifficulty: {res.diff}\nPTT: {res.ptt}'
        lb_res = ttk.Label(text=msg)
        lb_res.pack()
        btn_save = ttk.Button(window, text='Save', command=lambda: save(res))
        btn_save.pack()
    except Exception as e:
        print("Ah shit, here we go again...")
        messagebox.showerror(title='Error', message=e)

def save(res: arc):
    with open('scores.json', 'r+') as s:
        scores = json.load(s)
        scores['scores'].append({'name': res.name, 'score': res.score, 'diff': res.diff, 'ptt': res.ptt, 'songid': res.songid, 'const': res.const})
        s.seek(0)
        json.dump(scores, s, indent=4)


btn_select = ttk.Button(window, text='Select Image', command=lambda: selectImage())

btn_select.pack()

window.mainloop()
