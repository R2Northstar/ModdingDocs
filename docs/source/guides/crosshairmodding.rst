Crosshair Modding
=====================


Example Mod - Feel free to use this with your own mod

`Custom.Crosshairs <https://github.com/MysteriousRSA/Custom.Crosshairs>`__


INSTRUCTIONS
============
Using the example mod to create/modify a weapon's crosshair(s)


Installing the example mod:
-----------------------------

This mod is compatible with:

`VTOL <https://github.com/BigSpice/VTOL>`__,
`Viper <https://github.com/0neGal/viper>`__ And
`Thunderstore <https://northstar.thunderstore.io/>`__

Manual Installation:
--------------------

1: Download the latest release `From the Release
Page <https://github.com/MysteriousRSA/Custom.Crosshairs/releases>`__

2: Extract the zip file and move the folder "Mysterious.Crosshairs" to
``~\Titanfall2\R2Northstar\mods\``

Common Game Install Locations:

Steam: ``C:\Program Files (x86)\Steam\steamapps\common\Titanfall2``

Origin: ``C:\Program Files (x86)\Origin Games\Titanfall2``

|location|

How To Modify Crosshairs:
-------------------------

1: Go to
``~/Titanfall2/R2Northstar/mods/Mysterious.Crosshairs/keyvalues/scripts/weapons/mp_weapon_[desired weapon].txt``

2: you'll see something that looks like this:

::

   WeaponData
   {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_alternator" //This is the part you want to change
           }
       }
   }

3: change "ui/crosshair_alternator" to your desired crosshair NOTE:
Sometimes it helps to remove //comments

Overlapping Crosshairs
----------------------

It is possible to combine crosshairs by modifying the mp_weapon_[Desired
Weapons].txt

**Below is an example of combining the Alternator and R201 crosshairs
into one**

::

   WeaponData
   {
       active_crosshair_count              "2" //Amount of crosshairs you want to use

       RUI_CrosshairData
       {
           Crosshair_1                                                                     //Crosshair 1 Start
           {
               "ui"                        "ui/crosshair_alternator"   //First Crosshair
           }                                                                               //Crosshair 1 End
           Crosshair_2                                                                     //Crosshair 2 Start
           {
               "ui"                        "ui/crosshair_tri"          //Second Crosshair
           }                                                                               //Crosshair 2 End
       }
   }

**To add more crosshairs add another Crosshair\_\ X following the
formating in the script above.**

**The limit for this seems to be 4 Crosshairs onscreen at once**

How the script above appears:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|triandaltCH|

Adjust Crosshair Spread?
------------------------

| Simple add
| ``"base_spread"               "3.0"   //This is a spread Multiplier``
  Below the "ui" line, Like this

::

    {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_alternator" //THis is the Croshair
               "base_spread"               "3.0"   //This is a spread Multiplier, Line doesn't exist by default
           }
       }
   }

NOTE: This only affects the visual spread of the crosshair, not the actual
bullet spread. Positive Values increase spread while negative decrease
it.

No Crosshair?
-------------

::

   WeaponData
   {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_sniper_amped" //This means NO crosshair
           }
       }
   }

Crosshair Index:
----------------

These are the available crosshairs in-game, along with their in-game
reference:

|Crosshair examples|

Crosshair images are taken from the modding guide on
`https://noskill.gitbook.io/titanfall2/ <https://noskill.gitbook.io/titanfall2/>`__

Examples
--------

|CH1| |CH2|

.. _something-cursed:


Extra Info
==========

It is recommended to test this out in a private match first. Save any
changes you made to the desired weapon's file and type ``reload`` in
your console

All weapons that make use of special crosshairs have their defaults in
place, But there is nothing preventing you from modifying them, all the
files are there.

Keep in mind that some weapons have animated or dynamic crosshairs.
Weapons like the Charge Rifle, Cold Wae, Frag Grenade, etc... have
especially animated crosshairs. which can cause weirdness or jank when
used on other weapons or when using other crosshairs on them.
Animated weapons like the Charge rifle will work with animated crosshairs like ``ui/crosshair_titan_sniper``

Thank you to ``Cpone#0001`` from the `Northstar
Discord <https://northstar.tf/discord>`__ for helping me figure this out

Any Issues? Create an issue, or message me on Discord
``Mysterious#7899``

More info can be found `HERE <https://youtu.be/dQw4w9WgXcQ>`__


.. |Mod512Round| image:: https://user-images.githubusercontent.com/45333346/152405018-caa1be1b-f12e-42df-a62b-a7cff27a3142.png
.. |location| image:: https://user-images.githubusercontent.com/45333346/149657078-86db15a0-0ecc-4d53-9265-23d80a072cea.jpg
.. |triandaltCH| image:: https://user-images.githubusercontent.com/45333346/149623038-64937ab7-bb0f-450c-ba92-97c625e715bf.png
.. |Crosshair examples| image:: https://github.com/Riccorbypro/Custom.Crosshairs/raw/main/assets/crosshairs.png
.. |CH1| image:: https://user-images.githubusercontent.com/45333346/149503054-45eb1fa5-5e89-4bf1-bf58-b58c1bfab94b.png
.. |CH2| image:: https://user-images.githubusercontent.com/45333346/149503085-154c05b8-4a76-4d03-80aa-fe67fba1bcb1.png
.. |cursed| image:: https://user-images.githubusercontent.com/45333346/149503158-453c8879-df8d-45ca-845e-b5ef691c5566.png
 th
