import idc
import string

addr=0
for i in range(2123):
	addr=ida_search.find_text(addr,1,1,'0xFEE0',1)
	
	o0=GetOperandValue(addr+4,0)
	o1=GetOperandValue(addr+4,1)
	o=0
	idx=0
	#print '%x'%addr,hex(o0),hex(o1)
	if o1>o0:
                o=o1
                idx=1
	else:
                o=o0
                idx=0
        o=0xffff0000|o
	if 'movhi' in GetMnem(addr):
                target=(0xfee00000+o)&0xffffffff
                add_dref(addr+4,target,0)
                print hex(addr+4),hex(target)
                #MakeComm(addr+4,'%08X'%target)
                ida_offset.set_offset(addr+4,idx,0xfee00000)

	addr=addr+8
