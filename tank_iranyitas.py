#!/usr/bin/python

import sys
import RPi.GPIO as GPIO

class Tank:

    engedelyezett_parancsok = ["stop","elore","hatra","jobbra","balra"]
    relek = {"jobb_elore": 10, "jobb_hatra": 11, "bal_elore": 12, "bal_elore": 13, }

    def Execute(self):
        if self.check_parameterek_szama() and self.check_is_engedelyezett_parancs():
            self.iranyitas(sys.argv[0])

    def check_parameterek_szama(self):
        if len(sys.argv) != 2:
            print "Egy parameter kotlelezo. Hasznalat: stop|elore|hatra|jobbra|balra"
            return False
        else:
            return True

    def check_is_engedelyezett_parancs(self):
        if sys.argv[1] in self.engedelyezett_parancsok:
            return True
        else:
            print "Nem engedelyezett parameter. Hasznalat: stop|elore|hatra|jobbra|balra"
            return False


    def iranyitas(self, parameter):
        self.kimenetek_beallitasa()

        print "parameter: " + parameter

        if parameter == "stop":
            return False
        elif parameter == "elore":
            print "elore"
            GPIO.output(self.relek["jobb_elore"], True)
            GPIO.output(self.relek["bal_elore"], True)
        elif parameter == "hatra":
            print "hatra"
            GPIO.output(self.relek["jobb_hatra"], True)
            GPIO.output(self.relek["bal_hatra"], True)
        elif parameter == "jobbra":
            print "jobbra"
            GPIO.output(self.relek["jobb_elore"], True)
            GPIO.output(self.relek["bal_hatra"], True)
        elif parameter == "balra":
            print "balra"
            GPIO.output(self.relek["jobb_hatra"], True)
            GPIO.output(self.relek["bal_elore"], True)


    def kimenetek_beallitasa(self):
        ##GPIO.setmode(GPIO.BOARD)  regi csomag itt meg nemkell
        for rele in self.relek:
            print str(self.relek[rele]) + " - " + str(rele)
            GPIO.setup(self.relek[rele], GPIO.OUT)
            GPIO.output(self.relek[rele], False)


t = Tank()
t.Execute()