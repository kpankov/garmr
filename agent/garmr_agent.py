import re
import socket
import subprocess
import time
import logging
import json

import requests
from requests.structures import CaseInsensitiveDict
from urllib3.response import log

url = "http://127.0.0.1:5000/client/"

step = 0


def send_data(data_to_json):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    # data = '{"testbed_name":"my_login","testbed_ip":"my_password","client_type":"rdp","client_ip":"127.0.0.1"}'

    resp = requests.put(url, headers=headers, data=json.dumps(data_to_json))

    if resp.status_code == 200:
        logger.info("Data was sent successfully")

    if resp.status_code == 500:
        logger.error("Internal server error!")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    logger = logging.getLogger("garmr_agent")

    while True:
        logger.info("- - - - - - Step #{}".format(step))

        data = {}

        hostname = socket.gethostname()
        ip = socket.gethostbyname(socket.gethostname())

        data["hostname"] = hostname
        data["ip"] = ip

        location = ("127.0.0.1", 3389)  # RDP port
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = a_socket.connect_ex(location)
        a_socket.close()

        if result_of_check == 0:
            logger.info("RDP port is open")
            data["rdp"] = "on"
        else:
            logger.info("RDP port is not open")
            data["rdp"] = "off"

        res = subprocess.getoutput("qwinsta")
        users = re.findall(r">([\S_-]+)\s*([\S_-]+)", res)
        logger.info("qwinsta: {}".format(users))
        if len(users) == 1:
            data["users": str(users[0][1])]

        res = subprocess.getoutput("netstat -an")
        for server_client in re.findall(r"\s*TCP\s*([0-9\.]+):3389\s*([0-9\.]+):[0-9]+\s*ESTABLISHED", res):
            if server_client[1] != "127.0.0.1":
                print(server_client[1])

        send_data(data)

        step += 1
        time.sleep(5)
