# RnS_UVZ

A Python library to control the Rohde&amp;Schwarz UVZ Scanner

Usage example:

    uvz = UVZ('GPIB0::4::INSTR')
    # mode can be "M0", "M1", "M2" 
    # or "3p", "3p6p", "6p"
    uvz.mode = "M2"
    uvz.output = True
    uvz.channel = 18
