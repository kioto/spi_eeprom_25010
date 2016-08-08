#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import spitools as st

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <value>'.format(sys.argv[0]))
        exit()
    val = int(sys.argv[1], 0)
        
    spi = st.create()
    for addr in range(0x00, 0x80, 0x10):
        vals = [0xFF&val for i in range(0x10)]
        st.write(spi, addr, vals)
    
    res = st.read(spi, 0x00, 128)
    st.dump(res)
    #print(hex(res[0x10]))
# end of file


