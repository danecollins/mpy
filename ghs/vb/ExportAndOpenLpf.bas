' Code Module
Sub Main
	Project.ProcessDefinitions("Default").Export("mylpf.lpf")
	Shell("notepad.exe "+"mylpf.lpf")
End Sub
