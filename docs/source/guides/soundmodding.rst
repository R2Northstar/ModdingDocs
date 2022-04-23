 Sound Modding
 =============
 Getting Sounds Played
----------------------
To have sounds be played in-game, you need the audio event name. To get this, go into a private match and enter in the console:``sv_cheats 1`` and then:``ns_print_played_sounds 1``. Then do whatever plays the audio you want to replace and find the event name in the console's output.
Then go to your mod's folder (the one with mod.json), and make a folder called audio. For each sound you want to replace, make a folder called the event and a .json file called the event. In the folder put the sound you want.
In .json, put the following:
``{
	"EventId": [ "name_of_audio_event" ],
	"AudioSelectionStrategy": "random or sequential"
}``
In ``EventId`` put the event name
In ``AudioSelectionStrategy`` enter random or sequential
random: it will pick a random file from the folder and play it
sequential: it will go down alphetabetically

Creating Your Sound
--------------------
All sounds need to be .wav files with a sampling rate of 48000 or 44100 and no metadata.
Now you have to slow it down. In Audacity, select your entire sound, go to effects, then change speed. For multiplication factor, put 0,918. For percentage change, put -8,200. In standard vinyl rpm (translation error fix later) put 33 and 1/2 and "no disposable"

.. note::
    might be translation errors come back and fix those