import tkinter as tk 
from tkinter import ttk 


LARGEFONT =("Verdana", 25) 

class tkinterApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs) 
		
		# creating a container 
		container = tk.Frame(self) 
		container.pack() #side = "top", fill = "both" expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, Page1, Page2, Page3): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(StartPage) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 

# first window frame startpage 

class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2 
		label = tk.Label(self, text ="Gesundheitssystem von FMT", font = "Helvetica 20 bold") 
		label.grid(row = 1, padx = 10, pady = 10) 

		button1 = tk.Button(self, text ="Patient anlegen", bg = "light slate blue",
		width = 25, height = 2, command = lambda : controller.show_frame(Page1)) 
		button1.grid(row = 2, padx = 10, pady = 10) 

		## button to show frame 2 with text layout2 
		button2 = tk.Button(self, text ="Gesundheitsparameter anlegen", bg = "light slate blue",
		width = 25, height = 2, command = lambda : controller.show_frame(Page2)) 
		button2.grid(row = 3, padx = 10, pady = 10) 

		button3 = tk.Button(self, text ="Werte für Patienten erfassen", bg = "light slate blue",
		width = 25, height = 2, command = lambda : controller.show_frame(Page3))
		button3.grid(row = 4, padx = 10, pady = 10)

		


# second window frame page1 
class Page1(tk.Frame): 
	
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="Patient anlegen", font ="Helvetica 20 bold") 
		label.grid(row = 0, padx = 10, pady = 10, columnspan=4)

		lo1 = tk.Label(self, text="Geschlecht").grid(row=2, pady=8)

		var1 = tk.StringVar(self)
		var1.set("männlich") #falls nichts vorausgewählt sein soll .set(OptionList[0])

		opt = tk.OptionMenu(self, var1, "männlich", "weiblich").grid(row=2, column=1, pady=8)


		l1 = tk.Label(self, text="Vorname").grid(row=3, pady=8)
		l4 = tk.Label(self, text ="Nachname").grid(row=3, pady=8, padx=15, column=2)
		l2 = tk.Label(self, text="Gewicht").grid(row=4, pady=8)
		l3 = tk.Label(self, text="Größe").grid(row=5, pady=8)
	   
		e1 = tk.Entry(self).grid(row=3, column=1, pady=8)
		e4 = tk.Entry(self).grid(row=3, column=3, pady=8)
		e2 = tk.Entry(self).grid(row=4, column=1, pady=8)
		e3 = tk.Entry(self).grid(row=5, column=1, pady=8)

		b1 = tk.Button(self, text="Patient anlegen", width = 20, height = 2, bg="light slate blue").grid(row=6, column=1, pady=8)
		
		lo2=tk.Label(self, text="PatientenNr").grid(row=2, column=2, pady=8)
		PNr = [1,2,3]
		var2 = tk.StringVar(self)
		var2.set(PNr[1])

		opt = tk.OptionMenu(self,var2,*PNr).grid(row=2, column=3, pady=8)
		#opt.config(width, font)
		


		# button to show frame 2 with text 
		# layout2 
		button1 = ttk.Button(self, text ="zurück", 
							command = lambda : controller.show_frame(StartPage)) 
	
		# putting the button in its place 
		# by using grid 
		button1.grid(padx = 10, pady = 10) 

		# button to show frame 2 with text 
		# layout2 
		#button2 = ttk.Button(self, text ="Page 2", 
							#command = lambda : controller.show_frame(Page2)) 
	
		# putting the button in its place by 
		# using grid 
		#button2.grid(row = 2, column = 1, padx = 10, pady = 10) 




# third window frame page2 
class Page2(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="Gesundheitsparameter anlegen", font = "Helvetica 20 bold") 
		label.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan=4) 

		l1 = tk.Label(self, text="Bezeichnung").grid(row=2, column=1)
		l2 = tk.Label(self, text="GNr").grid(row=2, column=3)

		e1 = tk.Entry(self).grid(row=2, column=2)
		
		GNr = [1,2,3]
		var1 = tk.StringVar(self)
		var1.set(GNr[1])

		opt = tk.OptionMenu(self,var1,*GNr).grid(row=2, column=4, pady=8)
		
		b1 = tk.Button(self, text="Parameter anlegen", width = 20, height = 2, bg="light slate blue").grid(column=1,row=3, padx=15, pady=40)
		b2 = tk.Button(self, text="Parameter löschen",width = 20, height = 2, bg="light slate blue").grid(row=3, column=3, pady=40)
		# button to show frame 3 with text 
		# layout3 
		button2 = ttk.Button(self, text ="zurück", 
							command = lambda : controller.show_frame(StartPage)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(column=1 ,padx = 10, pady = 40) 

class Page3(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="Wert für Patienten eingeben", font = "Helvetica 20 bold") 
		label.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan=4) 

		l1 = tk.Label(self, text="Patienten ID").grid(row=2, column=1)
		l2 = tk.Label(self, text="Wert(Gld)").grid(row=2, column=3)
		l3 = tk.Label(self, text="Parameter(GNr)").grid(row=3, column=1)
		l4 = tk.Label(self, text="Datum").grid(row=4, column=1)
		l5 = tk.Label(self, text="Wert").grid(row=5, column=1)
		
	
		
		PaID = [1,2,3]
		var1 = tk.StringVar(self)
		var1.set(PaID[1])

		opt = tk.OptionMenu(self,var1,*PaID).grid(row=2, column=2, pady=8)
		#Wert unsicher ob liste oder rnd
		e1 = tk.Entry(self).grid(row=4, column=2)
		e2 = tk.Entry(self).grid(row=5, column=2)
		
		
		
		b1 = tk.Button(self, text="Wert speichern", width = 20, height = 2, bg="light slate blue").grid(column=1,row=6, padx=15, pady=40)
		b2 = tk.Button(self, text="Wert löschen",width = 20, height = 2, bg="light slate blue").grid(row=3, column=3, pady=40)

		# button to show frame 3 with text 
		# layout3 
		button2 = ttk.Button(self, text ="zurück", 
							command = lambda : controller.show_frame(StartPage)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(column=1 ,padx = 10, pady = 40) 
# Driver Code 
app = tkinterApp() 
app.mainloop() 
