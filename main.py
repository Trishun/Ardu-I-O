import ArduinoSerial
from Tkinter import *
import time
# zrobic z 3 suwakami na kolor diody
# zrobic odstepy pomiedzy guzikami

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        root.title("Arduino Interface")
        self.entryNum = 0
        self.scaleNum = 0
        self.sinusNum = 0
        self.odczytPinNum = 0
        self.frameF7 = 0
        self.sinButtonRed = 0
        self.sinButtonGreen = 0
        self.sinButtonBlue = 0
        self.AS = ArduinoSerial.ArduinoSerial(3)


    def get_scale(self,event):
        #### 3 wartości suwaków ####
        scaleR = self.scaleR.get()
        scaleG = self.scaleG.get()
        scaleB = self.scaleB.get()
        #### tu dajesz kod ###
        self.AS.led('RED %i' %(scaleR))
        self.AS.led('GREEN %i' %(scaleG))
        self.AS.led('BLUE %i' %(scaleB))



        ######################
##        print scaleR,scaleG,scaleB


    def dioda_rgb(self):
        #### po nacisnieciu guzika zmienia się kolor przycisku ####
        """ Zmiana 3 kolorów diody"""
        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"

        if self.bfunkcja1["fg"] == "black":
            ### Po nacisnieciu guzika który jest czarny zmiania kolor napisu na czerwony ###
            self.bfunkcja1["fg"] = "red"
            #### tu dajesz kod ###
            self.AS.led('RED ON')




            ######################
        elif self.bfunkcja1["fg"] == "red":
            ### Po nacisnieciu guzika który jest czerwony zmiania kolor napisu na zielony ###
            self.bfunkcja1["fg"] = "green"
            #### tu dajesz kod ###
            self.AS.led('GREEN ON')




            ######################

        elif self.bfunkcja1["fg"] == "green":
            ### Po nacisnieciu guzika który jest zielony zmiania kolor napisu na niebieski ###

            self.bfunkcja1["fg"] = "blue"
            #### tu dajesz kod ###
            self.AS.led('BLUE ON')



            ######################

        elif self.bfunkcja1["fg"] == "blue":
            ### Po nacisnieciu guzika który jest niebieski zmiania kolor napisu na czarny ###

            self.bfunkcja1["fg"] = "black"
            #### tu dajesz kod ###
            self.AS.led('BLUE OFF')



            ######################



    def entryget(self):
        # funkcja odnosi sie do guzika "Wypisz numer pinu" i działa
        # po nacisnieciu enter. zwraca wpisaną wartość
        #### tu dajesz kod ###

        self.AS.write('TOGGLE %s' %(self.entry1.get()))


        ######################
    def entry2get(self):
        #odnosi sie do guzka "odczyt z pinu" i dizała
        # po nacisnieciu enter. zwraca wpisaną wartość
        if self.frameF7 >0:
            self.f7.pack_forget()
            self.frameF7 = 0

        self.f7 = Frame(self.f6, height=10, width=32,pady=30)
        self.f7.pack()
        self.frameF7 +=1

        self.labelentry2 = Label(self.f7,height=1,text=self.AS.read(self.entry2.get()) )
        self.labelentry2.pack()
        #### tu dajesz kod ###

