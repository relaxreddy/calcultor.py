import tkinter as tk
def click(event):
    curr_text = display.get()
    clicked_btn_text = event.widget.cget("text")
    if clicked_btn_text == "=":
        try:
            result = eval(curr_text)
            display.set(result)
            label.config(text="q for quitting from the calculator",font="Verdana 12 bold italic")
        except Exception as e:
            display.set("Wrong Calculation")
            label.config(text="q for quitting from the calculator",font="Verdana 12 bold italic")
    elif clicked_btn_text == "C":
        display.set("")
        label.config(text="q for quitting from the calculator",font="Verdana 12 bold italic")
    elif clicked_btn_text == "q":
        app.destroy()

    else:
        is_operator = clicked_btn_text in "+-*/%"
        ends_with_op = curr_text.endswith(("+","-","*","/","%"))
        if is_operator and (not curr_text or ends_with_op):
            return
        else:
            display.set(curr_text + clicked_btn_text)

#creating calculator apploication window
app = tk.Tk()
app.title("Calculator")

#setting dimensions for application window
app.geometry("400x500")

frame = tk.Frame(app)
frame.pack()
frame.configure(bg="black",bd=2)
#widget for displaying calculation 
display = tk.StringVar()
start = tk.Entry(frame, textvariable=display, font="Arial 20 bold",bd=10,insertwidth=4,width=15)
start.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

label = tk.Label(frame,text="q for quitting from the calculator",font="Verdana 12 bold italic")
label.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


#creating buttons
buttons = [("C","%","/","q"),
           ("7","8","9","*"),
           ("4","5","6","-"),
           ("1","2","3","+"),
           ("00","0",".","=")]
row_num = 2
for row in buttons:
    col_num = 0
    for btn_txt in row:
        btn = tk.Button(frame, text=btn_txt,font="Arial 15 bold",padx=10,pady=10)
        btn.grid(row=row_num,column=col_num,padx=5,pady=5)
        btn.bind("<Button-1>",click)
        btn.configure(bg="green")
        col_num +=1
    row_num += 1

#main loop
app.mainloop()