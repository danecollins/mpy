' Code Module
Sub Main
	Dim x As ProjectItem
	Dim w As Window

	For Each w In Windows
		w.Close()
	Next w

	For Each x In Project.UserFolders.Folders(1).ProjectItems
		If (x.Type = 0) Then
			Project.Schematics(x.Name).NewWindow()
		End If
		If (x.Type = 5) Then
			Project.Graphs(x.Name).NewWindow()
		End If
	Next x

	Windows.Tile(0)
End Sub
