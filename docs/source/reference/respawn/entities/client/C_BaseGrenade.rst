.. _C-BaseGrenade:

C_BaseGrenade
=============

.. cpp:class:: C_BaseGrenade extends C_Projectile

    Inherits all properties from :ref:`C_Projectile <C-Projectile>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_BaseGrenade-GrenadeIgnite:

    .. cpp:function:: void GrenadeIgnite()

    .. _C_BaseGrenade-GrenadeHasIgnited:

    .. cpp:function:: bool GrenadeHasIgnited()

    .. _C_BaseGrenade-SetDoesExplode:

    .. cpp:function:: void SetDoesExplode(bool explodes)

    .. _C_BaseGrenade-GetFuseTime:

    .. cpp:function:: unknown GetFuseTime(unknown)

    .. _C_BaseGrenade-GetThrower:

    .. cpp:function:: entity GetThrower()

    .. _C_BaseGrenade-GetCreationTime:

    .. cpp:function:: unknown GetCreationTime(unknown)

    .. _C_BaseGrenade-GetDamageAmount:

    .. cpp:function:: unknown GetDamageAmount(unknown)

    .. _C_BaseGrenade-GetDamageRadius:

    .. cpp:function:: float GetDamageRadius()

    .. _C_BaseGrenade-ExplodeForCollisionCallback:

    .. cpp:function:: void ExplodeForCollisionCallback(vector normal)

    .. _C_BaseGrenade-InitMagnetic:

    .. cpp:function:: void InitMagnetic(float force, string attractKey)

    .. _C_BaseGrenade-MarkAsAttached:

    .. cpp:function:: void MarkAsAttached()

    .. _C_BaseGrenade-GetExplosionRadius:

    .. cpp:function:: float GetExplosionRadius()

    .. _C_BaseGrenade-GrenadeExplode:

    .. cpp:function:: void GrenadeExplode(vector normal)

