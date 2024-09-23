import tkinter as tk
import subprocess
import platform
import json

# definir
values = []
verfi = False
vacio = False

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
    global vacio
    valores = set(filtered_values)

    # ver que no este vacio
    all_none = all(val is None or val == 'None' for val in current_values)

    if all_none:
        print("Esta vacio")
        vacio = True  
    else:
        print("Tiene dato")
        vacio = False

    if len(valores) < len(filtered_values):
        message_label.config(text="Hay programas repetidos.", fg="red")
    else:
        message_label.config(text="", fg="red")


def create_option_menu(root, text, var, options):
    frame = tk.Frame(root, bg=root.cget("bg"))  
    label = tk.Label(frame, text=text, font=("Arial", 12, "bold"), fg=fg_color, bg=root.cget("bg"))
    label.pack(side=tk.LEFT, anchor='center', padx=5, pady=5)
    option_menu = tk.OptionMenu(frame, var, *options)
    option_menu.config(width=25, font=("Arial", 12), bg=button_bg, fg=fg_color)
    option_menu.pack(side=tk.TOP, padx=5, pady=5)
    frame.pack(side=tk.TOP, anchor='center', padx=20, pady=5)
    var.trace_add("write", update_values)

def create_option_link_menu(root, text, var):
    frame = tk.Frame(root, bg=root.cget("bg"))
    label = tk.Label(frame, text=text, font=("Arial", 12, "bold"), fg=fg_color, bg=root.cget("bg"))
    label.pack(side=tk.LEFT, padx=5, pady=5)
    entry = tk.Entry(frame, textvariable=var, font=("Arial", 12), fg=fg_color, bg=entry_bg)
    entry.pack(side=tk.RIGHT, padx=5, pady=3, anchor='w', expand=True, fill='x')
    frame.pack(side=tk.TOP, anchor='w', expand=True, fill='both', padx=10, pady=5)

def cerrar_dos(ventana):
    global values
    values = [var.get() for var in link_vars]
    ventana.destroy()
    buttonClick()

def links():
    global verfi
    global link_vars
    dos_ventana = tk.Toplevel(root)
    dos_ventana.title("QuickHabit Builder")
    dos_ventana.config(bg=root.cget("bg"))
    center_window(dos_ventana, 500, 350)

    label = tk.Label(dos_ventana, text="¿Deseas que tu navegador se inicie con algunas páginas?", font=("Arial", 12, "bold"), fg=fg_color, bg=dos_ventana.cget("bg"))
    label.pack(pady=10)

    label = tk.Label(dos_ventana, text="Ejemplo: https://ejemplo.com", font=("Arial", 11), fg=fg_color, bg=dos_ventana.cget("bg"))
    label.pack(pady=5)

    link_vars = [tk.StringVar(value="") for _ in range(4)]
    labels = ["Link 1:", "Link 2:", "Link 3:", "Link 4:"]
    
    for label, var in zip(labels, link_vars):
        create_option_link_menu(dos_ventana, label, var)

    verfi = True
    button = tk.Button(dos_ventana, text="Proceder", command=lambda: cerrar_dos(dos_ventana), bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
    button.pack(pady=15)

def buttonClick():
    global verfi
    global values
    global link_vars
    global vacio

    if "Navegador (Predeterminado)" in valores and verfi == False:
        links()
    else:
        if vacio == False:
            verfi = False
            with open('valores.json', 'w') as file:
                json.dump(list(valores), file)

            with open('valores_link.json', 'w') as file:
                json.dump(values, file)
                
            sistema = platform.system()
            
            if sistema == 'Windows':
                subprocess.run(["python", "create.py"])
            else:
                subprocess.run(["python3", "create.py"])

# cambiar a claro
def set_light_theme():
    global fg_color, bg_color, button_bg, button_fg, entry_bg
    fg_color = "#333"
    bg_color = "#f7f7f7"
    button_bg = "#e0e0e0"
    button_fg = "#333"
    entry_bg = "#ffffff"
    root.config(bg=bg_color)
    update_theme()

# cambiar a oscuro
def set_dark_theme():
    global fg_color, bg_color, button_bg, button_fg, entry_bg
    fg_color = "#fff"
    bg_color = "#333"
    button_bg = "#555"
    button_fg = "#fff"
    entry_bg = "#444"
    root.config(bg=bg_color)
    update_theme()

# actualizar colores
def update_theme():
    message_label.config(fg=fg_color, bg=bg_color)
    label.config(fg=fg_color, bg=bg_color)
    button.config(bg=button_bg, fg=button_fg)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label):
            widget.config(bg=bg_color, fg=fg_color)
        elif isinstance(widget, tk.Button):
            widget.config(bg=button_bg, fg=button_fg)
        elif isinstance(widget, tk.Entry):
            widget.config(bg=entry_bg, fg=fg_color)

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", root.quit)
root.title("QuickHabit Builder")
center_window(root, 600, 525)
root.wm_minsize(600, 565)

# tma claro por defecto
fg_color = "#333"
bg_color = "#f7f7f7"
button_bg = "#e0e0e0"
button_fg = "#333"
entry_bg = "#ffffff"
root.config(bg=bg_color)

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Ejecutar", menu=submenu)
submenu.add_command(label="Salir", command=root.quit)

submenu2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Temas", menu=submenu2)
submenu2.add_command(label="Claro", command=set_light_theme)
submenu2.add_command(label="Oscuro", command=set_dark_theme)

label = tk.Label(root, text="Elija qué aplicaciones desea ejecutar.", font=("Arial", 16, "bold"), fg=fg_color, bg=bg_color)
label.pack(pady=20)

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

message_label = tk.Label(root, text="", font=("Arial", 12), fg="red", bg=bg_color)
message_label.pack(side=tk.TOP, padx=5, pady=5)

create_option_menu(root, "1:", var1, options)
create_option_menu(root, "2:", var2, options)
create_option_menu(root, "3:", var3, options)
create_option_menu(root, "4:", var4, options)
create_option_menu(root, "5:", var5, options)
create_option_menu(root, "6:", var6, options)

button = tk.Button(root, text="Proceder", command=buttonClick, bg=button_bg, fg=button_fg, font=("Arial", 14, "bold"))
button.pack(pady=20)

message_label = tk.Label(root, text="Beta ver1.0.0", font=("Arial", 12), fg=button_fg, bg=bg_color)
message_label.pack(side=tk.RIGHT, anchor="sw", padx=5, pady=5)

root.mainloop()