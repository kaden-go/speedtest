import time
import logging
from SpeedtestModel import SpeedtestModel
from SpeedtestFileHandler import SpeedtestFileHandler

logging.basicConfig(level=logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter


if __name__ == "__main__":

    model = SpeedtestModel(threads = 0)
    fileHandler = SpeedtestFileHandler()

    intervall = 30

    logging.info("Initialize speedtest")

    while(True):
        data = model.get_data()

        print(">>logging data:")
        print(data)

        fileHandler.write_data(data)

        data.clear()
        time.sleep(60 * intervall)

