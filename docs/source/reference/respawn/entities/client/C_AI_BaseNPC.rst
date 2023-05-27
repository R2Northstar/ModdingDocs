.. _C-AI-BaseNPC:

C_AI_BaseNPC
============

.. cpp:class:: C_AI_BaseNPC extends C_BaseAnimating

    Inherits all properties from :ref:`C_BaseAnimating <C-BaseAnimating>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`C_NPC_Dropship <C-NPC-Dropship>`
    - :ref:`C_NPC_Titan <C-NPC-Titan>`
    - :ref:`C_NPC_SentryTurret <C-NPC-SentryTurret>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_AI_BaseNPC-GetRodeoRider:

    .. cpp:function:: entity GetRodeoRider()

    .. _C_AI_BaseNPC-GetWeaponAmmoMaxLoaded:

    .. cpp:function:: int GetWeaponAmmoMaxLoaded(entity weapon)

    .. _C_AI_BaseNPC-GetMainWeapons:

    .. cpp:function:: array<entity> GetMainWeapons()

    .. _C_AI_BaseNPC-DisablePhaseShiftFlags:

    .. cpp:function:: void DisablePhaseShiftFlags()

    .. _C_AI_BaseNPC-SetSharedEnergyRegenRate:

    .. cpp:function:: unknown SetSharedEnergyRegenRate(unknown)

    .. _C_AI_BaseNPC-GetAISettingsName:

    .. cpp:function:: string GetAISettingsName()

    .. _C_AI_BaseNPC-ContextAction-IsMeleeExecutionTarget:

    .. cpp:function:: bool ContextAction_IsMeleeExecutionTarget()

    .. _C_AI_BaseNPC-GetEntityAtPhaseShiftExitPosition:

    .. cpp:function:: entity GetEntityAtPhaseShiftExitPosition()

    .. _C_AI_BaseNPC-Dev-GetAISettingByKeyField:

    .. cpp:function:: var Dev_GetAISettingByKeyField(string key)

    .. _C_AI_BaseNPC-IsPhaseShiftedOrPending:

    .. cpp:function:: unknown IsPhaseShiftedOrPending(unknown)

    .. _C_AI_BaseNPC-PlayerMelee-ExecutionEndTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndTarget(unknown)

    .. _C_AI_BaseNPC-GetLatestPrimaryWeapon:

    .. cpp:function:: entity GetLatestPrimaryWeapon()

    .. _C_AI_BaseNPC-PlayerMelee-ExecutionStartAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartAttacker(unknown)

    .. _C_AI_BaseNPC-ContextAction-IsMeleeExecution:

    .. cpp:function:: bool ContextAction_IsMeleeExecution()

    .. _C_AI_BaseNPC-TraceToLocalPlayer:

    .. cpp:function:: TraceResults TraceToLocalPlayer()

    .. _C_AI_BaseNPC-ContextAction-SetInVehicle:

    .. cpp:function:: unknown ContextAction_SetInVehicle(unknown)

    .. _C_AI_BaseNPC-GetPlayerOrNPCViewVector:

    .. cpp:function:: vector GetPlayerOrNPCViewVector()

    .. _C_AI_BaseNPC-GetLastFiredTime:

    .. cpp:function:: unknown GetLastFiredTime(unknown)

    .. _C_AI_BaseNPC-AddSharedEnergy:

    .. cpp:function:: void AddSharedEnergy(int amount)

    .. _C_AI_BaseNPC-CanBeGroundExecuted:

    .. cpp:function:: unknown CanBeGroundExecuted(unknown)

    .. _C_AI_BaseNPC-GetWeaponAmmoLoaded:

    .. cpp:function:: int GetWeaponAmmoLoaded(entity weapon)

    .. _C_AI_BaseNPC-ContextAction-IsZipline:

    .. cpp:function:: unknown ContextAction_IsZipline(unknown)

    .. _C_AI_BaseNPC-PhaseShiftTimeRemaining:

    .. cpp:function:: float PhaseShiftTimeRemaining()

    .. _C_AI_BaseNPC-AISetting-LeechAnimSet:

    .. cpp:function:: string AISetting_LeechAnimSet()

    .. _C_AI_BaseNPC-ContextAction-ClearInVehicle:

    .. cpp:function:: unknown ContextAction_ClearInVehicle(unknown)

    .. _C_AI_BaseNPC-ClearOffhand:

    .. cpp:function:: unknown ClearOffhand(unknown)

    .. _C_AI_BaseNPC-AISetting-MaxFlyingSpeed:

    .. cpp:function:: float AISetting_MaxFlyingSpeed()

    .. _C_AI_BaseNPC-ContextAction-IsActive:

    .. cpp:function:: bool ContextAction_IsActive()

    .. _C_AI_BaseNPC-ContextAction-IsFastball:

    .. cpp:function:: unknown ContextAction_IsFastball(unknown)

    .. _C_AI_BaseNPC-ContextAction-IsLeeching:

    .. cpp:function:: bool ContextAction_IsLeeching()

    .. _C_AI_BaseNPC-GetSharedEnergyRegenDelay:

    .. cpp:function:: unknown GetSharedEnergyRegenDelay(unknown)

    .. _C_AI_BaseNPC-PlayerMelee-ExecutionEndAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndAttacker(unknown)

    .. _C_AI_BaseNPC-AISetting-LeechDataKnifeTag:

    .. cpp:function:: string AISetting_LeechDataKnifeTag()

    .. _C_AI_BaseNPC-AISetting-LeechAnimTag:

    .. cpp:function:: unknown AISetting_LeechAnimTag(unknown)

    .. _C_AI_BaseNPC-GetMeleeDamageMaxForTarget:

    .. cpp:function:: int GetMeleeDamageMaxForTarget(entity target)

    .. _C_AI_BaseNPC-Dev-GetAISettingAssetByKeyField:

    .. cpp:function:: unknown Dev_GetAISettingAssetByKeyField(unknown)

    .. _C_AI_BaseNPC-AISetting-MeleeChargeSet:

    .. cpp:function:: unknown AISetting_MeleeChargeSet(unknown)

    .. _C_AI_BaseNPC-IsNonCombatAI:

    .. cpp:function:: unknown IsNonCombatAI(unknown)

    .. _C_AI_BaseNPC-CanBeMeleeExecuted:

    .. cpp:function:: unknown CanBeMeleeExecuted(unknown)

    .. _C_AI_BaseNPC-GetSubclass:

    .. cpp:function:: unknown GetSubclass(unknown)

    .. _C_AI_BaseNPC-GetActiveWeapon:

    .. cpp:function:: enitity GetActiveWeapon()

    .. _C_AI_BaseNPC-GetAIClass:

    .. cpp:function:: int GetAIClass()

    .. _C_AI_BaseNPC-ContextAction-SetBusy:

    .. cpp:function:: void ContextAction_SetBusy()

    .. _C_AI_BaseNPC-EnablePhaseShiftFlags:

    .. cpp:function:: void EnablePhaseShiftFlags()

    .. _C_AI_BaseNPC-PlayerMelee-ExecutionStartTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartTarget(unknown)

    .. _C_AI_BaseNPC-GetSharedEnergyRegenRate:

    .. cpp:function:: unknown GetSharedEnergyRegenRate(unknown)

    .. _C_AI_BaseNPC-GetSharedEnergyTotal:

    .. cpp:function:: int GetSharedEnergyTotal()

    .. _C_AI_BaseNPC-PhaseShiftTimePassed:

    .. cpp:function:: unknown PhaseShiftTimePassed(unknown)

    .. _C_AI_BaseNPC-GetOffhandWeapons:

    .. cpp:function:: array<entity> GetOffhandWeapons()

    .. _C_AI_BaseNPC-GetAIClassName:

    .. cpp:function:: unknown GetAIClassName(unknown)

    .. _C_AI_BaseNPC-GetActiveWeaponPrimaryAmmoLoaded:

    .. cpp:function:: int GetActiveWeaponPrimaryAmmoLoaded()

    .. _C_AI_BaseNPC-IsInterruptable:

    .. cpp:function:: bool IsInterruptable()

    .. _C_AI_BaseNPC-IsUsingOffhandWeapon:

    .. cpp:function:: unknown IsUsingOffhandWeapon(unknown)

    .. _C_AI_BaseNPC-ContextAction-ClearFastball:

    .. cpp:function:: unknown ContextAction_ClearFastball(unknown)

    .. _C_AI_BaseNPC-TakeSharedEnergy:

    .. cpp:function:: void TakeSharedEnergy(int amount)

    .. _C_AI_BaseNPC-GetAttackSpreadAngle:

    .. cpp:function:: float GetAttackSpreadAngle()

    .. _C_AI_BaseNPC-ContextAction-IsRequisitionBattery:

    .. cpp:function:: unknown ContextAction_IsRequisitionBattery(unknown)

    .. _C_AI_BaseNPC-ContextAction-IsMeleeExecutionAttacker:

    .. cpp:function:: unknown ContextAction_IsMeleeExecutionAttacker(unknown)

    .. _C_AI_BaseNPC-SetSharedEnergyTotal:

    .. cpp:function:: unknown SetSharedEnergyTotal(unknown)

    .. _C_AI_BaseNPC-GetFirstRodeoRider:

    .. cpp:function:: enitity GetFirstRodeoRider()

    .. _C_AI_BaseNPC-GetSelectedWeapon:

    .. cpp:function:: unknown GetSelectedWeapon(unknown)

    .. _C_AI_BaseNPC-GetAntiTitanWeapon:

    .. cpp:function:: entity GetAntiTitanWeapon()

    .. _C_AI_BaseNPC-GetNumRodeoSlots:

    .. cpp:function:: int GetNumRodeoSlots()

    .. _C_AI_BaseNPC-GetBodyType:

    .. cpp:function:: string GetBodyType()

    .. _C_AI_BaseNPC-PhaseShiftCancel:

    .. cpp:function:: void PhaseShiftCancel()

    .. _C_AI_BaseNPC-ContextAction-ClearBusy:

    .. cpp:function:: void ContextAction_ClearBusy()

    .. _C_AI_BaseNPC-GetOffhandWeapon:

    .. cpp:function:: entity GetOffhandWeapon(int slot)

    .. _C_AI_BaseNPC-IsWeaponDisabled:

    .. cpp:function:: bool IsWeaponDisabled()

    .. _C_AI_BaseNPC-SetSharedEnergyRegenDelay:

    .. cpp:function:: void SetSharedEnergyRegenDelay(float delay)

    .. _C_AI_BaseNPC-GetTitanSoul:

    .. cpp:function:: entity GetTitanSoul()

    .. _C_AI_BaseNPC-ContextAction-IsRodeo:

    .. cpp:function:: unknown ContextAction_IsRodeo(unknown)

    .. _C_AI_BaseNPC-GetWeaponAmmoStockpile:

    .. cpp:function:: int GetWeaponAmmoStockpile(entity weapon)

    .. _C_AI_BaseNPC-ContextAction-IsBusy:

    .. cpp:function:: bool ContextAction_IsBusy()

    .. _C_AI_BaseNPC-OffsetPositionFromView:

    .. cpp:function:: vector OffsetPositionFromView(vector startPos, vector offset)

    .. _C_AI_BaseNPC-OffsetFromViewAngles:

    .. cpp:function:: unknown OffsetFromViewAngles(unknown)

    .. _C_AI_BaseNPC-GetMeleeWeapon:

    .. cpp:function:: entity GetMeleeWeapon()

    .. _C_AI_BaseNPC-ContextAction-IsInVehicle:

    .. cpp:function:: unknown ContextAction_IsInVehicle(unknown)

    .. _C_AI_BaseNPC-TraceToLocalPlayerSimple:

    .. cpp:function:: float TraceToLocalPlayerSimple()

    .. _C_AI_BaseNPC-GetSidearmWeapon:

    .. cpp:function:: unknown GetSidearmWeapon(unknown)

    .. _C_AI_BaseNPC-PhaseShiftBegin:

    .. cpp:function:: void PhaseShiftBegin(float warmUpTime, float duration)

    .. _C_AI_BaseNPC-ContextAction-SetFastball:

    .. cpp:function:: unknown ContextAction_SetFastball(unknown)

    .. _C_AI_BaseNPC-CanUseSharedEnergy:

    .. cpp:function:: bool CanUseSharedEnergy(int curCost)

    .. _C_AI_BaseNPC-GetSharedEnergyCount:

    .. cpp:function:: int GetSharedEnergyCount()

