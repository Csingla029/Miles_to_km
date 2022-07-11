import tkinter


def miles_to_km():
    miles=float(entry.get())
    km=miles*1.609
    label_3.config(text=f"{km}")


window = tkinter.Tk();
window.title("Mile to Km Converter")
# window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

entry = tkinter.Entry(width=10)
entry.grid(column=1,row=0)
label_0 = tkinter.Label(text="Miles")
label_0.grid(column=2,row=0)


label_1 = tkinter.Label(text="is equal to")
label_1.grid(column=0,row=1)

label_3 = tkinter.Label(text="0")
label_3.grid(column=1,row=1)

label_2 = tkinter.Label(text="Km")
label_2.grid(column=2,row=1)

button = tkinter.Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)
window.mainloop()