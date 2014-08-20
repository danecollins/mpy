' Script to start the AWR Guided Help Server

' $MENU=Hidden
Sub Main
	Start_GH_Server
End Sub
' $MENU=Configuration
Sub Start_GH_Server
	Dim x As String
	x = Application.Directories("AppDir")
	x = "cmd.exe /c ""cd " + x + "\ghs && server.py"""
	Debug.Print x
	Shell x,vbNormalFocus
End Sub