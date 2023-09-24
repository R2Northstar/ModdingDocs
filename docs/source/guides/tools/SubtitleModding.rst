Subtitle Modding
================

Subtitles Overview
------------------

In Titanfall 2 Subtitles are stored in ``.dat`` files which are essentially just "Valve Close Caption Data" files.
These files are located in the frontend VPK's.


Prequisites
-----------
	`VCCDSON <https://github.com/EM4Volts/vccdson>`__ 


.. note::
    VCCDSON is new and not tested with exotic characters from non latin languages.
    If used for cyrillic languages or other languages with non latin symbols
    it may ERROR or output non-valid .dat files.
    Please report Errors on github as an issue.


Editing Subtitles
-----------------
1. With a valid installation of Python 3 and VCCDSON just drag your desired subtitle ``.dat`` file on VCCDSON's ``main.py``.
2. Open the newly created ``.json`` and edit the Subtitles to your liking.
3. When done drag the ``.json`` on VCCDSON's ``main.py``.
4. Your new subtitle ``.dat`` should now be created.

    
Commands
^^^^^^^^

Subtitle strings can contain command blocks, recognizable by them being enclosed in < >


.. cpp:var:: <clr:red,green,blue>

    Signals the subtitles following the command to be colored in the used RGB values ranging from 0-255, can be used to change color mid sentence.
.. cpp:var:: <len:0>

    Will make the following text to be displayed for the amount specified in seconds.
.. cpp:var:: <delay:0>

    Will make the following text be delayed for the specified amount of seconds.
.. cpp:var:: <cr>

    Adds a newline at selected point in the string.
.. cpp:var:: <b>

    The following text will be Bold.
.. cpp:var:: <I>
    
    The following text will be italic.


