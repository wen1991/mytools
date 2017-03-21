import idc
import idaapi
import idautils	
	
def stm32f103seg():
	AddSeg(0x20000000 , 0x2000FFFF, 0, 1, 1, 2)
	AddSeg(0x40000000 , 0x400233FF, 0, 1, 1, 2)
	AddSeg(0xE000E000 , 0xE000EFFF, 0, 1, 1, 2)

def makedata(start):
	ea  = start 
	while ea < start+0x130:
		MakeDword(ea)
                ea=ea+4;
	
def makeBKP():
	sid = GetStrucIdByName("BKP_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "BKP_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "RESERVED0"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "DR1"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED1"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR2"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED2"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR3"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED3"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR4"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED4"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR5"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED5"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR6"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED6"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR7"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED7"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR8"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED8"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR9"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED9"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR10"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED10"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RTCCR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED11"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED12"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CSR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED13"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR11"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED14"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR12"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED15"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR13"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED16"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR14"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED17"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR15"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED18"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR16"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED19"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR17"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED20"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR18"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED21"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR19"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED22"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR20"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED23"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR21"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED24"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR22"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED25"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR23"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED26"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR24"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED27"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR25"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED28"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR26"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED29"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR27"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED30"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR28"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED31"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR29"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED32"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR30"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED33"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR31"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED34"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR32"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED35"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR33"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED36"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR34"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED37"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR35"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED38"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR36"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED39"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR37"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED40"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR38"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED41"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR39"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED42"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR40"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED43"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR41"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED44"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR42"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED45"			,	-1 , FF_WORD|FF_DATA, -1, 2)

	MakeName(0x40006C00,"BKP_Base")
	MakeStruct(0x40006C00,"BKP_TypeDef")
	

def makeRTC():
	sid = GetStrucIdByName("RTC_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "RTC_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "CRH"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED0"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CRL"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED1"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "PRLH"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED2"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "PRLL"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED3"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DIVH"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED4"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DIVL"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED5"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CNTH"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED6"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CNTL"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED7"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "ALRH"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED8"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "ALRL"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED9"			,	-1 , FF_WORD|FF_DATA, -1, 2)

	

def makeRCC():
	sid = GetStrucIdByName("RCC_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "RCC_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "CR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CFGR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CIR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "APB2RSTR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "APB1RSTR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "AHBENR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "APB2ENR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "APB1ENR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BDCR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CSR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)

def makeSCB():
	sid = GetStrucIdByName("SCB_Type")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "SCB_Type", 0)
	print "%x" % sid
	AddStrucMember(sid, "CPUID"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ICSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "VTOR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "AIRCR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SCR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CCR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SHP"				,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "SHCSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CFSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "HFSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "DFSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "MMFAR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BFAR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "AFSR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "PFR "				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "DFR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ADR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "MMFR "				,	-1 , FF_WORD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ISAR "				,	-1 , FF_WORD|FF_DATA, -1, 4)

def makeSysTick():
	sid = GetStrucIdByName("SysTick_Type")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "SysTick_Type", 0)
	print "%x" % sid
	AddStrucMember(sid, "CTRL"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LOAD"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "VAL"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CALIB"				,	-1 , FF_DWRD|FF_DATA, -1, 4)

def makeGPIO():
	sid = GetStrucIdByName("GPIO_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "GPIO_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "CRL"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CRH"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "IDR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ODR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BSRR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "BRR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LCKR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	
def makeFLASH():
	sid = GetStrucIdByName("FLASH_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "FLASH_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "ACR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "KEYR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "OPTKEYR"			        ,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "AR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "RESERVED"			        ,	-1 , FF_WORD|FF_DATA, -1, 4)
	AddStrucMember(sid, "OBR"				,	-1 , FF_WORD|FF_DATA, -1, 4)
	AddStrucMember(sid, "WRPR"				,	-1 , FF_WORD|FF_DATA, -1, 4)	


def makeGPIO_InitTypeDef():
	sid = GetStrucIdByName("GPIO_InitTypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "GPIO_InitTypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "GPIO_Pin"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "GPIO_Speed"			,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "GPIO_Mode"				,	-1 , FF_BYTE|FF_DATA, -1, 1)

def makeUSART():
	sid = GetStrucIdByName("USART_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "USART_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "SR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED0"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "DR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED1"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "BRR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED2"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CR1"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED3"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CR2"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED4"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "CR3"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED5"			,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "GTPR"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "RESERVED6"			,	-1 , FF_WORD|FF_DATA, -1, 2)


def makeUSART_InitTypeDef():
	sid = GetStrucIdByName("USART_InitTypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "USART_InitTypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "USART_BaudRate"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "USART_WordLength"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "USART_StopBits"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "USART_Parity"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "USART_Mode"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "USART_HardwareFlowControl"				,	-1 , FF_WORD|FF_DATA, -1, 2)
	
def makeNVIC():
	sid = GetStrucIdByName("NVIC_Type")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "NVIC_Type", 0)
	print "%x" % sid
	AddStrucMember(sid, "ISER"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E120-0xE000E100)
	AddStrucMember(sid, "RESERVED0"			,	-1 , FF_DWRD|FF_DATA, -1, 0XE000E180-0xE000E120)
	AddStrucMember(sid, "ICER"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E1A0-0XE000E180)
	AddStrucMember(sid, "RSERVED1"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E200-0xE000E1A0)
	AddStrucMember(sid, "ISPR"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E220-0xE000E200)
	AddStrucMember(sid, "RESERVED2"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E280-0xE000E220)
	AddStrucMember(sid, "ICPR"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E2A0-0xE000E280)
	AddStrucMember(sid, "RESERVED3"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E300-0xE000E2A0)
	AddStrucMember(sid, "IABR"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E320-0xE000E300)
	AddStrucMember(sid, "RESERVED4"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000E400-0xE000E320)
	AddStrucMember(sid, "IPR"			,	-1 , FF_BYTE|FF_DATA, -1, 0xE000E4F0-0xE000E400)
	AddStrucMember(sid, "RESERVED5"			,	-1 , FF_DWRD|FF_DATA, -1, 0xE000EF00-0xE000E4F0)
	AddStrucMember(sid, "STIR"			,	-1 , FF_DWRD|FF_DATA, -1, 4)
	
	


def makeNVIC_InitTypeDef():
	sid = GetStrucIdByName("NVIC_InitTypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "NVIC_InitTypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "NVIC_IRQChannel"			,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "NVIC_IRQChannelPreemptionPriority"	,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "NVIC_IRQChannelSubPriority"	,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "NVIC_IRQChannelCmd"		,	-1 , FF_BYTE|FF_DATA, -1, 1)


def makeADC():
	sid = GetStrucIdByName("ADC_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "ADC_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "SR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CR1"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "CR2"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SMPR1"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SMPR2"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JOFR1"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JOFR2"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JOFR3"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JOFR4"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "HTR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "LTR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SQR1"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SQR2"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SQR3"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JSQR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JDR1"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JDR2"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JDR3"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "JDR4"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "DR"				,	-1 , FF_DWRD|FF_DATA, -1, 4)


def makeADC_InitTypeDef():
	sid = GetStrucIdByName("ADC_InitTypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "ADC_InitTypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "ADC_Mode"				,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ADC_ScanConvMode"			,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "ADC_ContinuousConvMode"		,	-1 , FF_BYTE|FF_DATA, -1, 1)
	AddStrucMember(sid, "ADC_ExternalTrigConv"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ADC_DataAlign"			,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "ADC_NbrOfChannel"			,	-1 , FF_BYTE|FF_DATA, -1, 1)


def makeIWDG():
	sid = GetStrucIdByName("IWDG_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "IWDG_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "KR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "PR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "RLR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(sid, "SR"		,	-1 , FF_DWRD|FF_DATA, -1, 4)

def makeDOG():
        sid = GetStrucIdByName("Dog_TypeDef")
	if sid != -1:
		DelStruc(sid)
	sid = AddStrucEx(-1, "Dog_TypeDef", 0)
	print "%x" % sid
	AddStrucMember(sid, "dog_n"		,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "dog_click"		,	-1 , FF_WORD|FF_DATA, -1, 2)
	AddStrucMember(sid, "dog_2"		,	-1 , FF_WORD|FF_DATA, -1, 2)


def main():
	stm32f103seg()
	#makedata(0x00000000)
	makedata(0x08000000)
	makedata(0x08020000)
	makeBKP()
	MakeName(0x40006C00,"BKP_TypeDef_Base")
	MakeStruct(0x40006C00,"BKP_TypeDef")
	makeRTC()
	MakeName(0x40002800,"RTC_TypeDef_Base")
	MakeStruct(0x40002800,"RTC_TypeDef")
	makeRCC()
	MakeName(0x40021000,"RCC_TypeDef_Base")
	MakeStruct(0x40021000,"RCC_TypeDef")
	makeSCB()
	MakeName(0xE000ED00,"SCB_Type_Base")
	MakeStruct(0xE000ED00,"SCB_Type")
	makeSysTick()
	MakeName(0xE000E010,"SysTick_Type_Base")
	makeGPIO()
	MakeName(0x40010800,"Port A")
	MakeStruct(0x40010800,"GPIO_TypeDef")
	MakeName(0x40010C00,"Port_B")
	MakeStruct(0x40010C00,"GPIO_TypeDef")
	MakeName(0x40011000,"Port_C")
	MakeStruct(0x40011000,"GPIO_TypeDef")
	MakeName(0x40011400,"Port_D")
	MakeStruct(0x40011400,"GPIO_TypeDef")
	MakeName(0x40011800,"Port_E")
	MakeStruct(0x40011800,"GPIO_TypeDef")
	MakeName(0x40011C00,"Port_F")
	MakeStruct(0x40011C00,"GPIO_TypeDef")
	MakeName(0x40012000,"Port_G")
	MakeStruct(0x40012000,"GPIO_TypeDef")

	makeFLASH()
        MakeName(0x40022000,"FLASH_TypeDef_Base")
	MakeStruct(0x40022000,"FLASH_TypeDef")

        makeGPIO_InitTypeDef()

        makeUSART()
	makeUSART_InitTypeDef()
        makeNVIC()
        makeNVIC_InitTypeDef()

        makeADC()
        makeADC_InitTypeDef()
	makeIWDG()

        #Mobike use
        makeDOG()


if __name__ == '__main__':
	main()
