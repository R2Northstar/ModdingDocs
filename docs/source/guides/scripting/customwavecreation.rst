Creating Custom Missions for Frontier Defense
=============================================
.. Warning::
    There are two different branches for Frontier Defense as of writing this: ``9/1/2023``. What this means there is the `Vanilla`_ branch and the `Experimental`_ 
    branch of Frontier Defense. Anytime that something isn't in the `Vanilla`_ branch will have a warning on it stating that it is from the `Experimental`_ branch.

.. note::
    One last note, when I will be referencing wave(s) as a mission, the overall script to save the headache for wording.

Introductory
------------
Creating Custom Waves for Frontier Defense can be a little tricky as it needs a few things at minimum to run properly. As such you need the following to get it to run properly:

- Shop Position
- Dropship Position
- Dropship Angles
- int index = 1
- index=1
- array<WaveEvent> and  waveEvents.append

Here is a basic setup of the things mentioned above that would let the script run:

.. code-block:: 

    global function initFrontierDefenseData
    void function initFrontierDefenseData()
    {
        shopPosition = < -3862.13, 1267.69, 1060.06 >
	    FD_spawnPosition = < -838.6, 2629.63, 1592 >
	    FD_spawnAngles = < 0, 180, 0 >


        int index = 1
        array<WaveEvent> wave1
        wave1.append(CreateLegionTitanEvent( < 4060, 771, 1100 >, < 0.000000, 180, 0.000000 >,"",0,1,"",FD_TitanType.TITAN_ELITE) )
        waveEvents.append(wave1)
        index=1
        array<WaveEvent> wave2
        wave2.append(CreateLegionTitanEvent( < 4060, 771, 1100 >, < 0.000000, 180, 0.000000 >,"",0,1,"",FD_TitanType.TITAN_ELITE) )
        waveEvents.append(wave2)

    }




What this script does is on the first wave when possible, it will spawn a Legion Titan
at the coordinates and angles when the script is able to for the first wave. 
Afterwards, the second wave starts and spawns yet another Legion Titan at the 
same coordiantes/angles when available to do so. But what does this all mean? Well, I
Will be explaining below what everything means with some extra event types and variables.


Explaining What Everything Does in the Script 
---------------------------------------------

Here is another example of a mission I made to better explain 
some other Event types that you can use in your own script:

.. code-block::

    global function initFrontierDefenseData
    void function initFrontierDefenseData()
    {
        shopPosition = < -3862,1267,1060 >
        shopAngles =  <0,30,0>
        FD_spawnPosition = < -838,2629,1592 >
        FD_spawnAngles = < 0,180,0 >

        int index = 1

        array<WaveEvent> wave1
        wave1.append(CreateSmokeEvent(< 4060,771,1004 >,90,index++))
        wave1.append(CreateWaitForTimeEvent(5,index++))
        wave1.append(CreateWarningEvent(FD_IncomingWarnings.ArcTitanAlt,index++))
        wave1.append(CreateArcTitanEvent(< 4300,771,1004 >,< 0,180,0 >,"",index++))
        wave1.append(CreateDroppodGruntEvent(< 3733,100,1004 >,"",0))
        waveEvents.append(wave1)
        index=1
        array<WaveEvent> wave2
        wave2.append(CreateWarningEvent(FD_IncomingWarnings.LightWave,index++))
        wave2.append(CreateDroppodStalkerEvent(< 2851,4146,1000 >,"",index++))
        wave2.append(CreateLegionTitanEvent(< 4060,771,1004 >,< 0,180,0 >,"",index++))
        wave2.append(CreateWaitForTimeEvent(3,index++))
        wave2.append(CreateWarningEvent(FD_IncomingWarnings.MortarTitanIntro,index++))
        wave2.append(CreateMortarTitanEvent(< 2176,-3541,878 >,< 0,180,0 >,index++))
        wave2.append(CreateWaitForTimeEvent(3,index++))
        wave2.append(CreateMortarTitanEvent(< 2240,4887,1011 >,< 0,180,0 >,index++))
        waveEvents.append(wave2)

    }

Init Functions
##############
.. code-block::

    global function initFrontierDefenseData
    void function initFrontierDefenseData()

- These are what starts the script and calls the functions needed for the gamemode.

Brackets
########
.. code-block::

    {
    }

- This is what houses the main script from start to finish

ShopPosition and Angles
#######################
.. code-block::

    shopPosition = < -3862,1267,1060 >
    shopAngles =  <0,30,0>

- shopPosition spawns the shop at in-game coordinates via X,Y,Z
- shopAngles spawns the shop with rotations if defined via Y,A,P (Yaw, Angle, Pitch)

SpawnPosition and Angles
########################
.. code-block::

    FD_spawnPosition = < -838,2629,1592 >
    FD_spawnAngles = < 0,180,0 >

