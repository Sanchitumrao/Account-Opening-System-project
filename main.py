import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class mainPage:
        def __init__(self, root):
                    self.root = root
                    self.root.title("ACCOUNT OPENING SYSTEM")
                    self.root.geometry("650x500")
                    self.root.resizable(False, False)
                    self.root.configure(bg="#e6f2ff")

                    img = ImageTk.PhotoImage(Image.open('images/img.png').resize((260, 260)))
                    Bimage = tk.Label(self.root, image=img)
                    Bimage.image = img
                    Bimage.place(x=200, y=30)
                    #Choose bank label
                    ChooseBnkLabel=tk.Label(self.root,text="Choose Bank",
                                            width=15,
                                            height=2,
                                            bg="#caeffa")
                    ChooseBnkLabel.place(x=200,y=300)
                    #choose bank entry
                    BnkOptions=["Bank Of Baroda","Indian Bank","SBI"]
                    bank_dropdown=ttk.Combobox(root,values=BnkOptions,state="readonly",width=15)
                    bank_dropdown.pack()
                    bank_dropdown.place(x=340,y=310)
                    bank_dropdown.set("SBI")
                    #Account open btn
                    AcOpen_button = tk.Button(self.root, text='OPEN A/C',
                                font=('Courier New', 10),
                                width=15,
                                height=2,
                                relief="flat",
                                bg="green",
                                fg="white",)
                    AcOpen_button.place(x=200, y=380)
                    

                    #Exit btn
                    exit_button = tk.Button(self.root, text='EXIT',
                                font=('Courier New', 10),
                                width=15,
                                height=2,
                                relief="flat",
                                command=self.root.destroy,
                                bg="red",
                                fg="white",
                                activebackground="#caeffa")
                    exit_button.place(x=370, y=380)
if __name__ == "__main__":
    root = tk.Tk()
    app = mainPage(root)
    root.mainloop()