Sub Main
	Dim x As ProjectItem
	Dim w As Window

	Debug.Clear

	Dim user_folder As String
	user_folder = awrGetScriptArgument()
	Debug.Print user_folder

	If (Len(user_folder) > 0) Then
		' close all the windows first
		Debug.Print "closing windows"
		For Each w In Windows
			w.Close()
		Next w

		For Each x In Project.UserFolders.Folders(user_folder).ProjectItems
			Debug.Print x.Name
			If (x.Type = 0) Then
				Project.Schematics(x.Name).NewWindow()
			End If
			If (x.Type = 5) Then
				Project.Graphs(x.Name).NewWindow()
			End If
		Next x

		Windows.Tile(0)
	Else
		Debug.Print "No folder name specified"
	End If
End Sub
