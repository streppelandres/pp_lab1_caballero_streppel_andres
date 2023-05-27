import sys
import os

# Esto es re rancio, pero es para levantar los utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app import App

if __name__ == '__main__':
    App().start()