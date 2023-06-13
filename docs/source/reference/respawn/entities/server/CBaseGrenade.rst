.. _CBaseGrenade:

CBaseGrenade
============

.. cpp:class:: CBaseGrenade extends CProjectile

    Inherits all properties from :ref:`CProjectile <CProjectile>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CBaseGrenade-GrenadeIgnite:

    .. cpp:function:: void GrenadeIgnite()

    .. _CBaseGrenade-GrenadeHasIgnited:

    .. cpp:function:: bool GrenadeHasIgnited()

    .. _CBaseGrenade-SetGrenadeTimer:

    .. cpp:function:: void SetGrenadeTimer(float fuseTime)

    .. _CBaseGrenade-SetGrenadeIgnitionDuration:

    .. cpp:function:: void SetGrenadeIgnitionDuration(float fuseTime)

    .. _CBaseGrenade-InitMagnetic:

    .. cpp:function:: void InitMagnetic(float force, string attractKey)

    .. _CBaseGrenade-SetDoesExplode:

    .. cpp:function:: void SetDoesExplode(bool explodes)

    .. _CBaseGrenade-GetThrower:

    .. cpp:function:: entity GetThrower()

    .. _CBaseGrenade-MarkAsAttached:

    .. cpp:function:: void MarkAsAttached()

    .. _CBaseGrenade-GetCreationTime:

    .. cpp:function:: unknown GetCreationTime(unknown)

    .. _CBaseGrenade-GetDamageAmount:

    .. cpp:function:: unknown GetDamageAmount(unknown)

    .. _CBaseGrenade-GetDamageRadius:

    .. cpp:function:: float GetDamageRadius()

    .. _CBaseGrenade-ExplodeForCollisionCallback:

    .. cpp:function:: void ExplodeForCollisionCallback(vector normal)

    .. _CBaseGrenade-GetFuseTime:

    .. cpp:function:: unknown GetFuseTime(unknown)

    .. _CBaseGrenade-SetLauncherOwner:

    .. cpp:function:: unknown SetLauncherOwner(unknown)

    .. _CBaseGrenade-GetExplosionRadius:

    .. cpp:function:: float GetExplosionRadius()

    .. _CBaseGrenade-GrenadeExplode:

    .. cpp:function:: void GrenadeExplode(vector normal)

