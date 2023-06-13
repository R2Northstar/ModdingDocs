.. _C-Missile:

C_Missile
=========

.. cpp:class:: C_Missile extends C_Projectile

    Inherits all properties from :ref:`C_Projectile <C-Projectile>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_Missile-InitMissileForRandomDriftFromWeaponSettings:

    .. cpp:function:: void InitMissileForRandomDriftFromWeaponSettings(vector pos, vector dir)

    .. _C_Missile-GetHomingSpeedAtDodgingPlayer:

    .. cpp:function:: unknown GetHomingSpeedAtDodgingPlayer(unknown)

    .. _C_Missile-MissileExplode:

    .. cpp:function:: void MissileExplode()

    .. _C_Missile-InitMissileSpiral:

    .. cpp:function:: void InitMissileSpiral(vector pos, vector dir, int missileNumber, bool unknown_purpose1, bool unknown_purpose2)

    .. _C_Missile-SetMissileTarget:

    .. cpp:function:: void SetMissileTarget(enity target, vector offset)

    .. _C_Missile-ApplyMissileControlledDrift:

    .. cpp:function:: unknown ApplyMissileControlledDrift(unknown)

    .. _C_Missile-InitMissileForRandomDrift:

    .. cpp:function:: void InitMissileForRandomDrift(vector pos, vector dir)

    .. _C_Missile-ClearMissileTargetPosition:

    .. cpp:function:: unknown ClearMissileTargetPosition(unknown)

    .. _C_Missile-GetMissileTargetPosition:

    .. cpp:function:: unknown GetMissileTargetPosition(unknown)

    .. _C_Missile-SetMissileTargetPosition:

    .. cpp:function:: void SetMissileTargetPosition(vector pos)

    .. _C_Missile-GetHomingSpeed:

    .. cpp:function:: unknown GetHomingSpeed(unknown)

    .. _C_Missile-SetHomingSpeeds:

    .. cpp:function:: void SetHomingSpeeds(int speed, int speed_for_dodging_player)

    .. _C_Missile-GetSpeed:

    .. cpp:function:: unknown GetSpeed(unknown)

    .. _C_Missile-SetSpeed:

    .. cpp:function:: void SetSpeed(float speed)

    .. _C_Missile-InitMissileExpandContract:

    .. cpp:function:: void InitMissileExpandContract(vector outward, vector inward, float launchOutTime, float launchInLerpTime, float launchInTime, float launchStraightLerpTime, vector missileEndPos, bool applyRandSpread)

    .. _C_Missile-GetMissileTarget:

    .. cpp:function:: entity GetMissileTarget()

