import struct
import binascii

srCRCHigh = [
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80,
    0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81,
    0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80,
    0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80,
    0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81,
    0x40,
    0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81,
    0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81,
    0x40,
    0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81,
    0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80,
    0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80,
    0x41,
    0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81,
    0x40,
    0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80,
    0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40
]

srCRCLow = [
    0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06, 0x07, 0xC7, 0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D,
    0xCD,
    0x0F, 0xCF, 0xCE, 0x0E, 0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, 0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9, 0x1B, 0xDB, 0xDA,
    0x1A,
    0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC, 0x14, 0xD4, 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13,
    0xD3,
    0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, 0xF2, 0x32, 0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34,
    0xF4,
    0x3C, 0xFC, 0xFD, 0x3D, 0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A, 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38, 0x28, 0xE8, 0xE9,
    0x29,
    0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF, 0x2D, 0xED, 0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6,
    0x26,
    0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60, 0x61, 0xA1, 0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7,
    0x67,
    0xA5, 0x65, 0x64, 0xA4, 0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, 0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB, 0x69, 0xA9, 0xA8,
    0x68,
    0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA, 0xBE, 0x7E, 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75,
    0xB5,
    0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, 0x70, 0xB0, 0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52,
    0x92,
    0x96, 0x56, 0x57, 0x97, 0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C, 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E, 0x5A, 0x9A, 0x9B,
    0x5B,
    0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89, 0x4B, 0x8B, 0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C,
    0x8C,
    0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42, 0x43, 0x83, 0x41, 0x81, 0x80, 0x40
]


def calcCRC(byte: int, oldCRC):
    high, low = oldCRC & 0xFF, (oldCRC >> 8) & 0xFF
    uIndex = low ^ byte
    high, low = high ^ srCRCHigh[uIndex], srCRCLow[uIndex]
    CRC = (high << 8 | low)
    return CRC


def crc16(data: list):
    if isinstance(data, str):
        data = [int(b, 16) for b in data.split()]
    CRC = calcCRC(data[0], 0xFFFF)
    for i in range(1, len(data)):
        CRC = calcCRC(data[i], CRC)
    data.extend([(CRC // 256), (CRC % 256)])
    return bytearray(data)


class Galileo_packet:
    prefix = 1
    request = None

    def __init__(self):
        self.struct_rules = ''
        self.struct_data = []

    def set_device_version(self, device_version):
        print("Device version:", device_version)
        self.struct_rules += 'bB'
        self.struct_data.append(0x01)
        self.struct_data.append(device_version)

    def set_fw_version(self, fw_version):
        print("Firmware version:", fw_version)
        self.struct_rules += 'bB'
        self.struct_data.append(0x02)
        self.struct_data.append(fw_version)

    def set_imei(self, imei):
        if len(imei) < 15:
            for i in range(0, 15-len(imei)):
                imei = '0' + imei
        elif len(imei) > 15:
            imei = imei[0:15]
        print("IMEI:", imei)
        self.struct_rules += 'b'
        self.struct_data.append(0x03)
        for i in range(0, 15):
            self.struct_rules += 'b'
            self.struct_data.append(ord(imei[i]))


    def set_dev_id(self, dev_id):
        print("Device ID:", dev_id)
        self.struct_rules += 'bH'
        self.struct_data.append(0x04)
        self.struct_data.append(dev_id)

    def set_rec_number(self, rec_number):
        print("Record number:", rec_number)
        self.struct_rules += 'bH'
        self.struct_data.append(0x10)
        self.struct_data.append(rec_number)

    def set_datetime(self, tm):
        print("Datetime:", tm)
        self.struct_rules += 'bI'
        self.struct_data.append(0x20)
        self.struct_data.append(int(tm))

    def set_nav_data(self, latitude, longitude, sats, source):
        print("Sats:", sats, "source:", source, "lat:", latitude, "lon:", longitude)
        source_sats = (source << 4) + sats
        latitude = int(latitude * 1000000)
        longitude = int(longitude * 1000000)
        self.struct_rules += 'bbii'
        self.struct_data.append(0x30)
        self.struct_data.append(source_sats)
        self.struct_data.append(latitude)
        self.struct_data.append(longitude)

    def set_course(self, speed, course):
        print("Speed:", speed, "course:", course)
        self.struct_rules += 'bHH'
        self.struct_data.append(0x33)
        self.struct_data.append(speed*10)
        self.struct_data.append(course*10)

    def set_altitude(self, altitude):
        print("Altitude: ", altitude)
        self.struct_rules += 'bh'
        self.struct_data.append(0x34)
        self.struct_data.append(altitude)

    def set_hdop(self, hdop):
        print("HDOP: ", hdop)
        self.struct_rules += 'bB'
        self.struct_data.append(0x35)
        self.struct_data.append(hdop*10)

    def set_device_state(self, device_state):
        print("Device state: ", device_state, bin(device_state))
        self.struct_rules += 'bH'
        self.struct_data.append(0x40)
        self.struct_data.append(device_state)

    def set_power(self, power):
        print("Power:", power)
        self.struct_rules += 'bH'
        self.struct_data.append(0x41)
        self.struct_data.append(power)

    def set_battery(self, battery):
        print("Battery:", battery)
        self.struct_rules += 'bH'
        self.struct_data.append(0x42)
        self.struct_data.append(battery)

    def set_acc(self, acc):
        acc_all = (acc[2] << 20) + (acc[1] << 10) + acc[0]
        print("Acc:", acc)
        self.struct_rules += 'bI'
        self.struct_data.append(0x44)
        self.struct_data.append(acc_all)

    def set_eco_drive(self, eco_drive):
        print("Eco drive:", eco_drive)
        self.struct_rules += 'bBBBB'
        self.struct_data.append(0x47)
        self.struct_data.append(eco_drive[0])
        self.struct_data.append(eco_drive[1])
        self.struct_data.append(eco_drive[2])
        self.struct_data.append(eco_drive[3])


    def create_packet(self):
        self.struct_rules = '<bh' + self.struct_rules
        self.struct_data.insert(0, 0)  # length
        self.struct_data.insert(0, 1)  # prefix
        p = struct.pack(self.struct_rules, *self.struct_data)
        length = len(p) - 3
        self.struct_data[1] = length
        p = struct.pack(self.struct_rules, *self.struct_data)
        self.request = crc16(list(p))
        print("struct_rules", self.struct_rules)
        print("struct_data", self.struct_data)
        print("result", binascii.hexlify(self.request))

    def get_request(self):
        return self.request
