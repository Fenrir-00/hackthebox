import os, sys, time, io
import random
import platform
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo

  
sistema = platform.system()
limpieza = ""

if sistema == "Linux":
  limpieza = "clear"
elif sistema == "Windows":
  limpieza ="cls"


class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def incorrecto():
    os.system(f"{limpieza}")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)

def menu():
    os.system("mkdir maquina")
    os.chdir("maquina")
    var = input("introduce >> ")
    os.system(f"nmap -sC -sS -sV -p- -vvv -Pn -n  {var} --open oN namp")

menu()
