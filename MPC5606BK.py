#from idaapi import stroffflag, offflag
import idc
import idaapi
import idautils

def MakeADC():
	sid = GetStrucIdByName("ADC_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "ADC_stru", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_BYTE|FF_DATA, -1, 0x4000)
	
	MakeUnknown(0xFFE00000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE04000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFE00000,"ADC_stru")
	MakeStruct(0xFFE04000,"ADC_stru")
	MakeName(0xFFE00000,"ADC_0")
	MakeName(0xFFE04000,"ADC_1")
	
def MakeI2C():#I2C
	sid = GetStrucIdByName("I2C_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "I2C_stru", 0)
	print "%x" % sid

	AddStrucMember(sid, "IBAD"		,	 0x0000, FF_BYTE|FF_DATA, -1, 0x0001-0x0000)
	AddStrucMember(sid, "IBFD"		,	 0x0001, FF_BYTE|FF_DATA, -1, 0x0002-0x0001)
	AddStrucMember(sid, "IBCR"		,	 0x0002, FF_BYTE|FF_DATA, -1, 0x0003-0x0002)
	AddStrucMember(sid, "IBSR"		,	 0x0003, FF_BYTE|FF_DATA, -1, 0x0004-0x0003)
	AddStrucMember(sid, "IBDR"		,	 0x0004, FF_BYTE|FF_DATA, -1, 0x0005-0x0004)
	AddStrucMember(sid, "IBIC"		,	 0x0005, FF_BYTE|FF_DATA, -1, 0x0006-0x0005)
	AddStrucMember(sid, "Reserved1"	,	 0x0006, FF_BYTE|FF_DATA, -1, 0x4000-0x0006)
	
	MakeUnknown(0xFFE30000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFE30000,"I2C_stru")
	MakeName(0xFFE30000,"I2C_0")
	
def MakeLINFlex():
	sid = GetStrucIdByName("LINFlex_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "LINFlex_stru", 0)
	print "%x" % sid
	AddStrucMember(sid, "LINCR1", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINIER", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "INSR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINESR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "UARTCR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "UARTSR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINTCSR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINOCR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINTOCR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINFBRR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINIBRR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINCFR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LINCR2", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BIDR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BDRL1", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BDRM2", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFER", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFMI", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFMR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR0", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR1", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR2", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR3", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR4", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR5", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR6", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR7", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR8", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR9", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR10", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR11", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR12", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR13", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR14", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IFCR15", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Reserved"	,	-1, FF_BYTE|FF_DATA, -1, 0x4000-0x008C)
	
	MakeUnknown(0xFFE40000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE44000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE48000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE4C000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE50000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE54000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE58000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFE5C000, 0x4000, DOUNK_SIMPLE)

	MakeStruct(0xFFE40000,"LINFlex_stru")
	MakeStruct(0xFFE44000,"LINFlex_stru")
	MakeStruct(0xFFE48000,"LINFlex_stru")
	MakeStruct(0xFFE4C000,"LINFlex_stru")
	MakeStruct(0xFFE50000,"LINFlex_stru")
	MakeStruct(0xFFE54000,"LINFlex_stru")
	MakeStruct(0xFFE58000,"LINFlex_stru")
	MakeStruct(0xFFE5C000,"LINFlex_stru")
	
	MakeName(0xFFE40000,"LINFlex_0")
	MakeName(0xFFE44000,"LINFlex_1")
	MakeName(0xFFE48000,"LINFlex_2")
	MakeName(0xFFE4C000,"LINFlex_3")
	MakeName(0xFFE50000,"LINFlex_4")
	MakeName(0xFFE54000,"LINFlex_5")
	MakeName(0xFFE58000,"LINFlex_6")
	MakeName(0xFFE5C000,"LINFlex_7")
	
def MakeCTU():
	sid = GetStrucIdByName("CTU_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "CTU_stru", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_BYTE|FF_DATA, -1, 0x4000)	
	
	MakeUnknown(0xFFE64000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFE64000,"CTU_stru")
	MakeName(0xFFE64000,"CTU_0")
	
def MakeCAN_sampler():
	sid = GetStrucIdByName("CAN_sampler_stru")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "CAN_sampler_stru", 0)
	print "%x" % sid
	AddStrucMember(sid, "CR", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers0", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers1", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers2", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers3", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers4", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers5", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers6", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers7", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers8", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers9", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers10", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Sample_registers11", -1, FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "Reserved"	,	-1, FF_BYTE|FF_DATA, -1, 0x4000-0x0034)
	
	MakeUnknown(0xFFE70000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFE70000,"CAN_sampler_stru")
	MakeName(0xFFE70000,"CAN_sampler_0")
	
def MakeMPU():#MPU
	sid = GetStrucIdByName("MPU_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "MPU_stru", 0)
	print "%x" % sid

	AddStrucMember(sid, "MPU_CESR"					,	 0x0000, FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(sid, "Reserved1"					,	 0x0004, FF_BYTE|FF_DATA, -1, 0x0010-0x0004)
	AddStrucMember(sid, "MPU_EAR0"					,	 0x0010, FF_DWRD|FF_DATA, -1, 0x0014-0x0010)
	AddStrucMember(sid, "MPU_EDR0"					,	 0x0014, FF_DWRD|FF_DATA, -1, 0x0018-0x0014)
	AddStrucMember(sid, "MPU_EAR1"					,	 0x0018, FF_DWRD|FF_DATA, -1, 0x001C-0x0018)
	AddStrucMember(sid, "MPU_EDR1"					,	 0x001C, FF_DWRD|FF_DATA, -1, 0x0020-0x001C)
	AddStrucMember(sid, "MPU_EAR2"					,	 0x0020, FF_DWRD|FF_DATA, -1, 0x0024-0x0020)
	AddStrucMember(sid, "MPU_EDR2"					,	 0x0024, FF_DWRD|FF_DATA, -1, 0x0028-0x0024)
	AddStrucMember(sid, "Reserved2"					,	 0x0028, FF_BYTE|FF_DATA, -1, 0x0400-0x0028)
	AddStrucMember(sid, "MPU_RGD0"					,	 0x0400, FF_DWRD|FF_DATA, -1, 0x0410-0x0400)
	AddStrucMember(sid, "MPU_RGD1"					,	 0x0410, FF_DWRD|FF_DATA, -1, 0x0420-0x0410)
	AddStrucMember(sid, "MPU_RGD2"					,	 0x0420, FF_DWRD|FF_DATA, -1, 0x0430-0x0420)
	AddStrucMember(sid, "MPU_RGD3"					,	 0x0430, FF_DWRD|FF_DATA, -1, 0x0440-0x0430)
	AddStrucMember(sid, "MPU_RGD4"					,	 0x0440, FF_DWRD|FF_DATA, -1, 0x0450-0x0440)
	AddStrucMember(sid, "MPU_RGD5"					,	 0x0450, FF_DWRD|FF_DATA, -1, 0x0460-0x0450)
	AddStrucMember(sid, "MPU_RGD6"					,	 0x0460, FF_DWRD|FF_DATA, -1, 0x0470-0x0460)
	AddStrucMember(sid, "MPU_RGD7"					,	 0x0470, FF_DWRD|FF_DATA, -1, 0x0480-0x0470)
	AddStrucMember(sid, "Reserved3"					,	 0x0480, FF_BYTE|FF_DATA, -1, 0x0800-0x0480)
	AddStrucMember(sid, "MPU_RGDAAC0"				,	 0x0800, FF_DWRD|FF_DATA, -1, 0x0804-0x0800)
	AddStrucMember(sid, "MPU_RGDAAC1"				,	 0x0804, FF_DWRD|FF_DATA, -1, 0x0808-0x0804)
	AddStrucMember(sid, "MPU_RGDAAC2"				,	 0x0808, FF_DWRD|FF_DATA, -1, 0x080C-0x0808)
	AddStrucMember(sid, "MPU_RGDAAC3"				,	 0x080C, FF_DWRD|FF_DATA, -1, 0x0810-0x080C)
	AddStrucMember(sid, "MPU_RGDAAC4"				,	 0x0810, FF_DWRD|FF_DATA, -1, 0x0814-0x0810)
	AddStrucMember(sid, "MPU_RGDAAC5"				,	 0x0814, FF_DWRD|FF_DATA, -1, 0x0818-0x0814)
	AddStrucMember(sid, "MPU_RGDAAC6"				,	 0x0818, FF_DWRD|FF_DATA, -1, 0x081C-0x0818)
	AddStrucMember(sid, "MPU_RGDAAC7"				,	 0x081C, FF_DWRD|FF_DATA, -1, 0x0820-0x081C)
	AddStrucMember(sid, "Reserved4"					,	 0x0820, FF_BYTE|FF_DATA, -1, 0x4000-0x0820)
	
	MakeUnknown(0xFFF10000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF10000,"MPU_stru")
	MakeName(0xFFF10000,"MPU_0")
	
def MakeSWT():#SWT
	sid = GetStrucIdByName("SWT_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "SWT_stru", 0)
	print "%x" % sid
                                                                          
	AddStrucMember(sid, "SWT_CR"				,	0x0000 , FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(sid, "SWT_IR"				,	0x0004 , FF_DWRD|FF_DATA, -1, 0x0008-0x0004)
	AddStrucMember(sid, "SWT_TO"				,	0x0008 , FF_DWRD|FF_DATA, -1, 0x000C-0x0008)
	AddStrucMember(sid, "SWT_WN"				,	0x000C , FF_DWRD|FF_DATA, -1, 0x0010-0x000C)
	AddStrucMember(sid, "SWT_SR"				,	0x0010 , FF_DWRD|FF_DATA, -1, 0x0014-0x0010)
	AddStrucMember(sid, "SWT_CO"				,	0x0014 , FF_DWRD|FF_DATA, -1, 0x0018-0x0014)
	AddStrucMember(sid, "SWT_SK"				,	0x0018 , FF_DWRD|FF_DATA, -1, 0x001C-0x0018)
	AddStrucMember(sid, "Reserved"				,	0x001C , FF_DWRD|FF_DATA, -1, 0x4000-0x001C)
	
	MakeUnknown(0xFFF38000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF38000,"SWT_stru")
	MakeName(0xFFF38000,"SWT_0")
	
def MakeSTM():#STM
	sid = GetStrucIdByName("STM_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "STM_stru", 0)
	print "%x" % sid

	AddStrucMember(sid, "STM_CR"		,	 0x0000, FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(sid, "STM_CNT"		,	 0x0004, FF_DWRD|FF_DATA, -1, 0x0008-0x0004)
	AddStrucMember(sid, "Reserved1"		,	 0x0008, FF_BYTE|FF_DATA, -1, 0x000C-0x0008)
	AddStrucMember(sid, "Reserved2"		,	 0x000C, FF_BYTE|FF_DATA, -1, 0x0010-0x000C)
	AddStrucMember(sid, "STM_CCR0"		,	 0x0010, FF_DWRD|FF_DATA, -1, 0x0014-0x0010)
	AddStrucMember(sid, "STM_CIR0"		,	 0x0014, FF_DWRD|FF_DATA, -1, 0x0018-0x0014)
	AddStrucMember(sid, "STM_CMP0"		,	 0x0018, FF_DWRD|FF_DATA, -1, 0x001C-0x0018)
	AddStrucMember(sid, "Reserved3"		,	 0x001C, FF_BYTE|FF_DATA, -1, 0x0020-0x001C)
	AddStrucMember(sid, "STM_CCR1"		,	 0x0020, FF_DWRD|FF_DATA, -1, 0x0024-0x0020)
	AddStrucMember(sid, "STM_CIR1"		,	 0x0024, FF_DWRD|FF_DATA, -1, 0x0028-0x0024)
	AddStrucMember(sid, "STM_CMP1"		,	 0x0028, FF_DWRD|FF_DATA, -1, 0x002C-0x0028)
	AddStrucMember(sid, "Reserved4"		,	 0x002C, FF_BYTE|FF_DATA, -1, 0x0030-0x002C)
	AddStrucMember(sid, "STM_CCR2"		,	 0x0030, FF_DWRD|FF_DATA, -1, 0x0034-0x0030)
	AddStrucMember(sid, "STM_CIR2"		,	 0x0034, FF_DWRD|FF_DATA, -1, 0x0038-0x0034)
	AddStrucMember(sid, "STM_CMP2"		,	 0x0038, FF_DWRD|FF_DATA, -1, 0x003C-0x0038)
	AddStrucMember(sid, "Reserved5"		,	 0x003C, FF_BYTE|FF_DATA, -1, 0x0040-0x003C)
	AddStrucMember(sid, "STM_CCR3"		,	 0x0040, FF_DWRD|FF_DATA, -1, 0x0044-0x0040)
	AddStrucMember(sid, "STM_CIR3"		,	 0x0044, FF_DWRD|FF_DATA, -1, 0x0048-0x0044)
	AddStrucMember(sid, "STM_CMP3"		,	 0x0048, FF_DWRD|FF_DATA, -1, 0x004C-0x0048)
	AddStrucMember(sid, "Reserved6"		,	 0x004C, FF_BYTE|FF_DATA, -1, 0x4000-0x004C)

	MakeUnknown(0xFFF10000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF10000,"STM_stru")
	MakeName(0xFFF10000,"STM_0")
	
def MakeECSM():
	sid = GetStrucIdByName("ECSM_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "ECSM_stru", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_BYTE|FF_DATA, -1, 0x4000)
	
	MakeUnknown(0xFFF40000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF40000,"ECSM_stru")
	MakeName(0xFFF40000,"ECSM_0")
	
def MakeeDMA():
	sid = GetStrucIdByName("eDMA_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "eDMA_stru", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_BYTE|FF_DATA, -1, 0x4000)
	
	MakeUnknown(0xFFF44000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF44000,"eDMA_stru")
	MakeName(0xFFF44000,"eDMA_0")
	
def MakeINTC():#INTC
	sid = GetStrucIdByName("INTC_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "INTC_stru", 0)
	print "%x" % sid

	#simple_types = [ FF_BYTE, FF_WORD, FF_DWRD, FF_QWRD, FF_TBYT, FF_OWRD, FF_FLOAT, FF_DOUBLE, FF_PACKREAL ]
	#simple_sizes = [ 1, 2, 4, 8, 10, 16, 4, 8, 10 ]

	AddStrucMember(sid, "MCR",				 0x0000, FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(sid, "reserved1",	 	 0x0004, FF_DWRD|FF_DATA, -1, 0x0008-0x0004)
	AddStrucMember(sid, "CPR",			 	 0x0008, FF_DWRD|FF_DATA, -1, 0x000C-0x0008)
	AddStrucMember(sid, "reserved2",		 0x000C, FF_DWRD|FF_DATA, -1, 0x0014-0x0010)
	AddStrucMember(sid, "IACKR",			 0x0010, FF_DWRD|FF_DATA, -1, 0x0018-0x0014)
	AddStrucMember(sid, "reserved3",		 0x0014, FF_DWRD|FF_DATA, -1, 0x001C-0x0018)
	AddStrucMember(sid, "EOIR",				 0x0018, FF_DWRD|FF_DATA, -1, 0x0020-0x001C)
	AddStrucMember(sid, "reserved4",		 0x001C, FF_DWRD|FF_DATA, -1, 0x0024-0x0020)
	AddStrucMember(sid, "SSCIR0_3",			 0x0020, FF_BYTE|FF_DATA, -1, 0x0028-0x0024)
	AddStrucMember(sid, "SSCIR4_7",			 0x0024, FF_BYTE|FF_DATA, -1, 0x0028-0x0024)
	AddStrucMember(sid, "reserved5",	 	 0x0028, FF_BYTE|FF_DATA, -1, 0x0040-0x0028) 
	AddStrucMember(sid, "INTC_PSR0_3", 0x0040, FF_BYTE|FF_DATA, -1, 0x0044-0x0040)
	AddStrucMember(sid, "INTC_PSR4_7", 0x0044, FF_BYTE|FF_DATA, -1, 0x0048-0x0044)
	AddStrucMember(sid, "INTC_PSR8_11", 0x0048, FF_BYTE|FF_DATA, -1, 0x004C-0x0048)
	AddStrucMember(sid, "INTC_PSR12_15", 0x004C, FF_BYTE|FF_DATA, -1, 0x0050-0x004C)
	AddStrucMember(sid, "INTC_PSR16_19", 0x0050, FF_BYTE|FF_DATA, -1, 0x0054-0x0050)
	AddStrucMember(sid, "INTC_PSR20_23", 0x0054, FF_BYTE|FF_DATA, -1, 0x0058-0x0054)
	AddStrucMember(sid, "INTC_PSR24_27", 0x0058, FF_BYTE|FF_DATA, -1, 0x005C-0x0058)
	AddStrucMember(sid, "INTC_PSR28_31", 0x005C, FF_BYTE|FF_DATA, -1, 0x0060-0x005C)
	AddStrucMember(sid, "INTC_PSR32_35", 0x0060, FF_BYTE|FF_DATA, -1, 0x0064-0x0060)
	AddStrucMember(sid, "INTC_PSR36_39", 0x0064, FF_BYTE|FF_DATA, -1, 0x0068-0x0064)
	AddStrucMember(sid, "INTC_PSR40_43", 0x0068, FF_BYTE|FF_DATA, -1, 0x006C-0x0068)
	AddStrucMember(sid, "INTC_PSR44_47", 0x006C, FF_BYTE|FF_DATA, -1, 0x0070-0x006C)
	AddStrucMember(sid, "INTC_PSR48_51", 0x0070, FF_BYTE|FF_DATA, -1, 0x0074-0x0070)
	AddStrucMember(sid, "INTC_PSR52_55", 0x0074, FF_BYTE|FF_DATA, -1, 0x0078-0x0074)
	AddStrucMember(sid, "INTC_PSR56_59", 0x0078, FF_BYTE|FF_DATA, -1, 0x007C-0x0078)
	AddStrucMember(sid, "INTC_PSR60_63", 0x007C, FF_BYTE|FF_DATA, -1, 0x0080-0x007C)
	AddStrucMember(sid, "INTC_PSR64_67", 0x0080, FF_BYTE|FF_DATA, -1, 0x0084-0x0080)
	AddStrucMember(sid, "INTC_PSR68_71", 0x0084, FF_BYTE|FF_DATA, -1, 0x0088-0x0084)
	AddStrucMember(sid, "INTC_PSR72_75", 0x0088, FF_BYTE|FF_DATA, -1, 0x008C-0x0088)
	AddStrucMember(sid, "INTC_PSR76_79", 0x008C, FF_BYTE|FF_DATA, -1, 0x0090-0x008C)
	AddStrucMember(sid, "INTC_PSR80_83", 0x0090, FF_BYTE|FF_DATA, -1, 0x0094-0x0090)
	AddStrucMember(sid, "INTC_PSR84_87", 0x0094, FF_BYTE|FF_DATA, -1, 0x0098-0x0094)
	AddStrucMember(sid, "INTC_PSR88_91", 0x0098, FF_BYTE|FF_DATA, -1, 0x009C-0x0098)
	AddStrucMember(sid, "INTC_PSR92_95", 0x009C, FF_BYTE|FF_DATA, -1, 0x00A0-0x009C)
	AddStrucMember(sid, "INTC_PSR96_99", 0x00A0, FF_BYTE|FF_DATA, -1, 0x00A4-0x00A0)
	AddStrucMember(sid, "INTC_PSR100_103", 0x00A4, FF_BYTE|FF_DATA, -1, 0x00A8-0x00A4)
	AddStrucMember(sid, "INTC_PSR104_107", 0x00A8, FF_BYTE|FF_DATA, -1, 0x00AC-0x00A8)
	AddStrucMember(sid, "INTC_PSR108_111", 0x00AC, FF_BYTE|FF_DATA, -1, 0x00B0-0x00AC)
	AddStrucMember(sid, "INTC_PSR112_115", 0x00B0, FF_BYTE|FF_DATA, -1, 0x00B4-0x00B0)
	AddStrucMember(sid, "INTC_PSR116_119", 0x00B4, FF_BYTE|FF_DATA, -1, 0x00B8-0x00B4)
	AddStrucMember(sid, "INTC_PSR120_123", 0x00B8, FF_BYTE|FF_DATA, -1, 0x00BC-0x00B8)
	AddStrucMember(sid, "INTC_PSR124_127", 0x00BC, FF_BYTE|FF_DATA, -1, 0x00C0-0x00BC)
	AddStrucMember(sid, "INTC_PSR128_131", 0x00C0, FF_BYTE|FF_DATA, -1, 0x00C4-0x00C0)
	AddStrucMember(sid, "INTC_PSR132_135", 0x00C4, FF_BYTE|FF_DATA, -1, 0x00C8-0x00C4)
	AddStrucMember(sid, "INTC_PSR136_139", 0x00C8, FF_BYTE|FF_DATA, -1, 0x00CC-0x00C8)
	AddStrucMember(sid, "INTC_PSR140_143", 0x00CC, FF_BYTE|FF_DATA, -1, 0x00D0-0x00CC)
	AddStrucMember(sid, "INTC_PSR144_147", 0x00D0, FF_BYTE|FF_DATA, -1, 0x00D4-0x00D0)
	AddStrucMember(sid, "INTC_PSR148_151", 0x00D4, FF_BYTE|FF_DATA, -1, 0x00D8-0x00D4)
	AddStrucMember(sid, "INTC_PSR152_155", 0x00D8, FF_BYTE|FF_DATA, -1, 0x00DC-0x00D8)
	AddStrucMember(sid, "INTC_PSR156_159", 0x00DC, FF_BYTE|FF_DATA, -1, 0x00E0-0x00DC)
	AddStrucMember(sid, "INTC_PSR160_163", 0x00E0, FF_BYTE|FF_DATA, -1, 0x00E4-0x00E0)
	AddStrucMember(sid, "INTC_PSR164_167", 0x00E4, FF_BYTE|FF_DATA, -1, 0x00E8-0x00E4)
	AddStrucMember(sid, "INTC_PSR168_171", 0x00E8, FF_BYTE|FF_DATA, -1, 0x00EC-0x00E8)
	AddStrucMember(sid, "INTC_PSR172_175", 0x00EC, FF_BYTE|FF_DATA, -1, 0x00F0-0x00EC)
	AddStrucMember(sid, "INTC_PSR176_179", 0x00F0, FF_BYTE|FF_DATA, -1, 0x00F4-0x00F0)
	AddStrucMember(sid, "INTC_PSR180_183", 0x00F4, FF_BYTE|FF_DATA, -1, 0x00F8-0x00F4)
	AddStrucMember(sid, "INTC_PSR184_187", 0x00F8, FF_BYTE|FF_DATA, -1, 0x00FC-0x00F8)
	AddStrucMember(sid, "INTC_PSR188_191", 0x00FC, FF_BYTE|FF_DATA, -1, 0x0100-0x00FC)
	AddStrucMember(sid, "INTC_PSR192_195", 0x0100, FF_BYTE|FF_DATA, -1, 0x0104-0x0100)
	AddStrucMember(sid, "INTC_PSR196_199", 0x0104, FF_BYTE|FF_DATA, -1, 0x0108-0x0104)
	AddStrucMember(sid, "INTC_PSR200_203", 0x0108, FF_BYTE|FF_DATA, -1, 0x010C-0x0108)
	AddStrucMember(sid, "INTC_PSR204_207", 0x010C, FF_BYTE|FF_DATA, -1, 0x0110-0x010C)
	AddStrucMember(sid, "INTC_PSR208_211", 0x0110, FF_BYTE|FF_DATA, -1, 0x0114-0x0110)
	AddStrucMember(sid, "INTC_PSR212_215", 0x0114, FF_BYTE|FF_DATA, -1, 0x0118-0x0114)
	AddStrucMember(sid, "INTC_PSR216_219", 0x0118, FF_BYTE|FF_DATA, -1, 0x011C-0x0118)
	AddStrucMember(sid, "INTC_PSR220_223", 0x011C, FF_BYTE|FF_DATA, -1, 0x0120-0x011C)
	AddStrucMember(sid, "INTC_PSR224_227", 0x0120, FF_BYTE|FF_DATA, -1, 0x0124-0x0120)
	AddStrucMember(sid, "INTC_PSR228_231", 0x0124, FF_BYTE|FF_DATA, -1, 0x0128-0x0124)
	AddStrucMember(sid, "INTC_PSR232_233", 0x0128, FF_BYTE|FF_DATA, -1, 0x012C-0x0128)
	AddStrucMember(sid, "Reserved6"		 , 0x001C , FF_DWRD|FF_DATA, -1, 0x4000-0x012C)
	
	MakeUnknown(0xFFF48000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF48000,"INTC_stru")
	MakeName(0xFFF48000,"INTC_0")

def MakeDSPI():
	sid = GetStrucIdByName("DSPI_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "DSPI_stru", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_BYTE|FF_DATA, -1, 0x4000)
	
	MakeUnknown(0xFFF90000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFF94000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFF98000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFF9C000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFA0000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFA4000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFF90000,"DSPI_stru")
	MakeStruct(0xFFF94000,"DSPI_stru")
	MakeStruct(0xFFF98000,"DSPI_stru")
	MakeStruct(0xFFF9C000,"DSPI_stru")
	MakeStruct(0xFFFA0000,"DSPI_stru")
	MakeStruct(0xFFFA4000,"DSPI_stru")
	MakeName(0xFFF90000,"DSPI_0")	
	MakeName(0xFFF94000,"DSPI_1")	
	MakeName(0xFFF98000,"DSPI_2")	
	MakeName(0xFFF9C000,"DSPI_3")	
	MakeName(0xFFFA0000,"DSPI_4")	
	MakeName(0xFFFA4000,"DSPI_5")	

def MakeCAN_x():#FLEXCAN
	buf_id = GetStrucIdByName("canbuf_t")
	DelStruc(buf_id)
	if buf_id != -1:
		DelStruc(buf_id)
	buf_id = AddStrucEx(-1, "canbuf_t", 0)
	print "buf_id=%x" % buf_id
	AddStrucMember(buf_id, "FLAG"			,	 0x0000, FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(buf_id, "ID"			,	 0x0004, FF_DWRD|FF_DATA, -1, 0x0008-0x0004)
	AddStrucMember(buf_id, "DATA"			,	 0x0008, FF_BYTE|FF_DATA, -1, 0x0010-0x0008)
	
	sid = GetStrucIdByName("FLEXCAN_stru")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "FLEXCAN_stru", 0)
	print "%x" % sid

	#simple_types = [ FF_BYTE, FF_WORD, FF_DWRD, FF_QWRD, FF_TBYT, FF_OWRD, FF_FLOAT, FF_DOUBLE, FF_PACKREAL ]
	#simple_sizes = [ 1, 2, 4, 8, 10, 16, 4, 8, 10 ]

	AddStrucMember(sid, "MCR"			,	 0x0000, FF_DWRD|FF_DATA, -1, 0x0004-0x0000)
	AddStrucMember(sid, "CTRL"			,	 0x0004, FF_DWRD|FF_DATA, -1, 0x0008-0x0004)
	AddStrucMember(sid, "TIMER"			,	 0x0008, FF_DWRD|FF_DATA, -1, 0x000C-0x0008)
	AddStrucMember(sid, "Reserved1"		,	 0x000C, FF_BYTE|FF_DATA, -1, 0x0010-0x000C)
	AddStrucMember(sid, "RXGMASK"		,	 0x0010, FF_DWRD|FF_DATA, -1, 0x0014-0x0010)
	AddStrucMember(sid, "RX14MASK"		,	 0x0014, FF_DWRD|FF_DATA, -1, 0x0018-0x0014)
	AddStrucMember(sid, "RX15MASK"		,	 0x0018, FF_DWRD|FF_DATA, -1, 0x001C-0x0018)
	AddStrucMember(sid, "ECR"			,	 0x001C, FF_DWRD|FF_DATA, -1, 0x0020-0x001C)
	AddStrucMember(sid, "ESR"			,	 0x0020, FF_DWRD|FF_DATA, -1, 0x0024-0x0020)
	AddStrucMember(sid, "IMASK2"		,	 0x0024, FF_DWRD|FF_DATA, -1, 0x0028-0x0024)
	AddStrucMember(sid, "IMASK1"		,	 0x0028, FF_DWRD|FF_DATA, -1, 0x002C-0x0028)
	AddStrucMember(sid, "IFLAG2"		,	 0x002C, FF_DWRD|FF_DATA, -1, 0x0030-0x002C)
	AddStrucMember(sid, "IFLAG1"		,	 0x0030, FF_DWRD|FF_DATA, -1, 0x0034-0x0030)
	AddStrucMember(sid, "Reserved2"		,	 0x0034, FF_BYTE|FF_DATA, -1, 0x0080-0x0034)
	AddStrucMember(sid, "Message_Buf"	,	 0x0080, FF_BYTE|FF_DATA, -1, 0x0480-0x0080)
	AddStrucMember(sid, "Reserved3"		,	 0x0480, FF_BYTE|FF_DATA, -1, 0x0880-0x0480)
	AddStrucMember(sid, "RXIMR0_15"		,	 0x0880, FF_DWRD|FF_DATA, -1, 0x08C0-0x0880)
	AddStrucMember(sid, "RXIMR16_31"	,	 0x08C0, FF_DWRD|FF_DATA, -1, 0x0900-0x08C0)
	AddStrucMember(sid, "RXIMR32_63"	,	 0x0900, FF_DWRD|FF_DATA, -1, 0x0980-0x0900)
	AddStrucMember(sid, "Reserved4"		,	 0x0980, FF_DWRD|FF_DATA, -1, 0x4000-0x0980)
	SetMemberType(sid, 0x0080, FF_STRU|FF_DATA, buf_id, 64)
	
	MakeUnknown(0xFFFC0000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFC4000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFC8000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFCC000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFD0000, 0x4000, DOUNK_SIMPLE)
	MakeUnknown(0xFFFD4000, 0x4000, DOUNK_SIMPLE)
	MakeStruct(0xFFFC0000,"FLEXCAN_stru")
	MakeStruct(0xFFFC4000,"FLEXCAN_stru")
	MakeStruct(0xFFFC8000,"FLEXCAN_stru")
	MakeStruct(0xFFFCC000,"FLEXCAN_stru")
	MakeStruct(0xFFFD0000,"FLEXCAN_stru")
	MakeStruct(0xFFFD4000,"FLEXCAN_stru")
	MakeName(0xFFFC0000,"FLEXCAN_0")	
	MakeName(0xFFFC4000,"FLEXCAN_1")	
	MakeName(0xFFFC8000,"FLEXCAN_2")	
	MakeName(0xFFFCC000,"FLEXCAN_3")	
	MakeName(0xFFFD0000,"FLEXCAN_4")	
	MakeName(0xFFFD4000,"FLEXCAN_5")	
	
def makeMPC5606BK():
	MakeADC()
	MakeI2C()
	MakeLINFlex()
	MakeCTU()
	MakeCAN_sampler()
	MakeMPU()
	MakeSWT()
	MakeSTM()
	MakeECSM()
	MakeeDMA()
	MakeINTC()
	MakeDSPI()
	MakeCAN_x()

def makeSys_struc_1():
	sid = GetStrucIdByName("Sys_struc_1")
	DelStruc(sid)
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "Sys_struc_1", 0)
	print "%x" % sid
	
	AddStrucMember(sid, "UnDo_R", -1, FF_DWRD|FF_DATA, -1, 0x80)

	MakeUnknown(0x40000000, 0x80*512, DOUNK_SIMPLE)
	i=0
	while i<512:
		MakeStruct(0x40000000+i*0x80,"Sys_struc_1")
		i=i+1

def makelong(start,end):
	MakeUnknown(start, end-start, idaapi.DOUNK_SIMPLE)
	ea  = start
	while ea < end:
		MakeDword(ea)
                ea=ea+4;
def Bytecpy(dst,src,length):
        MakeUnknown(dst, length, DOUNK_SIMPLE)
	i=0
	while i < length:
                PatchByte(dst+i,Byte(src+i))
                i=i+1
def memset(addr,value,length):
        MakeUnknown(addr, length, DOUNK_SIMPLE)
	i=0
	while i < length:
                PatchByte(addr+i,value)
                i=i+1

def sub_1E2():#meminit
        #sub_19C()
        Bytecpy(0x40001340,0xA800,0x70)
        Bytecpy(0x400013B0,0xA870,0x14)
        #sub_2EE()
        memset(0x40000000,0,0x1340)
        memset(0x400013C8,0,0xEC)
        memset(0x400014B8,0,0x2264)

def sub_10FCA():#meminit
        #sub_19C()
        Bytecpy(0x40001340,0x34000,0x1d0)
        Bytecpy(0x40001510,0x341d0,0x44)
        Bytecpy(0x400017E8,0x34218,0x10)
        memset(0x40000000,0,0x1340)
        memset(0x40001558,0,0x28c)
        memset(0x400017F8,0,0x73cc)
        
       
	
def main():
#1
	#AddSeg(0xC0000000,0xC3FF4000, 0, 1, 1, 2)
	#AddSeg(0xFFE00000,0xFFFD8000, 0, 1, 1, 2)
	#makeMPC5606BK()
	#makeSys_struc_1()

	#makelong(0x9C94,0xA150)
	#makelong(0x20,0xEc)	
	#sub_1E2()
	#sub_10FCA()
	makelong(0x32B64,0x338C0)
	ea =0x32294
	while ea < 0x32B64:
                MakeByte(ea)
                MakeArray(ea,8)
                ea=ea+8

	
if __name__ == '__main__':
	main()
