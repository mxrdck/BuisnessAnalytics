#try:
    #import Tkinter as tk
#except:
    #import tkinter as tk
import tkinter as tk
from tkinter import ttk
from interface import Interface
from tkinter import messagebox as mbox  
from datetime import datetime

db = Interface()
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #self.frame=tk.Frame(bg="lavender", width=500, height=400)
        tk.Frame.configure(self, bg='azure')
        f2=tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f2.grid(row=2)
        label = tk.Label(self, text="Gesundheitssystem von FMT",
                         font="Helvetica 20 bold", bg="azure")
        label.grid(row=1, padx=10, pady=10)


        button1 = tk.Button(f2, text="Patient anlegen", bg="cornflower blue", activebackground="LightBlue1",
                            width=25, height=2, command=lambda: master.switch_frame(PageOne))
        button1.grid(row=2, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = tk.Button(f2, text="Gesundheitsparameter anlegen", bg="cornflower blue", activebackground="LightBlue1",
                            width=25, height=2, command=lambda: master.switch_frame(PageTwo))
        button2.grid(row=3, padx=10, pady=10)

        button3 = tk.Button(f2, text="Werte für Patienten erfassen", bg="cornflower blue", activebackground="LightBlue1",
                            width=25, height=2, command=lambda: master.switch_frame(PageThree))
        button3.grid(row=4, padx=10, pady=10)


class PageOne(tk.Frame):
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
            mbox.showerror('Value Error!','Please use\nStrings for first name and last name\nInteger for weight\nFloat for height')
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
                             command=lambda p=p: self.var2.set(p))

    def clear_all(self):
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')
        self.e3.delete(0,'end')
        self.e4.delete(0,'end')

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg="azure")

        f2 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f2.grid(row=2)
        f3 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f3.grid(row=3)


        label = tk.Label(self, text="Patient anlegen",
                         font="Helvetica 20 bold", bg="azure")
        label.grid(row=0, padx=10, pady=10)

        lo1 = tk.Label(f2, text="Geschlecht", bg="azure").grid(row=2, pady=8)

        self.var1 = tk.StringVar(self)
        # falls nichts vorausgewählt sein soll .set(OptionList[0])
        self.var1.set("männlich")

        opt = tk.OptionMenu(f2, self.var1, "männlich", "weiblich")
        opt["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        opt.config(bg="cornflower blue", activebackground="LightBlue1")
        opt.grid(row=2, column=1, pady=8)

        l1 = tk.Label(f2, text="Vorname", bg="azure").grid(row=3, pady=8)
        l4 = tk.Label(f2, text="Nachname", bg="azure").grid(row=3, pady=8, padx=15, column=2)
        l2 = tk.Label(f2, text="Gewicht", bg="azure").grid(row=4, pady=8)
        l3 = tk.Label(f2, text="Größe", bg="azure").grid(row=5, pady=8)

        self.e1 = tk.Entry(f2)
        self.e2 = tk.Entry(f2)
        self.e3 = tk.Entry(f2)
        self.e4 = tk.Entry(f2)

        self.e1.grid(row=3, column=1, pady=8)
        self.e4.grid(row=3, column=3, pady=8)
        self.e2.grid(row=4, column=1, pady=8)
        self.e3.grid(row=5, column=1, pady=8)

        b_add = tk.Button(f3, text="Patient anlegen", width=20, height=2,
                       bg="cornflower blue", activebackground="LightBlue1", command=self.b_add_patient)
        b_add.grid(row=1, column=2, pady=10, padx=10)

        b_delete = tk.Button(f3, text="Patient löschen", width=20, height=2,
                       bg="cornflower blue", activebackground="LightBlue1", command=self.b_del_patient)
        b_delete.grid(row=1, column=3, pady=10)

        lo2 = tk.Label(f2, text="PatientenNr", bg="azure").grid(row=2, column=2, pady=8)
        PNr = db.get_all_patients(only_ids=True)
        self.var2 = tk.StringVar(self)
        self.var2.set(PNr[0])

        self.opt2 = tk.OptionMenu(f2, self.var2, *PNr)
        self.opt2["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        self.opt2.config(bg="cornflower blue", activebackground="LightBlue1")
        self.opt2.grid(row=2, column=3, pady=8)

        # button to show frame 2 with text
        # layout2
        b_back = tk.Button(self, text="zurück", width=15, height=1, bg="cornflower blue", activebackground="LightBlue1",
                             command=lambda: master.switch_frame(StartPage))
        b_back.grid(pady=10, padx=15, row=4)
        #tk.Button(self, text="Go back to start page",
                  #command=lambda: master.switch_frame(StartPage)).grid()

class PageTwo(tk.Frame):

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
                             command=lambda p=p: self.var1.set(p))

    def clear_all(self):
        self.e1.delete(0,'end')

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg="azure")
        #tk.Frame.configure(self,bg='red')
        f2 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f2.grid(row=2)
        f3 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f3.grid(row=3)


        label = tk.Label(self, text="Gesundheitsparameter anlegen", font="Helvetica 20 bold", bg="azure")
        label.grid(row=0, padx=10, pady=10)

        l1 = tk.Label(f2, text="Bezeichnung", bg="azure").grid(row=2, column=1)
        l2 = tk.Label(f2, text="GNr", bg="azure").grid(row=2, column=3)

        self.e1 = tk.Entry(f2)
        self.e1.grid(row=2, column=2)

        GNr = db.get_all_params(only_ids=True)
        self.var1 = tk.StringVar(self)
        self.var1.set(GNr[0])

        self.opt = tk.OptionMenu(f2, self.var1, *GNr)
        self.opt["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        self.opt.config(bg="cornflower blue", activebackground="LightBlue1")
        self.opt.grid(row=2, column=4, pady=8)

        b1 = tk.Button(f3, text="Parameter anlegen", width=20, height=2,
                       bg="cornflower blue", activebackground="LightBlue1", command=self.b_add_param)
        b1.grid(column=2, row=1, padx=15, pady=10)

        b2 = tk.Button(f3, text="Parameter löschen", width=20, height=2,
                       bg="cornflower blue", activebackground="LightBlue1", command=self.b_del_param)
        b2.grid(row=1, column=3, pady=10)
        # button to show frame 3 with text
        # layout3
        b3 = tk.Button(self, text="zurück", width=15, height=1, bg="cornflower blue", activebackground="LightBlue1",
                             command=lambda: master.switch_frame(StartPage))
        b3.grid(pady=10, padx=15, row=4)


class PageThree(tk.Frame):

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
            hv_date = datetime.strptime(self.e1.get(),"%Y-%m-%d")
            hv_value = int(self.e2.get())
            

            ret = db.add_value_to_patient(patient_id, parameter_id, hv_date, hv_value)
            mbox.showinfo("Success", ret)
            self.update_dropdowns()
            self.clear_all()
        except ValueError:
            mbox.showerror('Value Error!','Please use\ncorrect date format for date\nInteger for Value')
        except Exception as e:
            mbox.showerror('Unknown Error', str(e))

    def update_dropdowns(self):
        menu = self.opt1["menu"]
        menu.delete(0, "end")

        for val in db.get_values_for_patient(self.var1.get()):
            menu.add_command(label=val, 
                             command=lambda val=val: self.var3.set(val))

    def clear_all(self):
        self.e1.delete(0,'end')
        self.e2.delete(0,'end')

    def populate_hv_option_menu(self, val):
        pat = int(val)

        menu = self.opt1["menu"]
        menu.delete(0, "end")

        for val in db.get_values_for_patient(pat):
            menu.add_command(label=val, 
                             command=lambda val=val: self.var3.set(val))

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='azure')
        f2 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f2.grid(row=2)
        f3 = tk.Frame(self, height=100, width=200, bg="azure", borderwidth=2)
        f3.grid(row=3)

        label = tk.Label(self, text="Wert für Patienten eingeben",
                         font="Helvetica 20 bold", bg="azure")
        label.grid(row=0, padx=10, pady=10)

        l1 = tk.Label(f2, text="Patienten ID", bg="azure").grid(row=2, column=1)
        l2 = tk.Label(f2, text="Wert(Gld)", bg="azure").grid(row=2, column=3)
        l3 = tk.Label(f2, text="Parameter(GNr)", bg="azure").grid(row=3, column=1)
        l4 = tk.Label(f2, text="Datum (YYYY-MM-DD)", bg="azure").grid(row=4, column=1, pady=10)
        l5 = tk.Label(f2, text="Wert", bg="azure").grid(row=5, column=1)

        paramID = db.get_all_params(only_ids=False)
        self.var2 = tk.StringVar(self)
        self.var2.set(paramID[0])

       
        self.PaID = db.get_all_patients(only_ids=True)
        self.var1 = tk.StringVar(self)
        self.var1.set(self.PaID[0])

        self.opt2 = tk.OptionMenu(f2, self.var1, *self.PaID, command=self.populate_hv_option_menu)
        self.opt2.grid(row=2, column=2, pady=8)
        self.opt2["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        self.opt2.config(bg="cornflower blue", activebackground="LightBlue1")

        self.opt0 = tk.OptionMenu(f2, self.var2, *paramID)
        self.opt0.grid(row=2, column=2, pady=8)
        self.opt0["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        self.opt0.config(bg="cornflower blue", activebackground="LightBlue1")
        self.opt0.grid(row=3, column=2, pady=8)

        hvs = db.get_values_for_patient(self.PaID[0])
        self.var3 = tk.StringVar(self)
        # falls nichts vorausgewählt sein soll .set(OptionList[0])
        self.var3.set(hvs[0])

        self.opt1 = tk.OptionMenu(f2, self.var3, *hvs)
        self.opt1.grid(
            row=2, column=4, pady=8)
        self.opt1["menu"].config(bg="cornflower blue", activebackground="LightBlue1", activeforeground="gray1")
        self.opt1.config(bg="cornflower blue", activebackground="LightBlue1")

        

        # Wert unsicher ob liste oder rnd
        self.e1 = tk.Entry(f2)
        self.e1.grid(row=4, column=2)
        self.e2 = tk.Entry(f2)
        self.e2.grid(row=5, column=2)

        b1 = tk.Button(f3, text="Wert speichern", width=20, height=2, bg="cornflower blue", 
                        command=self.b_add_val_to_patient, activebackground="LightBlue1")
        b1.grid(column=1, row=1, padx=15, pady=10)

        b2 = tk.Button(f3, text="Wert löschen", width=20, height=2, bg="cornflower blue", 
                        command=self.b_delete_val_from_patient, activebackground="LightBlue1")
        b2.grid(column=2, row=1, padx=15, pady=10)

        
        b3 = tk.Button(self, text="zurück", width=15, height=1, bg="cornflower blue", activebackground="LightBlue1",
                         command=lambda: master.switch_frame(StartPage))

        
        b3.grid(row=4, padx=10, pady=40)



if __name__ == "__main__":
    app = SampleApp()
    app.geometry('{}x{}'.format(800, 400))
    app.configure(bg="azure")
    app.mainloop()