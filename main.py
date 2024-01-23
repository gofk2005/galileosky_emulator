from galileo_packet import Galileo_packet
from sender import Sender
from time import time, sleep
from random import randint, uniform
import track

# Настройки телематического сервера
SERVER = 'xxx.xxx.xxx.xxx'
PORT = 9000

# Данные, которые будет отправлять устройство по умолчанию
device_version = 1
fw_version = 4
imei = '866533422971179'
dev_id = 1000
rec_number = 1
latitude = 55.123
longitude = 37.456
sats = 12
source = 0
speed = 22
course = 90
altitude = 100
hdop = 1
device_state = 1
power = 12000
battery = 4000
acc = (431, 520, 345)
eco_drive = (10, 50, 100, 200)


conn = Sender(SERVER, PORT)

tmp = True

for t in track.track:

    if rec_number % 10 == 0:
        tmp = not tmp

    if tmp:
        acceleration = 200
        breaking = 200
        turn = 200
        tussock = 200
    else:
        acceleration = randint(0,100)
        breaking = randint(0,100)
        turn = randint(0,100)
        tussock = randint(0,100)

    eco_drive = (acceleration, breaking, turn, tussock)
    speed, latitude, longitude, course = t

    packet = Galileo_packet()

    packet.set_device_version(device_version)
    packet.set_fw_version(fw_version)
    packet.set_imei(imei)
    packet.set_dev_id(dev_id)
    packet.set_rec_number(rec_number)
    packet.set_datetime(int(time()))
    packet.set_nav_data(latitude, longitude, sats, source)
    packet.set_course(speed, course)
    packet.set_altitude(altitude)
    packet.set_hdop(hdop)
    packet.set_device_state(device_state)
    packet.set_power(power)
    packet.set_battery(battery)
    packet.set_acc(acc)
    packet.set_eco_drive(eco_drive)

    packet.create_packet()

    conn.send(packet.get_request())

    rec_number += 1
    sleep(3)