- FD_spawnPosition and FD_spawnAngles are what tell the game to start the Dropship animation, keep in mind this can be a bit finicky when it comes to positioning it as when respawning, the ship may clip through brushes and terrain.

.. note ::
    Without spawnPosition and spawnAngles, the game **will crash!**

int index
#########

.. code-block::
    
    int index = 1

- This tell the gamescript (Squirrel) to start the wave script.


waveEvents
##########

.. code-block::

    array<WaveEvent> wave1
    waveEvents.append(wave1)

- This is the heart of the script, what tells the game where to spawn/do in-game Events.

Appending Wave Events
#####################
.. code-block::

    array<WaveEvent> wave1
    wave1.append(CreateSmokeEvent(< 4060,771,1004 >,90,index++))
    wave1.append(CreateWaitForTimeEvent(5,index++))
    wave1.append(CreateWarningEvent(FD_IncomingWarnings.ArcTitanAlt,index++))
    wave1.append(CreateArcTitanEvent(< 4300,771,1004 >,< 0,180,0 >,"",index++))
    wave1.append(CreateDroppodGruntEvent(< 3733,100,1004 >,"",0))
    waveEvents.append(wave1)


- Now this is where it gets interesting, inside of the array, this is where you put your Events at for each wave. 
- There are multiple types of events that you can use (Enemies, Time, Smoke, Etc.) which to script it, it always starts with ``wave#.append`` Then the Event type ``CreateSmokeEvent``, then the variables that come after it ``(< 0,0,0 >,90,index++))`` (Which varies on events, which will be Referenced in Cheat Sheet).
- Always, the formula for writing an append goes as follows ``wave#.append(EventHere(VariablesHere,index++/0))``
- An example of this is as follows ``wave1.append(CreateSmokeEvent(< 0,0,0 >,90,index++))``
- ``index++`` or ``0`` is very important to include at the end of your variable listing as shown in the example above, if you do not include it, your script **will crash**!
    - The difference between the two is, ``index++`` advances the script one line in the array as ``0`` is used on the very last wave append to end the array. Failure to include ``0`` at the end of an array **will crash**!

.. note::
    It is very important to keep track of what wave number you are making it for and to document that number for that array. The number can be any number, it can even be inconsistant as long as it's the same number for that array. Failure to do so will cause the script **to crash**!

What Events Can I Make?
#######################

- There are over 26 different events you can make on the `Vanilla`_ branch of Frontier Defense (39 from the `Experimental`_ branch)
- There are two different types of events you can make, there are ``Enemies`` and ``Logic``
    - The Enemy events are self explanatory, they spawn the enemy at XYZ(and YAP, depending on if it uses that variable).
    - The Logic events is what controls how the script runs (Mainly CreateWaitForTimeEvent and CreateWaitUntilAliveEvent)

Enemy Events
^^^^^^^^^^^^

- There are over 21 different enemy types that can be spawned in
    - ``Normal`` (DropPod: Grunt, Ticks, Stalkers, Spectres, Reapers, CloakDrones, Drones)
    - ``Titans`` (Monarch, Legion, Tone, Ronin, Scorch, Ion, NorthstarSniper, ToneSniper)
    - ``Special Titans`` (Arc, Nuke, Mortar)
    - ``Custom Enemy Types`` (GenericSpawn and GenericTitan)
    - ``Smoke`` 
    - The typical structure for adding an enemy goes as follows(Template For every Enemy will be in `Cheat Sheet`_):
.. error::
    If you do not include spaces between the coordinates and angle brackets (<>), the game **will crash!** This applies to anything with coordinates in the script. 
.. note::
    The "" references route points that every maps has, a list will be in `Cheat Sheet`_. It is also Recommended to know said routes as if you spawn an enemy across the map from the route point, it will ignore harvester direction and try to get to the start of the route on the map, then to the harvester.
        - Normal ``wave#.append(Create"EnemyTypeHere"Event(< X,Y,Z >,"",index++/0))``


Logic Events
^^^^^^^^^^^^

