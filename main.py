from tkinter import * #Importando tkinter para GUI

#Definindo função para finalizar o aplicativo
def Finalizar():
    root.destroy() 
#Definindo função para converter de Km/h para M/s
def KmParaMs():
    KmEntry.place(rely=.6, relx=.3, anchor=CENTER)
    KmPorHora = KmEntry.get()
    def calcular():
        KmPorHora = float(KmEntry.get())
        resultado = round((KmPorHora/3.6), 2)
        resultado = str(resultado)
        ResultadoLabel = Label(root, text=resultado+" Km/h", fg="red", width=50)
        ResultadoLabel.place(rely=.8, relx=.3, anchor=CENTER)
    ConverterButton = Button(root, text="Calcular", command=calcular)
    ConverterButton.place(rely=.7, relx=.3, anchor=CENTER)
#Definindo função para converter M/s para Km/h
def MsParaKmh():
    MsEntry.place(rely=.6, relx=.7, anchor=CENTER)
    MporS = MsEntry.get()
    def calcular():
        MporS = float(MsEntry.get())
        resultado = round((MporS*3.6), 2)
        resultado = str(resultado)
        ResultadoLabel = Label(root, text=resultado+" m/s", fg="red", width=50)
        ResultadoLabel.place(rely=.8, relx=.7, anchor=CENTER)
    CalcularButton = Button(root, text="Calcular", command=calcular)
    CalcularButton.place(rely=.7, relx=.7, anchor=CENTER)

#Criando a raiz base da interface
root = Tk()
root.title(" Conversor de velocidades KM/H - M/S")
root.geometry("400x300")

#Criando os campos de input
KmEntry = Entry(root)
MsEntry = Entry(root)

#Criando os botões e atribuindo as funções para eles
KmParaMsButton = Button(root, text="Km/h para M/s", command=KmParaMs)
KmParaMsButton.place(rely=.5, relx=.3, anchor=CENTER)
MsParaKmhButton = Button(root, text="M/s para Km/h", command=MsParaKmh)
MsParaKmhButton.place(rely=.5, relx=.7, anchor=CENTER)
FinalizarButton = Button(root, text="Finalizar", command=Finalizar)
FinalizarButton.place(rely=.9, relx=.5, anchor=CENTER)

#Colocando a GUI em loop
root.mainloop()
