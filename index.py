import tkinter as tk
import subprocess
import json  

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def update_values(*args):
    current_values = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()]
    filtered_values = [val for val in current_values if val != options[0]]
    global valores
    valores = set(filtered_values)
    if len(valores) < len(filtered_values):
        message_label.config(text="Hay programas repetidos.", fg="red")
    else:
        message_label.config(text="", fg="red")

def create_option_menu(root, text, var, options):
    frame = tk.Frame(root)
    label = tk.Label(frame, text=text, font=("Arial", 12), fg="black")
    label.pack(side=tk.LEFT, padx=5, pady=5)
    option_menu = tk.OptionMenu(frame, var, *options)
    option_menu.pack(side=tk.LEFT, padx=5, pady=5)
    frame.pack(side=tk.TOP, anchor='w')
    var.trace_add("write", update_values)

def buttonClick():
    # Guardar los valores en un archivo
    with open('valores.json', 'w') as file:
        json.dump(list(valores), file)
    subprocess.run(["python3", "create.py"])

root = tk.Tk()
root.title("QuickHabit Builder")
center_window(root, 800, 600)

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=submenu)
submenu.add_command(label="Nuevo")
submenu.add_command(label="Abrir")
submenu.add_separator()
submenu.add_command(label="Salir", command=root.quit)

submenu2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Temas", menu=submenu2)
submenu2.add_command(label="Claro")
submenu2.add_command(label="Oscuro")

label = tk.Label(root, text="Elija qué aplicaciones desea ejecutar.", font=("Arial", 16), fg="black")
label.pack()

def read_options(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

options = read_options('programas.txt')

var1 = tk.StringVar(value=options[0])
var2 = tk.StringVar(value=options[0])
var3 = tk.StringVar(value=options[0])
var4 = tk.StringVar(value=options[0])
var5 = tk.StringVar(value=options[0])
var6 = tk.StringVar(value=options[0])

message_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
message_label.pack(side=tk.TOP, padx=5, pady=5)

create_option_menu(root, "1:", var1, options)
create_option_menu(root, "2:", var2, options)
create_option_menu(root, "3:", var3, options)
create_option_menu(root, "4:", var4, options)
create_option_menu(root, "5:", var5, options)
create_option_menu(root, "6:", var6, options)

button = tk.Button(root, text="Proceder", command=buttonClick)
button.pack()

root.mainloop()
