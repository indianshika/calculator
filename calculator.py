import tkinter as tkr
app = tkr.Tk(__name__)
app.title('Calculator')
app.geometry('400x400')

### LABEL ###

tkr.Label(app, text = 'CALCULATOR',font=('Times',20,'bold'),fg='black').place(x=100,y=10)
tkr.Label(app,text = 'By Anshika Agrawal',font=('Times',10,'bold italic'),fg='black').place(x=150,y=40)
tkr.Label(app,text = 'First value') .place(x=30,y=70)
tkr.Label(app,text = 'Second value') .place(x=200,y=70)

### ENTRY BOX ###

fv= tkr.Variable(app)
tkr.Entry(app,textvariable=fv,width=15).place(x=30,y=90)

sv = tkr.Variable(app)
tkr.Entry(app,textvariable=sv,width=15).place(x=200,y=90)

### FUNCTION ###

def operate(op) :
     res.set(eval(fv.get()+op+sv.get()))
     

###  Button ###

tkr.Button(app,text= '+' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command= lambda:operate('+')).place(x=30,y=150)
tkr.Button(app,text= '-' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command=lambda:operate('-')).place(x=90,y=150)
tkr.Button(app,text= '*' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command=lambda:operate('*')).place(x=150,y=150)
tkr.Button(app,text= '/' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command=lambda:operate('/')).place(x=210,y=150)
tkr.Button(app,text= '%' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command=lambda:operate('%')).place(x=270,y=150)
tkr.Button(app,text= '//' ,bg= 'black' ,fg='white',width =3,font=('Arial',15), command=lambda:operate('//')).place(x=330,y=150)

### RESULT LABEL ###

tkr.Label(app,text = 'RESULT',font=('Times',20,'bold')).place(x=150,y=250)
res = tkr.Variable(app)
res.set('0')
tkr.Label(app,textvariable= res,bg='black',fg='white', font=('Arial',15)).place(x=150,y=300)

app.mainloop()






