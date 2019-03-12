from tkinter import Tk,Canvas,Button,GROOVE,Label,FLAT,IntVar,Checkbutton,PhotoImage,Entry
#import images
import random
import time
import platform
import webbrowser
class mainmenu:
    def __init__(self):
        self.mode = mode()
    def create(self,update):
        if update:
            self.updateavailable()
        
        w=Tk()
        #w.iconbitmap('images/icon.xpm')
        w.title("TBM-Notentraining")
        w.geometry("1000x800")
        w.config(bg='white')
        def E():
            w.destroy()
            #mode = mode()
            self.mode.start()
        einfach=Button(w,
                    text="Spielen",
                    bg='green',
                    fg='black',
                    relief=GROOVE,
                    width=40,
                    font=10,
                    command=E)
        #schwer.place(x=300,y=430)
        einfach.place(x=300,y=350)
        #mittel.place(x=300,y=390)
        w.mainloop()
    def updateavailable(self):
        w=Tk()
        #w.iconbitmap('images/icon.xpm')
        w.title("TBM-Notentraining")
        w.geometry("1000x800")
        w.config(bg='white')
        def down():
            if platform.system()=="Windows":
                webbrowser.open_new_tab("https://github.com/StarMiner99/musik/raw/master/windows/musik-latest.exe")
            else:
                webbrowser.open_new_tab("https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/StarMiner99/musik/tree/master/source")
        text = Label(w,text="Es gibt ein neues Update!")
        download = Button(w, text="DOWNLOAD",bg="red",command=down)
        text.place(x=300,y=350)
        download.place(x=300,y=450)
        w.mainloop()
        