##        value = self.AS.read(self.entry2.get())

        ######################

    ####################################################################

    def pol_roz(self):
        # działa po naciśnieciu guzika "Połącz/Rozłącz"
        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#0b0"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"
        #### tu dajesz kod ###
        self.AS.toogle



        ######################


    def syn_czas(self):
        # działa po naciśnieciu guzika "synchronizacja czasu"

        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#0b0"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"
        self.AS._set_datetime

    def sinus_red(self):
        # działa po naciśnięciu "Dioda sinus" a potem guzika "red"
        #### tu dajesz kod ###
        if self.sinButtonRed == 0:
            #włączenie sinusa
            self.sinButtonRed += 1
            print "on"
            self.AS.led('RED SIN')
        else:
            #wyłączenie sinusa
            self.sinButtonRed -= 1
            print "off"
            self.AS.led('RED OFF')




        ######################



    def sinus_green(self):
        # działa po naciśnięciu "Dioda sinus" a potem guzika "green"
        #### tu dajesz kod ###
        if self.sinButtonGreen == 0:
            #włączenie sinusa
            self.sinButtonGreen += 1
            print "on"
            self.AS.led('GREEN SIN')
        else:
            #wyłączenie sinusa
            self.sinButtonGreen -= 1
            print "off"
            self.AS.led('GREEN OFF')




        ######################

    def sinus_blue(self):
        # działa po naciśnięciu "Dioda sinus" a potem guzika "blue"

        #### tu dajesz kod ###
        if self.sinButtonBlue == 0:
            #włączenie sinusa
            self.sinButtonBlue += 1
            print "on"
            self.AS.led('BLUE SIN')
        else:
            #wyłączenie sinusa
            self.sinButtonBlue -= 1
            print "off"
            self.AS.led('BLUE OFF')



        ######################

    ############## te są do działania guzików . Nic tu nie rób ########
    def dis_enter_text(self):
        self.f3.pack_forget()

    def dis_scale(self):
        self.f4.pack_forget()

    def dis_sinus(self):
        self.f5.pack_forget()

    def dis_odczyt_pin(self):
        self.f6.pack_forget()

    def odczyt_pin(self):
        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#0b0"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"

        if self.odczytPinNum > 0:
            pass
        else:
            self.odczytPinNum += 1

            self.f6 = Frame(self, height=10, width=32,pady=30)
            self.f6.pack()

            self.labelentry2 = Label(self.f6,text="Numer pinu do odczytu:")
            self.labelentry2.pack()

            self.entry2 = Entry(self.f6,width=15)
            self.entry2.pack()

            self.buttonEnter2 = Button(self.f6,text="Enter")
            self.buttonEnter2 ["command"] = self.entry2get
            self.buttonEnter2.pack()



    def sinus(self):
        ### do pokazania guzików red green blue. Nic nie rób ###
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#0b0"
        self.bfunkcja1["bg"] = "#dadada"

        if self.sinusNum > 0:
            pass
        else:
            self.sinusNum +=1
            self.f5 = Frame(self, height=10, width=32,pady=30)
            self.f5.pack()

            self.buttonEnter = Button(self.f5,text="Red",height=3)
            self.buttonEnter ["command"] = self.sinus_red
            self.buttonEnter.pack(side="left")

            self.buttonEnter = Button(self.f5,text="Green",height=3)
            self.buttonEnter ["command"] = self.sinus_green
            self.buttonEnter.pack(side="left")

            self.buttonEnter = Button(self.f5,text="Blue",height=3)
            self.buttonEnter ["command"] = self.sinus_blue
            self.buttonEnter.pack(side="left")
            print "Inicjuję funkcje sinus"

    def entry(self):
        """Do wpisywania numeru pinu"""
        ### do pokazania pola do wpisywania i guzika enter. W tym nic nie rób ######
        if self.scaleNum > 0:
            self.dis_scale()
            self.scaleNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#dadada"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#0b0"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"

        if self.entryNum > 0:
            pass
        else:
            self.entryNum += 1
            self.f3 = Frame(self, height=10, width=32, pady=30)
            self.f3.pack()

            self.labelentry1 = Label(self.f3,text="Numer pinu:")
            self.labelentry1.pack()

            self.entry1= Entry(self.f3,width=15)
            self.entry1.pack()

            self.buttonEnter = Button(self.f3,text="Enter")
            self.buttonEnter ["command"] = self.entryget
            self.buttonEnter.pack()

    def dioda_suwaki(self):
        #### tu nic nie rób ####
        """ Do "kolor diody"""
        if self.entryNum > 0:
            self.dis_enter_text()
            self.entryNum = 0
        if self.sinusNum > 0:
            self.dis_sinus()
            self.sinusNum = 0
        if self.odczytPinNum > 0:
            self.dis_odczyt_pin()
            self.odczytPinNum = 0
        self.bSynCzas["bg"] = "#dadada"
        self.bOdczPin["bg"] = "#dadada"
        self.bRgbScale["bg"] = "#0b0"
        self.bPolRoz["bg"] = "#dadada"
        self.bfunkcja2["bg"] = "#dadada"
        self.bsinus["bg"] = "#dadada"
        self.bfunkcja1["bg"] = "#dadada"

        if self.scaleNum > 0:
            pass
        else:
            self.scaleNum += 1
            self.f4 = Frame(self, height=50, width=32,pady=30)
            self.f4.pack()

            self.scaleR = Scale(self.f4, from_=0, to=255,label="Red",bg="red",troughcolor="white",fg="white")
            self.scaleR["command"] = self.get_scale
            self.scaleR.pack(side="left")

            self.scaleG = Scale(self.f4, from_=0, to=255,label="Green", bg="green",troughcolor="white",fg="white")
            self.scaleG["command"] = self.get_scale
            self.scaleG.pack(side="left")

            self.scaleB = Scale(self.f4, from_=0, to=255,label="blue", bg="blue",troughcolor="white",fg="white")
            self.scaleB["command"] = self.get_scale
            self.scaleB.pack(side="left")

    def createWidgets(self):
        #################### Robi guziki. Nic nie rób ######
        """odstepy i nagłówek"""
