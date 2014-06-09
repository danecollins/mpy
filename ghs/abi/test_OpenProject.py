import abi.OpenProject
import abi.awrde
import os
from   unittest.mock import patch
from   io import StringIO


def test_without_name():

    expected = \
"""Content-type: text/html

<head><title>In Simulate.py</title></head>
<body>
<h1>Command debug log</h1>
<p><font color=red>Link has no project name.</font></p>
</body>
""".strip()

    os.environ['QUERY_STRING'] =''

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)


def test_with_name_without_simulation():

    expected = \
"""Content-type: text/html

<head><title>In Simulate.py</title></head>
<body>
<h1>Command debug log</h1>
<p>Opening project: AM.emp</p>
EMULATING OpenProject(AM.emp)
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=AM.emp'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

def test_with_name_with_simulation():

    expected = \
"""Content-type: text/html

<head><title>In Simulate.py</title></head>
<body>
<h1>Command debug log</h1>
<p>Opening project: AM.emp</p>
EMULATING OpenProject(AM.emp)
EMULATING Project.Simulate()
</body>
""".strip()

    os.environ['QUERY_STRING'] ='name=AM.emp&simulate=1'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

