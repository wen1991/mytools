import idc
import idaapi
import idautils


def Can_Id_index(start):
        MakeUnknown(start, 0x1000, idaapi.DOUNK_SIMPLE)
        ea = start
        end = start+0x1000
	while ea < end:
		MakeWord(ea)
		ea=ea+2	
def MakeCan_struct(start,end):
	MakeUnknown(start, end-start, idaapi.DOUNK_SIMPLE)
	ea =start
	while ea < end :
		MakeWord(ea)
		MakeWord(ea+0x2)
		MakeDword(ea+0x4)
		MakeDword(ea+0x8)
		MakeDword(ea+0xC)
		MakeDword(ea+0x10)
		MakeDword(ea+0x14)
		MakeDword(ea+0x18)
		MakeDword(ea+0x1C)
		ea=ea+0x20		
def DealChannel(start):
	MakeUnknown(start, 0x2C*7, idaapi.DOUNK_SIMPLE)
	ea  = start
	end =start+0x2C*7
	while ea < end:
		oft = 0
		MakeName(ea,"%s_Task"% GetString(Dword(ea+0xC),-1,0))
		while oft < 0x2C:
			MakeDword(ea+oft)
			if oft==0x10:
				Can_Id_index(Dword(ea+oft))
				if Dword(ea+oft-4)!=0:
					MakeName(Dword(ea+oft),GetString(Dword(ea+oft-4),-1,0)+"_ID_INDEX")
			oft=oft+4;        
		ea=ea+0x2C
def makelong(start,end):
	MakeUnknown(start, end-start, idaapi.DOUNK_SIMPLE)
	ea  = start
	while ea < end:
		MakeDword(ea)
                ea=ea+4;
def MakeChannel_Task():#Channel_Task
	sid = GetStrucIdByName("Channel_Task")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "Channel_Task", 0)
	print "%x" % sid

	AddStrucMember(sid, "Channel_addr"	        ,	 0x00, FF_DWRD|FF_DATA, -1, 0x04-0x00)
	AddStrucMember(sid, "str4C_addr"		,	 0x04, FF_DWRD|FF_DATA, -1, 0x08-0x04)
	AddStrucMember(sid, "res1"			,	 0x08, FF_DWRD|FF_DATA, -1, 0x0C-0x08)
	AddStrucMember(sid, "callback_addr"	        ,	 0x0C, FF_DWRD|FF_DATA, -1, 0x10-0x0C)
	AddStrucMember(sid, "Time_stamp"	        ,	 0x10, FF_DWRD|FF_DATA, -1, 0x14-0x10)
	AddStrucMember(sid, "frames_count"		,	 0x14, FF_DWRD|FF_DATA, -1, 0x18-0x14)


def main():
	#DealChannel(0x42BDC)
	#makelong(0xBBE98,0xD988C)
	#MakeCan_struct(0xBBE98,0xD3D58)
	MakeChannel_Task()
if __name__ == '__main__':
	main()
