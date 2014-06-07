
from abi import awrde
import os
from   unittest.mock import patch
from   io import StringIO


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