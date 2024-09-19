import tkinter as tk
import platform
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()

# Identifica sistema
sistema = platform.system()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    
def read_values():
    with open('valores.json', 'r') as file:
        global datos
        datos = json.load(file)
    
def read_values_link():
    try:
        with open('valores_link.json', 'r') as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        return {}
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error inesperado: {e}")
        return {}

# Traer datos
read_values()
valores_link = read_values_link()

datos = datos[:6] 

#Incompatibilidad
def cerrar(ventana):
    ventana.destroy()  
    proceso()


def proceso():
    # Preestablecidos
    for i in range(len(datos)):
        if datos[i] == "Navegador (Predeterminado)":
            datos[i] = "webbrowser.open('')"

    for i in range(len(datos)):
        if datos[i] == "Visual Studio Code":
            if sistema == 'Windows':
                datos[i] = datos[i] = 'subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Programs\\Microsoft VS Code\\Code.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/code"])'
            
    for i in range(len(datos)):
        if datos[i] == "GitHub (Web)":
            datos[i] = "webbrowser.open('https://github.com')"     
            
    for i in range(len(datos)):
        if datos[i] == "Figma":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Figma\\Figma.exe")])'
            elif sistema == 'Linux':
                datos[i] = "" 

    for i in range(len(datos)):
        if datos[i] == "GIMP":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "GIMP 2\\bin\\gimp-2.10.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/gimp"])'

    for i in range(len(datos)):
        if datos[i] == "Blender":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Blender Foundation\\Blender 3.6\\blender.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/blender"])'

    for i in range(len(datos)):
        if datos[i] == "Notion":
            datos[i] = "webbrowser.open('https://notion.so')"
            
    for i in range(len(datos)):
        if datos[i] == "Slack":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Programs\\Slack\\Slack.exe")])'
            elif sistema == 'Linux':
                datos[i] = ""   
            
    for i in range(len(datos)):
        if datos[i] == "Zoom":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Zoom\\bin\\Zoom.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/zoom"])'

    for i in range(len(datos)):
        if datos[i] == "Postman":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Postman\\Postman.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/opt/Postman/Postman"])'

    for i in range(len(datos)):
        if datos[i] == "Docker":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Docker/Docker Desktop.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["sudo", "systemctl", "start", "docker"])'
            
    for i in range(len(datos)):
        if datos[i] == "Krita":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Krita (x64)\\bin\\krita.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/krita"])'

    for i in range(len(datos)):
        if datos[i] == "Audacity":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Audacity\\audacity.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/audacity"])'

    for i in range(len(datos)):
        if datos[i] == "Spotify (Web)":
            datos[i] = "webbrowser.open('https://open.spotify.com')"     
            
    for i in range(len(datos)):
        if datos[i] == "Spotify (App)":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Spotify\\Spotify.exe")])'
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/spotify"])'

    for i in range(len(datos)):
        if datos[i] == "You Tube Music (Web)":
            datos[i] = "webbrowser.open('https://music.youtube.com')"
            
    for i in range(len(datos)):
        if datos[i] == "You Tube Music (App)":
            if sistema == 'Windows':
                datos[i] = 'subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "YouTube Music\\YouTube Music.exe")])'
            elif sistema == 'Linux':
                datos[i] = "" 
                
    #Si hay un dato vacio
    for i in range(len(datos)):
        if datos[i] is None:
            datos[i] = ""  
            
    global dato1, dato2, dato3, dato4, dato5, dato6    
    dato1, dato2, dato3, dato4, dato5, dato6 = (datos + [""] * 6)[:6]

    print(f'dato1 = {dato1}')
    print(f'dato2 = {dato2}')
    print(f'dato3 = {dato3}')
    print(f'dato4 = {dato4}')
    print(f'dato5 = {dato5}')
    print(f'dato6 = {dato6}')
    print(sistema)
    
    guardar()



def guardar():
    global dato
    # Salida
    ruta_save = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if ruta_save:
        contenido = f'''
#!/usr/bin/env python3

import subprocess
import webbrowser
import os

{dato1}
{dato2}
{dato3}
{dato4}
{dato5}
{dato6}

# Script creado por QuickHabit Builder.
# 2024 - https://github.com/JozefBarquero/QuickHabitBuilder
# ver 1.0.0
        '''
        with open(ruta_save, "w") as archivo:
            archivo.write(contenido)


if datos in ('Figma', 'Slack', 'You Tube Music (App)'):
    dos_ventana = tk.Toplevel(root)
    dos_ventana.title("QuickHabit Builder")
    center_window(dos_ventana, 900, 300)

    label = tk.Label(dos_ventana, text="Lo sentimos, algunos de estos programas no están disponibles en su sistema operativo y serán ignorados.", font=("Arial", 12), fg="black")
    label.pack()

    label = tk.Label(dos_ventana, text="- Figma", font=("Arial", 12), fg="black")
    label.pack()
    label = tk.Label(dos_ventana, text="- Slack", font=("Arial", 12), fg="black")
    label.pack()
    label = tk.Label(dos_ventana, text="- You Tube Music (App)", font=("Arial", 12), fg="black")
    label.pack()

    label = tk.Label(dos_ventana, text="¿Desea continuar?", font=("Arial", 12), fg="black")
    label.pack()

    button = tk.Button(dos_ventana, text="Aceptar", command=lambda: cerrar(dos_ventana))
    button.pack()

else:
    proceso()

        
# Error
if sistema != 'Windows' or 'Linux':
    def cerrar_dos(ventana):
        ventana.destroy()  

    def incompatible_dos():
        dos_ventana = tk.Toplevel(root)
        dos_ventana.title("QuickHabit Builder")
        center_window(dos_ventana, 900, 300)

        label = tk.Label(dos_ventana, text="Lo sentimos, Sistama Operativo no soportado.", font=("Arial", 12), fg="black")
        label.pack()
        
        button = tk.Button(dos_ventana, text="Aceptar", command=lambda: cerrar_dos(dos_ventana))
        button.pack()

        root.mainloop()