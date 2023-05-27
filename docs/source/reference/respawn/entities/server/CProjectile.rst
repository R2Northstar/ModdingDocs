.. _CProjectile:

CProjectile
===========

.. cpp:class:: CProjectile extends CBaseAnimating

    Inherits all properties from :ref:`CBaseAnimating <CBaseAnimating>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`CMissile <CMissile>`
    - :ref:`CCrossbowBolt <CCrossbowBolt>`
    - :ref:`CBaseGrenade <CBaseGrenade>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CProjectile-ForceAdjustToGunBarrelDisabled:

    .. cpp:function:: unknown ForceAdjustToGunBarrelDisabled(unknown)

    .. _CProjectile-GetProjectileCreationTimeServer:

    .. cpp:function:: unknown GetProjectileCreationTimeServer(unknown)

    .. _CProjectile-ProjectileGetWeaponChargeLevel:

    .. cpp:function:: unknown ProjectileGetWeaponChargeLevel(unknown)

    .. _CProjectile-ProjectileGetMods:

    .. cpp:function:: array<string> ProjectileGetMods()

    .. _CProjectile-GetTimeToProjectileDeath:

    .. cpp:function:: unknown GetTimeToProjectileDeath(unknown)

    .. _CProjectile-GetProjectileCreationTime:

    .. cpp:function:: float GetProjectileCreationTime()

    .. _CProjectile-SetProjectileDestructionDistance:

    .. cpp:function:: unknown SetProjectileDestructionDistance(unknown)

    .. _CProjectile-DamageAliveOnly:

    .. cpp:function:: unknown DamageAliveOnly(unknown)

    .. _CProjectile-GetProjectileAllowHeadShots:

    .. cpp:function:: unknown GetProjectileAllowHeadShots(unknown)

    .. _CProjectile-ProjectileGetRodeoDamage:

    .. cpp:function:: unknown ProjectileGetRodeoDamage(unknown)

    .. _CProjectile-GetProjectileWeaponSettingString:

    .. cpp:function:: unknown GetProjectileWeaponSettingString(unknown)

    .. _CProjectile-GetProjectileWeaponSettingVector:

    .. cpp:function:: unknown GetProjectileWeaponSettingVector(unknown)

    .. _CProjectile-GetProjectileWeaponSettingFloat:

    .. cpp:function:: float GetProjectileWeaponSettingFloat(string setting)

    .. _CProjectile-GetProjectileWeaponSettingInt:

    .. cpp:function:: int GetProjectileWeaponSettingInt(string setting)

    .. _CProjectile-ProjectileSetDamageSourceID:

    .. cpp:function:: void ProjectileSetDamageSourceID(int id)

    .. _CProjectile-ProjectileGetDamageSourceID:

    .. cpp:function:: int ProjectileGetDamageSourceID()

    .. _CProjectile-SetWeaponClassName:

    .. cpp:function:: void SetWeaponClassName(string name)

    .. _CProjectile-SetProjectileImpactDamageOverride:

    .. cpp:function:: void SetProjectileImpactDamageOverride(int flag)

    .. _CProjectile-SetImpactEffectTable:

    .. cpp:function:: void SetImpactEffectTable(string fxTableHandle)

    .. _CProjectile-SetReducedEffects:

    .. cpp:function:: void SetReducedEffects()

    .. _CProjectile-SetProjectileLifetime:

    .. cpp:function:: void SetProjectileLifetime(float lifetime)

    .. _CProjectile-SetProjectilTrailEffectIndex:

    .. cpp:function:: void SetProjectilTrailEffectIndex(int index)

    .. _CProjectile-ProjectileGetWeaponInfoFileKeyFieldAsset:

    .. cpp:function:: asset ProjectileGetWeaponInfoFileKeyFieldAsset(string key)

    .. _CProjectile-ProjectileGetWeaponInfoFileKeyField:

    .. cpp:function:: string ProjectileGetWeaponInfoFileKeyField(string key)

    .. _CProjectile-SetVortexRefired:

    .. cpp:function:: void SetVortexRefired(bool refired)

    .. _CProjectile-ProjectileGetWeaponClassName:

    .. cpp:function:: string ProjectileGetWeaponClassName()

    .. _CProjectile-GetProjectileWeaponSettingAsset:

    .. cpp:function:: asset GetProjectileWeaponSettingAsset(string setting)

    .. _CProjectile-GetProjectileWeaponSettingBool:

    .. cpp:function:: bool GetProjectileWeaponSettingBool(string setting)