##        self.theLabel = Label(self, text='')
##        self.theLabel.pack()

        self.f0 = Frame(self, height=10, width=32)
        self.f0.pack()

        self.f1 = Frame(self, height=20, width=850)
        self.f1.pack(side="top")
        self.bcontainer = Frame(self)
        self.bcontainer.pack()

        self.bcontainer1 = Frame(self)
        self.bcontainer1.pack()

        self.f2 = Frame(self, height=40, width=500)
        self.f2.pack(side="bottom")
        ###################################
        """ parametry wejsciowe funkcji dioda_rgb"""

        self.bfunkcja1 = Button(self.bcontainer,text="Dioda RGB",fg="black",height=3)
        self.bfunkcja1["command"] =  self.dioda_rgb
        self.bfunkcja1.pack(side="left")

        ###################################
        """ parametry wejsciowe funkcji funkcja1"""
        self.bfunkcja2 = Button(self.bcontainer,text="Wpisz numer pinu",height=3)
        self.bfunkcja2["command"] = self.entry
        self.bfunkcja2.pack(side="left")
        ###################################
        """ parametry wejsciowe funkcji Dioda Sinus"""
        self.bsinus = Button(self.bcontainer,text="Dioda Sinus",height=3)
        self.bsinus["command"] = self.sinus
        self.bsinus.pack(side="left")
        #######################################################
        """ parametry wejsciowe diody z suwakami"""
        self.bRgbScale= Button(self.bcontainer, text="Kolor diody",height=3)
        self.bRgbScale["command"] = self.dioda_suwaki
        self.bRgbScale.pack(side="left")
        #######################################################
        self.bPolRoz= Button(self.bcontainer, text="Polącz/Rozłącz",height=3)
        self.bPolRoz["command"] = self.pol_roz
        self.bPolRoz.pack(side="left")
        ######################################################
        self.bSynCzas= Button(self.bcontainer, text="Synchronizacja Czasu",height=3)
        self.bSynCzas["command"] = self.syn_czas
        self.bSynCzas.pack(side="left")
        #####################################################
        self.bOdczPin= Button(self.bcontainer, text="Odczyt Z Pinu",height=3)
        self.bOdczPin["command"] = self.odczyt_pin
        self.bOdczPin.pack(side="left")
        
root = Tk()
app = Application(master=root)
app.mainloop()
##root.destroy()
