# -*- coding:utf-8 -*-
from urllib import request
import json
import time
import socket

# resp = request.urlopen("https://api.genmymodel.com/projects/public?page=0&type=BPMN2&minDataSize=10000")


# resp = request.urlopen("https://api.genmymodel.com/projects/_RjgDADWBEemd9voZzRIYOg/bpmn")

# request.urlretrieve("https://api.genmymodel.com/projects/_RjgDADWBEemd9voZzRIYOg/bpmn", "file.bpmn")
# print(resp.read())


base_url = "https://api.genmymodel.com/projects/public?page={}&type=BPMN2&minDataSize=10000"
page_size = 20
total_pages = 183

for i in range(1, total_pages):
    print("-"*50)
    try:
        resp = request.urlopen(base_url.format(i), timeout=30)
    except socket.timeout:
        with open("miss.txt", mode='a', encoding='utf-8') as miss:
            miss.write("page_{} timeout\n".format(i))
        continue
    print("page:{}".format(i))

    resp = json.loads(resp.read(), encoding='utf-8')
    projects = resp["projects"]
    for j in range(page_size):
        print("paragram:{}".format(j))
        project = projects[j]
        owner = project["owner"]
        name = project["name"]
        id = project["projectId"]
        links = project["links"]
        bpmn_link = links[3]
        bpmn_url = bpmn_link['href']

        file_name = "files/{}_{}_{}.bpmn".format(i, j, id)
        print(bpmn_url)
        try:
            resp = request.urlopen(bpmn_url, timeout=30)
            # print(resp.read())
            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(resp.read().decode())
            # request.urlretrieve(bpmn_url, file_name)
        except socket.timeout:
            with open("miss.txt", mode='a', encoding='utf-8') as miss:
                miss.write(file_name+"\n")
            continue
        # time.sleep(1)
        # request.ur

    # print(resp)
