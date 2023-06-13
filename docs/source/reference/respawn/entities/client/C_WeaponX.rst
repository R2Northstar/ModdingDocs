.. _C-WeaponX:

C_WeaponX
=========

.. cpp:class:: C_WeaponX extends C_BaseCombatWeapon

    Inherits all properties from :ref:`C_BaseCombatWeapon <C-BaseCombatWeapon>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_WeaponX-HasMod:

    .. cpp:function:: bool HasMod(string mod)

    .. _C_WeaponX-GetRodeoDamage:

    .. cpp:function:: unknown GetRodeoDamage(unknown)

    .. _C_WeaponX-GetSmartAmmoWeaponType:

    .. cpp:function:: string GetSmartAmmoWeaponType()

    .. _C_WeaponX-Raise:

    .. cpp:function:: unknown Raise(unknown)

    .. _C_WeaponX-HasSilencer:

    .. cpp:function:: unknown HasSilencer(unknown)

    .. _C_WeaponX-IsDischarging:

    .. cpp:function:: unknown IsDischarging(unknown)

    .. _C_WeaponX-GetBurstFireShotsPending:

    .. cpp:function:: int GetBurstFireShotsPending()

    .. _C_WeaponX-GetNextAttackAllowedTime:

    .. cpp:function:: unknown GetNextAttackAllowedTime(unknown)

    .. _C_WeaponX-IsSustainedLaserWeapon:

    .. cpp:function:: unknown IsSustainedLaserWeapon(unknown)

    .. _C_WeaponX-GetWeaponChargeLevel:

    .. cpp:function:: float GetWeaponChargeLevel()

    .. _C_WeaponX-GetNPCMissFastPlayer:

    .. cpp:function:: unknown GetNPCMissFastPlayer(unknown)

    .. _C_WeaponX-SetModBitField:

    .. cpp:function:: unknown SetModBitField(unknown)

    .. _C_WeaponX-GetAllowHeadShots:

    .. cpp:function:: bool GetAllowHeadShots()

    .. _C_WeaponX-SmartAmmo-UntrackEntity:

    .. cpp:function:: void SmartAmmo_UntrackEntity(entity target)

    .. _C_WeaponX-SetLifetimeShotsRemaining:

    .. cpp:function:: unknown SetLifetimeShotsRemaining(unknown)

    .. _C_WeaponX-GetImpactTableIndex:

    .. cpp:function:: unknown GetImpactTableIndex(unknown)

    .. _C_WeaponX-GetWeaponExplosionDamageFlags:

    .. cpp:function:: unknown GetWeaponExplosionDamageFlags(unknown)

    .. _C_WeaponX-GetWeaponChargeTime:

    .. cpp:function:: float GetWeaponChargeTime()

    .. _C_WeaponX-SetWeaponEnergyCost:

    .. cpp:function:: void SetWeaponEnergyCost(int cost)

    .. _C_WeaponX-ShowWeapon:

    .. cpp:function:: unknown ShowWeapon(unknown)

    .. _C_WeaponX-Deploy:

    .. cpp:function:: unknown Deploy(unknown)

    .. _C_WeaponX-SetWeaponPrimaryClipCountAbsolute:

    .. cpp:function:: void SetWeaponPrimaryClipCountAbsolute(int clipsize)

    .. _C_WeaponX-GetLifetimeShotsRemaining:

    .. cpp:function:: unknown GetLifetimeShotsRemaining(unknown)

    .. _C_WeaponX-GetWeaponBurstFireCount:

    .. cpp:function:: int GetWeaponBurstFireCount()

    .. _C_WeaponX-SetSustainedDischargeFractionForced:

    .. cpp:function:: void SetSustainedDischargeFractionForced(float frac)

    .. _C_WeaponX-GetWeaponDefaultEnergyCost:

    .. cpp:function:: unknown GetWeaponDefaultEnergyCost(unknown)

    .. _C_WeaponX-GetWeaponSettingInt:

    .. cpp:function:: int GetWeaponSettingInt(int setting)

    .. _C_WeaponX-GetWeaponSettingString:

    .. cpp:function:: string GetWeaponSettingString(string setting)

    .. _C_WeaponX-PlayWeaponEffect:

    .. cpp:function:: void PlayWeaponEffect(asset effect1P, asset effect3P, string tagName)

    .. _C_WeaponX-GetWeaponSettingAsset:

    .. cpp:function:: unknown GetWeaponSettingAsset(unknown)

    .. _C_WeaponX-GetWeaponSettingVector:

    .. cpp:function:: unknown GetWeaponSettingVector(unknown)

    .. _C_WeaponX-EmitWeaponSound-1p3p:

    .. cpp:function:: void EmitWeaponSound_1p3p(string sound1P, string sound3P)

    .. _C_WeaponX-ForceRelease:

    .. cpp:function:: void ForceRelease()

    .. _C_WeaponX-GetWeaponSettingBool:

    .. cpp:function:: bool GetWeaponSettingBool(int setting)

    .. _C_WeaponX-GetWeaponClassName:

    .. cpp:function:: string GetWeaponClassName()

    .. _C_WeaponX-SetMods:

    .. cpp:function:: void SetMods(array<string> mods)

    .. _C_WeaponX-GetMods:

    .. cpp:function:: array<string> GetMods()

    .. _C_WeaponX-SetViewmodelAmmoModelIndex:

    .. cpp:function:: void SetViewmodelAmmoModelIndex(int index)

    .. _C_WeaponX-HideWeapon:

    .. cpp:function:: unknown HideWeapon(unknown)

    .. _C_WeaponX-IsLoadoutPickup:

    .. cpp:function:: unknown IsLoadoutPickup(unknown)

    .. _C_WeaponX-GetScriptFlags0:

    .. cpp:function:: int GetScriptFlags0()

    .. _C_WeaponX-SetScriptFlags0:

    .. cpp:function:: unknown SetScriptFlags0(unknown)

    .. _C_WeaponX-SetScriptTime0:

    .. cpp:function:: void SetScriptTime0(float gameTime)

    .. _C_WeaponX-DoMeleeHitConfirmation:

    .. cpp:function:: void DoMeleeHitConfirmation(float severityScale)

    .. _C_WeaponX-GetSustainedDischargePulseFrequency:

    .. cpp:function:: unknown GetSustainedDischargePulseFrequency(unknown)

    .. _C_WeaponX-IsReadyToFire:

    .. cpp:function:: bool IsReadyToFire()

    .. _C_WeaponX-GetSustainedDischargeDuration:

    .. cpp:function:: float GetSustainedDischargeDuration()

    .. _C_WeaponX-GetCoreDuration:

    .. cpp:function:: float GetCoreDuration()

    .. _C_WeaponX-IsInCooldown:

    .. cpp:function:: unknown IsInCooldown(unknown)

    .. _C_WeaponX-SetAttackKickRollScale:

    .. cpp:function:: void SetAttackKickRollScale(float scale)

    .. _C_WeaponX-GetWeaponDamageForce:

    .. cpp:function:: unknown GetWeaponDamageForce(unknown)

    .. _C_WeaponX-SetChargeAnimIndex:

    .. cpp:function:: void SetChargeAnimIndex(int index)

    .. _C_WeaponX-GetChargeAnimIndex:

    .. cpp:function:: int GetChargeAnimIndex()

    .. _C_WeaponX-GetInventoryIndex:

    .. cpp:function:: unknown GetInventoryIndex(unknown)

    .. _C_WeaponX-GetForcedADS:

    .. cpp:function:: unknown GetForcedADS(unknown)

    .. _C_WeaponX-SmartAmmo-GetTargets:

    .. cpp:function:: array<entity> SmartAmmo_GetTargets()

    .. _C_WeaponX-SetForcedADS:

    .. cpp:function:: void SetForcedADS()

    .. _C_WeaponX-GetChargeDuration:

    .. cpp:function:: unknown GetChargeDuration(unknown)

    .. _C_WeaponX-GetReloadMilestoneIndex:

    .. cpp:function:: int GetReloadMilestoneIndex()

    .. _C_WeaponX-GetWeaponZoomFOV:

    .. cpp:function:: unknown GetWeaponZoomFOV(unknown)

    .. _C_WeaponX-EmitWeaponSound:

    .. cpp:function:: void EmitWeaponSound(string sound)

    .. _C_WeaponX-GetGrenadeIgnitionTime:

    .. cpp:function:: unknown GetGrenadeIgnitionTime(unknown)

    .. _C_WeaponX-GetGrenadeFuseTime:

    .. cpp:function:: float GetGrenadeFuseTime()

    .. _C_WeaponX-EmitWeaponNpcSound-DontUpdateLastFiredTime:

    .. cpp:function:: void EmitWeaponNpcSound_DontUpdateLastFiredTime(int volume, float time)

    .. _C_WeaponX-GetWeaponReadyHint:

    .. cpp:function:: unknown GetWeaponReadyHint(unknown)

    .. _C_WeaponX-SetWeaponPrimaryAmmoCount:

    .. cpp:function:: void SetWeaponPrimaryAmmoCount(int count)

    .. _C_WeaponX-GetMeleeAnim3p:

    .. cpp:function:: unknown GetMeleeAnim3p(unknown)

    .. _C_WeaponX-ShouldPredictProjectiles:

    .. cpp:function:: bool ShouldPredictProjectiles()

    .. _C_WeaponX-CheckWeaponIsDisabled:

    .. cpp:function:: unknown CheckWeaponIsDisabled(unknown)

    .. _C_WeaponX-GetMeleeAttackRange:

    .. cpp:function:: float GetMeleeAttackRange()

    .. _C_WeaponX-PlayWeaponEffectReturnViewEffectHandle:

    .. cpp:function:: void PlayWeaponEffectReturnViewEffectHandle(asset fpEffect, asset unknown_purpose, string tag)

    .. _C_WeaponX-IsWeaponOffhand:

    .. cpp:function:: bool IsWeaponOffhand()

    .. _C_WeaponX-GetMeleeCanHitHumanSized:

    .. cpp:function:: bool GetMeleeCanHitHumanSized()

    .. _C_WeaponX-GetMeleeLungeTargetAngle:

    .. cpp:function:: unknown GetMeleeLungeTargetAngle(unknown)

    .. _C_WeaponX-GetMeleeLungeTargetRange:

    .. cpp:function:: float GetMeleeLungeTargetRange()

    .. _C_WeaponX-GetWeaponDamageFlags:

    .. cpp:function:: int GetWeaponDamageFlags()

    .. _C_WeaponX-SmartAmmo-GetNewTargetTime:

    .. cpp:function:: unknown SmartAmmo_GetNewTargetTime(unknown)

    .. _C_WeaponX-GetShotCount:

    .. cpp:function:: int GetShotCount()

    .. _C_WeaponX-SmartAmmo-TrackEntity:

    .. cpp:function:: void SmartAmmo_TrackEntity(entity hitEnt, LMG_SMART_AMMO_TRACKER_TIME)

    .. _C_WeaponX-GetNextAttackAllowedTimeRaw:

    .. cpp:function:: unknown GetNextAttackAllowedTimeRaw(unknown)

    .. _C_WeaponX-GetMeleeCanHitTitans:

    .. cpp:function:: bool GetMeleeCanHitTitans()

    .. _C_WeaponX-GetSmartAmmoHudLockStyle:

    .. cpp:function:: unknown GetSmartAmmoHudLockStyle(unknown)

    .. _C_WeaponX-GetModBitField:

    .. cpp:function:: unknown GetModBitField(unknown)

    .. _C_WeaponX-SetWeaponPrimaryClipCountNoRegenReset:

    .. cpp:function:: void SetWeaponPrimaryClipCountNoRegenReset(int clipsize)

    .. _C_WeaponX-AddMod:

    .. cpp:function:: void AddMod(string mod)

    .. _C_WeaponX-IsForceRelease:

    .. cpp:function:: bool IsForceRelease()

    .. _C_WeaponX-GetDamageSourceID:

    .. cpp:function:: int GetDamageSourceID()

    .. _C_WeaponX-GetWeaponSettingFloat:

    .. cpp:function:: float GetWeaponSettingFloat(int setting)

    .. _C_WeaponX-FireWeaponBullet-Special:

    .. cpp:function:: void FireWeaponBullet_Special(vector origin, vector direction, int numShots, int damageType, bool noAntilag, bool noSpread, bool onlyDamageEntitiesOnce, bool unknownPurpose, bool noTracers, bool activeShot, bool doTraceBrushOnly)

    .. _C_WeaponX-IsBurstFireInProgress:

    .. cpp:function:: bool IsBurstFireInProgress()

    .. _C_WeaponX-SmartAmmo-GetTrackedEntities:

    .. cpp:function:: array<entity> SmartAmmo_GetTrackedEntities()

    .. _C_WeaponX-IsWeaponCharging:

    .. cpp:function:: unknown IsWeaponCharging(unknown)

    .. _C_WeaponX-SetNextAttackAllowedTime:

    .. cpp:function:: void SetNextAttackAllowedTime(float time)

    .. _C_WeaponX-SmartAmmo-GetFirePosition:

    .. cpp:function:: vector SmartAmmo_GetFirePosition(entity target, int burstIndex)

    .. _C_WeaponX-SmartAmmo-GetStoredTargets:

    .. cpp:function:: array<entity> SmartAmmo_GetStoredTargets()

    .. _C_WeaponX-GetAmmoDisplay:

    .. cpp:function:: unknown GetAmmoDisplay(unknown)

    .. _C_WeaponX-ClearForcedADS:

    .. cpp:function:: void ClearForcedADS()

    .. _C_WeaponX-SetAttackKickScale:

    .. cpp:function:: unknown SetAttackKickScale(unknown)

    .. _C_WeaponX-EmitWeaponNpcSound:

    .. cpp:function:: void EmitWeaponNpcSound(int volume, float duration)

    .. _C_WeaponX-SmartAmmo-IsEnabled:

    .. cpp:function:: bool SmartAmmo_IsEnabled(bool enabled)

    .. _C_WeaponX-GetWeaponChargeTimeRemaining:

    .. cpp:function:: unknown GetWeaponChargeTimeRemaining(unknown)

    .. _C_WeaponX-GetMeleeAttackAngle:

    .. cpp:function:: unknown GetMeleeAttackAngle(unknown)

    .. _C_WeaponX-GetWeaponInfoFileKeyFieldAsset:

    .. cpp:function:: unknown GetWeaponInfoFileKeyFieldAsset(unknown)

    .. _C_WeaponX-SetWeaponChargeFractionForced:

    .. cpp:function:: void SetWeaponChargeFractionForced(float frac)

    .. _C_WeaponX-GetWeaponInfoFileKeyField:

    .. cpp:function:: var GetWeaponInfoFileKeyField(string key)

    .. _C_WeaponX-ResetWeaponToDefaultEnergyCost:

    .. cpp:function:: void ResetWeaponToDefaultEnergyCost()

    .. _C_WeaponX-GetWeaponChargeEnergyCost:

    .. cpp:function:: unknown GetWeaponChargeEnergyCost(unknown)

    .. _C_WeaponX-GetWeaponReadyToFireProgress:

    .. cpp:function:: unknown GetWeaponReadyToFireProgress(unknown)

    .. _C_WeaponX-AllowUse:

    .. cpp:function:: bool AllowUse()

    .. _C_WeaponX-GetWeaponChargeLevelMax:

    .. cpp:function:: float GetWeaponChargeLevelMax()

    .. _C_WeaponX-GetWeaponChargeFraction:

    .. cpp:function:: float GetWeaponChargeFraction()

    .. _C_WeaponX-SetWeaponBurstFireCount:

    .. cpp:function:: void SetWeaponBurstFireCount(int amount)

    .. _C_WeaponX-SmartAmmo-GetNumTrackersOnEntity:

    .. cpp:function:: int SmartAmmo_GetNumTrackersOnEntity(entity target)

    .. _C_WeaponX-GetSustainedDischargeRemainder:

    .. cpp:function:: unknown GetSustainedDischargeRemainder(unknown)

    .. _C_WeaponX-GetWeaponType:

    .. cpp:function:: int GetWeaponType()

    .. _C_WeaponX-IsWeaponAdsButtonPressed:

    .. cpp:function:: bool IsWeaponAdsButtonPressed()

    .. _C_WeaponX-IsWeaponInAds:

    .. cpp:function:: bool IsWeaponInAds()

    .. _C_WeaponX-IsReloading:

    .. cpp:function:: bool IsReloading()

    .. _C_WeaponX-GetWeaponUtilityEntity:

    .. cpp:function:: entity GetWeaponUtilityEntity()

    .. _C_WeaponX-SetLifetimeShotsRemainingInfinite:

    .. cpp:function:: unknown SetLifetimeShotsRemainingInfinite(unknown)

    .. _C_WeaponX-GetWeaponPrimaryClipCount:

    .. cpp:function:: int GetWeaponPrimaryClipCount()

    .. _C_WeaponX-SetWeaponPrimaryClipCount:

    .. cpp:function:: void SetWeaponPrimaryClipCount(int)

    .. _C_WeaponX-RemoveMod:

    .. cpp:function:: void RemoveMod(string mod)

    .. _C_WeaponX-GetWeaponPrimaryAmmoCount:

    .. cpp:function:: int GetWeaponPrimaryAmmoCount()

    .. _C_WeaponX-SmartAmmo-SetTarget:

    .. cpp:function:: unknown SmartAmmo_SetTarget(unknown)

    .. _C_WeaponX-GetAmmoPerShot:

    .. cpp:function:: int GetAmmoPerShot()

    .. _C_WeaponX-PlayWeaponEffectNoCull:

    .. cpp:function:: void PlayWeaponEffectNoCull(asset effect1P, asset effect3P, string tagName)

    .. _C_WeaponX-GetWeaponReadyMsg:

    .. cpp:function:: unknown GetWeaponReadyMsg(unknown)

    .. _C_WeaponX-GetWeaponPrimaryClipCountMax:

    .. cpp:function:: int GetWeaponPrimaryClipCountMax()

    .. _C_WeaponX-FireWeaponMissile:

    .. cpp:function:: entity FireWeaponMissile(vector origin, vector dir, float missileSpeed, int contactDamageType, int explosionDamageType, bool doPopup, bool predict)

    .. _C_WeaponX-FireWeaponGrenade:

    .. cpp:function:: entity FireWeaponGrenade(vector attackPos, vector throwVelocity, vector angularVelocity, float fuseTime, int contactDamageType, int explosionDamageType, bool isPredicted, bool isLagCompensated, bool bounce?)

    .. _C_WeaponX-FireWeaponBolt:

    .. cpp:function:: entity FireWeaponBolt(vector origin, vector dir, float projectileSpeed, int contactDamageType, int explosionDamageType, bool predict, int index)

    .. _C_WeaponX-IsNetOptimized:

    .. cpp:function:: unknown IsNetOptimized(unknown)

    .. _C_WeaponX-GetAttackPosition:

    .. cpp:function:: vector GetAttackPosition()

    .. _C_WeaponX-SetWeaponSkin:

    .. cpp:function:: void SetWeaponSkin(int skin)

    .. _C_WeaponX-StopWeaponEffect:

    .. cpp:function:: void StopWeaponEffect(asset effect1P, asset effect3P)

    .. _C_WeaponX-GetProjectilesPerShot:

    .. cpp:function:: int GetProjectilesPerShot()

    .. _C_WeaponX-SmartAmmo-SetNewTargetTime:

    .. cpp:function:: unknown SmartAmmo_SetNewTargetTime(unknown)

    .. _C_WeaponX-StopWeaponSound:

    .. cpp:function:: void StopWeaponSound(string sound)

    .. _C_WeaponX-SetWeaponCamo:

    .. cpp:function:: unknown SetWeaponCamo(unknown)

    .. _C_WeaponX-GetWeaponClass:

    .. cpp:function:: string GetWeaponClass()

    .. _C_WeaponX-IsSustainedDischargeWeapon:

    .. cpp:function:: bool IsSustainedDischargeWeapon()

    .. _C_WeaponX-TimeUntilReadyToFire:

    .. cpp:function:: unknown TimeUntilReadyToFire(unknown)

    .. _C_WeaponX-DeployInstant:

    .. cpp:function:: unknown DeployInstant(unknown)

    .. _C_WeaponX-SmartAmmo-StoreTargets:

    .. cpp:function:: void SmartAmmo_StoreTargets()

    .. _C_WeaponX-GetAttackDirection:

    .. cpp:function:: vector GetAttackDirection()

    .. _C_WeaponX-GetCurrentAltFireIndex:

    .. cpp:function:: int GetCurrentAltFireIndex()

    .. _C_WeaponX-GetMaxDamageFarDist:

    .. cpp:function:: float GetMaxDamageFarDist()

    .. _C_WeaponX-SetWeaponChargeFraction:

    .. cpp:function:: float SetWeaponChargeFraction()

    .. _C_WeaponX-IsWeaponRegenDraining:

    .. cpp:function:: bool IsWeaponRegenDraining()

    .. _C_WeaponX-GetWeaponOwner:

    .. cpp:function:: entity GetWeaponOwner()

    .. _C_WeaponX-GetWeaponCurrentEnergyCost:

    .. cpp:function:: int GetWeaponCurrentEnergyCost()

    .. _C_WeaponX-FireWeaponBullet:

    .. cpp:function:: entity FireWeaponBullet(vector origin, vector dir, int numBullets, damageType)

    .. _C_WeaponX-SmartAmmo-IsVisibleTarget:

    .. cpp:function:: bool SmartAmmo_IsVisibleTarget(entity trackedEnt)

    .. _C_WeaponX-GetDamageAmountForArmorType:

    .. cpp:function:: int GetDamageAmountForArmorType(int armor)

    .. _C_WeaponX-RegenerateAmmoReset:

    .. cpp:function:: void RegenerateAmmoReset()

    .. _C_WeaponX-GetScriptTime0:

    .. cpp:function:: float GetScriptTime0()

    .. _C_WeaponX-GetSustainedDischargeFraction:

    .. cpp:function:: unknown GetSustainedDischargeFraction(unknown)

    .. _C_WeaponX-IsChargeWeapon:

    .. cpp:function:: bool IsChargeWeapon()

    .. _C_WeaponX-SmartAmmo-GetSearchAngle:

    .. cpp:function:: unknown SmartAmmo_GetSearchAngle(unknown)

    .. _C_WeaponX-IsCooldownPending:

    .. cpp:function:: unknown IsCooldownPending(unknown)

    .. _C_WeaponX-SmartAmmo-Clear:

    .. cpp:function:: void SmartAmmo_Clear(bool unknown_purpose, bool clearPartialLocks)

