Damage History 
==============

Damage history stores the information of damage in a struct.

DamageHistoryStruct
-------------------
============================ ===================================================================
Variable name                short description
============================ ===================================================================
string attackerName          name of the attacker
string attackerPetName       name of the titan
vector origin                position of the victim
float damage                 The amount of damage inflicted
int damageType               A value from the :ref:`damage-flag-overview`
int damageSourceId           Damage souce ID from the gun ( :ref:`damage-source-id-overview` )
entity attacker              Entity of the attacker
int attackerEHandle          
float attackerHealthPercent  How much health the attacker has in %
float time                   When the damage was inflicted
array<string> weaponMods     Array of mods on the attacking gun
bool victimIsTitan           ``true`` if the victim died in the Titan
bool rodeoDamage             ``true`` if the damage was inflicted in rodeo mode
============================ ===================================================================

Getting the damage history
--------------------------

Geting the info from the entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get the damage history for any player entity with ``player.e.recentDamageHistory``, this is of the type ``array<DamageHistoryStruct>`` and gets automatically updated by the game. The higher the index the older the ``DamageHistoryStruct`` is ( so you would get the most recent struct you do ``player.e.recentDamageHistory[ 0 ]`` ).

Getter functions
^^^^^^^^^^^^^^^^

.. cpp:function:: array<DamageHistoryStruct> GetDamageEventsForTime( entity player, float time )

    :param entity player: The player you want the damage histroy from.

    :param float time: How old the damage history can be in seconds.

    :returns: All ``DamageHistoryStruct`` found in the given time frame.

Setter functions
^^^^^^^^^^^^^^^^


.. cpp:function:: DamageHistoryStruct function StoreDamageHistoryAndUpdate( entity storeEnt, float maxTime, float damage, vector damageOrigin, int damageType, int damageSourceId, entity attacker = null, array<string> weaponMods = [] )


.. cpp:function:: void function UpdateDamageHistory( entity player, float maxTime, float time )

    Removes all ``DamageHistoryStruct`` in the time frame ``time - maxTime``

    :param entity player: The player you want to update the damage histroy from.

    :param float maxTime: How old the damage history can maximally be

    :param float time: How old the damage history can be in seconds.


Build in Checks
---------------

.. cpp:function:: float function GetLastDamageTime( entity player )
.. cpp:function:: bool function WasRecentlyHitByEntity( entity player, entity ent, float hitTime )
.. cpp:function:: bool function WasRecentlyHitForDamage( entity player, float damageAmount, float hitTime )
.. cpp:function:: bool function WasRecentlyHitForDamageType( entity player, float damageType, float hitTime )
.. cpp:function:: float function GetTotalDamageTaken( entity player )
.. cpp:function:: float function GetTotalDamageTakenInTime( entity player, float hitTime )
.. cpp:function:: array<entity> function GetTitansHitMeInTime( entity player, float hitTime )
.. cpp:function:: float function GetTotalDamageTakenByPlayer( entity player, entity attacker )
.. cpp:function:: array<AttackerDamage> function GetDamageSortedByAttacker( entity ent, float totalTime )
.. cpp:function:: bool function WasRecentlyHitByDamageSourceId( entity player, int damageSourceId, float hitTime )
.. cpp:function:: AssistingPlayerStruct function GetLatestAssistingPlayerInfo( entity ent )

    .. note:: 

        The ``AssistingPlayerStruct`` has the following elements:

        * entity player
        * int damageSourceId
        * float assistTime

.. cpp:function:: array<DamageHistoryStruct> function GetRodeoAttacksByPlayer( entity player, entity attacker, float time )
.. cpp:function:: string function GetLastDamageSourceStringForAttacker( entity victim, entity attacker )
.. cpp:function:: float function TotalDamageOverTime_BlendedOut( entity soul, float start, float end )
.. cpp:function:: void function ClearRecentDamageHistory( entity player )