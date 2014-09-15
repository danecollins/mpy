
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


Adding a new command
-----------------------------------------------------------------------------
1. If the command requires arguments add it to custom.html
2. Create the function call in awrde.py
3. Add the test in test_awrde.py
4. create the {command}.py
5. Add the test to test_commands.py
6. Add the command to get_command_list() in urltools.py
7. Run the tests
8. Restart server (server needs to reread list of commands)

Things that must be in sync
-----------------------------------------------------------------------------
- urltools.get_command_list() must contain the names of all the commands
- All commands that take arguments must be in custom.html 
  - ideally this file would be generated automatically like index.html TBD



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