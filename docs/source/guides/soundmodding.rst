Sound Modding
==============

Getting Sounds Played
----------------------

To have sounds be played in-game, you need the audio event name. To get this, go into a private match and enter in the console:``sv_cheats 1`` and then:``ns_print_played_sounds 1``. Then do whatever plays the audio you want to replace and find the event name in the console's output.
Then go to your mod's folder (the one with mod.json), and make a folder called audio. For each sound you want to replace, make a folder called the event and a .json file called the event. In the folder put the sound you want.
In .json, put the following:

.. code-block:: json

    {
        "EventId": [ "name_of_audio_event" ],
        "AudioSelectionStrategy": "random or sequential"
    }

In ``EventId`` put the event name, and in ``AudioSelectionStrategy`` enter random or sequential. If you choose random, the game will pick a random sound from the folder and play it. If you pick sequential, the go down alphebetically and loop back.

Creating Your Sound
--------------------

All sounds need to be .wav files with a sampling rate of 48000 or 44100 and no metadata.
Now you have to slow it down. In Audacity, select your entire sound, go to effects, then change speed. For speed multiplier, put 0.918. For percent change, put -8,200. In standard vinyl rpm make the second box n/a.
