# RnS_UVZ
A Python library to control the Rohde&amp;Schwarz UVZ Scanner

Usage example:

    uvz = UVZ('GPIB0::4::INSTR')
    uvz.mode = "M2"
    uvz.output = True
    uvz.channel = 18