class mode:
    def __init__(self):
        self.answer = None
    def start(self):
        master=Tk()
        #master.iconbitmap('images/icon.xpm')
        master.title("TBM-Notentraining")
        w=Canvas(master,bg='white',width=1000, height=800)
        def ok():
            if violin.get() == 0 and bass.get() == 0:
                erlabel.place(x=300,y=450)
                w.update()
            else:
                master.destroy()
                self.rrun(violin.get(),bass.get(),kreuz.get(),b.get(),doppelb.get(),doppelkreuz.get())
            
        Ok=Button(w,
                  text="OK",
                  bg='blue',
                  fg='white',
                  relief=GROOVE,
                  width=40,
                  font=10,
                  command=ok)
        erlabel=Label(w,
                      text='Bitte kreuze Violinschluesel und/oder Bassschluesel an.',
                      bg='red',
                      fg='black',
                      relief=FLAT,
                      font=7)
        Ok.place(x=300,y=500)
        violin=IntVar()
        bass=IntVar()
        kreuz=IntVar()
        b=IntVar()
        doppelb = IntVar()
        doppelkreuz=IntVar()

        O1= Checkbutton(w,text="Violinschluessel: ",variable=violin,bg='green',fg='black',relief=GROOVE,font=10)
        O2= Checkbutton(w,text="Bassschluessel: ",variable=bass,bg='green',fg='black',relief=GROOVE,font=10)
        O3= Checkbutton(w,text="Kreuz: ",variable=kreuz,bg='green',fg='black',relief=GROOVE,font=10)
        O4=Checkbutton(w,text='"Be":',variable=b,bg='green',fg='black',relief=GROOVE,font=10)
        O5=Checkbutton(w,text="Doppelkreuz: ",variable=doppelkreuz,bg='green',fg='black',relief=GROOVE,font=10)
        O6=Checkbutton(w,text='"Doppelbe": ',variable=doppelb,bg='green',fg='black',relief=GROOVE,font=10)

        O6.place(x=300,y=350)
        O5.place(x=300,y=300)
        O4.place(x=300,y=250)
        O3.place(x=300,y=200)
        O2.place(x=300,y=150)
        O1.place(x=300,y=100)
        w.pack()
    def rrun(self,sopran, bass, kreuz,b,doppelb,doppelkreuz):
        master=Tk()
        #master.iconbitmap('images/icon.xpm')
        master.title("TBM-Notentraining")
        w=Canvas(master,bg='white',width=1000,height=800)
        def ok():
            master.destroy()
            self.run(sopran, bass, kreuz,b,doppelb,doppelkreuz)
        w.create_text(200,400,font=100,anchor='nw',fill='black',text="Regeln:\nGebe den gesuchten Notennamen unten in das Textfeld ein und druecke OK!")
        Ok=Button(w,
                  text="OK",
                  bg='blue',
                  fg='white',
                  relief=GROOVE,
                  width=40,
                  font=10,
                  command=ok)
        Ok.place(x=300,y=600)
        w.pack()
    def run(self,sopran, bass, kreuz,b,doppelb,doppelkreuz):
        
        master=Tk()
        #master.iconbitmap('images/icon.xpm')
        master.title("TBM-Notentraining")
        
        basslist=["E","F","G","A","H","c","d","e","f","g","a","h","c'"]
        sopranlist=["c'","d'","e'","f'","g'","a'","h'","c''","d''","e''","f''","g''","a''"]
        notecordlist=[[True,580],[False,548],[False,516],[False,484],[False,452],[False,420],[False,388],  [False,356],[False,324],[False,292],[False,260],[False,228],[True,196]]#64
        wrong = 0
        right = 0
        for x in range(0,10):
            self.answer = None
            w=Canvas(master,bg='white',width=1000,height=800)
            w.create_text(300,50,font=100,anchor='nw',fill='black',text="Gebe die Notennamen ein(vergesse die Striche nicht)")
            w.pack()
            schlist = []
            if sopran == 1:
                schlist.append(0)
            if bass == 1:
                schlist.append(1)
                
            d = random.choice(schlist)
            if d==0:
                be = False
                he = False

                dbe = False
                dhe = False
                    
                img = PhotoImage(file='images/sopran.png')
                note = PhotoImage(file='images/note.png')
                b = PhotoImage(file='images/b.png')
                h = PhotoImage(file='images/kreuz.png')
                blank = PhotoImage(file='images/blank.png')


                doppelbim = PhotoImage(file='images/doppelb.png')
                doppelkreuzim = PhotoImage(file='images/doppelkreuz.png')
                
                vzlist=[blank,h,b,doppelkreuzim,doppelbim]

                w.create_image(50,100,image=img,anchor='nw')
                w.update()
                
                no=random.randint(0,12)

                rightanswer=sopranlist[no]
                
                w.create_image(500,notecordlist[no][1],image=note,anchor='center')
                
                vorlist = [0]
                if kreuz == 1:
                    vorlist.append(1)
                if b == 1:
                    vorlist.append(2)
                if doppelkreuz == 1:
                    vorlist.append(3)
                if doppelb == 1:
                    vorlist.append(4)
                    
                bkt = random.choice(vorlist)
                
                if bkt == 1:
                    size=notecordlist[no][1]
                    he = True
                elif bkt == 2:
                    size=notecordlist[no][1]-30
                    be = True
                elif bkt == 3:
                    size=notecordlist[no][1]
                    dhe = True
                elif bkt == 4:
                    size=notecordlist[no][1]-30
                    dbe = True
                else:
                    size=notecordlist[no][1]
                w.create_image(400,size,image=vzlist[bkt], anchor='center')
                if notecordlist[no][0]:
                    w.create_line(430,notecordlist[no][1],570,notecordlist[no][1],width=10)
                w.update()


                if he:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    strrd = newstr+"is"+"'"*stripc
                    rightanswer = str(strrd)
                elif be:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    if newstr == 'a' or newstr == 'A' or newstr == 'e' or newstr == 'E':
                        strrd = newstr+'s'+"'"*stripc
                    elif newstr == 'h':
                        strrd = 'b'+ "'"*stripc
                    elif newstr == 'H':
                        strrd = 'B'+ "'"*stripc 
                    else:
                        strrd = newstr+"es"+"'"*stripc
                    rightanswer = str(strrd)
                
                elif dhe:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    strrd = newstr+"isis"+"'"*stripc
                    rightanswer = str(strrd)
                elif dbe:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    if newstr=='a' or newstr=='A':
                        strrd = newstr+'ses'+"'"*stripc
                    elif newstr=='e' or newstr=='E':
                        strrd = newstr+'ses'+"'"*stripc
                    else:
                        strrd = newstr+"eses"+"'"*stripc
                    rightanswer = str(strrd)


                
            if d==1:
                be = False
                he = False
                dbe = False
                dhe = False
                
                img = PhotoImage(file='images/bass.png')
                note = PhotoImage(file='images/note.png')
                b = PhotoImage(file='images/b.png')
                h = PhotoImage(file='images/kreuz.png')
                blank = PhotoImage(file='images/blank.png')
                doppelbim = PhotoImage(file='images/doppelb.png')
                doppelkreuzim = PhotoImage(file='images/doppelkreuz.png')
                
                vzlist=[blank,h,b,doppelkreuzim,doppelbim]
                w.create_image(50,100,image=img,anchor='nw')
                w.update()
                
                no=random.randint(0,12)
                rightanswer=basslist[no]
                
                w.create_image(500,notecordlist[no][1],image=note,anchor='center')


                vorlist = [0]
                if kreuz == 1:
                    vorlist.append(1)
                if b == 1:
                    vorlist.append(2)
                if doppelkreuz == 1:
                    vorlist.append(3)
                if doppelb == 1:
                    vorlist.append(4)
                
                bkt = random.choice(vorlist)
                
                if bkt == 1:
                    size=notecordlist[no][1]
                    he = True
                elif bkt == 2:
                    size=notecordlist[no][1]-30
                    be = True
                elif bkt == 3:
                    size=notecordlist[no][1]
                    dhe = True
                elif bkt == 4:
                    size=notecordlist[no][1]-30
                    dbe = True
                else:
                    size=notecordlist[no][1]
                w.create_image(400,size,image=vzlist[bkt], anchor='center')
                if notecordlist[no][0]:
                    w.create_line(430,notecordlist[no][1],570,notecordlist[no][1],width=10)
                w.update()

                
                if he:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    strrd = newstr+"is"+"'"*stripc
                    rightanswer = str(strrd)
                elif be:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    if newstr == 'a' or newstr == 'A' or newstr == 'e' or newstr == 'E':
                        strrd = newstr+'s'+"'"*stripc
                    elif newstr == 'h':
                        strrd = 'b'+ "'"*stripc
                    elif newstr == 'H':
                        strrd = 'B'+ "'"*stripc 
                    else:
                        strrd = newstr+"es"+"'"*stripc
                    rightanswer = str(strrd)
                elif dhe:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    strrd = newstr+"isis"+"'"*stripc
                    rightanswer = str(strrd)
                elif dbe:
                    stripc = rightanswer.count("'")
                    newstr=rightanswer.strip("'")
                    if newstr=='a' or newstr=='A':
                        strrd = newstr+'ses'+"'"*stripc
                    else:
                        strrd = newstr+"eses"+"'"*stripc
                    rightanswer = str(strrd)
            
            loop = 0
            self.user_Entry=Entry(w,bg='white',
                    fg="black",
                    relief=GROOVE,
                    highlightcolor="white",
                    highlightthickness=2,
                    highlightbackground='blue',
                    width=40,
                    font=10,
                    bd=5)
            best=Button(w,
                      text="OK",
                      bg='Blue',
                      fg="white",
                      relief=GROOVE,
                      font=10,
                      command=self.ok)
            master.bind('<Return>',self.ok)
