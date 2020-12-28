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
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (StartPage, Page1, Page2): 

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
		label = ttk.Label(self, text ="Gesundheitssystem von FMT", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 1, column = 0, padx = 10, pady = 10) 

		button1 = tk.Button(self, text ="Hasmid anlegen", bg = "light slate blue",
		width = 25, height = 2, command = lambda : controller.show_frame(Page1)) 
	
		# putting the button in its place by 
		# using grid 
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
		label = ttk.Label(self, text ="Patient anlegen", font = LARGEFONT) 
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		lo1 = tk.Label(self, text="Geschlecht").grid(row=2)

		var1 = tk.StringVar(self)
		var1.set("männlich") #falls nichts vorausgewählt sein soll .set(OptionList[0])

		opt = tk.OptionMenu(self, var1, "männlich", "weiblich").grid(row=2, column=1)


		l1 = tk.Label(self, text="Vorname").grid(row=3, pady=8)
		l4 = tk.Label(self, text ="Nachname").grid(row=3, pady=8, column=2)
		l2 = tk.Label(self, text="Gewicht").grid(row=4, pady=8)
		l3 = tk.Label(self, text="Größe").grid(row=5, pady=8)
	   
		e1 = tk.Entry(self).grid(row=3, column=1, pady=8)
		e4 = tk.Entry(self).grid(row=3, column=3, pady=8)
		e2 = tk.Entry(self).grid(row=4, column=1, pady=8)
		e3 = tk.Entry(self).grid(row=5, column=1, pady=8)

		b1 = tk.Button(self, text="Patient anlegen", width = 25, height = 2, bg="light slate blue").grid(row=6, column=1, pady=8)
		


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
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT) 
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		# button to show frame 2 with text 
		# layout2 
		button1 = ttk.Button(self, text ="Page 1", 
							command = lambda : controller.show_frame(Page1)) 
	
		# putting the button in its place by 
		# using grid 
		button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

		# button to show frame 3 with text 
		# layout3 
		button2 = ttk.Button(self, text ="Startpage", 
							command = lambda : controller.show_frame(StartPage)) 
	
		# putting the button in its place by 
		# using grid 
		button2.grid(row = 2, column = 1, padx = 10, pady = 10) 


# Driver Code 
app = tkinterApp() 
app.mainloop() 
