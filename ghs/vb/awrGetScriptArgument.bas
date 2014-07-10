Function awrGetScriptArgument() As String
	Dim s As StatusItem
	Dim itemtext As String
	Dim argument_header As String


	' This must match the variable used in awrde.py
	argument_header = "SCRIPT_ARGUMENT:"
	header_len = Len(argument_header)

	For Each s In Status.Items
		itemtext = s.Text
		Debug.Print StrComp(Left(itemtext, header_len),argument_header)
		If StrComp(head,argument_headder)=0 Then
			awrGetScriptArgument = Right(itemtext,Len(itemtext)-header_len)
			s.Delete()
		End If
	Next s

End Function