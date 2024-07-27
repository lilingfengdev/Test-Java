import json
import os
from functools import lru_cache
from typing import List, Iterable, Any
from dataclasses import dataclass
import re
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.ndimage import gaussian_filter1d

gc_api = "https://gceasy.ycrash.cn/analyzeGC?apiKey=7127d22e-1005-42dd-be6d-fdc671bf492c"


@dataclass
class Data:
    cps: List[float]
    time: str
    gc_data: Any


@lru_cache
def get_gc(jdk):
    response = requests.post(
        gc_api,
        data=open(os.path.join("output", jdk, "gc.log"), "rb").read(),
        headers={'Content-Type': 'text'}
    )
    return json.loads(response.content)


report = open("all.report", "w+")


def reportdata(gc, data):
    report.write("\n")
    report.write(f"GC:{gc}\n")
    report.write(f'吞吐量:{data["gcKPI"]["throughputPercentage"]}MS\n')
    report.write(f'最大暂停时间:{data["gcKPI"]["maxPauseTime"]}MS\n')
    report.write(f'平均暂停时间:{data["gcKPI"]["averagePauseTime"]}MS\n')
    report.write("\n")


plt.rcParams['font.family'] = 'SimHei'
plt.rcParams["xtick.labelsize"] = 10

plt.title("吞吐量")
plt.ylabel("吞吐量")
plt.xlabel("GC 引擎")
memory = []
for jdk in os.listdir("output"):
    reportdata(jdk, get_gc(jdk))
    memory.append(get_gc(jdk)["gcKPI"]["throughputPercentage"])

report.close()
plt.bar(os.listdir("output"), memory, width=0.2)
plt.xticks(rotation=30)
plt.show()

plt.title("暂停时间")
plt.ylabel("最大暂停时间")
plt.xlabel("GC 引擎")
memory = []
for jdk in os.listdir("output"):
    memory.append(get_gc(jdk)["gcKPI"]["maxPauseTime"])

plt.bar(os.listdir("output"), memory, width=0.2)
plt.xticks(rotation=30)
plt.show()

plt.title("暂停时间")
plt.ylabel("平均暂停时间")
plt.xlabel("GC 引擎")
memory = []
for jdk in os.listdir("output"):
    memory.append(get_gc(jdk)["gcKPI"]["averagePauseTime"])

plt.bar(os.listdir("output"), memory, width=0.2)
plt.xticks(rotation=30)
plt.show()
