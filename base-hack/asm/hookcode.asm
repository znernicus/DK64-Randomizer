START_HOOK:
	NinWarpCode:
		JAL 	checkNinWarp
		NOP
		J 		0x807132CC
		NOP

	Jump_CrankyDecouple:
		J 		CrankyDecouple
		NOP
	Jump_ForceToBuyMoveInOneLevel:
		J 		ForceToBuyMoveInOneLevel
		NOP

	PatchCrankyCode:
		LUI t3, hi(Jump_CrankyDecouple)
		LW t3, lo(Jump_CrankyDecouple) (t3)
		LUI t4, 0x8002
		SW t3, 0x60E0 (t4) // Store Hook
		SW r0, 0x60E4 (t4) // Store NOP

		LUI t3, hi(Jump_ForceToBuyMoveInOneLevel)
		LW t3, lo(Jump_ForceToBuyMoveInOneLevel) (t3)
		LUI t4, 0x8002
		SW 	t3, 0x60A8 (t4) // Store Hook
		SW 	r0, 0x60AC (t4) // Store NOP
		SW 	r0, 0x6160 (t4) // Store NOP to prevent loop

		JR 		ra
		NOP

	CrankyDecouple:
		BEQ		a0, t0, CrankyDecouple_Bitfield
		OR 		v1, a0, r0
		BEQZ 	a0, CrankyDecouple_Bitfield
		NOP

		CrankyDecouple_Progessive:
			J 		0x800260E8
			NOP

		CrankyDecouple_Bitfield:
			J 		0x800260F0
			NOP

	ForceToBuyMoveInOneLevel:
		ADDU 	t3, t3, t9
		SLL 	t3, t3, 1
		LBU 	t2, 0xC (s2) // Current Level
		SLL 	t1, t2, 2
		SUBU 	t1, t1, t2
		SLL 	t1, t1, 1 // Current Level * 6
		J 		0x800260B4
		ADDU 	v1, v1, t1

	InstanceScriptCheck:
		ADDIU 	t1, r0, 1
		ADDI 	t4, t4, -1 // Reduce move_index by 1
		SLLV 	t4, t1, t4 // 1 << move_index
		ADDIU 	t1, r0, 0
		AND 	at, t6, t4 // at = kong_moves & move_index
		BEQZ 	at, InstanceScriptCheck_Fail
		NOP

		InstanceScriptCheck_Success:
			J 	0x8063EE14
			NOP

		InstanceScriptCheck_Fail:
			J 	0x8063EE1C
			NOP

	SaveToFileFixes:
		BNEZ 	s0, SaveToFileFixes_Not0
		ANDI 	a1, s3, 0xFF
		B 		SaveToFileFixes_Finish
		ADDIU  	a0, r0, 10 // Stores it in unused slot

		SaveToFileFixes_Not0:
			ADDIU 	a0, s0, 4

		SaveToFileFixes_Finish:
			J 		0x8060DFFC
			NOP

	BarrelMovesFixes:
		LBU 	t0, 0x4238 (t0) // Load Barrel Moves Array Slot
		ADDI 	t0, t0, -1 // Reduce move_value by 1
		ADDIU 	v1, r0, 1
		SLLV 	t0, v1, t0 // Get bitfield value
		AND  	v1, t0, t9
		BEQZ 	v1, BarrelMovesFixes_Finish
		NOP
		ADDIU 	v1, r0, 1

		BarrelMovesFixes_Finish:
			J 		0x806F6EB4
			NOP

	ChimpyChargeFix:
		ANDI 	t6, t6, 1
		LUI	 	v1, 0x8080
		J 		0x806E4938
		ADDIU 	v1, v1, 0xBB40

	OStandFix:
		LBU 	t2, 0xCA0C (t2)
		ANDI 	t2, t2, 1
		J 		0x806E48B4
		ADDIU 	a0, r0, 0x25

	HunkyChunkyFix2:
		BNEL 	v1, at, HunkyChunkyFix2_Finish
		LI 		at, 4
		ANDI 	a2, a0, 1
		BLEZL 	a2, HunkyChunkyFix2_Finish
		LI 		at, 4
		J 		0x8067ECC8
		NOP

		HunkyChunkyFix2_Finish:
			J 		0x8067ECD0
			nop

	EarlyFrameCode:
		JAL 	earlyFrame
		NOP
		JAL 	0x805FC668
		NOP
		J 		0x805FC404
		NOP

	displayListCode:
		JAL 	displayListModifiers
		OR 		a0, s0, r0
		OR 		s0, v0, r0
		LUI 	a0, 0x8075
		ADDIU 	a0, a0, 0x531C
		LHU 	v1, 0x0 (a0)
		LUI 	v0, 0x8075
		J 		0x80714184
		LBU 	v0, 0x5314 (v0)

	updateLag:
		LUI 	t6, hi(FrameReal)
		LW 		a0, lo(FrameReal) (t6)
		LUI 	t6, hi(FrameLag)
		LW 		a1, lo(FrameLag) (t6)
		SUBU 	a1, a0, a1
		LUI 	t6, hi(StoredLag)
		SH 		a1, lo(StoredLag) (t6)
		LUI 	t6, 0x8077
		J 		0x8060067C
		LBU 	t6, 0xAF14 (t6)

	getLobbyExit:
		LUI 	a1, hi(ReplacementLobbyExitsArray)
		SLL 	t7, t6, 1
		ADDU 	a1, a1, t7
		J 		0x80600064
		LHU 	a1, lo(ReplacementLobbyExitsArray) (a1)

	damageMultiplerCode:
		BGEZ 	a3, damageMultiplerCode_Finish
		LB 		t9, 0x2FD (v0)
		LUI 	t2, hi(DamageMultiplier)
		LBU 	t2, lo(DamageMultiplier) (t2)
		MULTU 	a3, t2
		MFLO 	a3

		damageMultiplerCode_Finish:
			J 		0x806C9A84
			ADDU 	t0, t9, a3

	PauseExtraHeight:
		LUI 	s1, hi(InitialPauseHeight)
		LHU 	s1, lo(InitialPauseHeight) (s1)
		J 		0x806A9820
		ADDIU 	s0, s0, 0x5CC

	PauseExtraSlotCode:
		LUI 	t9, hi(InitialPauseHeight)
		LHU 	t9, lo(InitialPauseHeight) (t9)
		ADDIU 	t9, t9, 0xCC
		BNE 	s1, t9, PauseExtraSlotCode_Normal
		NOP
		LUI 	t9, hi(ExpandPauseMenu)
		LBU 	t9, lo(ExpandPauseMenu) (t9)
		BEQZ  	t9, PauseExtraSlotCode_Skip
		SRA 	t4, a2, 0x10
		SLL 	t6, t7, 2
		LUI 	t9, hi(PauseSlot3TextPointer)
		J 		0x806A996C
		ADDIU 	t8, t9, lo(PauseSlot3TextPointer)

		PauseExtraSlotCode_Skip:
			J 		0x806A9980
			NOP

		PauseExtraSlotCode_Normal:
			LW 		t9, 0x0 (s6)
			J 		0x806A9964
			SRA 	t4, a2, 0x10

	PauseExtraSlotClamp0:
		LUI 	a2, 0x427C
		LUI 	t4, hi(ExpandPauseMenu)
		LBU 	t4, lo(ExpandPauseMenu) (t4)
		J 		0x806A87C4
		ADDIU 	t4, t4, 2

	PauseExtraSlotClamp1:
		LUI 	a3, 0x3F80
		LUI 	at, hi(ExpandPauseMenu)
		LBU 	at, lo(ExpandPauseMenu) (at)
		SUBU 	at, t8, at
		J 		0x806A8768
		SLTI 	at, at, 0x3

	PauseExtraSlotCustomCode:
		LB 		v0, 0x17 (s0) // Load Slot Position
		ADDIU 	at, r0, 3
		BNE 	at, v0, PauseExtraSlotCustomCode_Finish
		NOP
		ADDIU 	a0, r0, 0x22
		JAL 	0x805FF378 // Init Map Change
		ADDIU 	a1, r0, 0
		J 		0x806A8A20
		ADDIU 	at, r0, 2
		
		PauseExtraSlotCustomCode_Finish:
			J 		0x806A880C
			ADDIU 	at, r0, 2

	IGTLoadFromFile:
		SLL 	at, v0, 2
		SUBU 	at, at, v0
		SLL 	v0, at, 1
		LUI 	at, hi(BalancedIGT)
		J 		0x8060DD3C
		SW 		v0, lo(BalancedIGT) (at)

	IGTSaveToFile:
		ADDIU 	at, r0, 6
		LUI	 	s0, hi(BalancedIGT)
		LWU 	s0, lo(BalancedIGT) (s0)
		DIVU 	s0, at
		MFLO 	s0
		LUI 	at, 0x40
		J 		0x8060DF4C
		SLTU 	at, s0, at

	FileScreenDLCode_Jump:
		J 		FileScreenDLCode
		NOP

	FileScreenDLCode_Write:
		LUI t3, hi(FileScreenDLCode_Jump)
		LW t3, lo(FileScreenDLCode_Jump) (t3)
		LUI t4, 0x8003
		SW t3, 0x937C (t4) // Store Hook
		JR 	ra
		SW r0, 0x9380 (t4) // Store NOP

	FileScreenDLCode:
		ADDIU 	s0, t4, -0x140
		JAL 	display_text
		ADDIU 	a0, s2, 8
		J 		0x80029690
		ADDIU 	s2, v0, 0

.align 0x10
END_HOOK: