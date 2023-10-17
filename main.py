import tkinter as tk

class tela():
    def __init__(self):
        self.tela=tk.Tk()
        self.tela.title("Calculator")
        self.tela.resizable(width=False,height=False)

        self.Res=""
        self.Valores=0
        self.WIDTH=10
        self.HEIGHT=3
        self.FONTE="Arial 14 bold"

        self.Resultado=tk.Label(self.tela)

        def atualizar(auxBt):#atualização do Display
            self.Res+=auxBt
            print(self.Res)
            self.auxResultado.set(self.Res)

        def calcular(self):
            Digitos=[]
            Oper=[]
            Num=[]
            for i in self.Res:
                if i.isdigit():
                    Digitos.append(i)
                else:
                    Oper.append(i)
                    Digitos.append("*")
            print(Oper)
            print(Digitos)
            NumStr="".join(Digitos)
            NumStr=NumStr.split("*")
            #for j in NumStr:
              #  Num.append(j)
            print(NumStr)
            #print(Num)

            if Oper[0]=="+":
                ResTotal=int(NumStr[0])+int(NumStr[1])

            if Oper[0]=="-":
                ResTotal=int(NumStr[0])-int(NumStr[1])
            
            if Oper[0]=="X":
                ResTotal=int(NumStr[0])*int(NumStr[1])

            if Oper[0]=="÷":
                ResTotal=int(NumStr[0])/int(NumStr[1])

            self.auxResultado.set(str(ResTotal))


    #label resultado -  display da calculadora
        self.auxResultado=tk.StringVar()
        self.auxResultado.set("---")
        self.lbResultado=tk.Label(self.tela,textvariable=self.auxResultado, font=self.FONTE)
        self.lbResultado.grid(row=0,columnspan=3)

    #button 0
        self.auxBt0=tk.StringVar()
        self.auxBt0.set(0)
        self.bt0=tk.Button(self.tela,textvariable=self.auxBt0,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt0.get()))
        self.bt0.grid(row=4,column=0,padx=2,pady=2)

    #button 1
        self.auxBt1=tk.StringVar()
        self.auxBt1.set(1)
        self.bt1=tk.Button(self.tela,textvariable=self.auxBt1,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt1.get()))
        self.bt1.grid(row=1,column=0,padx=2,pady=2)

    #button 2
        self.auxBt2=tk.StringVar()
        self.auxBt2.set(2)
        self.bt2=tk.Button(self.tela,textvariable=self.auxBt2,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt2.get()))
        self.bt2.grid(row=1,column=1,padx=2,pady=2)
    
    #button 3
        self.auxBt3=tk.StringVar()
        self.auxBt3.set(3)
        self.bt3=tk.Button(self.tela,textvariable=self.auxBt3,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt3.get()))
        self.bt3.grid(row=1,column=2,padx=2,pady=2)

    #button 4
        self.auxBt4=tk.StringVar()
        self.auxBt4.set(4)
        self.bt4=tk.Button(self.tela,textvariable=self.auxBt4,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt4.get()))
        self.bt4.grid(row=2,column=0,padx=2,pady=2)

    #button 5
        self.auxBt5=tk.StringVar()
        self.auxBt5.set(5)
        self.bt5=tk.Button(self.tela,textvariable=self.auxBt5,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt5.get()))
        self.bt5.grid(row=2,column=1,padx=2,pady=2)

    #button 6
        self.auxBt6=tk.StringVar()
        self.auxBt6.set(6)
        self.bt6=tk.Button(self.tela,textvariable=self.auxBt6,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt6.get()))
        self.bt6.grid(row=2,column=2,padx=2,pady=2)

    #button 7
        self.auxBt7=tk.StringVar()
        self.auxBt7.set(7)
        self.bt7=tk.Button(self.tela,textvariable=self.auxBt7,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt7.get()))
        self.bt7.grid(row=3,column=0,padx=2,pady=2)

    #button 8
        self.auxBt8=tk.StringVar()
        self.auxBt8.set(8)
        self.bt8=tk.Button(self.tela,textvariable=self.auxBt8,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt8.get()))
        self.bt8.grid(row=3,column=1,padx=2,pady=2)

    #button 9
        self.auxBt9=tk.StringVar()
        self.auxBt9.set(9)
        self.bt9=tk.Button(self.tela,textvariable=self.auxBt9,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command=lambda:atualizar(self.auxBt9.get()))
        self.bt9.grid(row=3,column=2,padx=2,pady=2)

    #button +
        self.auxBtMais=tk.StringVar()
        self.auxBtMais.set("+")
        self.btMais=tk.Button(self.tela,textvariable=self.auxBtMais,width=self.WIDTH,height=self.HEIGHT, bg="Light gray",font=self.FONTE,command=lambda:atualizar(self.auxBtMais.get()))
        self.btMais.grid(row=1,column=3,padx=2,pady=2)

    #button -
        self.auxBtMenos=tk.StringVar()
        self.auxBtMenos.set("-")
        self.btMenos=tk.Button(self.tela,textvariable=self.auxBtMenos,width=self.WIDTH,height=self.HEIGHT, bg="Light gray",font=self.FONTE,command=lambda:atualizar(self.auxBtMenos.get()))
        self.btMenos.grid(row=2,column=3,padx=2,pady=2)

    #button X
        self.auxBtMult=tk.StringVar()
        self.auxBtMult.set("X")
        self.btMult=tk.Button(self.tela,textvariable=self.auxBtMult,width=self.WIDTH,height=self.HEIGHT, bg="Light gray",font=self.FONTE,command=lambda:atualizar(self.auxBtMult.get()))
        self.btMult.grid(row=3,column=3,padx=2,pady=2)

    #button /
        self.auxBtDiv=tk.StringVar()
        self.auxBtDiv.set("÷")
        self.btDiv=tk.Button(self.tela,textvariable=self.auxBtDiv,width=self.WIDTH,height=self.HEIGHT, bg="Light gray",font=self.FONTE,command=lambda:atualizar(self.auxBtDiv.get()))
        self.btDiv.grid(row=4,column=3,padx=2,pady=2)

    #button =
        self.auxBtIgual=tk.StringVar()
        self.auxBtIgual.set("=")
        self.btIgual=tk.Button(self.tela,textvariable=self.auxBtIgual,width=self.WIDTH,height=self.HEIGHT, bg="gray",font=self.FONTE,command=lambda : calcular(self))
        self.btIgual.grid(row=4,column=2,padx=2,pady=2)

    #button Ponto
        self.auxBtPonto=tk.StringVar()
        self.auxBtPonto.set(".")
        self.btPonto=tk.Button(self.tela,textvariable=self.auxBtPonto,width=self.WIDTH,height=self.HEIGHT,font=self.FONTE,command="none")
        self.btPonto.grid(row=4,column=1,padx=2,pady=2)

        self.tela.mainloop()

tela()