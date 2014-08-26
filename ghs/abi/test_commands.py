
import abi.awrde
import os
from   unittest.mock import patch
from   io import StringIO

abi.awrde.set_test_mode(True)

import abi.CloseWindows #############################################
def test_CloseWindows():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Closing All Windows
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.CloseWindows.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.LoadProject #############################################
def test_LoadProject_without_name():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
<p><font color=red>Link has no project name.</font></p>
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.LoadProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)


def test_LoadProject_with_name_without_simulation():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
<p>Opening project: AM.emp</p>
EMULATING LoadProject(AM.emp)
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=AM.emp'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.LoadProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_LoadProject_with_name_with_simulation():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
<p>Opening project: AM.emp</p>
EMULATING LoadProject(AM.emp)
EMULATING Project.Simulate()
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=AM.emp&simulate=1'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.LoadProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.OpenSchematic ############################################
def test_OpenSchematic():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Opening schematic MySchematic
EMULATING Cascading windows
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=MySchematic'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenSchematic.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.OpenSystemDiagram ############################################
def test_OpenSystemDiagram():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Opening system diagram Tranceiver
EMULATING Cascading windows
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=Tranceiver'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenSystemDiagram.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.OpenUserFolder ###########################################
def test_OpenUserFolder():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Opening all items in user folder named MyFolder
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=MyFolder'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenUserFolder.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.RunScript ################################################
def test_RunScript_without_args():
    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
<p>Running script MyScript</p>
EMULATING Running script MyScript
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=MyScript'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.RunScript.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)    


def test_RunScript_with_arg():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
<p>Running script MyScript with argument MyArg</p>
EMULATING Setting argument to MyArg
EMULATING Running script MyScript
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=MyScript&arg=MyArg'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.RunScript.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected) 

import abi.Simulate #################################################
def test_Simulate():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Project.Simulate()
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.Simulate.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

import abi.TileHorizontal #################################################
def test_TileHorizontal():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Tiling windows horizontally
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.TileHorizontal.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)


import abi.TileVertical #################################################
def test_TileVertical():

    expected = \
"""Content-type: text/html

<head><title>In ABI Command</title></head>
<body>
<h1>Command debug log</h1>
EMULATING Tiling windows vertically
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.TileVertical.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)