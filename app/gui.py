import tkinter as tk
from tkinter import ttk
from interface import Interface
from tkinter import messagebox as mbox  

db = Interface()
LARGEFONT = ("Verdana", 25)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack()  # side = "top", fill = "both" expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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

            frame.grid(row=0, column=0, sticky="nsew")

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
        label = tk.Label(self, text="Gesundheitssystem von FMT",
                         font="Helvetica 20 bold")
        label.grid(row=1, padx=10, pady=10)

        button1 = tk.Button(self, text="Patient anlegen", bg="light slate blue",
                            width=25, height=2, command=lambda: controller.show_frame(Page1))
        button1.grid(row=2, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = tk.Button(self, text="Gesundheitsparameter anlegen", bg="light slate blue",
                            width=25, height=2, command=lambda: controller.show_frame(Page2))
        button2.grid(row=3, padx=10, pady=10)

        button3 = tk.Button(self, text="Werte für Patienten erfassen", bg="light slate blue",
                            width=25, height=2, command=lambda: controller.show_frame(Page3))
        button3.grid(row=4, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def b_add_patient(self):
        try:
            first_name = self.e1.get()
            last_name = self.e4.get()
            weight = int(self.e2.get())
            height = float(self.e3.get())
            sex = self.var1.get()
            ret = db.add_patient(first_name,last_name,height,weight,sex)
            mbox.showinfo('Success', ret)
            #update all dropdowns afterwards
            self.update_patients_dropdown()
            self.clear_all()
        except ValueError:
            mbox.showerror('Value Error!','Please use Strings for first and last name and sex, integer for weight and float for height')
        except Exception as e:
            mbox.showerror('Unknown Error', str(e))


    def b_del_patient(self):
        try:
            p_id = int(self.var2.get())
            ret = db.delete_patient(p_id)
            mbox.showinfo('Success', ret)
            self.update_patients_dropdown()
        except Exception as e:
            mbox.showerror('Error',str(e))

    def update_patients_dropdown(self):
        menu = self.opt2["menu"]
        menu.delete(0, "end")

        for p in db.get_all_patients(only_ids=True):
            menu.add_command(label=p, 
                             command=lambda value=p: self.var2.set(p))

    def clear_all(self):
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')
        self.e3.delete(0,'end')
        self.e4.delete(0,'end')

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Patient anlegen",
                         font="Helvetica 20 bold")
        label.grid(row=0, padx=10, pady=10, columnspan=4)

        lo1 = tk.Label(self, text="Geschlecht").grid(row=2, pady=8)

        self.var1 = tk.StringVar(self)
        # falls nichts vorausgewählt sein soll .set(OptionList[0])
        self.var1.set("männlich")

        opt = tk.OptionMenu(self, self.var1, "männlich", "weiblich").grid(
            row=2, column=1, pady=8)

        l1 = tk.Label(self, text="Vorname").grid(row=3, pady=8)
        l4 = tk.Label(self, text="Nachname").grid(
            row=3, pady=8, padx=15, column=2)
        l2 = tk.Label(self, text="Gewicht").grid(row=4, pady=8)
        l3 = tk.Label(self, text="Größe").grid(row=5, pady=8)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)

        self.e1.grid(row=3, column=1, pady=8)
        self.e4.grid(row=3, column=3, pady=8)
        self.e2.grid(row=4, column=1, pady=8)
        self.e3.grid(row=5, column=1, pady=8)

        b_add = tk.Button(self, text="Patient anlegen", width=20, height=2,
                       bg="light slate blue", command=self.b_add_patient).grid(row=6, column=1, pady=8)

        b_delete = tk.Button(self, text="Patient löschen", width=20, height=2,
                       bg="light slate blue", command=self.b_del_patient).grid(row=6, column=2, pady=40)

        lo2 = tk.Label(self, text="PatientenNr").grid(row=2, column=2, pady=8)
        PNr = db.get_all_patients(only_ids=True)
        self.var2 = tk.StringVar(self)
        self.var2.set(PNr[0])

        self.opt2 = tk.OptionMenu(self, self.var2, *PNr)
        self.opt2.grid(row=2, column=3, pady=8)
        # opt.config(width, font)

        # button to show frame 2 with text
        # layout2
        b_back = ttk.Button(self, text="zurück",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        b_back.grid(padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        # button2 = ttk.Button(self, text ="Page 2",
        # command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# third window frame page2
class Page2(tk.Frame):

    def b_add_param(self):

        try:
            denotation = self.e1.get()
            ret = db.add_health_param(denotation)
            mbox.showinfo('Success', ret)
            self.update_dropdowns()
            self.clear_all()
        except Exception as e:
            mbox.showerror('Error', str(e))

    
    def b_del_param(self):

        try:
            param = int(self.var1.get())
            ret = db.delete_health_param(param)
            mbox.showinfo('Success', ret)
            self.update_dropdowns()
        except Exception as e:
            mbox.showerror('Error', str(e))


    def update_dropdowns(self):
        menu = self.opt["menu"]
        menu.delete(0, "end")

        for p in db.get_all_params(only_ids=True):
            menu.add_command(label=p, 
                             command=lambda value=p: self.var1.set(p))

    def clear_all(self):
        self.e1.delete(0,'end')



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Gesundheitsparameter anlegen", font="Helvetica 20 bold")
        label.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

        l1 = tk.Label(self, text="Bezeichnung").grid(row=2, column=1)
        l2 = tk.Label(self, text="GNr").grid(row=2, column=3)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=2)

        GNr = db.get_all_params(only_ids=True)
        self.var1 = tk.StringVar(self)
        self.var1.set(GNr[0])

        self.opt = tk.OptionMenu(self, self.var1, *GNr)
        self.opt.grid(row=2, column=4, pady=8)

        b1 = tk.Button(self, text="Parameter anlegen", width=20, height=2,
                       bg="light slate blue", command=self.b_add_param).grid(column=1, row=3, padx=15, pady=40)
        b2 = tk.Button(self, text="Parameter löschen", width=20, height=2,
                       bg="light slate blue", command=self.b_del_param).grid(row=3, column=3, pady=40)
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="zurück",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(column=1, padx=10, pady=40)


class Page3(tk.Frame):

    def b_delete_val_from_patient(self):
        try:
            val = self.var3.get().split(' ')[0].replace(':','')
            val = int(val)
            ret = db.remove_value_from_patient(val)
            mbox.showinfo('Success', str(ret))
            self.update_dropdowns()
        except Exception as e:
            mbox.showerror('Error', str(e))

    def b_add_val_to_patient(self):
        try:

            patient_id = int(self.var1.get())
            parameter_id = int(self.var2.get().split(' ')[0].replace(':',''))
            hv_date = self.e1.get()
            hv_value = self.e2.get()
            

            ret = db.add_value_to_patient(patient_id, parameter_id, hv_date, hv_value)
            mbox.showinfo("Success", ret)
            self.update_dropdowns()
        except Exception as e:
            mbox.showerror("Error", str(e))

    def update_dropdowns(self):
        menu = self.opt1["menu"]
        menu.delete(0, "end")

        for val in db.get_values_for_patient(self.var1.get()):
            menu.add_command(label=val, 
                             command=lambda value=val: self.var3.set(val))

    def clear_all(self):
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')

    def populate_hv_option_menu(self, val):
        pat = int(val)

        menu = self.opt1["menu"]
        menu.delete(0, "end")

        for val in db.get_values_for_patient(pat):
            menu.add_command(label=val, 
                             command=lambda value=val: self.var3.set(val))

                             

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wert für Patienten eingeben",
                         font="Helvetica 20 bold")
        label.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

        l1 = tk.Label(self, text="Patienten ID").grid(row=2, column=1)
        l2 = tk.Label(self, text="Wert(Gld)").grid(row=2, column=3)
        l3 = tk.Label(self, text="Parameter(GNr)").grid(row=3, column=1)
        l4 = tk.Label(self, text="Datum (YYYY-MM-DD)").grid(row=4, column=1, pady=10)
        l5 = tk.Label(self, text="Wert").grid(row=5, column=1, pady=10)


        paramID = db.get_all_params(only_ids=False)
        self.var2 = tk.StringVar(self)
        # falls nichts vorausgewählt sein soll .set(OptionList[0])
        self.var2.set(paramID[0])

        self.opt0 = tk.OptionMenu(self, self.var2, *paramID)
        self.opt0.grid(
            row=3, column=2, pady=8)

        


        self.PaID = db.get_all_patients(only_ids=True)
        self.var1 = tk.StringVar(self)
        self.var1.set(self.PaID[0])

        hvs = db.get_values_for_patient(self.PaID[0])
        self.var3 = tk.StringVar(self)
        # falls nichts vorausgewählt sein soll .set(OptionList[0])
        self.var3.set(hvs[0])

        self.opt1 = tk.OptionMenu(self, self.var3, *hvs)
        self.opt1.grid(
            row=2, column=4, pady=8)

        self.opt2 = tk.OptionMenu(self, self.var1, *self.PaID, command=self.populate_hv_option_menu)
        self.opt2.grid(row=2, column=2, pady=8)
        # Wert unsicher ob liste oder rnd
        self.e1 = tk.Entry(self)
        self.e1.grid(row=4, column=2)
        self.e2 = tk.Entry(self)
        self.e2.grid(row=5, column=2)

        b1 = tk.Button(self, text="Wert speichern", width=20, height=2,
                       bg="light slate blue", command=self.b_add_val_to_patient).grid(column=1, row=6, padx=15, pady=40)
        b2 = tk.Button(self, text="Wert löschen", width=20, height=2,
                       bg="light slate blue", command=self.b_delete_val_from_patient).grid(row=6, column=3, pady=40)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="zurück",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(column=1, padx=10, pady=40)


# Driver Code
app = tkinterApp()
app.mainloop()
