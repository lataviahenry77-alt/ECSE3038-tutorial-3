from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


def hottest(devices):
    hot = devices[0]
    for d in devices:
        if d["temp"] > hot["temp"]:
            hot = d
    return hot


def average_temp(devices):
    total = 0
    for d in devices:
        total += d["temp"]
    return total / len(devices)

@app.get("/devices")
async def every_devices():
    return readings

@app.get("/devices/hottest")
async def hottest_devices():
    return hottest(readings)

@app.get("/devices/online")
async def online_devices():
    result = []
    for device in readings:
        if device["online"]:
            result.append(device)
    return result