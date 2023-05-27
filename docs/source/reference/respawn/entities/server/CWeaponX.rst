.. _CWeaponX:

CWeaponX
========

.. cpp:class:: CWeaponX extends CBaseCombatWeapon

    Inherits all properties from :ref:`CBaseCombatWeapon <CBaseCombatWeapon>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CWeaponX-GetProScreenOwner:

    .. cpp:function:: unknown GetProScreenOwner(unknown)

    .. _CWeaponX-MarkAsLoadoutPickup:

    .. cpp:function:: unknown MarkAsLoadoutPickup(unknown)

    .. _CWeaponX-HasSilencer:

    .. cpp:function:: unknown HasSilencer(unknown)

    .. _CWeaponX-IsDischarging:

    .. cpp:function:: unknown IsDischarging(unknown)

    .. _CWeaponX-FireWeaponMissile:

    .. cpp:function:: entity FireWeaponMissile(vector origin, vector dir, float missileSpeed, int contactDamageType, int explosionDamageType, bool doPopup, bool predict)

    .. _CWeaponX-GetAllowHeadShots:

    .. cpp:function:: bool GetAllowHeadShots()

    .. _CWeaponX-SmartAmmo-IsEnabled:

    .. cpp:function:: bool SmartAmmo_IsEnabled(bool enabled)

    .. _CWeaponX-GetImpactTableIndex:

    .. cpp:function:: unknown GetImpactTableIndex(unknown)

    .. _CWeaponX-GetWeaponChargeTime:

    .. cpp:function:: float GetWeaponChargeTime()

    .. _CWeaponX-SetWeaponEnergyCost:

    .. cpp:function:: void SetWeaponEnergyCost(int cost)

    .. _CWeaponX-GetWeaponDamageFlags:

    .. cpp:function:: int GetWeaponDamageFlags()

    .. _CWeaponX-SetProScreenIntValForIndex:

    .. cpp:function:: unknown SetProScreenIntValForIndex(unknown)

    .. _CWeaponX-Deploy:

    .. cpp:function:: unknown Deploy(unknown)

    .. _CWeaponX-SetWeaponPrimaryClipCountAbsolute:

    .. cpp:function:: void SetWeaponPrimaryClipCountAbsolute(int clipsize)

    .. _CWeaponX-IsBurstFireInProgress:

    .. cpp:function:: bool IsBurstFireInProgress()

    .. _CWeaponX-GetWeaponBurstFireCount:

    .. cpp:function:: int GetWeaponBurstFireCount()

    .. _CWeaponX-SetSustainedDischargeFractionForced:

    .. cpp:function:: void SetSustainedDischargeFractionForced(float frac)

    .. _CWeaponX-GetWeaponDefaultEnergyCost:

    .. cpp:function:: unknown GetWeaponDefaultEnergyCost(unknown)

    .. _CWeaponX-GetWeaponSettingInt:

    .. cpp:function:: int GetWeaponSettingInt(int setting)

    .. _CWeaponX-GetWeaponReadyHint:

    .. cpp:function:: unknown GetWeaponReadyHint(unknown)

    .. _CWeaponX-GetWeaponPrimaryClipCount:

    .. cpp:function:: int GetWeaponPrimaryClipCount()

    .. _CWeaponX-PlayWeaponEffect:

    .. cpp:function:: void PlayWeaponEffect(asset effect1P, asset effect3P, string tagName)

    .. _CWeaponX-IsReadyToFire:

    .. cpp:function:: bool IsReadyToFire()

    .. _CWeaponX-GetChargeDuration:

    .. cpp:function:: unknown GetChargeDuration(unknown)

    .. _CWeaponX-GetForcedADS:

    .. cpp:function:: unknown GetForcedADS(unknown)

    .. _CWeaponX-SetForcedADS:

    .. cpp:function:: void SetForcedADS()

    .. _CWeaponX-GetWeaponZoomFOV:

    .. cpp:function:: unknown GetWeaponZoomFOV(unknown)

    .. _CWeaponX-GetMeleeCanHitTitans:

    .. cpp:function:: bool GetMeleeCanHitTitans()

    .. _CWeaponX-GetWeaponChargeLevelMax:

    .. cpp:function:: float GetWeaponChargeLevelMax()

    .. _CWeaponX-GetWeaponSettingFloat:

    .. cpp:function:: float GetWeaponSettingFloat(int setting)

    .. _CWeaponX-SetNextAttackAllowedTime:

    .. cpp:function:: void SetNextAttackAllowedTime(float time)

    .. _CWeaponX-GetWeaponChargeTimeRemaining:

    .. cpp:function:: unknown GetWeaponChargeTimeRemaining(unknown)

    .. _CWeaponX-IsForceReleaseFromServer:

    .. cpp:function:: bool IsForceReleaseFromServer()

    .. _CWeaponX-GetMeleeAttackAngle:

    .. cpp:function:: unknown GetMeleeAttackAngle(unknown)

    .. _CWeaponX-GetWeaponInfoFileKeyFieldAsset:

    .. cpp:function:: unknown GetWeaponInfoFileKeyFieldAsset(unknown)

    .. _CWeaponX-GetNextAttackAllowedTimeRaw:

    .. cpp:function:: unknown GetNextAttackAllowedTimeRaw(unknown)

    .. _CWeaponX-SmartAmmo-GetNumTrackersOnEntity:

    .. cpp:function:: int SmartAmmo_GetNumTrackersOnEntity(entity target)

    .. _CWeaponX-GetSustainedDischargeRemainder:

    .. cpp:function:: unknown GetSustainedDischargeRemainder(unknown)

    .. _CWeaponX-SetProScreenFloatValForIndex:

    .. cpp:function:: unknown SetProScreenFloatValForIndex(unknown)

    .. _CWeaponX-SetWeaponPrimaryClipCount:

    .. cpp:function:: void SetWeaponPrimaryClipCount(int)

    .. _CWeaponX-RemoveMod:

    .. cpp:function:: void RemoveMod(string mod)

    .. _CWeaponX-GetWeaponPrimaryClipCountMax:

    .. cpp:function:: int GetWeaponPrimaryClipCountMax()

    .. _CWeaponX-SetWeaponSkin:

    .. cpp:function:: void SetWeaponSkin(int skin)

    .. _CWeaponX-GetProjectilesPerShot:

    .. cpp:function:: int GetProjectilesPerShot()

    .. _CWeaponX-SmartAmmo-TrackEntity:

    .. cpp:function:: void SmartAmmo_TrackEntity(entity hitEnt, LMG_SMART_AMMO_TRACKER_TIME)

    .. _CWeaponX-IsWeaponOffhand:

    .. cpp:function:: bool IsWeaponOffhand()

    .. _CWeaponX-IsSustainedDischargeWeapon:

    .. cpp:function:: bool IsSustainedDischargeWeapon()

    .. _CWeaponX-AddMod:

    .. cpp:function:: void AddMod(string mod)

    .. _CWeaponX-GetWeaponPrimaryAmmoCount:

    .. cpp:function:: int GetWeaponPrimaryAmmoCount()

    .. _CWeaponX-IsWeaponAdsButtonPressed:

    .. cpp:function:: bool IsWeaponAdsButtonPressed()

    .. _CWeaponX-GetAmmoDisplay:

    .. cpp:function:: unknown GetAmmoDisplay(unknown)

    .. _CWeaponX-GetMeleeAttackRange:

    .. cpp:function:: float GetMeleeAttackRange()

    .. _CWeaponX-DeployInstant:

    .. cpp:function:: unknown DeployInstant(unknown)

    .. _CWeaponX-GetAttackDirection:

    .. cpp:function:: vector GetAttackDirection()

    .. _CWeaponX-GetCurrentAltFireIndex:

    .. cpp:function:: int GetCurrentAltFireIndex()

    .. _CWeaponX-GetMaxDamageFarDist:

    .. cpp:function:: float GetMaxDamageFarDist()

    .. _CWeaponX-SetWeaponChargeFraction:

    .. cpp:function:: float SetWeaponChargeFraction()

    .. _CWeaponX-GetWeaponOwner:

    .. cpp:function:: entity GetWeaponOwner()

    .. _CWeaponX-GetWeaponInfoFileKeyField:

    .. cpp:function:: var GetWeaponInfoFileKeyField(string key)

    .. _CWeaponX-SetScriptFlags0:

    .. cpp:function:: unknown SetScriptFlags0(unknown)

    .. _CWeaponX-GetSustainedDischargeDuration:

    .. cpp:function:: float GetSustainedDischargeDuration()

    .. _CWeaponX-GetScriptTime0:

    .. cpp:function:: float GetScriptTime0()

    .. _CWeaponX-GetSustainedDischargeFraction:

    .. cpp:function:: unknown GetSustainedDischargeFraction(unknown)

    .. _CWeaponX-SetScriptTime0:

    .. cpp:function:: void SetScriptTime0(float gameTime)

    .. _CWeaponX-GetSustainedDischargePulseFrequency:

    .. cpp:function:: unknown GetSustainedDischargePulseFrequency(unknown)

    .. _CWeaponX-GetChargeAnimIndex:

    .. cpp:function:: int GetChargeAnimIndex()

    .. _CWeaponX-IsForceRelease:

    .. cpp:function:: bool IsForceRelease()

    .. _CWeaponX-HasMod:

    .. cpp:function:: bool HasMod(string mod)

    .. _CWeaponX-GetRodeoDamage:

    .. cpp:function:: unknown GetRodeoDamage(unknown)

    .. _CWeaponX-GetWeaponDamageForce:

    .. cpp:function:: unknown GetWeaponDamageForce(unknown)

    .. _CWeaponX-Raise:

    .. cpp:function:: unknown Raise(unknown)

    .. _CWeaponX-GetNextAttackAllowedTime:

    .. cpp:function:: unknown GetNextAttackAllowedTime(unknown)

    .. _CWeaponX-GetModBitField:

    .. cpp:function:: unknown GetModBitField(unknown)

    .. _CWeaponX-IsSustainedLaserWeapon:

    .. cpp:function:: unknown IsSustainedLaserWeapon(unknown)

    .. _CWeaponX-GetWeaponChargeLevel:

    .. cpp:function:: float GetWeaponChargeLevel()

    .. _CWeaponX-GetNPCMissFastPlayer:

    .. cpp:function:: unknown GetNPCMissFastPlayer(unknown)

    .. _CWeaponX-SetModBitField:

    .. cpp:function:: unknown SetModBitField(unknown)

    .. _CWeaponX-ForceChargeEndNoAttack:

    .. cpp:function:: unknown ForceChargeEndNoAttack(unknown)

    .. _CWeaponX-SetChargeAnimIndex:

    .. cpp:function:: void SetChargeAnimIndex(int index)

    .. _CWeaponX-SmartAmmo-UntrackEntity:

    .. cpp:function:: void SmartAmmo_UntrackEntity(entity target)

    .. _CWeaponX-SetLifetimeShotsRemaining:

    .. cpp:function:: unknown SetLifetimeShotsRemaining(unknown)

    .. _CWeaponX-GetWeaponExplosionDamageFlags:

    .. cpp:function:: unknown GetWeaponExplosionDamageFlags(unknown)

    .. _CWeaponX-SmartAmmo-GetTrackedEntities:

    .. cpp:function:: array<entity> SmartAmmo_GetTrackedEntities()

    .. _CWeaponX-SetWeaponPrimaryAmmoCount:

    .. cpp:function:: void SetWeaponPrimaryAmmoCount(int count)

    .. _CWeaponX-GetGrenadeIgnitionTime:

    .. cpp:function:: unknown GetGrenadeIgnitionTime(unknown)

    .. _CWeaponX-GetReloadMilestoneIndex:

    .. cpp:function:: int GetReloadMilestoneIndex()

    .. _CWeaponX-GetLifetimeShotsRemaining:

    .. cpp:function:: unknown GetLifetimeShotsRemaining(unknown)

    .. _CWeaponX-GetWeaponReadyToFireProgress:

    .. cpp:function:: unknown GetWeaponReadyToFireProgress(unknown)

    .. _CWeaponX-GetWeaponSettingString:

    .. cpp:function:: string GetWeaponSettingString(string setting)

    .. _CWeaponX-ForceReleaseFromServer:

    .. cpp:function:: void ForceReleaseFromServer()

    .. _CWeaponX-GetCoreDuration:

    .. cpp:function:: float GetCoreDuration()

    .. _CWeaponX-GetMeleeAnim3p:

    .. cpp:function:: unknown GetMeleeAnim3p(unknown)

    .. _CWeaponX-ForceRelease:

    .. cpp:function:: void ForceRelease()

    .. _CWeaponX-GetShotCount:

    .. cpp:function:: int GetShotCount()

    .. _CWeaponX-IsInCooldown:

    .. cpp:function:: unknown IsInCooldown(unknown)

    .. _CWeaponX-SetAttackKickRollScale:

    .. cpp:function:: void SetAttackKickRollScale(float scale)

    .. _CWeaponX-GetInventoryIndex:

    .. cpp:function:: unknown GetInventoryIndex(unknown)

    .. _CWeaponX-ShouldPredictProjectiles:

    .. cpp:function:: bool ShouldPredictProjectiles()

    .. _CWeaponX-GetWeaponChargeFraction:

    .. cpp:function:: float GetWeaponChargeFraction()

    .. _CWeaponX-GetWeaponSettingAsset:

    .. cpp:function:: unknown GetWeaponSettingAsset(unknown)

    .. _CWeaponX-GetWeaponSettingBool:

    .. cpp:function:: bool GetWeaponSettingBool(int setting)

    .. _CWeaponX-SetMods:

    .. cpp:function:: void SetMods(array<string> mods)

    .. _CWeaponX-GetMods:

    .. cpp:function:: array<string> GetMods()

    .. _CWeaponX-IsLoadoutPickup:

    .. cpp:function:: unknown IsLoadoutPickup(unknown)

    .. _CWeaponX-SetProScreenOwner:

    .. cpp:function:: unknown SetProScreenOwner(unknown)

    .. _CWeaponX-ForceDryfireEvent:

    .. cpp:function:: void ForceDryfireEvent()

    .. _CWeaponX-EmitWeaponSound:

    .. cpp:function:: void EmitWeaponSound(string sound)

    .. _CWeaponX-PlayWeaponEffectOnOwner:

    .. cpp:function:: void PlayWeaponEffectOnOwner(asset effect, int bodypart)

    .. _CWeaponX-SetWeaponUtilityEntity:

    .. cpp:function:: void SetWeaponUtilityEntity(entity ent)

    .. _CWeaponX-FireWeaponBullet-Special:

    .. cpp:function:: void FireWeaponBullet_Special(vector origin, vector direction, int numShots, int damageType, bool noAntilag, bool noSpread, bool onlyDamageEntitiesOnce, bool unknownPurpose, bool noTracers, bool activeShot, bool doTraceBrushOnly)

    .. _CWeaponX-ThrowWeapon:

    .. cpp:function:: unknown ThrowWeapon(unknown)

    .. _CWeaponX-GetScriptFlags0:

    .. cpp:function:: int GetScriptFlags0()

    .. _CWeaponX-DoMeleeHitConfirmation:

    .. cpp:function:: void DoMeleeHitConfirmation(float severityScale)

    .. _CWeaponX-GetSmartAmmoWeaponType:

    .. cpp:function:: string GetSmartAmmoWeaponType()

    .. _CWeaponX-SmartAmmo-Clear:

    .. cpp:function:: void SmartAmmo_Clear(bool unknown_purpose, bool clearPartialLocks)

    .. _CWeaponX-IsCooldownPending:

    .. cpp:function:: unknown IsCooldownPending(unknown)

    .. _CWeaponX-GetWeaponChargeEnergyCost:

    .. cpp:function:: unknown GetWeaponChargeEnergyCost(unknown)

    .. _CWeaponX-SmartAmmo-GetStoredTargets:

    .. cpp:function:: array<entity> SmartAmmo_GetStoredTargets()

    .. _CWeaponX-ClearForcedADS:

    .. cpp:function:: void ClearForcedADS()

    .. _CWeaponX-SetAttackKickScale:

    .. cpp:function:: unknown SetAttackKickScale(unknown)

    .. _CWeaponX-CheckWeaponIsDisabled:

    .. cpp:function:: unknown CheckWeaponIsDisabled(unknown)

    .. _CWeaponX-SetWeaponChargeFractionForced:

    .. cpp:function:: void SetWeaponChargeFractionForced(float frac)

    .. _CWeaponX-ForceSustainedDischargeEnd:

    .. cpp:function:: unknown ForceSustainedDischargeEnd(unknown)

    .. _CWeaponX-IsReloading:

    .. cpp:function:: bool IsReloading()

    .. _CWeaponX-SetLifetimeShotsRemainingInfinite:

    .. cpp:function:: unknown SetLifetimeShotsRemainingInfinite(unknown)

    .. _CWeaponX-SmartAmmo-IsVisibleTarget:

    .. cpp:function:: bool SmartAmmo_IsVisibleTarget(entity trackedEnt)

    .. _CWeaponX-SetWeaponPrimaryClipCountNoRegenReset:

    .. cpp:function:: void SetWeaponPrimaryClipCountNoRegenReset(int clipsize)

    .. _CWeaponX-GetWeaponCurrentEnergyCost:

    .. cpp:function:: int GetWeaponCurrentEnergyCost()

    .. _CWeaponX-SetWeaponBurstFireCount:

    .. cpp:function:: void SetWeaponBurstFireCount(int amount)

    .. _CWeaponX-EnableCatchAnimation:

    .. cpp:function:: unknown EnableCatchAnimation(unknown)

    .. _CWeaponX-GetAttackPosition:

    .. cpp:function:: vector GetAttackPosition()

    .. _CWeaponX-SmartAmmo-SetTarget:

    .. cpp:function:: unknown SmartAmmo_SetTarget(unknown)

    .. _CWeaponX-GetWeaponReadyMsg:

    .. cpp:function:: unknown GetWeaponReadyMsg(unknown)

    .. _CWeaponX-SmartAmmo-GetNewTargetTime:

    .. cpp:function:: unknown SmartAmmo_GetNewTargetTime(unknown)

    .. _CWeaponX-StopWeaponSound:

    .. cpp:function:: void StopWeaponSound(string sound)

    .. _CWeaponX-SetWeaponCamo:

    .. cpp:function:: unknown SetWeaponCamo(unknown)

    .. _CWeaponX-GetWeaponClass:

    .. cpp:function:: string GetWeaponClass()

    .. _CWeaponX-PlayWeaponEffectNoCull:

    .. cpp:function:: void PlayWeaponEffectNoCull(asset effect1P, asset effect3P, string tagName)

    .. _CWeaponX-GetWeaponClassName:

    .. cpp:function:: string GetWeaponClassName()

    .. _CWeaponX-GetSmartAmmoHudLockStyle:

    .. cpp:function:: unknown GetSmartAmmoHudLockStyle(unknown)

    .. _CWeaponX-SmartAmmo-GetFirePosition:

    .. cpp:function:: vector SmartAmmo_GetFirePosition(entity target, int burstIndex)

    .. _CWeaponX-StopWeaponEffect:

    .. cpp:function:: void StopWeaponEffect(asset effect1P, asset effect3P)

    .. _CWeaponX-TimeUntilReadyToFire:

    .. cpp:function:: unknown TimeUntilReadyToFire(unknown)

    .. _CWeaponX-GetWeaponSettingVector:

    .. cpp:function:: unknown GetWeaponSettingVector(unknown)

    .. _CWeaponX-SmartAmmo-StoreTargets:

    .. cpp:function:: void SmartAmmo_StoreTargets()

    .. _CWeaponX-AllowUse:

    .. cpp:function:: bool AllowUse()

    .. _CWeaponX-IsWeaponRegenDraining:

    .. cpp:function:: bool IsWeaponRegenDraining()

    .. _CWeaponX-EmitWeaponNpcSound:

    .. cpp:function:: void EmitWeaponNpcSound(int volume, float duration)

    .. _CWeaponX-EmitWeaponNpcSound-DontUpdateLastFiredTime:

    .. cpp:function:: void EmitWeaponNpcSound_DontUpdateLastFiredTime(int volume, float time)

    .. _CWeaponX-IsNetOptimized:

    .. cpp:function:: unknown IsNetOptimized(unknown)

    .. _CWeaponX-GetMeleeCanHitHumanSized:

    .. cpp:function:: bool GetMeleeCanHitHumanSized()

    .. _CWeaponX-FireWeaponBolt:

    .. cpp:function:: entity FireWeaponBolt(vector origin, vector dir, float projectileSpeed, int contactDamageType, int explosionDamageType, bool predict, int index)

    .. _CWeaponX-GetWeaponUtilityEntity:

    .. cpp:function:: entity GetWeaponUtilityEntity()

    .. _CWeaponX-FireWeaponGrenade:

    .. cpp:function:: entity FireWeaponGrenade(vector attackPos, vector throwVelocity, vector angularVelocity, float fuseTime, int contactDamageType, int explosionDamageType, bool isPredicted, bool isLagCompensated, bool bounce?)

    .. _CWeaponX-GetAmmoPerShot:

    .. cpp:function:: int GetAmmoPerShot()

    .. _CWeaponX-FireWeaponBullet:

    .. cpp:function:: entity FireWeaponBullet(vector origin, vector dir, int numBullets, damageType)

    .. _CWeaponX-GetDamageAmountForArmorType:

    .. cpp:function:: int GetDamageAmountForArmorType(int armor)

    .. _CWeaponX-RegenerateAmmoReset:

    .. cpp:function:: void RegenerateAmmoReset()

    .. _CWeaponX-IsWeaponInAds:

    .. cpp:function:: bool IsWeaponInAds()

    .. _CWeaponX-GetWeaponType:

    .. cpp:function:: int GetWeaponType()

    .. _CWeaponX-IsWeaponCharging:

    .. cpp:function:: unknown IsWeaponCharging(unknown)

    .. _CWeaponX-EmitWeaponSound-1p3p:

    .. cpp:function:: void EmitWeaponSound_1p3p(string sound1P, string sound3P)

    .. _CWeaponX-GetBurstFireShotsPending:

    .. cpp:function:: int GetBurstFireShotsPending()

    .. _CWeaponX-IsChargeWeapon:

    .. cpp:function:: bool IsChargeWeapon()

    .. _CWeaponX-SmartAmmo-SetNewTargetTime:

    .. cpp:function:: unknown SmartAmmo_SetNewTargetTime(unknown)

    .. _CWeaponX-SmartAmmo-GetTargets:

    .. cpp:function:: array<entity> SmartAmmo_GetTargets()

    .. _CWeaponX-ResetWeaponToDefaultEnergyCost:

    .. cpp:function:: void ResetWeaponToDefaultEnergyCost()

    .. _CWeaponX-SmartAmmo-GetSearchAngle:

    .. cpp:function:: unknown SmartAmmo_GetSearchAngle(unknown)

    .. _CWeaponX-GetMeleeLungeTargetRange:

    .. cpp:function:: float GetMeleeLungeTargetRange()

    .. _CWeaponX-GetMeleeLungeTargetAngle:

    .. cpp:function:: unknown GetMeleeLungeTargetAngle(unknown)

    .. _CWeaponX-GetGrenadeFuseTime:

    .. cpp:function:: float GetGrenadeFuseTime()

    .. _CWeaponX-GetDamageSourceID:

    .. cpp:function:: int GetDamageSourceID()

