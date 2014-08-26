
Test Structure
-----------------------------------------------------------------------------
urltools.py
  * handles printing help messages
  * handles url processing
  * handles getting files from the internet

  Tested by test_urltools.py
    * py.test urltools.py
    * lowest level, should be tested first

awrde.py
  * interfaces with awrde, no other file connects to awrde
  * provides high level functions to run commands.  one function per command
  
  Tested by test_awrde.py
    * py.test awrde.py
    * lowest level, should be tested first

{Command}.py
  * All commands are listed in urltools.get_command_list
  * Each command is in a separate file named {command}.py
  * Commands have a doc section which is used to generate index.html
  * Commands that take arguments have to be added to confluence/custom.html

  Tests are performed by test_command.py
    * py.test test_command.py
    * should make sure awrde.py and urltools.py tests run first



Things that must be in sync
-----------------------------------------------------------------------------
- urltools.get_command_list() must contain the names of all the commands


Generating docs (index.html)
-----------------------------------------------------------------------------
cd html
genindex.py
cp index.html ..


Idiosyncracies
-----------------------------------------------------------------------------
We have both OpenProject and LoadProject.  LoadProject is preferred because
it is consistent with LoadSchematic and LoadSystemDiagram but OpenProject is
retained for backward compatibility.