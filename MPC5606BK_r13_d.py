import idc
import string

addr=0
while addr != 0x000A0220 :
        addr=ida_search.find_text(addr,1,1,'(r13)',1)
        if addr < 0x10000 :
                ida_offset.set_offset(addr,1,0x400093B0)
        else :
                ida_offset.set_offset(addr,1,0x40009510)
        print '%x'%addr
        addr=addr+4
        
addr=0x2000
while addr != 0x00031C18:
        addr=ida_search.find_text(addr,1,1,'r13,',1)
        if addr < 0x10000 :
                ida_offset.set_offset(addr,2,0x400093B0)
        else :
                ida_offset.set_offset(addr,2,0x40009510)
        print '%x'%addr
        addr=addr+4
