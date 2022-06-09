Sound Modding
==============

**Some of the terms and their meanings in this article;**



-  ``AudioSelectionStrategy`` ("sequential" or "random"): Selection
   strategy for multiple override samples. If you have more than one
   sounds, you can choose ``"random"`` to randomize them, if you have only
   one sound, or more than one sound but you want to play them in alphabetical order, you can simply use ``"sequential"``
-  ``Mod.json:`` is a required file that informs the game engine how to set
   up and use a mod. You can find example template in this article.
-  ``Audio Event IDs:`` Every event has different IDs. In order for the game
   to choose the sound it should play at that moment, it must first know
   its ID. And so do you, to start to change them, you must identify the
   exact sound first.

Audio Type
------------------------------------

-  Use only ``WAV`` format and either ``"48000hz" or "44100hz"`` sample rate.
-  Check the last section of this article for more info and recommended tools.

Step 1 - Identifying the Sound
-------------------------------

First you need to identify the exact sound. There's a command for this:
``ns_print_played_sounds 1`` It will show all the audio events that
are happening at that moment on the console.

For example, use your Grapple and open the console the ID will be
``pilot_grapple_fire``

A console example: |console|

All weapons, boosts, tacticals have different events IDs on different surfaces (concrete, solidmetal, wood, dirt etc.)
That's why you must identify the exact event/s. Examples based on Grapple:

-  Concrete impact: ``concrete_grapple_impact_1p_vs_3p``
-  Solidmetal impact: ``solidmetal_grapple_extract_1p_vs_3p`` etc.


**NOTE:** "ns_print_played_sounds 1" will show you every event ID. Not
just in-match ones. For example:

- The sound when you move the cursor to an option it will be ``menu_focus``, and clicking sound will be ``menu_accept`` or menu music ``mainmenu_music``
- After every sound, you can check the console to identify it.
Step 2 - Creating Folders
-------

When you successfully identified your event and have the audio file/s
ready. It's time to making it.
First of all, you need 2 things:

- Audio Folder - Put your sound file/s in ``Audio`` folder.
- Mod.json file - Basic ``mod.json`` file. There's a template below.

Example of a mod.json:

.. code-block:: json

   {
     "Name": "MOD_NAME_HERE",
     "Description": "DESCRIPTION_HERE",
     "Version": "1.0.0",
     "LoadPriority": 2
   }

**Note: Version number is not that important if you don't want to release the
mod publicly.**

Audio Folder example:

|audiofolder|

Audio folder must contain your audio files as ``WAV`` format either
``48000hz or 44100hz`` sample rate and folder name must be the ``Event
ID.``

For example let's say we are making a Grapple sound mod;

-  ``event_id_here`` (folder, your .wav file must be in it)
-  ``event_id_here.json`` (don't forget to edit)

JSON files must contain "EventID" and "AudioSelectionStrategy"

- Example ``event_id_here.json`` based on this imaginary Grapple sound mod:

.. code-block:: json

   {
       "EventId": [ "pilot_grapple_fire" ],
       "AudioSelectionStrategy": "sequential"
   }

After the whole process you should have ``Audio`` folder and ``mod.json`` file with the all additions I just explained.

Creating Your Sound
--------------------
- **Recommended tool:** `Audacity <https://www.audacityteam.org/download/>`_

Open/Add your audio as a track to Audacity and set your sample rate to
either 48000hz or 44100hz. In Audacity, select your entire track, open
the effects dropdown menu, then click Change Speed. In the dialog set
either Speed Multiplier to 0.918 or Percent Change to -8,200. After
that, export your track as .wav and make sure you don't add any
metadata.

Installation
-------------
-  Basic methods apply.
-  Once you are done with the mod, copy or drag the folder (which contains audio folder and mod.json) to "Titanfall 2/r2Northstar/Mods" and that's all.

.. |audiofolder| image:: https://raw.githubusercontent.com/rwynx/audio-overriding-northstar/main/Images/audiofolder3.png
.. |console| image:: https://raw.githubusercontent.com/rwynx/audio-overriding-northstar/main/Images/audioeventeample.png
