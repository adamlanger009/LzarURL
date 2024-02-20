import pyshorteners
import tkinter as tk




def submit_url():
    long_url = entry.get()
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    entry_two.delete(0,100)
    entry_two.insert(0, short_url)
    






root = tk.Tk()
root.title("Lzar URL")
root.configure(background="green")
root.geometry("500x500")



label = tk.Label(root, text="URL Shortener", font=("Courier 22 bold"))
label.pack()


entry = tk.Entry(root, width= 40)
entry.focus_set()
entry.pack()
entry.insert(0,"Enter URL Here")

submit_btn = tk.Button(root, text="Submit", command=submit_url)
submit_btn.pack()


entry_two = tk.Entry(root, width= 40)
entry_two.focus_set()
entry_two.pack()
entry_two.insert(0,"Final URL Will Be Displayed Here (Do not enter url here)")





root.mainloop()






    




