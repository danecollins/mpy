'-------------------------------------------------------------------------------
'-- VBS script file
'-- Created on 06/27/2013 15:13:41
'-- Author: 
'-- Comment: 
'-------------------------------------------------------------------------------
Option Explicit  'Forces the explicit declaration of all the variables in a script. 
Dim i, f, fso, Browser, Selection, SelFiles, Msg
Dim MWO, sparfile,name

If Navigator.Display.CurrDataProvider.IsKindOf(eDataFinder) Then 
  Msg = "Files Selected in the Tree-View Browser Are:" & vbCRLF 
  Browser = TRUE 
  Set Selection = Navigator.Display.CurrDataProvider.Browser.SelectedElements 
  IF Selection.Count = 0 THEN 
    Msg = "Files Selected in the Search Results List Are:" & vbCRLF 
    Browser = FALSE 
    Set Selection = Navigator.Display.CurrDataProvider.ResultsList.Selection 
  END IF 
  Msg = Msg & String(60, "-") & vbCRLF 
  SelFiles = GetDiscreteFiles(Selection, Browser)
  ' Now have the list of info files but need the list of spar files
  rem Set fso = CreateObject("Scripting.FileSystemObject") 
  rem Set f = fso.OpenTextFile(AutoActPath & "Selected File Paths.txt", 2, True)
  set MWO = CreateObject("AWR.MWOffice.11.0")
  FOR i = 1 TO UBound(SelFiles)
    ''' convert get spar filename and open in MWO
    sparfile = InfoToSparFilename(SelFiles(i).Properties("fullpath").Value)
    name = GetFilename(SelFiles(i).Properties("fullpath").Value)
    
    call MWO.Project.DataFiles.Add(name,sparfile,False,0)
  NEXT 

End if 

Function InfoToSparFilename(fn)
  Dim filebase
  
  filebase = mid(fn,1,len(fn)-7)
  filebase = filebase & "s2p"
  InfoToSparFilename = filebase
End Function 'InfoToSparFilename

Function GetFilename(fn)
  Dim filebase
  
  filebase = mid(fn,1,len(fn)-8) 'one more than above to get rid of .
  filebase = mid(filebase,instrrev(filebase,"\")+1)
  GetFilename = filebase
end Function


Function GetDiscreteFiles(Selection, Browser) 
  Dim i, k, SelectionType, SelFiles, FilePath, PathDict 
  Set PathDict = CreateObject("Scripting.Dictionary") 
  ReDim SelFiles(0) 
  IF Selection.Count > 0 THEN 
    SelectionType = GetSelType(Selection, Browser) 
    Select Case SelectionType 
      Case eSearchFile 
        ReDim SelFiles(Selection.Count) 
        FOR i = 1 TO Selection.Count 
          Set SelFiles(i) = Selection(i) 
        NEXT ' i 
      Case eSearchChannelGroup 
        ReDim SelFiles(Selection.Count) 
        FOR i = 1 TO Selection.Count 
          FilePath = Selection(i).Root.Properties("fullpath").Value 
          IF FilePath <> "" THEN 
            IF NOT PathDict.Exists(FilePath) THEN 
              k = k + 1 
              ReDim Preserve SelFiles(k) 
              Set SelFiles(k) = Selection(i).Root 
              PathDict.Add FilePath, k 
            END IF 
          END IF ' FilePath <> "" THEN 
        NEXT ' i 
        ReDim Preserve SelFiles(k) 
      Case eSearchChannel 
        ReDim SelFiles(Selection.Count) 
        FOR i = 1 TO Selection.Count 
          FilePath = Selection(i).ChannelGroup.Root.Properties("fullpath").Value 
          IF FilePath <> "" THEN 
            IF NOT PathDict.Exists(FilePath) THEN 
              k = k + 1 
              ReDim Preserve SelFiles(k) 
              Set SelFiles(k) = Selection(i).ChannelGroup.Root 
              PathDict.Add FilePath, k 
            END IF 
          END IF ' FilePath <> "" THEN 
        NEXT ' i 
        ReDim Preserve SelFiles(k) 
    End Select ' SelectionType 
  END IF ' Selection.Count > 0 
GetDiscreteFiles = SelFiles 
End Function ' GetDiscreteFiles() 


Function GetSelType(Selection, Browser) 
  Dim SelectionType 
  IF NOT Selection.Count > 0 THEN Exit Function 
  IF (Browser) THEN 
    SelectionType = GetElemType(Selection(1)) 
  ElseIF Selection.IsKindOf(eElementsSelection) THEN 
    SelectionType = GetElemType(Selection(1)) 
  ElseIF Selection.IsKindOf(eColumnsSelection) THEN 
    SelectionType = eColumnsSelection 
  ElseIF Selection.IsKindOf(eCellsSelection) THEN 
    SelectionType = eCellsSelection 
  END IF ' Selection is Element, Cell, or Column 
GetSelType = SelectionType 
End Function ' GetSelType() 


Function GetElemType(Element) 
  Dim ElementLevel 
  IF Element.IsKindOf(eComputerFolder) THEN 
    ElementLevel = eComputerFolder 
  ElseIF Element.IsKindOf(eSearchFolder) THEN 
    ElementLevel = eSearchFolder 
  ElseIF Element.IsKindOf(eComputerFile) THEN 
    ElementLevel = eComputerFile 
  ElseIF Element.IsKindOf(eSearchFile) THEN 
    ElementLevel = eSearchFile 
  ElseIF Element.IsKindOf(eSearchChannelGroup) THEN 
    ElementLevel = eSearchChannelGroup 
  ElseIF Element.IsKindOf(eSearchChannel) THEN 
    ElementLevel = eSearchChannel 
  END IF ' Element.IsKindOf() 
GetElemType = ElementLevel 
End Function ' GetElemType() 
