#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Importamos la librería gráfica wxPython.
import wx
import time
import asyncio
import wx.adv

print("wx")
for x in dir(wx):
  if x.startswith('EVT_'):
      print(x)
print("wx.adv")
for x in dir(wx.adv):
  if x.startswith('EVT_'):
      print(x)
# Nuestra clase que hereda de wx.Frame y que representará la ventana.
class MyFrame(wx.Frame):
    l = 0
    # Función donde se inicializa, donde se crean o se declaran los
    # miembros (variables) de la clase.
    def __init__(self, parent, id, title):
        # Inicializamos la clase wx.Frame de la cual heredará esta.
        wx.Frame.__init__(self, parent, id, title)
        # Creamos una lista de elementos a mostrar.
        self.listbox_boleta = wx.ListBox(self, -1)#Boleta
        self.listbox_productos = wx.ListBox(self, -1)#Productos
        self.listbox_pedidos = wx.ListBox(self, -1)#Pedidos
        # Creamos los botones.
        self.button_1 = wx.Button(self, -1, u"Click aquí", size=(20,20))
        self.button_2 = wx.Button(self, -1, u"Cerrar")
        self.btn_0 = wx.Button(self, -1, u"")#wx.Bitmap('texit.png')
        self.btn_1 = wx.Button(self, -1, u"7")
        self.btn_2 = wx.Button(self, -1, u"8")
        self.btn_3 = wx.Button(self, -1, u"9")
        self.btn_4 = wx.Button(self, -1, u"")
        self.btn_5 = wx.Button(self, -1, u"")
        self.btn_6 = wx.Button(self, -1, u"")
        self.btn_7 = wx.Button(self, -1, u"4")
        self.btn_8 = wx.Button(self, -1, u"5")
        self.btn_9 = wx.Button(self, -1, u"6") 
        self.btn_10 = wx.Button(self, -1, u"")
        self.btn_11 = wx.Button(self, -1, u"")
        self.btn_12 = wx.Button(self, -1, u"")
        self.btn_13 = wx.Button(self, -1, u"1")
        self.btn_14 = wx.Button(self, -1, u"2")
        self.btn_15 = wx.Button(self, -1, u"3")
        self.btn_16 = wx.Button(self, -1, u"")
        self.btn_17 = wx.Button(self, -1, u"")
        self.btn_18 = wx.Button(self, -1, u"")
        self.btn_19 = wx.Button(self, -1, u".")
        self.btn_20 = wx.Button(self, -1, u"0")
        self.btn_21 = wx.Button(self, -1, u"C")
        self.btn_22 = wx.Button(self, -1, u"")
        self.btn_23 = wx.Button(self, -1, u"")
        #Creamos la hora
        self.st_hora = wx.StaticText(self,label="00:00")
        # Llamamos otros métodos que creamos para la inicialización.
        self.__do_layout()
        self.__set_properties()
        self.__set_event()
        #Crea el evento tiempo usando wx.Timer como accion del evento EVT_TIMER
        self.Bind(wx.EVT_TIMER, self.Hora)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)

     

    # Esta función ordenará los elementos de nuestra ventana (bloques principales),
    # mediante el uso de sizers.
    def __do_layout(self):
        btn_grid = wx.GridSizer(4, 6, 5, 2)
        btn_grid.AddMany([
                (self.btn_0, 0, wx.EXPAND),
                (self.btn_1, 0, wx.EXPAND),
                (self.btn_2, 0, wx.EXPAND),
                (self.btn_3, 0, wx.EXPAND),
                (self.btn_4, 0, wx.EXPAND),
                (self.btn_5, 0, wx.EXPAND),
                (self.btn_6, 0, wx.EXPAND),
                (self.btn_7, 0, wx.EXPAND),
                (self.btn_8, 0, wx.EXPAND),
                (self.btn_9, 0, wx.EXPAND),
                (self.btn_10, 0, wx.EXPAND),
                (self.btn_11, 0, wx.EXPAND),
                (self.btn_12, 0, wx.EXPAND),
                (self.btn_13, 0, wx.EXPAND),
                (self.btn_14, 0, wx.EXPAND),
                (self.btn_15, 0, wx.EXPAND),
                (self.btn_16, 0, wx.EXPAND),
                (self.btn_17, 0, wx.EXPAND),
                (self.btn_18, 0, wx.EXPAND),
                (self.btn_19, 0, wx.EXPAND),
                (self.btn_20, 0, wx.EXPAND),
                (self.btn_21, 0, wx.EXPAND),
                (self.btn_22, 0, wx.EXPAND),
                (self.btn_23, 0, wx.EXPAND)])

        # Creamos los sizers de tipo BoxSizer donde los elementos se
        # irán incluyendo de manera vertical y horizontalmente.
        sizer_0 = wx.BoxSizer(wx.VERTICAL) #Layout principal
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)#Layout columna de sizer_3 y productos
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)#Layout Boton 1 y boton 2
        sizer_3 = wx.BoxSizer(wx.VERTICAL) #Layout Calculadora y Boleta
        # Incluímos los elementos en los sizers mediante su método Add,
        # con los siguientes argumentos:
        #    1. Nombre del elemento a agregar (variable)
        #    2. Proporción que ocupará el elemento dentro del sizer.
        #    3. Margenes que tendrá el elemento: wx.ALL = Todos. wx.EXPAND
        #    4. Espacio de los margenes.
        #btn_layout
        sizer_3.Add(self.listbox_boleta, 1, wx.EXPAND|wx.ALL, 5)
        sizer_3.Add(btn_grid, 0, wx.EXPAND|wx.ALL, 5)
        sizer_1.Add(sizer_3, 1, wx.EXPAND|wx.ALL, 5)
        sizer_1.Add(self.listbox_productos, 2, wx.EXPAND|wx.ALL, 5)
        sizer_2.Add(self.listbox_pedidos, 2, wx.EXPAND|wx.ALL, 5)
        sizer_2.Add(self.button_1, 0, wx.ALL, 5)
        sizer_2.Add(self.button_2, 0, wx.ALL, 5)
        sizer_2.Add(self.st_hora, 0, wx.ALL, 5)
        
        sizer_0.Add(sizer_2, 0, wx.EXPAND|wx.ALL, 5)
        sizer_0.Add(sizer_1, 1, wx.EXPAND|wx.ALL, 5)
        # Establecemos el sizer principal a la ventana.
        self.SetSizer(sizer_0)
        self.Layout()
     
    # Esta función establecerá las propiedades a los elementos.
    def __set_properties(self):
		#Configurar la ventana principal, tamaño y titulo de la ventana
		#window = wx.Frame(None,title="TPV", size=wx.GetDisplaySize(), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
 
        # Tamaño de la ventana.
        self.SetSize( wx.GetDisplaySize() )
        # Color de fondo de uno de los miembros (elementos)
        self.button_1.SetBackgroundColour( wx.Colour(200, 255, 100) )
        # Fuente del texto del listbox_boleta.
        self.listbox_boleta.SetFont( wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.NORMAL) )
 
    # Esta función establecerá los diferentes eventos a los elementos.
    def __set_event(self):
        self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button_2)
        
    # Función al precionar el button_1
    def OnButton1(self, event):
        # Agregamos un texto al listbox_boleta.
        self.l = self.l + 1
        self.listbox_boleta.Append(u"sa" + str(self.l))
        event.Skip()

    #Hora del sistema
    def Hora(self,event):
        localtime = str(time.strftime('%H:%M:%S'))
        self.st_hora.Label=str(localtime)

    # Función al preccionar el button_2
    def OnButton2(self, event):
        self.Close()
        event.Skip()
     
     

# Instaciamos la clase App donde se ejecutará nuestra ventana.
app = wx.App(0)
# Instanciamos la clase MyFrame que representa nuestra ventana.
frame = MyFrame(None, -1, "TPV")
# Mostramos la ventana.
frame.Show()
# Esto crea una especie de bucle mientras nuestra ventana este abierta.
app.MainLoop()