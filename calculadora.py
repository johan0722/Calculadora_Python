from tkinter import Button,Tk,Text,END,re

class Interfaz:
    def __init__(self, ventana):
        #Inicializar venta con un titulo
        self.ventana= ventana
        self.ventana.title("Calculadora")

        #Agregamos la caja de texto para ver los resultados
        self.pantalla = Text(ventana,state="disabled", width=40,height=3,background="orchid",foreground="white", font=("Helvatica", 15))

        #Ubicar a pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operacion mostrada como una string vacia 
        self.operacion=""

        #Agregar botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton5=self.crearBoton(u"\u232B",escribir=False)
        boton4=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)

        #Ubicar botones con el grid
        botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador=0
        
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el ultimo boton al final 
        botones[16].grid(row=5,column=0,columnspan=4)
        return

    #Crea un boton mostrando el valor predeterminado
    def crearBoton(self,valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho,height=alto,font=("Helvatica", 15),command=lambda:self.click(valor,escribir))

    #Controla el evento dsiparado alhacer click en el boton
    def click(self, texto, escribir):
        #Si el parametro escribir es true, entonces el parametro texto debe mostrarse en pantalla
        if not escribir:
            #solo calcular si hay una operacion que debe ser evaluada y si el ususario presiono =
            if texto=="=" and self.operacion!="":
                #remplazar el valor unicode de la division por el operador de division de python /
                self.operacion=re.sub(u"\u00f7", "/", self.operacion)
                resultado = str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #si se presiono el boton de borrado, limpiar la pantalla
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
            #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return
    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

        
    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state="disabled")
        return

ventana_principal = Tk()
calculadora =  Interfaz(ventana_principal)
ventana_principal.mainloop()
