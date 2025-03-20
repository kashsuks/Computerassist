import tkinter as tk
from userInterface import UserInterface

def main():
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()