- Logic Events is what tells the script when and how to execute the code, or to announce something during the wave (CreateWarningEvent)
- There is over 4 different types of Logic Events
    - ``CreateWaitForTimeEvent``
        - As what it suggests, it waits for a certain amount of time (in seconds, can be a decimal) before executing the next line of code in the script.
    - ``CreateWaitUntilAliveEvent``
        - This Event waits to start the next line of code based on how many enemies are alive on the map.
            - ``Ex``: we set the event to be 5, and we spawn over 8 enemies before this event, the code will wait to execute the next line of code until the enemy count on the map drops to 5 or lower(**Not Meaning Overall Enemy Count!!!**).
    - ``CreateWaitUntilAliveWeightedEvent`` (This event is mostly broken as Zanieon, the main developer for Frontier Defense, doesn't even know what it does.).
        - As Zanieon sums it up: Ngl but this is confusing af to "guess" how the fuck the weights works, say 15 means 3 Titans, but what if i want only the titans to count? i can't because 15 infantry units may get in the way, this a bad way to control the spawning flow.
    - ``CreateWarningEvent``
        - This event creates a warning event for Droz or Davis to announce to everyone on the server what's coming in a wave.

.. dropdown:: CreateWarningEvents Variables

     - CloakDrone
     - ArcTitan
     - Reaper
     - MortarTitan
     - NukeTitan
     - ReaperAlt
     - Ticks
     - Stalkers
     - MortarSpectre
     - ReaperTicks
     - Flyers
     - EliteTitans (`Experimental`_ Branch!)
     - infantry
     - CloakDroneIntro
     - EnemyTitansIncoming
     - MortarTitansIntro
     - NukeTitanIntro
     - ArcTitanInto
     - TitanfallBlocked (`Experimental`_ Branch!)
     - PreNukeTitan
     - PreMortarTitan
     - PreArcTitan
     - Everything
     - LightWave
     - MediumWave
     - HeavyWave
     - NoMoreTitansInWave
     - ArcTitanAlt
     - ComboNukeMortar
     - ComboArcNuke
     - ComboNukeCloak
     - ComboNukeTrain
     


.. note::
    It is very important to include logic (Mainly WaitForTime and WaitUntilAlive) in your script or it may cause a **crash** if you are spamming a lot of enemies at once!

index
#####
- This tell the script to advance squirrel's index to 1, it is used between waves. It is needed or the script **will crash**!

Using Both Event Types in The Example Script
--------------------------------------------

- Lets add A few enemy types and Logic to our Example script from above.
    - For our wave1 array, let's add another Grunt Droppod, a Reaper, and some Logic

.. note::
    It's best not to spam Titans on Wave 1 as no player has a titan, so it's better to lightly spam grunts, if your sadistic enough!


Cheat Sheet
-----------

.. note::
    This cheat sheet is a reference point to help make your scripts for missions


Shop
####

- ``shopPosition = <X,Y,Z>`` As what it suggests, it spawns the shop at in-game coordinates.
- ``shopAngles = <Y,A,P>`` As what it suggests, it changes the shops rotation by either the Yaw, Angle, or Pitch.

Spawning Types(For Pilots):  
###########################

- ``FD_DropPodSpawns.append(< X,Y,Z >)`` 
    - Spawns you in a drop pod and drops you at In-game Coords.
    - Ex. FD_DropPodSpawns.append(< -3000, 226, 1158 >)

Wave Events:
############


Enemy Types:
############

Normal AI:
^^^^^^^^^^

Titans:
^^^^^^^

Elite Titans:
^^^^^^^^^^^^^
.. Warning ::
    The Elite Titans are from the `Experimental`_ branch! Use that branch if you want to use Elite Titans!

.. Note ::
    Special Titans ``Arc, Nuke, Mortar`` **cannot be elites**

To make a Titan an elite, you must add an extra parameter at the end of the create event to set it to an elite:

- ``FD_TitanType.TITAN_ELITE``

And a serverside variable must also be enabled for said elite to spawn, without it, the elite will not spawn in even with the added parameter:

- ``ns_fd_allow_elite_titans 1``

An example of this would be: 

- ``wave5.append(CreateLegionTitanEvent(<4779,-2194,-53>,<0,-170,0>,index++,1,"",FD_TitanType.TITAN_ELITE))``


Troubleshooting
###############

``[SERVER] Index "#" is beyond array size of #``

- What this typically means is when you don't end a wave.append with ``0`` instead of ``index++`` at the end of the WaveEvent array.

- Instead of ending with index++:

.. code-block::

    wave1.append(CreateDroppodGruntEvent(< 4120,800,1004 >,"",index++))
    wave1.append(CreateDroppodGruntEvent(< 4150,730,1004 >,"",index++))
    waveEvents.append(wave1)
    index=1
    array<WaveEvent> wave2

It needs to end with 0:

.. code-block:: 

    wave1.append(CreateDroppodGruntEvent(< 4120,800,1004 >,"",index++))
    wave1.append(CreateDroppodGruntEvent(< 4150,730,1004 >,"",0))
    waveEvents.append(wave1)
    index=1
    array<WaveEvent> wave2

Game Limitations
################

- ``511 Enemies in one wave`` and ``511 Waves at a time``
    - What this means is you can have up to 511 enemies each wave and have up to 511 waves in your mission script. 

.. _Experimental: https://github.com/Zanieon/NorthstarMods/tree/gamemode_fd_experimental
.. _Vanilla: https://github.com/R2Northstar/NorthstarMods/tree/gamemode_fd