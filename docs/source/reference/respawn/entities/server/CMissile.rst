.. _CMissile:

CMissile
========

.. cpp:class:: CMissile extends CProjectile

    Inherits all properties from :ref:`CProjectile <CProjectile>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CMissile-InitMissileForRandomDriftFromWeaponSettings:

    .. cpp:function:: void InitMissileForRandomDriftFromWeaponSettings(vector pos, vector dir)

    .. _CMissile-GetHomingSpeedAtDodgingPlayer:

    .. cpp:function:: unknown GetHomingSpeedAtDodgingPlayer(unknown)

    .. _CMissile-ApplyMissileControlledDrift:

    .. cpp:function:: unknown ApplyMissileControlledDrift(unknown)

    .. _CMissile-InitMissileForRandomDrift:

    .. cpp:function:: void InitMissileForRandomDrift(vector pos, vector dir)

    .. _CMissile-MissileExplode:

    .. cpp:function:: void MissileExplode()

    .. _CMissile-ClearMissileTargetPosition:

    .. cpp:function:: unknown ClearMissileTargetPosition(unknown)

    .. _CMissile-GetMissileTargetPosition:

    .. cpp:function:: unknown GetMissileTargetPosition(unknown)

    .. _CMissile-SetMissileTargetPosition:

    .. cpp:function:: void SetMissileTargetPosition(vector pos)

    .. _CMissile-SetMissileTarget:

    .. cpp:function:: void SetMissileTarget(enity target, vector offset)

    .. _CMissile-GetHomingSpeed:

    .. cpp:function:: unknown GetHomingSpeed(unknown)

    .. _CMissile-SetHomingSpeeds:

    .. cpp:function:: void SetHomingSpeeds(int speed, int speed_for_dodging_player)

    .. _CMissile-GetSpeed:

    .. cpp:function:: unknown GetSpeed(unknown)

    .. _CMissile-SetSpeed:

    .. cpp:function:: void SetSpeed(float speed)

    .. _CMissile-SetExplosionRadius:

    .. cpp:function:: unknown SetExplosionRadius(unknown)

    .. _CMissile-SetDamage:

    .. cpp:function:: unknown SetDamage(unknown)

    .. _CMissile-InitMissileSpiral:

    .. cpp:function:: void InitMissileSpiral(vector pos, vector dir, int missileNumber, bool unknown_purpose1, bool unknown_purpose2)

    .. _CMissile-InitMissileExpandContract:

    .. cpp:function:: void InitMissileExpandContract(vector outward, vector inward, float launchOutTime, float launchInLerpTime, float launchInTime, float launchStraightLerpTime, vector missileEndPos, bool applyRandSpread)

    .. _CMissile-GetMissileTarget:

    .. cpp:function:: entity GetMissileTarget()

