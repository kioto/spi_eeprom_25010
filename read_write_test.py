#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import spitools as st

OFFSET = 0x00

def write_read(spi, offset):
    print('Offset:',hex( offset))
    for addr in range(0x00, 0x80, 0x10):
        vals = [0xFF&(addr+i+offset) for i in range(0x10)]
        st.write(spi, addr, vals)
    res = st.read(spi, 0x00, 128)
    st.dump(res)

if __name__ == '__main__':
    spi = st.create()
    write_read(spi, 0x00)
    write_read(spi, 0x01)
    write_read(spi, 0x10)
    
# end of file


