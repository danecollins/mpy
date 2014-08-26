
import os
import sys
import datetime
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi.urltools import html_message, html_error, html_test

## This file contains all the code that directly interfaces with awrde_com_obj
## and provides simple functions called by the web interface


if os.name == 'nt':
    import win32com.client
    awrc = win32com.client.constants


TEST_MODE = False ## set the defailt

def test_mode():
    return TEST_MODE

def set_test_mode(m):
    global TEST_MODE
    TEST_MODE = m

##
## Internal Utility functions
##
def setArgument(val):
    if test_mode():
        html_test('Setting argument to ' + val)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if awrde_com_obj:
            awrde_com_obj.SetUserSetting("ABI","arg1",val)
        else:
            html_error('Could not connect to AWR Design Environment')

##
## Public functions
##
def Simulate():
    if test_mode():
        html_test('Project.Simulate()')
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if awrde_com_obj:
            awrde_com_obj.Project.Simulate()
            html_message('Simulate command sent')
        else:
            html_error('Could not connect to AWR Design Environment')

def OpenSchematic(name):
    if test_mode():
        html_test('Opening schematic %s' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening schematic %s" % name)
            awrde_com_obj.Project.Schematics(name).NewWindow()
        else:
            html_error('Could not connect to AWR Design Environment')

def LoadSchematic(name):
    if test_mode():
        html_test('LoadSchematic(%s)' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening schematic: %s" % name)
            # to import we need the base name of the schematic
            imported_name = os.path.basename(name).strip('.sch')
            awrde_com_obj.Schematics.Import(imported_name,name)
        else:
            html_error('Could not connect to AWR Design Environment')

def OpenSystemDiagram(name):
    if test_mode():
        html_test('Opening system diagram %s' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening system diagram: %s" % name)
            awrde_com_obj.Project.SystemDiagrams(name).NewWindow()
        else:
            html_error('Could not connect to AWR Design Environment')

def LoadSystemDiagram(name):
    if test_mode():
        html_test('LoadSystemDiagram(%s)' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening system diagram: %s" % name)
            # to import we need the base name of the system diagram
            imported_name = os.path.basename(name).strip('.sys')
            awrde_com_obj.SystemDiagrams.Import(imported_name,name)
        else:
            html_error('Could not connect to AWR Design Environment')

def LoadProject(name):
    if test_mode():
        html_test('LoadProject(%s)' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening project: %s" % name)
            awrde_com_obj.Open(name)
        else:
            html_error('Could not connect to AWR Design Environment')


def CloseWindows():
    if test_mode():
        html_test('Closing All Windows')
    else:
        html_message("Closing all windows")
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        for window in awrde_com_obj.Windows:
            window.close()

def TileWindowsHorizontal():
    if test_mode():
        html_test('Tiling windows horizontally')
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde_com_obj.Windows.Tile(1)

def TileWindowsVertical():
    if test_mode():
        html_test('Tiling windows vertically')
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde_com_obj.Windows.Tile(0)       

def CascadeWindows():
    if test_mode():
        html_test('Cascading windows')
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde_com_obj.Windows.Cascade()

def OpenUserFolder(name):
    if test_mode():
        html_test('Opening all items in user folder named %s' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening user folder: %s" % name)
            # close all windows first
            for win in awrde_com_obj.Windows:
                win.Close()

            for item in awrde_com_obj.Project.UserFolders.Folders(name).ProjectItems:
                item = win32com.client.CastTo(item,'IProjectItem')
                
                if (item.Type == awrc.mwPIT_Schematic):
                    awrde_com_obj.Project.Schematics(item.Name).NewWindow()

                if (item.Type == awrc.mwPIT_Graph):
                    awrde_com_obj.Project.Graphs(item.Name).NewWindow()

                    awrde_com_obj.Windows.Tile(0)
        else:
            html_error('Could not connect to AWR Design Environment')

def ZoomOnElement(sch, id):
    if test_mode():
        html_test('Zoming in on element %s in schematic %s' % (id, sch))
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            sch_obj = awrde_com_obj.Project.Schematics(sch)
            element_obj = sch_obj.Elements(id)
            if (sch_obj.Views.Count == 0):
                sch_obj.NewWindow()

            left = element_obj.Left
            top  = element_obj.Top
            width = element_obj.Width
            height = element_obj.Height
            newleft  = left - width*.2
            newtop   = top - height*.2
            right = left + width*1.2
            bottom = top + height*1.2
            sch_obj.Views(1).ViewArea(newleft, newtop, right, bottom)
        else:
                html_error('Could not connect to AWR Design Environment')


def RunScript(*args):
    name = args[0]
    if (len(args) > 1):
        setArgument(args[1])

    if test_mode():
        html_test('Running script %s' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde_com_obj.Project.ProjectScripts.Item(name).Routines.Item("Main").Run()
        
  
