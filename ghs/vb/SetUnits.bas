' This script sets the units used in the Balanced Amplifier Layout App Note
Sub Main
	Project.Units(mwUT_Frequency).MultType = mwUMT_Giga
	Project.Units(mwUT_Resistance).MultType = mwUMT_none
	Project.Units(mwUT_Angle).MultType = mwUMT_Deg
	Project.Units(mwUT_Conductance).MultType = mwUMT_none
	Project.Units(mwUT_Temperature).MultType = mwUMT_DegC
	Project.Units(mwUT_Inductance).MultType = mwUMT_n
	Project.Units(mwUT_Time).MultType = mwUMT_n
	Project.Units.Item(mwUT_Capacitance).MultType = mwUMT_p
	Project.Units(mwUT_Voltage).MultType = mwUMT_none
	Project.Units(mwUT_Current).MultType = mwUMT_m
	Project.Units(mwUT_LengthEnglish).MultType = mwUMT_mil

End Sub
