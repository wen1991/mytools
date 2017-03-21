import idc
import idaapi
import idautils


class MPC5669G_core:
	def __INIT__(self):
		self.r0		=0
		self.r1		=0
		self.r2		=0
		self.sp		=0
		self.gp		=0
		self.r5		=0
		self.r6		=0
		self.r7		=0
		self.r8		=0
		self.r9		=0
		self.r10	=0
		self.r11	=0
		self.r12	=0
		self.r13	=0
		self.r14	=0
		self.r15	=0
		self.r16	=0
		self.r17	=0
		self.r18	=0
		self.r19	=0
		self.r20	=0
		self.r21	=0
		self.r22	=0
		self.r23	=0
		self.r24	=0
		self.r25    =0
		self.r26    =0
		self.r27    =0
		self.r28    =0
		self.r29    =0
		self.ep     =0
		self.lp     =0

	def makefunc1(self,fun_start,fun_end):
		

















def main():
	start	=0;
	end		=0;
	ea 		= start
	while ea < end :
		fun_start	=NextFunction(ea)
		fun_end		=FindFuncEnd(fun_start)
		MPC5669G_core.makefunc1(fun_start,fun_end)
		ea = fun_end+4

if __name__ == '__main__':
	main()