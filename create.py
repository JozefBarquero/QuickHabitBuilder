import tkinter as tk
import platform
import os
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()
root.protocol("WM_DELETE_WINDOW", root.quit)


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

print(datos)
print(sistema)

datos = datos[:6] 

def guardar():
    # Obtener la ruta del escritorio
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    ruta_save = filedialog.asksaveasfilename(initialdir=escritorio, defaultextension=".pyw", filetypes=[("Python Files", "*.pyw")])
    
    if ruta_save:
        contenido = f'''
#!/usr/bin/env python3

import subprocess
import webbrowser
import os

import platform

def run_command(command):
    if platform.system() == "Windows":
        return subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        return subprocess.run(command)

def open_program(command):
    if platform.system() == "Windows":
        return subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        return subprocess.Popen(command)

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
        with open(ruta_save, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
            
    if root.winfo_exists():
        root.destroy()
    if root2.winfo_exists():
        root2.destroy()

            
#Para windows extra compatibilidad:
spotify = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify'], check=True)
    print("Spotify abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("APPDATA"), "Spotify\\Spotify.exe")])
        print("Spotify abierto desde la instalación en AppData\\Roaming.")
    except FileNotFoundError:
        print("Spotify no se encuentra instalado.")
    '''   

vscode = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\Microsoft.VisualStudioCode_8wekyb3d8bbwe!App'], check=True)
    print("Visual Studio Code abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Programs\\Microsoft VS Code\\Code.exe")])
        print("Visual Studio Code abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("Visual Studio Code no se encuentra instalado.")
'''

gimp = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\GIMP.GIMP2_8wekyb3d8bbwe!App'], check=True)
    print("GIMP abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "GIMP 2\\bin\\gimp-2.10.exe")])
        print("GIMP abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("GIMP no se encuentra instalado.")
'''

blender = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\BlenderFoundation.Blender_8wekyb3d8bbwe!App'], check=True)
    print("Blender abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Blender Foundation\\Blender 3.6\\blender.exe")])
        print("Blender abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("Blender no se encuentra instalado.")
'''

zoom = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\ZoomVideoCommunications.Zoom_8wekyb3d8bbwe!App'], check=True)
    print("Zoom abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Zoom\\bin\\Zoom.exe")])
        print("Zoom abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("Zoom no se encuentra instalado.")
'''

audacity = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\Audacity.Audacity_8wekyb3d8bbwe!App'], check=True)
    print("Audacity abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("ProgramFiles"), "Audacity\\audacity.exe")])
        print("Audacity abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("Audacity no se encuentra instalado.")
'''

youtube_music = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\GoogleInc.YouTubeMusic_8wekyb3d8bbwe!App'], check=True)
    print("YouTube Music abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("YouTube Music App no se encuentra instalada.")
'''

figma = f'''      
try:
    subprocess.run(['powershell', '-command', 'Start-Process shell:AppsFolder\\Figma.Figma_8wekyb3d8bbwe!App'], check=True)
    print("Figma abierto desde la Microsoft Store.")
except (subprocess.CalledProcessError, FileNotFoundError):
    try:
        subprocess.Popen([os.path.join(os.getenv("LOCALAPPDATA"), "Figma\\Figma.exe")])
        print("Figma abierto desde la instalación tradicional.")
    except FileNotFoundError:
        print("Figma no se encuentra instalado.")
'''

def incompa():
    global root2
    print("Elemento incompatible")
    if sistema == 'Linux':
        root2 = tk.Tk()
        root2.title("QuickHabit Builder")
        center_window(root2, 650, 200)

        label = tk.Label(root2, text="Lo sentimos, seleccionaste algunos programas incompatibles con tu sistema operativo.", font=("Arial", 12), fg="black")
        label.pack()

        label = tk.Label(root2, text="Programas incompatibles en tu sistema:", font=("Arial", 10), fg="black")
        label.pack()
        label = tk.Label(root2, text="- Figma", font=("Arial", 12), fg="black")
        label.pack()
        label = tk.Label(root2, text="- You Tube Music (App)", font=("Arial", 12), fg="black")
        label.pack()

        label = tk.Label(root2, text="¿Continuar ignorando esos programas?", font=("Arial", 12), fg="black")
        label.pack()

        button = tk.Button(root2, text="Aceptar", command=proceso)
        button.pack()
        root2.protocol("WM_DELETE_WINDOW", root2.quit)
        return()

def proceso():
    global root2
    if 'root2' in globals() and root2.winfo_exists():
        root2.destroy()

    print("Proceso ejecutado")
    global proceso    
    # Preestablecidos
    for i in range(len(datos)):
        if datos[i] == "Navegador (Predeterminado)":
            datos[i] = "webbrowser.open('https://')"

    for i in range(len(datos)):
        if datos[i] == "Visual Studio Code":
            if sistema == 'Windows':
                datos[i] = vscode
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/code"])'
            
    for i in range(len(datos)):
        if datos[i] == "GitHub (Web)":
            datos[i] = "webbrowser.open('https://github.com')"     
            
    for i in range(len(datos)):
        if datos[i] == "Figma":
            if sistema == 'Windows':
                datos[i] = figma
            elif sistema == 'Linux':
                datos[i] = "" 

    for i in range(len(datos)):
        if datos[i] == "GIMP":
            if sistema == 'Windows':
                datos[i] = gimp
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/gimp"])'

    for i in range(len(datos)):
        if datos[i] == "Blender":
            if sistema == 'Windows':
                datos[i] = blender
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/blender"])'

    for i in range(len(datos)):
        if datos[i] == "Notion":
            datos[i] = "webbrowser.open('https://notion.so')"
            
    for i in range(len(datos)):
        if datos[i] == "Zoom":
            if sistema == 'Windows':
                datos[i] = zoom
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/zoom"])'

    for i in range(len(datos)):
        if datos[i] == "Audacity":
            if sistema == 'Windows':
                datos[i] = audacity
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/audacity"])'

    for i in range(len(datos)):
        if datos[i] == "Spotify (Web)":
            datos[i] = "webbrowser.open('https://open.spotify.com')"     
                 
    for i in range(len(datos)):
        if datos[i] == "Spotify (App)":
            if sistema == 'Windows':
                datos[i] = spotify
            elif sistema == 'Linux':
                datos[i] = 'subprocess.Popen(["/usr/bin/spotify"])'

    for i in range(len(datos)):
        if datos[i] == "You Tube Music (Web)":
            datos[i] = "webbrowser.open('https://music.youtube.com')"
            
    for i in range(len(datos)):
        if datos[i] == "You Tube Music (App)":
            if sistema == 'Windows':
                datos[i] = youtube_music
            elif sistema == 'Linux':
                datos[i] = "" 

    #Si hay un dato vacio
    for i in range(len(datos)):
        if datos[i] is None:
            datos[i] = ""  
            
    global dato1, dato2, dato3, dato4, dato5, dato6    
    dato1, dato2, dato3, dato4, dato5, dato6 = (datos + [""] * 6)[:6]
    
    guardar()

def problem():
    print("si inicia")
    for i in range(len(datos)):
        print(f"Verificando: {datos[i]}")
        if datos[i] not in ('Figma', 'Slack', 'You Tube Music (App)'):
            proceso()
            print("se ejecuta?")
            break
        else:
            incompa()
            break


print("llego")
problem()
root.mainloop()