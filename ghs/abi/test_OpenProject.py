import abi.OpenProject
import abi.awrde
import os
from   unittest.mock import patch
from   io import StringIO


def test_html_header():

    os.environ['QUERY_STRING'] ='name=AM.emp'
    
    expected = \
"""Content-type: text/html

<head><title>In Simulate.py</title></head>
<body>
<h1>Command debug log</h1>
<p>Opening project: AM.emp</p>
EMULATING OpenProject(AM.emp)
""".strip()
    with patch('sys.stdout',new=StringIO()) as fake_out:
        abi.OpenProject.main()
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)