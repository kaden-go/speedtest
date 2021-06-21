import time
from SpeedtestModel import SpeedtestModel
from SpeedtestFileHandler import SpeedtestFileHandler

if __name__ == "__main__":

    model = SpeedtestModel(threads = 0)
    fileHandler = SpeedtestFileHandler()

    intervall = 30

    print(">>init speedtest...")

    while(True):
        data = model.get_data()

        print(">>logging data:")
        print(data)

        fileHandler.write_data(data)

        data.clear()
        time.sleep(60 * intervall)

