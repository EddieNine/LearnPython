from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False, False)

def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text = entry.get(1.0, END)
    open_file.write(text)
    open_file.close()

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if not file_path:  # Cancelar ou arquivo inválido
        return
    with open(file_path, 'r') as file:
        content = file.read()
        entry.delete(1.0, END)  # Limpa o conteúdo existente
        entry.insert(INSERT, content)

Button(root, width=20, height=2, bg='#fff', text='Save File', command=save_file).place(x=100, y=5)
Button(root, width=20, height=2, bg='#fff', text='Open File', command=load_file).place(x=300, y=5)

entry = Text(root, height=33, width=72, wrap=WORD)
entry.place(x=10, y=60)

root.mainloop()
