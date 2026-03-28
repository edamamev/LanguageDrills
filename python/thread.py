#!/usr/bin/python3
# https://realpython.com/intro-to-python-threading/

import logging
import threading
import time
logger = logging.getLogger(__name__)

def thread_function(name):
    logger.info("Thread %s: starting", name)
    time.sleep(2)
    logger.info("Thread %s: finishing", name)

def main():
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(\
        filename='thread.log',\
        level=logging.INFO,\
        format=format,\
        datefmt="%H:%M:%S"\
    )

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=("1"))
    logger.info("Main   : before running thread")
    x.start()
    logger.info("Main   : wait for the thread to finish")
    logger.info("Main   : all done")


if __name__ == "__main__":
    main()
