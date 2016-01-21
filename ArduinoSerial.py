import serial
import datetime
import math


class ArduinoSerial(object):

    def __init__(self, port):
        self._ser = serial.Serial('COM%i'%(port))

    @property
    def _set_datetime(self):
        t1 = datetime.datetime(1970,1,1,0,0,0)
        self._ser.write("%s@"%(str(int(math.ceil(datetime.timedelta.total_seconds(datetime.datetime.now()-t1))))))

    @property
    def start(self):
        self._ser.write("#")

    def write(self, insc):
        self._ser.write("%s#"%(insc))

    def led(self, insc):
        self._ser.write("%s!"%(insc))


    def read(self, port):
        input_tab = []
        input_str = ""
        try:
            port = int(port)
        except:
            return "Not an INT"
        self._ser.write("%i$"%(port))
        while not False:
            x = self._ser.read(1)
            input_tab.append(str(x))
            if x == '\n':
                break
        return input_str.join(input_tab[:-2])

    @property
    def toogle(self):
        if self._ser.is_open:
            self._close
            print "Serial closed"
        else:
            self._open
            print "Serial opened"

    @property
    def _close(self):
        self._ser.close()
    @property
    def _open(self):
        self._ser.open()

if __name__ == '__main__':
    a = ArduinoSerial(3)
    
