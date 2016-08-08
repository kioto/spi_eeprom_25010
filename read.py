#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import spitools as st

if __name__ == '__main__':
    spi = st.create()
    
    vals = st.read(spi, 0x00)
    st.dump(vals)

# end of file
