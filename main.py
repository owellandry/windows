import tkinter as tk
from tkinter import messagebox
import subprocess

def activate_windows(version):
    if version == 1:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 2:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 3:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'W269N-WFGWX-YVC9B-4J6C9-T83GX']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 4:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'MH37W-N47XK-V7XM9-C7227-GCQG9']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 5:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 6:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 7:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'NPPR9-FWDCX-D2C8J-H872K-2YT43']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 8:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 9:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'YYVX9-NTFWV-6MDM3-9PT4T-4M68B']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 10:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', '44RPN-FTY23-9VTTB-MP9BX-T84FV']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 11:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")
    elif version == 12:
        command = ['slmgr.vbs', '-upk']
        subprocess.call(command)
        command = ['slmgr', '/ipk', 'Q269N-WFGWX-YVC9B-4J6C9-T83GX']
        subprocess.call(command)
        command = ['slmgr', '/skms', 'kms.digiboy.ir']
        subprocess.call(command)
        command = ['slmgr', '/ato']
        subprocess.call(command)
        messagebox.showinfo("Activación exitosa", "FELICIDADES, has activado tu Windows")

def show_menu():
    window = tk.Tk()
    window.title("ACTIVACION DE WINDOWS")
    window.configure(background='blue')
    window.geometry("400x400")

    label = tk.Label(window, text="BIENVENIDO", font=("Arial", 18), bg="blue", fg="white")
    label.pack(pady=20)

    label_version = tk.Label(window, text="ELIJE TU VERSIÓN DE WINDOWS", font=("Arial", 14), bg="blue", fg="white")
    label_version.pack(pady=10)

    version_choices = [
        "Windows 10/11 Home",
        "Windows 10/11 Home Single Lenguage",
        "Windows 10/11 Pro",
        "Windows 10/11 Pro N",
        "Windows 10/11 Education",
        "Windows 10/11 Education N",
        "Windows 10/11 Enterprise",
        "Windows 10/11 Enterprise N",
        "Windows 10/11 Enterprise G",
        "Windows 10/11 Enterprise G N",
        "Windows 10/11 Workstations",
        "Windows 10/11 Ultimate"
    ]

    selected_version = tk.StringVar(window)

    dropdown = tk.OptionMenu(window, selected_version, *version_choices)
    dropdown.config(width=30, font=("Arial", 12))
    dropdown.pack(pady=10)

    def activate():
        version_index = version_choices.index(selected_version.get())
        activate_windows(version_index + 1)

    button = tk.Button(window, text="ACTIVAR", font=("Arial", 14), command=activate)
    button.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    show_menu()
