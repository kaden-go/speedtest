import csv
from datetime import date, datetime

header = ['downstream [Mbit/s]', 'upstream [Mbit/s]', 'ping [ms]', 'timestamp']

class SpeedtestFileHandler():

    def __init__(self):
        self.__file = None
        self.__writer = None
        self.__init = False
        self.__write_header()

    def __open_file(self):
        date = datetime.today().strftime('%d%m')
        self.file = open('data/speedtest_data_' + date + '.csv', 'a') 
        self.writer = csv.writer(self.file)

    def __close_file(self):
        self.file.close()

    def __write_header(self):
        self.__open_file()
        self.writer.writerow(header)
        self.__close_file()

    def write_data(self, data):
        self.__open_file()
        self.writer.writerow(data)
        self.__close_file()