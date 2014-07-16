
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
    
    expected = 'EMULATING Project.Simulate()'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.Simulate()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_OpenProject():
    
    expected = 'EMULATING OpenProject(AM.emp)'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.OpenProject('AM.emp')
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


def test_RunScript_noargs():
    
    expected = 'EMULATING Running script: fubar'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.RunScript('fubar')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_RunScript_withargs():

    expected = 'EMULATING Setting argument to: myarg\nEMULATING Running script: fubar'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        awrde.RunScript('fubar', 'myarg')
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)
