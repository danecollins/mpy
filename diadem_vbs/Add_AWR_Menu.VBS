'-------------------------------------------------------------------------------
'-- VBS script file
'-- Created on 07/31/2013 08:41:25
'-- Author: 
'-- Comment: 
'-------------------------------------------------------------------------------
Option Explicit  'Forces the explicit declaration of all the variables in a script.
' Create new custom menu item
Call MenuItemAdd("NAVIGATOR","7","PopUp","AWR Interface")
 
' Add a new item to the menu
Call MenuItemAdd("NAVIGATOR","7.1","MenuItem","Selected to MWO","ScriptStart(""Export_to_mwo_script.vbs"")")