##            print(best)

            best.place(x=700, y=600)
            self.user_Entry.place(x=250,y=600)
            self.user_Entry.focus()

            w.update()
            #print(rightanswer)
            #w.mainloop()
            while True:
                
                if self.answer == None:
                    pass
                
                elif self.answer == rightanswer:
                    self.answer = None
                    master.unbind('<Return>')
                    rightImg = PhotoImage(file="./images/right.png")
                    w.create_image(500,400,image=rightImg, anchor='center')
                    w.update()
                    time.sleep(4)
                    w.destroy()
                    right = right +1
                    break
                else:
                    self.answer = None
                    master.unbind('<Return>')
                    wrongImg = PhotoImage(file="./images/wrong.png")
                    rilab = Label(w,
                                text="Richtige Antwort: "+rightanswer,
                                bg = "#00ff15",
                                fg = "blue",
                                anchor="nw",
                                relief=FLAT,
                                font=10)
                    w.create_image(500,400,image=wrongImg, anchor='center')
                    rilab.place(x=400,y=520)
                    w.update()
                    time.sleep(4)
                    w.destroy()
                    wrong = wrong +1
                    break
                time.sleep(0.100)
                #print(self.answer)
                loop += 1
                w.update()
       
        master.config(bg='white')
        def menu():
            main = mainmenu()
            master.destroy()
            main.create(False)
        def close():
            master.destroy()


        labelw = Label(master,
                        text="Falsche Antworten: "+str(wrong),
                        bg = "red",
                        fg = "yellow",
                        anchor="center",
                        relief=FLAT,
                        font=10)
        labelr = Label(master,
                       text="Richtige Antworten: "+str(right),
                       bg="#00ff15",
                       fg="blue",
                       anchor="center",
                       relief=FLAT,
                       font=10)


        
        men=Button(master,
                  text="Menu",
                  bg='Blue',
                  fg="white",
                  anchor="center",
                  relief=GROOVE,
                  font=10,
                  command=menu)
        clo=Button(master,
                  text="Schliessen",
                  bg='Blue',
                  fg="white",
                  relief=GROOVE,
                  anchor="center",
                  font=10,
                  command=close)
        labelw.place(x=250,y=200)
        labelr.place(x=500,y=200)
        men.place(x=500 ,y=350)
        clo.place(x=500,y=450)
        master.update()
            
        
        
       # w.mainloop()
        master.mainloop()
    def ok(self,event=None):
        #global answer
        #answerlist = []
        self.answer = self.user_Entry.get()
        #answerlist.append(answer)
       # print(an)
       # print(user_Entry.get())
        
        
