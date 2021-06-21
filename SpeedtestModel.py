import speedtest
from datetime import datetime

class SpeedtestModel():

    def __init__(self, threads):
        self.__data = []
        self.__servers = []
        self.__threads = threads
        self.__noConnection = False

    def __perform_speedtest(self):
        try:
            s = speedtest.Speedtest()
            print(">>performing measurement...")
            s.get_servers(self.__servers)
            s.get_best_server()
            s.download(threads=self.__threads)
            s.upload(threads=self.__threads)

            self.__get_data(s.results.dict())
            self.__add_timestamp()

        except speedtest.ConfigRetrievalError:
            print(">>ERR: no connection to server")
            self.__data = [0,0,0]
            self.__add_timestamp()

    def __get_data(self, results):
        dl = results.get('download')/1000000
        ul = results.get('upload')/1000000
        ping = results.get('ping')

        self.__data.append(round(dl, 2))
        self.__data.append(round(ul, 2))
        self.__data.append(round(ping, 0))

    def __add_timestamp(self):
        now = datetime.now().time()
        date = datetime.now().date()
        timestamp = date.strftime('%m/%d/%Y-') + now.strftime('%H%M')
        self.__data.append(timestamp)

    def get_data(self):
        self.__perform_speedtest()
        return self.__data
    

