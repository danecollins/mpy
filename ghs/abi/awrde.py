
import os
import sys
import datetime
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi.urltools import html_message, html_error, html_test

## This file contains all the code that directly interfaces with AWRDE
## and provides simple functions called by the web interface


if os.name == 'nt':
    import win32com.client

AWRDE_TEST_MODE = True

def test_mode():
    return AWRDE_TEST_MODE

def set_test_mode(m):
    AWRDE_TEST_MODE = m


def Simulate():
    if test_mode():
        html_test('Project.Simulate()')
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        if awrde:
            awrde.Project.Simulate()
            html_message('Simulate command sent')
        else:
            html_error('Could not connect to AWR Design Environment')

def OpenSchematic(name):
    if test_mode():
        html_test('Project.OpenSchematic(%s)' % name)
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde):
            html_message("Opening schematic: %s" % name)
            awrde.Project.Schematics(name).NewWindow()
        else:
            html_error('Could not connect to AWR Design Environment')

def OpenProject(name):
    if test_mode():
        html_test('OpenProject(%s)' % name)
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        if (awrde):
            html_message("Opening project: %s" % name)
            awrde.Open(name)
        else:
            html_error('Could not connect to AWR Design Environment')


def CloseAllWindows():
    if test_mode():
        html_test('Closing All Windows')
    else:
        html_message("Closing all windows")
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        for window in awrde.Windows:
            window.close()

def TileWindowsHorizontal():
    if (test_mode):
        html_test('Tiling windows horizontally')
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde.Windows.Tile(1)

def TileWindowsVertical():
    if (test_mode):
        html_test('Tiling windows vertically')
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde.Windows.Tile(0)       

def CascadeWindows():
    if (test_mode):
        html_test('Cascading windows')
    else:
        awrde=win32com.client.Dispatch("MWOApp.MWOffice")
        awrde.Windows.Cascade()
  