
from Tkinter import*
import random
import tkMessageBox
import PIL
from PIL import ImageTk,Image
import os
import os.path

class Sabatinator(object):

    def __init__(self):
  
        
        self.root = Tk()
        self.pts=0
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='/Users/mac/Desktop/SABATINATOR2.0/Resource/jardim.gif'))
        self.root.wm_title("SABATINATOR")
        img = ImageTk.PhotoImage(file="/Users/mac/Desktop/SABATINATOR2.0/Resource/jardim.png")
        self.canvas=Canvas(self.root,width=500, height=500,bg="white")
        self.canvas.pack()
        self.canvas.create_image(250,250,image=img)
        self.buttontext=StringVar()
        self.buttontext.set("jogar")
        self.b1=Button(self.root, textvariable=self.buttontext, command = self.start,anchor="n", width = 10,)
        self.b1_window=self.canvas.create_window(10,10,window=self.b1)
        self.b1.pack()


  
         

        self.root.mainloop()



    def start(self):
        self.text=Text(self.root)

        self.b1.pack_forget()
    
        self.text_label=Label(self.root,text="***SABATINATOR-JARDIM DE ALAH***")
        self.text_label.pack()
        self.question = Label(self.root,text="Digite o numero de rodadas: ")
        self.question.pack()
    
        self.question_entry=StringVar()
        self.b2=Entry(self.root,textvariable=self.question_entry)
        self.b2.pack()
    
        self.button_text=StringVar()
        self.button_text.set("Jogar")
        self.b3=Button(self.root,textvariable=self.button_text,command=self.makescreen)
        self.b3.pack()
    
        self.label= Label(self.root,text="")
        self.label.pack()
        
    def makescreen(self):

        self.canvas.pack_forget()
        self.text_label.pack_forget()
        self.question.pack_forget()
        self.b1.pack_forget()
        self.b2.pack_forget()
        self.b3.pack_forget()

        #self.frame= Frame(self.root,height=500,width=500,bg="black")
        #self.frame.pack()

        self.startgame()
        
        

    def startgame(self):
        self.list_verify=[]
        self.names={}
        self.keys=[]
        self.values=[]
        input_doc=open("/Users/mac/Desktop/SABATINATOR2.0/Resource/exalunos.txt")
        input_doc_2=open("/Users/mac/Desktop/SABATINATOR2.0/Resource/apelidos.txt")
        for line in input_doc:
            self.values.append(line)
        for line in input_doc_2:
            self.keys.append(line)
        self.names=dict(zip(self.keys,self.values))
        self.make_it_start()

    def make_it_start(self):
        numero=self.userinput()
        apelido=self.select_random_name()   
        apelido_low=apelido.lower().replace(" ","").rstrip()+".jpg"
        print(apelido_low)
        #creating the images randomly\
        pic=Image.open("/Users/mac/Desktop/SABATINATOR2.0/fotosJDA/"+apelido_low)
        pic=pic.resize((400,500),Image.ANTIALIAS)
        path = ImageTk.PhotoImage(pic)

        self.b8=Label(self.root,text="TOTAL: "+ str(self.pts))
        self.b8.pack()
        
        self.canvas2=Canvas(self.root,width=500, height=500,bg="white")
        self.canvas2.image=path
        self.canvas2.pack()
        self.my_img=self.canvas2.create_image(250,250,image=path)
        
        self.start_label= Label(self.root,text="Quem e o " + apelido.strip()+ " ?",bg="yellow")
        self.start_label.pack()
        self.verdadeiro=self.names[apelido]
        self.question_entry=StringVar()

        self.b5=Entry(self.root,textvariable=self.question_entry)
        self.b5.pack()
        self.b6=Button(self.root,text="Enter",command=self.verify_answer,width=10)
        self.b6.pack()
        self.b7=Button(self.root,text="Continuar",command=self.del_my_buttom,width=10)
        self.b7.pack()

        
             
    def verify_answer(self):

        nome=self.userinput().strip()
        string=nome.replace(" ","")
        string2=self.verdadeiro.replace(" ","")
        teste=string.lower()
        teste2=string2.lower()
        
         
        if teste.strip()==teste2.strip():
            tkMessageBox.showinfo( "Parabens", "Acertou!!")
            self.pts+=1
        else:
            tkMessageBox.showinfo( "CANA", "CANA!! O nome correto e: " + self.verdadeiro)
            self.pts-=1
           

        self.erase()        

        
    def userinput(self):
        variable=self.question_entry.get()
        return variable

    def erase (self):
         self.start_label.pack_forget()
         self.b5.pack_forget()                          
         self.b6.pack_forget()
         self.canvas2.delete(self.my_img)
         self.b8.pack_forget()
 
    def del_my_buttom(self):
        self.b7.pack_forget()
        self.canvas2.pack_forget()
        self.make_it_start()

    def select_random_name(self):
        nick=random.choice(self.names.keys())
        if nick not in self.list_verify:
            self.list_verify.append(nick)
            return nick
        else:
            self.select_random_name()

    def score(self):
        
        
      

 
                
                        


Sabatinator()       
    
