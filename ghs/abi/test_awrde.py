
from abi import awrde
import os
from   unittest.mock import patch
from   io import StringIO

awrde.set_test_mode(True)


def test_Simulate():
    
    expected = 'EMULATING Project.Simulate()'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.Simulate()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_OpenSchematic():
    
    expected = 'EMULATING Opening schematic MySchematic'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.OpenSchematic('MySchematic')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_OpenSystemDiagram():
    
    expected = 'EMULATING Opening system diagram MyDiagram'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.OpenSystemDiagram('MyDiagram')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_LoadProject():
    
    expected = 'EMULATING LoadProject(AM.emp)'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.LoadProject('AM.emp')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_CloseWindows():
    
    expected = 'EMULATING Closing All Windows'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.CloseWindows()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)


def test_TileHor():
    
    expected = 'EMULATING Tiling windows horizontally'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.TileWindowsHorizontal()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_TileVer():
    
    expected = 'EMULATING Tiling windows vertically'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.TileWindowsVertical()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_Cascade():
    
    expected = 'EMULATING Cascading windows'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.CascadeWindows()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_OpenUserFolder():
    
    expected = 'EMULATING Opening all items in user folder named MyFolder'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.OpenUserFolder('MyFolder')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_ZoomOnElement():
    
    expected = 'EMULATING Zoming in on element MLIN.TL1 in schematic MySchematic'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.ZoomOnElement('MySchematic', 'MLIN.TL1')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_RunScript_noargs():
    
    expected = 'EMULATING Running script fubar'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.RunScript('fubar')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_RunScript_withargs():

    expected = 'EMULATING Setting argument to myarg\nEMULATING Running script fubar'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.RunScript('fubar', 'myarg')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)
