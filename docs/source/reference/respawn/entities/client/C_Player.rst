.. _C-Player:

C_Player
========

.. cpp:class:: C_Player extends C_BaseAnimating

    Inherits all properties from :ref:`C_BaseAnimating <C-BaseAnimating>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_Player-Lunge-SetMaxTime:

    .. cpp:function:: unknown Lunge_SetMaxTime(unknown)

    .. _C_Player-GetRodeoRider:

    .. cpp:function:: entity GetRodeoRider()

    .. _C_Player-GetWeaponAmmoMaxLoaded:

    .. cpp:function:: int GetWeaponAmmoMaxLoaded(entity weapon)

    .. _C_Player-GetVoicePackIndex:

    .. cpp:function:: unknown GetVoicePackIndex(unknown)

    .. _C_Player-DisablePhaseShiftFlags:

    .. cpp:function:: void DisablePhaseShiftFlags()

    .. _C_Player-IsInThirdPersonReplay:

    .. cpp:function:: bool IsInThirdPersonReplay()

    .. _C_Player-SniperCam-Activate:

    .. cpp:function:: unknown SniperCam_Activate(unknown)

    .. _C_Player-Weapon-CustomActivityClearAttachedModel:

    .. cpp:function:: unknown Weapon_CustomActivityClearAttachedModel(unknown)

    .. _C_Player-DisableWeaponViewModel:

    .. cpp:function:: unknown DisableWeaponViewModel(unknown)

    .. _C_Player-GetPlayerRequestedSettingsField:

    .. cpp:function:: unknown GetPlayerRequestedSettingsField(unknown)

    .. _C_Player-PlayerMelee-SetState:

    .. cpp:function:: void PlayerMelee_SetState(int state)

    .. _C_Player-JoltCockpitOrigin:

    .. cpp:function:: unknown JoltCockpitOrigin(unknown)

    .. _C_Player-Rodeo-StopCameraSmoothing:

    .. cpp:function:: void Rodeo_StopCameraSmoothing(float factor)

    .. _C_Player-GetRemoteTurret:

    .. cpp:function:: entity GetRemoteTurret()

    .. _C_Player-GetPlayerMins:

    .. cpp:function:: unknown GetPlayerMins(unknown)

    .. _C_Player-ContextAction-IsMeleeExecutionTarget:

    .. cpp:function:: bool ContextAction_IsMeleeExecutionTarget()

    .. _C_Player-IsMuted:

    .. cpp:function:: bool IsMuted()

    .. _C_Player-GetPlayerGameStat:

    .. cpp:function:: int GetPlayerGameStat(int PGS)

    .. _C_Player-SetOneHandedWeaponUsageOn:

    .. cpp:function:: unknown SetOneHandedWeaponUsageOn(unknown)

    .. _C_Player-GetViewVector:

    .. cpp:function:: vector GetViewVector()

    .. _C_Player-CameraAngles:

    .. cpp:function:: vector CameraAngles()

    .. _C_Player-GetEntScreenSpaceBounds:

    .. cpp:function:: EntityScreenSpaceBounds GetEntScreenSpaceBounds(entity ent, int padding)

    .. _C_Player-PlayerMelee-ExecutionEndTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndTarget(unknown)

    .. _C_Player-PlayerMelee-EndAttack:

    .. cpp:function:: void PlayerMelee_EndAttack()

    .. _C_Player-Lunge-ClearTarget:

    .. cpp:function:: void Lunge_ClearTarget()

    .. _C_Player-IsZipliningInReverse:

    .. cpp:function:: unknown IsZipliningInReverse(unknown)

    .. _C_Player-SmartAmmo-GetHighestLocksOnMeEntities:

    .. cpp:function:: array<entity> SmartAmmo_GetHighestLocksOnMeEntities()

    .. _C_Player-GetPlayerModHealth:

    .. cpp:function:: float GetPlayerModHealth()

    .. _C_Player-GetSuitGrapplePower:

    .. cpp:function:: int GetSuitGrapplePower()

    .. _C_Player-IsGliding:

    .. cpp:function:: unknown IsGliding(unknown)

    .. _C_Player-GetPlayerSettingsAsset:

    .. cpp:function:: unknown GetPlayerSettingsAsset(unknown)

    .. _C_Player-HolsterWeapon:

    .. cpp:function:: void HolsterWeapon()

    .. _C_Player-ContextAction-SetInVehicle:

    .. cpp:function:: unknown ContextAction_SetInVehicle(unknown)

    .. _C_Player-SetMeleeDisabled:

    .. cpp:function:: void SetMeleeDisabled()

    .. _C_Player-GetPlayerOrNPCViewVector:

    .. cpp:function:: vector GetPlayerOrNPCViewVector()

    .. _C_Player-SmartAmmo-GetHighestLockOnMeFraction:

    .. cpp:function:: float SmartAmmo_GetHighestLockOnMeFraction()

    .. _C_Player-SetSelectedOffhandToMelee:

    .. cpp:function:: void SetSelectedOffhandToMelee()

    .. _C_Player-Lunge-IsLungingToPosition:

    .. cpp:function:: unknown Lunge_IsLungingToPosition(unknown)

    .. _C_Player-GetLastFiredTime:

    .. cpp:function:: unknown GetLastFiredTime(unknown)

    .. _C_Player-AddSharedEnergy:

    .. cpp:function:: void AddSharedEnergy(int amount)

    .. _C_Player-IsPlayback:

    .. cpp:function:: unknown IsPlayback(unknown)

    .. _C_Player-GetXP:

    .. cpp:function:: int GetXP()

    .. _C_Player-GetCrosshairPos:

    .. cpp:function:: unknown GetCrosshairPos(unknown)

    .. _C_Player-Weapon-GetCustomActivityDuration:

    .. cpp:function:: unknown Weapon_GetCustomActivityDuration(unknown)

    .. _C_Player-GetSuitPower:

    .. cpp:function:: unknown GetSuitPower(unknown)

    .. _C_Player-ViewOffsetEntity-SetLerpOutTime:

    .. cpp:function:: unknown ViewOffsetEntity_SetLerpOutTime(unknown)

    .. _C_Player-GetObjectiveIndex:

    .. cpp:function:: int GetObjectiveIndex()

    .. _C_Player-GetViewRight:

    .. cpp:function:: vector GetViewRight()

    .. _C_Player-GetPlayerRagdoll:

    .. cpp:function:: unknown GetPlayerRagdoll(unknown)

    .. _C_Player-ClearOffhand:

    .. cpp:function:: unknown ClearOffhand(unknown)

    .. _C_Player-SetLastPingTime:

    .. cpp:function:: void SetLastPingTime(float time)

    .. _C_Player-GetTitanEmbarkEnabled:

    .. cpp:function:: bool GetTitanEmbarkEnabled()

    .. _C_Player-Rodeo-StartCameraSmoothing:

    .. cpp:function:: void Rodeo_StartCameraSmoothing(float factor)

    .. _C_Player-ViewOffsetEntity-SetLerpInTime:

    .. cpp:function:: unknown ViewOffsetEntity_SetLerpInTime(unknown)

    .. _C_Player-GetOutOfBoundsDeadTime:

    .. cpp:function:: int GetOutOfBoundsDeadTime()

    .. _C_Player-ContextAction-IsFastball:

    .. cpp:function:: unknown ContextAction_IsFastball(unknown)

    .. _C_Player-GetLastPingTime:

    .. cpp:function:: float GetLastPingTime()

    .. _C_Player-ContextAction-IsLeeching:

    .. cpp:function:: bool ContextAction_IsLeeching()

    .. _C_Player-GetMeleeDisabled:

    .. cpp:function:: unknown GetMeleeDisabled(unknown)

    .. _C_Player-PlayerMelee-ExecutionEndAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndAttacker(unknown)

    .. _C_Player-GetHotDropImpactTime:

    .. cpp:function:: float GetHotDropImpactTime(entity titan = this.titan, string animation = HOTDROP_TURBO_ANIM)

    .. _C_Player-PhaseShiftCancel:

    .. cpp:function:: void PhaseShiftCancel()

    .. _C_Player-HasClassPosMod:

    .. cpp:function:: unknown HasClassPosMod(unknown)

    .. _C_Player-GetDodgePower:

    .. cpp:function:: int GetDodgePower()

    .. _C_Player-GetForcedDialogueOnly:

    .. cpp:function:: bool GetForcedDialogueOnly()

    .. _C_Player-HasUsePrompt:

    .. cpp:function:: unknown HasUsePrompt(unknown)

    .. _C_Player-IsDoubleJumping:

    .. cpp:function:: unknown IsDoubleJumping(unknown)

    .. _C_Player-Lunge-SetTargetEntity:

    .. cpp:function:: void Lunge_SetTargetEntity(entity target, bool unknown_purpose)

    .. _C_Player-GetNumPingsUsed:

    .. cpp:function:: unknown GetNumPingsUsed(unknown)

    .. _C_Player-IsBot:

    .. cpp:function:: bool IsBot()

    .. _C_Player-GetGen:

    .. cpp:function:: int GetGen()

    .. _C_Player-GetPlayerMaxs:

    .. cpp:function:: unknown GetPlayerMaxs(unknown)

    .. _C_Player-GetObserverMode:

    .. cpp:function:: int GetObserverMode()

    .. _C_Player-Weapon-CustomActivityAttachModel:

    .. cpp:function:: unknown Weapon_CustomActivityAttachModel(unknown)

    .. _C_Player-HideCrosshairNames:

    .. cpp:function:: void HideCrosshairNames()

    .. _C_Player-IsUsingOffhandWeapon:

    .. cpp:function:: unknown IsUsingOffhandWeapon(unknown)

    .. _C_Player-TakeSharedEnergy:

    .. cpp:function:: void TakeSharedEnergy(int amount)

    .. _C_Player-JoltCockpitAngles:

    .. cpp:function:: unknown JoltCockpitAngles(unknown)

    .. _C_Player-GetFOV:

    .. cpp:function:: unknown GetFOV(unknown)

    .. _C_Player-FreezeControlsOnClient:

    .. cpp:function:: void FreezeControlsOnClient()

    .. _C_Player-ContextAction-IsRequisitionBattery:

    .. cpp:function:: unknown ContextAction_IsRequisitionBattery(unknown)

    .. _C_Player-InPartyChat:

    .. cpp:function:: bool InPartyChat()

    .. _C_Player-HasPassive:

    .. cpp:function:: bool HasPassive(int passive)

    .. _C_Player-IsScriptMenuOn:

    .. cpp:function:: unknown IsScriptMenuOn(unknown)

    .. _C_Player-Lunge-GetStartPositionOffset:

    .. cpp:function:: vector Lunge_GetStartPositionOffset()

    .. _C_Player-GetPlayerRequestedSettings:

    .. cpp:function:: unknown GetPlayerRequestedSettings(unknown)

    .. _C_Player-PlayerMelee-StartAttack:

    .. cpp:function:: void PlayerMelee_StartAttack(int attackState)

    .. _C_Player-GetSkillMU:

    .. cpp:function:: unknown GetSkillMU(unknown)

    .. _C_Player-GetAntiTitanWeapon:

    .. cpp:function:: entity GetAntiTitanWeapon()

    .. _C_Player-GetNumRodeoSlots:

    .. cpp:function:: int GetNumRodeoSlots()

    .. _C_Player-GetCrosshairData:

    .. cpp:function:: unknown GetCrosshairData(unknown)

    .. _C_Player-IsHoverEnabled:

    .. cpp:function:: unknown IsHoverEnabled(unknown)

    .. _C_Player-SetHoldToSwapSlot:

    .. cpp:function:: unknown SetHoldToSwapSlot(unknown)

    .. _C_Player-SetSafeHealthFrac:

    .. cpp:function:: unknown SetSafeHealthFrac(unknown)

    .. _C_Player-SniperCam-GetParams:

    .. cpp:function:: unknown SniperCam_GetParams(unknown)

    .. _C_Player-GetBodyType:

    .. cpp:function:: string GetBodyType()

    .. _C_Player-GetFirstPersonProxy:

    .. cpp:function:: entity GetFirstPersonProxy()

    .. _C_Player-GetViewModelEntity:

    .. cpp:function:: entity GetViewModelEntity()

    .. _C_Player-Lunge-IsLungingToEntity:

    .. cpp:function:: bool Lunge_IsLungingToEntity()

    .. _C_Player-ContextAction-ClearBusy:

    .. cpp:function:: void ContextAction_ClearBusy()

    .. _C_Player-DisableWeaponWithSlowHolster:

    .. cpp:function:: unknown DisableWeaponWithSlowHolster(unknown)

    .. _C_Player-ContextAction-IsBusy:

    .. cpp:function:: bool ContextAction_IsBusy()

    .. _C_Player-GetSuitJumpPower:

    .. cpp:function:: unknown GetSuitJumpPower(unknown)

    .. _C_Player-GetCinematicEventFlags:

    .. cpp:function:: int GetCinematicEventFlags()

    .. _C_Player-GetPlayerRequestedClass:

    .. cpp:function:: unknown GetPlayerRequestedClass(unknown)

    .. _C_Player-GetTitanDisembarkEnabled:

    .. cpp:function:: bool GetTitanDisembarkEnabled()

    .. _C_Player-GetPlayerName:

    .. cpp:function:: string GetPlayerName()

    .. _C_Player-GetSharedEnergyTotal:

    .. cpp:function:: int GetSharedEnergyTotal()

    .. _C_Player-ContextAction-IsRodeo:

    .. cpp:function:: unknown ContextAction_IsRodeo(unknown)

    .. _C_Player-GetMainWeapons:

    .. cpp:function:: array<entity> GetMainWeapons()

    .. _C_Player-HasMic:

    .. cpp:function:: bool HasMic()

    .. _C_Player-ClientCommand:

    .. cpp:function:: void ClientCommand(string command)

    .. _C_Player-SniperCam-IsActive:

    .. cpp:function:: unknown SniperCam_IsActive(unknown)

    .. _C_Player-SetPingGroupStartTime:

    .. cpp:function:: void SetPingGroupStartTime(float gametime)

    .. _C_Player-Lunge-GetEndPositionOffset:

    .. cpp:function:: vector Lunge_GetEndPositionOffset()

    .. _C_Player-SetSharedEnergyRegenRate:

    .. cpp:function:: unknown SetSharedEnergyRegenRate(unknown)

    .. _C_Player-GetLevel:

    .. cpp:function:: int GetLevel()

    .. _C_Player-GetViewUp:

    .. cpp:function:: vector GetViewUp()

    .. _C_Player-UnfreezeControlsOnClient:

    .. cpp:function:: unknown UnfreezeControlsOnClient(unknown)

    .. _C_Player-GetObserverTarget:

    .. cpp:function:: entity GetObserverTarget()

    .. _C_Player-GetEntityAtPhaseShiftExitPosition:

    .. cpp:function:: entity GetEntityAtPhaseShiftExitPosition()

    .. _C_Player-IsHovering:

    .. cpp:function:: unknown IsHovering(unknown)

    .. _C_Player-IsInAirSlowMo:

    .. cpp:function:: unknown IsInAirSlowMo(unknown)

    .. _C_Player-GetPlayerSettings:

    .. cpp:function:: string GetPlayerSettings()

    .. _C_Player-CanUseSharedEnergy:

    .. cpp:function:: bool CanUseSharedEnergy(int curCost)

    .. _C_Player-IsPhaseShiftedOrPending:

    .. cpp:function:: unknown IsPhaseShiftedOrPending(unknown)

    .. _C_Player-RumbleEffect:

    .. cpp:function:: void RumbleEffect(int x, int y, int z)

    .. _C_Player-GetObjectiveEndTime:

    .. cpp:function:: float GetObjectiveEndTime()

    .. _C_Player-CreateClientPointCamera:

    .. cpp:function:: unknown CreateClientPointCamera(unknown)

    .. _C_Player-GetLatestPrimaryWeapon:

    .. cpp:function:: entity GetLatestPrimaryWeapon()

    .. _C_Player-PlayerMelee-ExecutionStartAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartAttacker(unknown)

    .. _C_Player-ContextAction-IsMeleeExecution:

    .. cpp:function:: bool ContextAction_IsMeleeExecution()

    .. _C_Player-HasBadReputation:

    .. cpp:function:: bool HasBadReputation()

    .. _C_Player-TraceToLocalPlayer:

    .. cpp:function:: TraceResults TraceToLocalPlayer()

    .. _C_Player-DisableWeapon:

    .. cpp:function:: unknown DisableWeapon(unknown)

    .. _C_Player-GetPlayerNetInt:

    .. cpp:function:: int GetPlayerNetInt(string state)

    .. _C_Player-OffsetPositionFromView:

    .. cpp:function:: vector OffsetPositionFromView(vector startPos, vector offset)

    .. _C_Player-PlayerMelee-SetAttackRecoveryShouldBeQuick:

    .. cpp:function:: void PlayerMelee_SetAttackRecoveryShouldBeQuick(bool beQuick)

    .. _C_Player-GetPlayerClass:

    .. cpp:function:: string GetPlayerClass()

    .. _C_Player-GetSharedEnergyCount:

    .. cpp:function:: int GetSharedEnergyCount()

    .. _C_Player-HasGrapple:

    .. cpp:function:: unknown HasGrapple(unknown)

    .. _C_Player-GetPilotClassIndex:

    .. cpp:function:: unknown GetPilotClassIndex(unknown)

    .. _C_Player-ContextAction-IsZipline:

    .. cpp:function:: unknown ContextAction_IsZipline(unknown)

    .. _C_Player-MayGrapple:

    .. cpp:function:: bool MayGrapple()

    .. _C_Player-Grapple:

    .. cpp:function:: void Grapple(vector direction)

    .. _C_Player-GetObjectiveEntity:

    .. cpp:function:: entity GetObjectiveEntity()

    .. _C_Player-ContextAction-ClearInVehicle:

    .. cpp:function:: unknown ContextAction_ClearInVehicle(unknown)

    .. _C_Player-GetPersistentVar:

    .. cpp:function:: var GetPersistentVar(string key)

    .. _C_Player-GetAbilityUpBinding:

    .. cpp:function:: unknown GetAbilityUpBinding(unknown)

    .. _C_Player-StopArcCannon:

    .. cpp:function:: void StopArcCannon()

    .. _C_Player-GetInputAxisForward:

    .. cpp:function:: float GetInputAxisForward()

    .. _C_Player-IsWallRunning:

    .. cpp:function:: void IsWallRunning()

    .. _C_Player-DeployWeapon:

    .. cpp:function:: void DeployWeapon()

    .. _C_Player-GetRank:

    .. cpp:function:: unknown GetRank(unknown)

    .. _C_Player-GetActiveBurnCardIndex:

    .. cpp:function:: int GetActiveBurnCardIndex()

    .. _C_Player-CockpitJolt:

    .. cpp:function:: void CockpitJolt(vector joltDir, float severity)

    .. _C_Player-IsCrouched:

    .. cpp:function:: bool IsCrouched()

    .. _C_Player-ContextAction-IsActive:

    .. cpp:function:: bool ContextAction_IsActive()

    .. _C_Player-GetPlayerSettingsField:

    .. cpp:function:: string GetPlayerSettingsField(string field)

    .. _C_Player-PlayerMelee-IsAttackActive:

    .. cpp:function:: bool PlayerMelee_IsAttackActive()

    .. _C_Player-GetPlayerModsForPos:

    .. cpp:function:: unknown GetPlayerModsForPos(unknown)

    .. _C_Player-GetActiveWeaponPrimaryAmmoLoaded:

    .. cpp:function:: int GetActiveWeaponPrimaryAmmoLoaded()

    .. _C_Player-GetFaction:

    .. cpp:function:: unknown GetFaction(unknown)

    .. _C_Player-GetCommunityName:

    .. cpp:function:: unknown GetCommunityName(unknown)

    .. _C_Player-SetFOVScale:

    .. cpp:function:: unknown SetFOVScale(unknown)

    .. _C_Player-StopEffectOnPlayerHands:

    .. cpp:function:: unknown StopEffectOnPlayerHands(unknown)

    .. _C_Player-StartEffectOnPlayerHands:

    .. cpp:function:: unknown StartEffectOnPlayerHands(unknown)

    .. _C_Player-GetPlayerNetEnt:

    .. cpp:function:: entity GetPlayerNetEnt(string key)

    .. _C_Player-GetPlayerNetTime:

    .. cpp:function:: float GetPlayerNetTime(string key)

    .. _C_Player-IsSprinting:

    .. cpp:function:: unknown IsSprinting(unknown)

    .. _C_Player-GetSharedEnergyRegenDelay:

    .. cpp:function:: unknown GetSharedEnergyRegenDelay(unknown)

    .. _C_Player-GetPlayerNetBool:

    .. cpp:function:: bool GetPlayerNetBool(string key)

    .. _C_Player-GetAdsFraction:

    .. cpp:function:: float GetAdsFraction()

    .. _C_Player-OffsetFromViewAngles:

    .. cpp:function:: unknown OffsetFromViewAngles(unknown)

    .. _C_Player-GetInputAxisRight:

    .. cpp:function:: float GetInputAxisRight()

    .. _C_Player-IsInputCommandReleased:

    .. cpp:function:: unknown IsInputCommandReleased(unknown)

    .. _C_Player-GetAttackSpread:

    .. cpp:function:: unknown GetAttackSpread(unknown)

    .. _C_Player-IsInputCommandPressed:

    .. cpp:function:: unknown IsInputCommandPressed(unknown)

    .. _C_Player-GetTitanTarget:

    .. cpp:function:: unknown GetTitanTarget(unknown)

    .. _C_Player-EnablePhaseShiftFlags:

    .. cpp:function:: void EnablePhaseShiftFlags()

    .. _C_Player-GetSidearmWeapon:

    .. cpp:function:: unknown GetSidearmWeapon(unknown)

    .. _C_Player-SetNumPingsUsed:

    .. cpp:function:: void SetNumPingsUsed(int num)

    .. _C_Player-GetPingGroupAccumulator:

    .. cpp:function:: int GetPingGroupAccumulator()

    .. _C_Player-Lunge-IsActive:

    .. cpp:function:: bool Lunge_IsActive()

    .. _C_Player-GetPingGroupStartTime:

    .. cpp:function:: float GetPingGroupStartTime()

    .. _C_Player-GetNumPingsAvailable:

    .. cpp:function:: int GetNumPingsAvailable()

    .. _C_Player-IsBoosting:

    .. cpp:function:: unknown IsBoosting(unknown)

    .. _C_Player-IsClassPosModAvailableForPlayerSetting:

    .. cpp:function:: unknown IsClassPosModAvailableForPlayerSetting(unknown)

    .. _C_Player-GetSharedEnergyRegenRate:

    .. cpp:function:: unknown GetSharedEnergyRegenRate(unknown)

    .. _C_Player-IsStanding:

    .. cpp:function:: bool IsStanding()

    .. _C_Player-HasClassMod:

    .. cpp:function:: unknown HasClassMod(unknown)

    .. _C_Player-ContextAction-SetFastball:

    .. cpp:function:: unknown ContextAction_SetFastball(unknown)

    .. _C_Player-GetPersistentVarAsInt:

    .. cpp:function:: int GetPersistentVarAsInt(string key)

    .. _C_Player-PhaseShiftBegin:

    .. cpp:function:: void PhaseShiftBegin(float warmUpTime, float duration)

    .. _C_Player-SetNumPingsAvailable:

    .. cpp:function:: void SetNumPingsAvailable(int num)

    .. _C_Player-TraceToLocalPlayerSimple:

    .. cpp:function:: float TraceToLocalPlayerSimple()

    .. _C_Player-ContextAction-IsInVehicle:

    .. cpp:function:: unknown ContextAction_IsInVehicle(unknown)

    .. _C_Player-GetMeleeWeapon:

    .. cpp:function:: entity GetMeleeWeapon()

    .. _C_Player-GetWeaponAmmoStockpile:

    .. cpp:function:: int GetWeaponAmmoStockpile(entity weapon)

    .. _C_Player-SetSharedEnergyRegenDelay:

    .. cpp:function:: void SetSharedEnergyRegenDelay(float delay)

    .. _C_Player-StartArcCannon:

    .. cpp:function:: void StartArcCannon()

    .. _C_Player-GetTargetInCrosshairRange:

    .. cpp:function:: unknown GetTargetInCrosshairRange(unknown)

    .. _C_Player-GetOffhandWeapon:

    .. cpp:function:: entity GetOffhandWeapon(int slot)

    .. _C_Player-IsPlayingRanked:

    .. cpp:function:: unknown IsPlayingRanked(unknown)

    .. _C_Player-GetTitanSoul:

    .. cpp:function:: entity GetTitanSoul()

    .. _C_Player-SetMenuCameraEntity:

    .. cpp:function:: unknown SetMenuCameraEntity(unknown)

    .. _C_Player-IsZiplining:

    .. cpp:function:: bool IsZiplining()

    .. _C_Player-GetPlayerNetFloat:

    .. cpp:function:: float GetPlayerNetFloat(string state)

    .. _C_Player-Weapon-StartCustomActivity:

    .. cpp:function:: void Weapon_StartCustomActivity(string animation, bool unknown_purpose)

    .. _C_Player-EnableWeaponWithSlowDeploy:

    .. cpp:function:: unknown EnableWeaponWithSlowDeploy(unknown)

    .. _C_Player-EnableWeapon:

    .. cpp:function:: unknown EnableWeapon(unknown)

    .. _C_Player-Lunge-SetMaxEndSpeed:

    .. cpp:function:: unknown Lunge_SetMaxEndSpeed(unknown)

    .. _C_Player-GetOffhandWeapons:

    .. cpp:function:: array<entity> GetOffhandWeapons()

    .. _C_Player-SetScriptMenuOff:

    .. cpp:function:: void SetScriptMenuOff()

    .. _C_Player-Dev-GetPlayerSettingByKeyField:

    .. cpp:function:: unknown Dev_GetPlayerSettingByKeyField(unknown)

    .. _C_Player-SniperCam-SetParams:

    .. cpp:function:: unknown SniperCam_SetParams(unknown)

    .. _C_Player-IsWeaponDisabled:

    .. cpp:function:: bool IsWeaponDisabled()

    .. _C_Player-ClearMeleeDisabled:

    .. cpp:function:: void ClearMeleeDisabled()

    .. _C_Player-ClearMenuCameraEntity:

    .. cpp:function:: unknown ClearMenuCameraEntity(unknown)

    .. _C_Player-IsThirdPersonObserver:

    .. cpp:function:: unknown IsThirdPersonObserver(unknown)

    .. _C_Player-GetSyncedEntity:

    .. cpp:function:: unknown GetSyncedEntity(unknown)

    .. _C_Player-GetPlayerModHealthPerSegment:

    .. cpp:function:: unknown GetPlayerModHealthPerSegment(unknown)

    .. _C_Player-IsInputCommandHeld:

    .. cpp:function:: bool IsInputCommandHeld(int flag)

    .. _C_Player-GetPredictedFirstPersonProxy:

    .. cpp:function:: enitity GetPredictedFirstPersonProxy()

    .. _C_Player-SetHandsEffectControlPoint:

    .. cpp:function:: unknown SetHandsEffectControlPoint(unknown)

    .. _C_Player-Lunge-IsGroundExecute:

    .. cpp:function:: bool Lunge_IsGroundExecute()

    .. _C_Player-GetActiveWeapon:

    .. cpp:function:: enitity GetActiveWeapon()

    .. _C_Player-GetAttackSpreadAngle:

    .. cpp:function:: float GetAttackSpreadAngle()

    .. _C_Player-IsWallHanging:

    .. cpp:function:: bool IsWallHanging()

    .. _C_Player-ContextAction-IsMeleeExecutionAttacker:

    .. cpp:function:: unknown ContextAction_IsMeleeExecutionAttacker(unknown)

    .. _C_Player-ContextAction-ClearFastball:

    .. cpp:function:: unknown ContextAction_ClearFastball(unknown)

    .. _C_Player-GetSelectedWeapon:

    .. cpp:function:: unknown GetSelectedWeapon(unknown)

    .. _C_Player-SetSharedEnergyTotal:

    .. cpp:function:: unknown SetSharedEnergyTotal(unknown)

    .. _C_Player-GetFirstRodeoRider:

    .. cpp:function:: enitity GetFirstRodeoRider()

    .. _C_Player-IsObserver:

    .. cpp:function:: unknown IsObserver(unknown)

    .. _C_Player-CameraPosition:

    .. cpp:function:: vector CameraPosition()

    .. _C_Player-GetPlayerSettingsMods:

    .. cpp:function:: array<string> GetPlayerSettingsMods()

    .. _C_Player-SetRodeoLookHeight:

    .. cpp:function:: unknown SetRodeoLookHeight(unknown)

    .. _C_Player-PhaseShiftTimePassed:

    .. cpp:function:: unknown PhaseShiftTimePassed(unknown)

    .. _C_Player-PlayerMelee-ExecutionStartTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartTarget(unknown)

    .. _C_Player-GetTitanBubbleShieldTime:

    .. cpp:function:: unknown GetTitanBubbleShieldTime(unknown)

    .. _C_Player-SetPingGroupAccumulator:

    .. cpp:function:: void SetPingGroupAccumulator(int acc)

    .. _C_Player-ContextAction-SetBusy:

    .. cpp:function:: void ContextAction_SetBusy()

    .. _C_Player-GetTitanSoulBeingRodeoed:

    .. cpp:function:: entity GetTitanSoulBeingRodeoed()

    .. _C_Player-SetRodeoLookDistance:

    .. cpp:function:: unknown SetRodeoLookDistance(unknown)

    .. _C_Player-UnhideCrosshairNames:

    .. cpp:function:: void UnhideCrosshairNames()

    .. _C_Player-GetUsePromptEntity:

    .. cpp:function:: unknown GetUsePromptEntity(unknown)

    .. _C_Player-GetViewForward:

    .. cpp:function:: vector GetViewForward()

    .. _C_Player-SetScriptMenuOn:

    .. cpp:function:: void SetScriptMenuOn()

    .. _C_Player-GetZoomFrac:

    .. cpp:function:: float GetZoomFrac()

    .. _C_Player-GetPetTitan:

    .. cpp:function:: entity GetPetTitan()

    .. _C_Player-GetPetTitanMode:

    .. cpp:function:: int GetPetTitanMode()

    .. _C_Player-GetCockpit:

    .. cpp:function:: entity GetCockpit()

    .. _C_Player-IsPartyLeader:

    .. cpp:function:: bool IsPartyLeader()

    .. _C_Player-GetHardpointEntity:

    .. cpp:function:: entity GetHardpointEntity()

    .. _C_Player-SmartAmmo-GetPreviousHighestLockOnMeFraction:

    .. cpp:function:: float SmartAmmo_GetPreviousHighestLockOnMeFraction()

    .. _C_Player-IsClassModAvailableForPlayerSetting:

    .. cpp:function:: unknown IsClassModAvailableForPlayerSetting(unknown)

    .. _C_Player-GetAbilityDownBinding:

    .. cpp:function:: unknown GetAbilityDownBinding(unknown)

    .. _C_Player-ViewOffsetEntity-SetEntity:

    .. cpp:function:: unknown ViewOffsetEntity_SetEntity(unknown)

    .. _C_Player-GetPlayerSubClass:

    .. cpp:function:: unknown GetPlayerSubClass(unknown)

    .. _C_Player-Weapon-GetCustomActivityFraction:

    .. cpp:function:: unknown Weapon_GetCustomActivityFraction(unknown)

    .. _C_Player-Lunge-LockPitch:

    .. cpp:function:: void Lunge_LockPitch(bool lock)

    .. _C_Player-Lunge-SetSmoothTime:

    .. cpp:function:: void Lunge_SetSmoothTime(float time)

    .. _C_Player-EnableWeaponViewModel:

    .. cpp:function:: unknown EnableWeaponViewModel(unknown)

    .. _C_Player-Weapon-IsInCustomActivity:

    .. cpp:function:: unknown Weapon_IsInCustomActivity(unknown)

    .. _C_Player-GetClassPosCount:

    .. cpp:function:: unknown GetClassPosCount(unknown)

    .. _C_Player-GetUsePromptPosition:

    .. cpp:function:: unknown GetUsePromptPosition(unknown)

    .. _C_Player-PhaseShiftTimeRemaining:

    .. cpp:function:: float PhaseShiftTimeRemaining()

    .. _C_Player-GetWeaponAmmoLoaded:

    .. cpp:function:: int GetWeaponAmmoLoaded(entity weapon)

    .. _C_Player-Weapon-HasCustomActivity:

    .. cpp:function:: unknown Weapon_HasCustomActivity(unknown)

    .. _C_Player-IsDodging:

    .. cpp:function:: unknown IsDodging(unknown)

    .. _C_Player-IsTraversing:

    .. cpp:function:: void IsTraversing()

    .. _C_Player-IsSliding:

    .. cpp:function:: unknown IsSliding(unknown)

    .. _C_Player-SniperCam-Deactivate:

    .. cpp:function:: unknown SniperCam_Deactivate(unknown)

    .. _C_Player-PlayerMelee-SetAttackHitEntity:

    .. cpp:function:: void PlayerMelee_SetAttackHitEntity(entity ent)

    .. _C_Player-PlayerMelee-GetState:

    .. cpp:function:: int PlayerMelee_GetState()

    .. _C_Player-SetTitanEmbarkEnabled:

    .. cpp:function:: void SetTitanEmbarkEnabled(bool enabled)

    .. _C_Player-IsTalking:

    .. cpp:function:: bool IsTalking()

    .. _C_Player-Weapon-StopCustomActivity:

    .. cpp:function:: unknown Weapon_StopCustomActivity(unknown)

    .. _C_Player-GetNextTitanRespawnAvailable:

    .. cpp:function:: float GetNextTitanRespawnAvailable()

    .. _C_Player-SetTitanDisembarkEnabled:

    .. cpp:function:: void SetTitanDisembarkEnabled(bool enabled)

    .. _C_Player-Lunge-GetTargetEntity:

    .. cpp:function:: unknown Lunge_GetTargetEntity(unknown)

    .. _C_Player-Lunge-SetTargetPosition:

    .. cpp:function:: void Lunge_SetTargetPosition(vector pos)

    .. _C_Player-Lunge-GetTargetPosition:

    .. cpp:function:: unknown Lunge_GetTargetPosition(unknown)

    .. _C_Player-Lunge-SetEndPositionOffset:

    .. cpp:function:: void Lunge_SetEndPositionOffset(vector offset)

    .. _C_Player-SetOneHandedWeaponUsageOff:

    .. cpp:function:: unknown SetOneHandedWeaponUsageOff(unknown)

    .. _C_Player-Lunge-EnableFlying:

    .. cpp:function:: void Lunge_EnableFlying()

    .. _C_Player-GetPlayerNameWithClanTag:

    .. cpp:function:: string GetPlayerNameWithClanTag()

    .. _C_Player-SetRodeoLookRight:

    .. cpp:function:: unknown SetRodeoLookRight(unknown)

    .. _C_Player-IsMantling:

    .. cpp:function:: unknown IsMantling(unknown)

    .. _C_Player-PlayerMelee-GetAttackHitEntity:

    .. cpp:function:: entity PlayerMelee_GetAttackHitEntity()

    .. _C_Player-GetTitanBuildTime:

    .. cpp:function:: unknown GetTitanBuildTime(unknown)

    .. _C_Player-Code-GetActiveBurnCardIndex:

    .. cpp:function:: int Code_GetActiveBurnCardIndex()

