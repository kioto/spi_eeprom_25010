#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import spidev

WAIT  = 0.0014
SPEED = 10000000  # 10M

def create():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = SPEED
    return spi

def write_enable(spi):
    spi.xfer2([0x06])

def write(spi, addr, data):
    write_enable(spi)
    time.sleep(WAIT)
    array = [0x02, 0x00, addr] + data
    res = spi.xfer2(array)
    time.sleep(WAIT)
    return res

def read(spi, addr=0, num=128):
    res = spi.xfer2([0x03, 0x00, addr] + [0x00 for i in range(num)])
    time.sleep(WAIT)
    return res[3:]

def int2hex(val):
    return hex(val)[2:].zfill(2)

def dump(vals):
    line = ''
    print('00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f')
    print('-----------------------------------------------')
    for i in range(len(vals)):
        line += int2hex(vals[i]) + ' '
        if not ((i+1) % 16):
            print(line)
            line = ''
    if line:
        print(line)        
        
# end of file
