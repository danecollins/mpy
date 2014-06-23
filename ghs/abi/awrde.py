
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

TEST_MODE = False ## set the defailt

def test_mode():
    return TEST_MODE

def set_test_mode(m):
    global TEST_MODE
    TEST_MODE = m


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
        html_test('Project.OpenSchematic(%s)' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde_com_obj):
            html_message("Opening schematic: %s" % name)
            awrde_com_obj.Project.Schematics(name).NewWindow()
        else:
            html_error('Could not connect to AWR Design Environment')

def OpenProject(name):
    if test_mode():
        html_test('OpenProject(%s)' % name)
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

def RunScript(name):
    if test_mode():
        html_test('Running script: %s' % name)
    else:
        awrde_com_obj=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde.Project.ProjectScripts.Item(script_name).Routines.Item("Main").Run()
        
  
