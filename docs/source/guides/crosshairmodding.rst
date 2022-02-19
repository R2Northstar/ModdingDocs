Crosshair Modding
=====================


This guide shows how the following example mod was made

`Custom.Crosshairs <https://github.com/MysteriousRSA/Custom.Crosshairs>`__


INSTRUCTIONS
============

How To Modify Crosshairs:
-------------------------

1: create the following files
``~/Titanfall2/R2Northstar/mods/Your.Mod/keyvalues/scripts/weapons/mp_weapon_[desired weapon].txt``
   * [Desired_weapon.txt]'s name must match the weapon's .nut file name if it has one
   * mp_weapon_sniper.nut = mp_weapon_sniper.txt
   
2: Add the following into the newly created .txt file

::

   WeaponData
   {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_alternator"
           }
       }
   }

3: change "ui/crosshair_alternator" to your desired crosshair, as shown in the Crosshair Index

Overlapping Crosshairs
----------------------
It is possible to combine crosshairs by modifying the mp_weapon_[Desired_Weapons].txt

**Below is an example of combining the Alternator and R201 crosshairs
into one**

::

   WeaponData
   {
       active_crosshair_count              "2" 
       RUI_CrosshairData
       {
           Crosshair_1                                                                     
           {
               "ui"                        "ui/crosshair_alternator"   
           }                                                                               
           Crosshair_2                                                                     
           {
               "ui"                        "ui/crosshair_tri"          
           }                                                                               
       }
   }

* active_crosshair_count should be set to the amount of crosshairs you wish to overlap

**To add more crosshairs add another Crosshair\_\ X following the
formating in the script above.**

**The limit for this seems to be 4 Crosshairs onscreen at once**

How the script above appears:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|triandaltCH|

Adjust Crosshair Spread?
------------------------

| Simply add the following line
| ``"base_spread"               "3.0"``
|  Below the "ui" line, Like this

::

    {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_alternator" // This is the Croshair
               "base_spread"               "3.0"   // This is a spread Multiplier, Line doesn't exist by default
           }
       }
   }

* NOTE: This only affects the visual spread of the crosshair, not the actual bullet spread. Positive Values increase spread while negative decrease it.
   * Range seems to be "-10" to "10"

No Crosshair?
-------------

::

   WeaponData
   {   
       RUI_CrosshairData
       {
           Crosshair_1 
           {
               "ui"                        "ui/crosshair_sniper_amped" 
           }
       }
   }

* "ui/crosshair_sniper_amped" means NO crosshair is shown

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

* It is recommended to test this out in a private match first. Save any changes you made to the desired weapon's file and type ``reload`` in your console

* All weapons that make use of special crosshairs have their defaults in place, But there is nothing preventing you from modifying them, all the files are there.

* Keep in mind that some weapons have animated or dynamic crosshairs. Weapons like the Charge Rifle, Cold Wae, Frag Grenade, etc... have especially animated crosshairs. which can cause weirdness or jank when used on other weapons or when using other crosshairs on them.
   * Animated weapons like the Charge rifle will work with animated crosshairs like ``ui/crosshair_titan_sniper``

Thank you to ``Cpone#0001`` and ``Nixie#8251`` from the `Northstar
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
