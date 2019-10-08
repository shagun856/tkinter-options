import tkinter

def shows():
    res="Entered text:%s"%(txt.get())
    label.configure(text=res)
window= tkinter.Tk()
window.title("ROOT")
label= tkinter.Label(window, text="Enter Text here",font=("Arial",10))
label.grid(row=0,column=0)
txt= tkinter.Entry(window,width=10)
txt.grid(row=0,column=1)
bt= tkinter.Button(window, text="Show Text",font=("Arial",10),bg="black",fg="white",command=shows)
bt.grid(row=1,column=0,sticky=tkinter.W,pady=4)
RWidth=window.winfo_screenwidth()
RHeight=window.winfo_screenheight()
window.geometry(("%dx%d")%(RWidth,RHeight))
window.mainloop()
