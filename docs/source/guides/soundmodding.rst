Sound Modding
==============

**Some of the terms and their meanings in this article;**

-  ``mod.json`` documented here: :doc:`/guides/gettingstarted`. You can find an example template in this article.
-  ``AudioSelectionStrategy`` (``sequential`` or ``random``): Selection
   strategy for multiple override samples. If you have one sound or you want to play them in alphabetical order,
   choose ``sequential``. If you have more than one sound and you want to randomize them, you can choose ``random``.
-  ``Audio Event IDs`` Every event has a different ID. In order for the game
   to choose the sound it should play at that moment, it must first know
   its event ID. To start to change sounds, you must identify the 
   event ID which plays it first.

Audio Type
-----------

-  You will need to use ``WAV`` format and either ``48000hz`` or ``44100hz`` sample rate.
-  more details later in :ref:`Creating Your Sound`

Step 1 - Identifying the Sound
-------------------------------

First you need to identify the exact sound. There's a command for this:
``ns_print_played_sounds 1`` It will show all the audio events that
are happening at that moment on the console.

For example, use your Grapple and open the console the event ID will be
``pilot_grapple_fire``

Hot it looks in the console: |console|

All weapons, boosts, tacticals have different events IDs on different surfaces (concrete, solidmetal, wood, dirt etc.)
That's why you must identify the exact event/s. Examples based on Grapple:

-  Concrete impact: ``concrete_grapple_impact_1p_vs_3p``
-  Solidmetal impact: ``solidmetal_grapple_extract_1p_vs_3p`` etc.


**NOTE:** ``ns_print_played_sounds 1`` will show you every event ID. Not
just in-match ones. For example:

- The sound when you move the cursor to an option it will be ``menu_focus``, and clicking sound will be ``menu_accept`` or menu music ``mainmenu_music``
- After every sound, you can check the console to identify it.

Step 2 - Creating Folders
--------------------------

When you successfully identified your event and have the audio file/s
ready it's time to set up the folder structure.
Assuming the event name is ``pilot_grapple_fire``, the folder structure of your mod should look like this:

.. code-block::
   
   author.mod/
   ├── audio/
   │   ├── pilot_grapple_fire/
   │   │   └── my_audio.wav
   │   └── pilot_grapple_fire.json
   └── mod.json
   

Example of a ``mod.json``

.. code-block:: json

   {
     "Name": "MOD_NAME_HERE",
     "Description": "DESCRIPTION_HERE",
     "Version": "0.1.0",
     "LoadPriority": 2
   }


**Inside the ``audio/`` folder:**

-  ``pilot_grapple_fire/`` folder which needs to contain your .wav file(s)
-  ``pilot_grapple_fire.json`` json used to configure the sound override, dont forget to edit.

You will have to add that folder with your sound and the json for each event you want to override.
The event JSON files must contain both EventId and AudioSelectionStrategy like this:

.. code-block:: json

   {
       "EventId": [ "pilot_grapple_fire" ],
       "AudioSelectionStrategy": "sequential"
   }

Creating Your Sound
--------------------
- **Recommended tool:** `Audacity <https://www.audacityteam.org/download/>`_

Open/Add your audio as a track to Audacity and set your sample rate to
either ``48000hz`` or ``44100hz``. In Audacity, select your entire track, open
the effects dropdown menu, then click ``Change Speed``. In the dialog set
either ``Speed Multiplier`` to ``0.918`` or ``Percent Change`` to ``-8,200``. After
that, export your track as ``wav`` and make sure you don't add any
metadata.

Installation
-------------
-  As with any mod, the folder which contains your ``mod.json`` needs to be inside ``Titanfall 2/r2Northstar/Mods/``.

.. |console| image:: https://raw.githubusercontent.com/rwynx/audio-overriding-northstar/main/Images/audioeventeample.png
