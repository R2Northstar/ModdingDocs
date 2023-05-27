.. _CBaseCombatCharacter:

CBaseCombatCharacter
====================

.. cpp:class:: CBaseCombatCharacter extends CBaseAnimating

    Inherits all properties from :ref:`CBaseAnimating <CBaseAnimating>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`CTurret <CTurret>`
    - :ref:`CPlayer <CPlayer>`
    - :ref:`CAI_BaseNPC <CAI-BaseNPC>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CBaseCombatCharacter-GetRodeoRider:

    .. cpp:function:: entity GetRodeoRider()

    .. _CBaseCombatCharacter-GetMainWeapons:

    .. cpp:function:: array<entity> GetMainWeapons()

    .. _CBaseCombatCharacter-SetRodeoRider:

    .. cpp:function:: void SetRodeoRider(int slot, entity rider)

    .. _CBaseCombatCharacter-DisablePhaseShiftFlags:

    .. cpp:function:: void DisablePhaseShiftFlags()

    .. _CBaseCombatCharacter-GetWeaponAmmoStockpile:

    .. cpp:function:: int GetWeaponAmmoStockpile(entity weapon)

    .. _CBaseCombatCharacter-SetSharedEnergyRegenRate:

    .. cpp:function:: unknown SetSharedEnergyRegenRate(unknown)

    .. _CBaseCombatCharacter-GiveWeapon:

    .. cpp:function:: void GiveWeapon(string weapon)

    .. _CBaseCombatCharacter-GetOffhandWeapons:

    .. cpp:function:: array<entity> GetOffhandWeapons()

    .. _CBaseCombatCharacter-SetActiveWeaponBySlot:

    .. cpp:function:: unknown SetActiveWeaponBySlot(unknown)

    .. _CBaseCombatCharacter-SetSharedEnergyRegenDelay:

    .. cpp:function:: void SetSharedEnergyRegenDelay(float delay)

    .. _CBaseCombatCharacter-GetSharedEnergyTotal:

    .. cpp:function:: int GetSharedEnergyTotal()

    .. _CBaseCombatCharacter-CanUseSharedEnergy:

    .. cpp:function:: bool CanUseSharedEnergy(int curCost)

    .. _CBaseCombatCharacter-TakeSharedEnergy:

    .. cpp:function:: void TakeSharedEnergy(int amount)

    .. _CBaseCombatCharacter-ContextAction-IsRequisitionBattery:

    .. cpp:function:: unknown ContextAction_IsRequisitionBattery(unknown)

    .. _CBaseCombatCharacter-IsValidTetherID:

    .. cpp:function:: unknown IsValidTetherID(unknown)

    .. _CBaseCombatCharacter-RemoveTether:

    .. cpp:function:: unknown RemoveTether(unknown)

    .. _CBaseCombatCharacter-GetLatestPrimaryWeapon:

    .. cpp:function:: entity GetLatestPrimaryWeapon()

    .. _CBaseCombatCharacter-PlayerMelee-ExecutionStartAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartAttacker(unknown)

    .. _CBaseCombatCharacter-AddTether:

    .. cpp:function:: unknown AddTether(unknown)

    .. _CBaseCombatCharacter-SetHudInfoVisibilityTestAlwaysPasses:

    .. cpp:function:: unknown SetHudInfoVisibilityTestAlwaysPasses(unknown)

    .. _CBaseCombatCharacter-GetPlayerOrNPCViewUp:

    .. cpp:function:: unknown GetPlayerOrNPCViewUp(unknown)

    .. _CBaseCombatCharacter-SetNPCPriorityOverride:

    .. cpp:function:: unknown SetNPCPriorityOverride(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsMeleeExecution:

    .. cpp:function:: bool ContextAction_IsMeleeExecution()

    .. _CBaseCombatCharacter-ContextAction-RequisitionBatteryEnd:

    .. cpp:function:: unknown ContextAction_RequisitionBatteryEnd(unknown)

    .. _CBaseCombatCharacter-ContextAction-RequisitionBatteryStart:

    .. cpp:function:: unknown ContextAction_RequisitionBatteryStart(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsInVehicle:

    .. cpp:function:: unknown ContextAction_IsInVehicle(unknown)

    .. _CBaseCombatCharacter-PlayerMelee-ExecutionEndTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndTarget(unknown)

    .. _CBaseCombatCharacter-ContextAction-SetInVehicle:

    .. cpp:function:: unknown ContextAction_SetInVehicle(unknown)

    .. _CBaseCombatCharacter-SetActiveWeaponPrimaryAmmoTotal:

    .. cpp:function:: unknown SetActiveWeaponPrimaryAmmoTotal(unknown)

    .. _CBaseCombatCharacter-PlayerMelee-ExecutionStartTarget:

    .. cpp:function:: unknown PlayerMelee_ExecutionStartTarget(unknown)

    .. _CBaseCombatCharacter-ContextAction-ClearFastball:

    .. cpp:function:: unknown ContextAction_ClearFastball(unknown)

    .. _CBaseCombatCharacter-ContextAction-SetFastball:

    .. cpp:function:: unknown ContextAction_SetFastball(unknown)

    .. _CBaseCombatCharacter-GetPlayerOrNPCViewVector:

    .. cpp:function:: vector GetPlayerOrNPCViewVector()

    .. _CBaseCombatCharacter-DropWeapon:

    .. cpp:function:: unknown DropWeapon(unknown)

    .. _CBaseCombatCharacter-ContextAction-SetBusy:

    .. cpp:function:: void ContextAction_SetBusy()

    .. _CBaseCombatCharacter-GetSelectedWeapon:

    .. cpp:function:: unknown GetSelectedWeapon(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsZipline:

    .. cpp:function:: unknown ContextAction_IsZipline(unknown)

    .. _CBaseCombatCharacter-Event-LeechStart:

    .. cpp:function:: unknown Event_LeechStart(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsRodeo:

    .. cpp:function:: unknown ContextAction_IsRodeo(unknown)

    .. _CBaseCombatCharacter-GetLastFiredTime:

    .. cpp:function:: unknown GetLastFiredTime(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsMeleeExecutionTarget:

    .. cpp:function:: bool ContextAction_IsMeleeExecutionTarget()

    .. _CBaseCombatCharacter-ContextAction-IsMeleeExecutionAttacker:

    .. cpp:function:: unknown ContextAction_IsMeleeExecutionAttacker(unknown)

    .. _CBaseCombatCharacter-AddSharedEnergy:

    .. cpp:function:: void AddSharedEnergy(int amount)

    .. _CBaseCombatCharacter-GetSharedEnergyCount:

    .. cpp:function:: int GetSharedEnergyCount()

    .. _CBaseCombatCharacter-GetEntityAtPhaseShiftExitPosition:

    .. cpp:function:: entity GetEntityAtPhaseShiftExitPosition()

    .. _CBaseCombatCharacter-PhaseShiftTimePassed:

    .. cpp:function:: unknown PhaseShiftTimePassed(unknown)

    .. _CBaseCombatCharacter-PhaseShiftBegin:

    .. cpp:function:: void PhaseShiftBegin(float warmUpTime, float duration)

    .. _CBaseCombatCharacter-GetWeaponAmmoLoaded:

    .. cpp:function:: int GetWeaponAmmoLoaded(entity weapon)

    .. _CBaseCombatCharacter-PhaseShiftCancel:

    .. cpp:function:: void PhaseShiftCancel()

    .. _CBaseCombatCharacter-GetHealthPerSegment:

    .. cpp:function:: unknown GetHealthPerSegment(unknown)

    .. _CBaseCombatCharacter-PhaseShiftTimeRemaining:

    .. cpp:function:: float PhaseShiftTimeRemaining()

    .. _CBaseCombatCharacter-IsPhaseShiftedOrPending:

    .. cpp:function:: unknown IsPhaseShiftedOrPending(unknown)

    .. _CBaseCombatCharacter-GetSettingsHeadshotFX:

    .. cpp:function:: void GetSettingsHeadshotFX()

    .. _CBaseCombatCharacter-GetTitanSoul:

    .. cpp:function:: entity GetTitanSoul()

    .. _CBaseCombatCharacter-SetTitanSoul:

    .. cpp:function:: void SetTitanSoul(entity soul)

    .. _CBaseCombatCharacter-SetHealthPerSegment:

    .. cpp:function:: unknown SetHealthPerSegment(unknown)

    .. _CBaseCombatCharacter-GetWeaponAmmoMaxLoaded:

    .. cpp:function:: int GetWeaponAmmoMaxLoaded(entity weapon)

    .. _CBaseCombatCharacter-GetMeleeWeapon:

    .. cpp:function:: entity GetMeleeWeapon()

    .. _CBaseCombatCharacter-GiveExistingWeapon:

    .. cpp:function:: unknown GiveExistingWeapon(unknown)

    .. _CBaseCombatCharacter-GetAttackSpreadAngle:

    .. cpp:function:: float GetAttackSpreadAngle()

    .. _CBaseCombatCharacter-SetInventoryChangedCallbackEnabled:

    .. cpp:function:: unknown SetInventoryChangedCallbackEnabled(unknown)

    .. _CBaseCombatCharacter-GetPlayerOrNPCViewRight:

    .. cpp:function:: vector GetPlayerOrNPCViewRight()

    .. _CBaseCombatCharacter-ContextAction-ClearInVehicle:

    .. cpp:function:: unknown ContextAction_ClearInVehicle(unknown)

    .. _CBaseCombatCharacter-GetPlayerOrNPCViewForward:

    .. cpp:function:: unknown GetPlayerOrNPCViewForward(unknown)

    .. _CBaseCombatCharacter-IsWeaponDisabled:

    .. cpp:function:: bool IsWeaponDisabled()

    .. _CBaseCombatCharacter-TakeWeapon:

    .. cpp:function:: void TakeWeapon(string weapon)

    .. _CBaseCombatCharacter-ClearOffhand:

    .. cpp:function:: unknown ClearOffhand(unknown)

    .. _CBaseCombatCharacter-GetOffhandWeapon:

    .. cpp:function:: entity GetOffhandWeapon(int slot)

    .. _CBaseCombatCharacter-TakeOffhandWeapon-NoDelete:

    .. cpp:function:: unknown TakeOffhandWeapon_NoDelete(unknown)

    .. _CBaseCombatCharacter-TakeOffhandWeapon:

    .. cpp:function:: void TakeOffhandWeapon(int slot)

    .. _CBaseCombatCharacter-ResetHealthChangeRate:

    .. cpp:function:: void ResetHealthChangeRate()

    .. _CBaseCombatCharacter-SetActiveWeaponPrimaryAmmoLoaded:

    .. cpp:function:: unknown SetActiveWeaponPrimaryAmmoLoaded(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsActive:

    .. cpp:function:: bool ContextAction_IsActive()

    .. _CBaseCombatCharacter-GetOutOfBoundsDeadTime:

    .. cpp:function:: int GetOutOfBoundsDeadTime()

    .. _CBaseCombatCharacter-OffsetFromViewAngles:

    .. cpp:function:: unknown OffsetFromViewAngles(unknown)

    .. _CBaseCombatCharacter-OffsetPositionFromView:

    .. cpp:function:: vector OffsetPositionFromView(vector startPos, vector offset)

    .. _CBaseCombatCharacter-IsUsingOffhandWeapon:

    .. cpp:function:: unknown IsUsingOffhandWeapon(unknown)

    .. _CBaseCombatCharacter-TakeWeaponNow:

    .. cpp:function:: void TakeWeaponNow(string weapon)

    .. _CBaseCombatCharacter-ContextAction-IsFastball:

    .. cpp:function:: unknown ContextAction_IsFastball(unknown)

    .. _CBaseCombatCharacter-GetSidearmWeapon:

    .. cpp:function:: unknown GetSidearmWeapon(unknown)

    .. _CBaseCombatCharacter-ContextAction-IsLeeching:

    .. cpp:function:: bool ContextAction_IsLeeching()

    .. _CBaseCombatCharacter-GetSharedEnergyRegenDelay:

    .. cpp:function:: unknown GetSharedEnergyRegenDelay(unknown)

    .. _CBaseCombatCharacter-SetActiveWeaponByName:

    .. cpp:function:: void SetActiveWeaponByName(string weapon)

    .. _CBaseCombatCharacter-PlayerMelee-ExecutionEndAttacker:

    .. cpp:function:: unknown PlayerMelee_ExecutionEndAttacker(unknown)

    .. _CBaseCombatCharacter-SetTargetInfoIcon:

    .. cpp:function:: unknown SetTargetInfoIcon(unknown)

    .. _CBaseCombatCharacter-GetSharedEnergyRegenRate:

    .. cpp:function:: unknown GetSharedEnergyRegenRate(unknown)

    .. _CBaseCombatCharacter-ReplaceActiveWeapon:

    .. cpp:function:: unknown ReplaceActiveWeapon(unknown)

    .. _CBaseCombatCharacter-EnablePhaseShiftFlags:

    .. cpp:function:: void EnablePhaseShiftFlags()

    .. _CBaseCombatCharacter-SetNumRodeoSlots:

    .. cpp:function:: void SetNumRodeoSlots(int)

    .. _CBaseCombatCharacter-GetActiveWeaponPrimaryAmmoLoaded:

    .. cpp:function:: int GetActiveWeaponPrimaryAmmoLoaded()

    .. _CBaseCombatCharacter-SetCloakReactEndTime:

    .. cpp:function:: unknown SetCloakReactEndTime(unknown)

    .. _CBaseCombatCharacter-RefillAllAmmo:

    .. cpp:function:: unknown RefillAllAmmo(unknown)

    .. _CBaseCombatCharacter-SetOutOfBoundsDeadTime:

    .. cpp:function:: unknown SetOutOfBoundsDeadTime(unknown)

    .. _CBaseCombatCharacter-SetSharedEnergyTotal:

    .. cpp:function:: unknown SetSharedEnergyTotal(unknown)

    .. _CBaseCombatCharacter-GetFirstRodeoRider:

    .. cpp:function:: enitity GetFirstRodeoRider()

    .. _CBaseCombatCharacter-ClearNPCPriorityOverride:

    .. cpp:function:: unknown ClearNPCPriorityOverride(unknown)

    .. _CBaseCombatCharacter-Event-LeechEnd:

    .. cpp:function:: unknown Event_LeechEnd(unknown)

    .. _CBaseCombatCharacter-GetAntiTitanWeapon:

    .. cpp:function:: entity GetAntiTitanWeapon()

    .. _CBaseCombatCharacter-TransferTethersToEntity:

    .. cpp:function:: unknown TransferTethersToEntity(unknown)

    .. _CBaseCombatCharacter-PrintInventory:

    .. cpp:function:: unknown PrintInventory(unknown)

    .. _CBaseCombatCharacter-GetNumRodeoSlots:

    .. cpp:function:: int GetNumRodeoSlots()

    .. _CBaseCombatCharacter-TakeWeapon-NoDelete:

    .. cpp:function:: unknown TakeWeapon_NoDelete(unknown)

    .. _CBaseCombatCharacter-ContextAction-ClearBusy:

    .. cpp:function:: void ContextAction_ClearBusy()

    .. _CBaseCombatCharacter-GiveOffhandWeapon:

    .. cpp:function:: void GiveOffhandWeapon(string ordnanceName, int slot, array<string> mods)

    .. _CBaseCombatCharacter-SetNPCPriorityOverride-NoThreat:

    .. cpp:function:: void SetNPCPriorityOverride_NoThreat()

    .. _CBaseCombatCharacter-ContextAction-IsBusy:

    .. cpp:function:: bool ContextAction_IsBusy()

    .. _CBaseCombatCharacter-GiveExistingOffhandWeapon:

    .. cpp:function:: unknown GiveExistingOffhandWeapon(unknown)

    .. _CBaseCombatCharacter-GetActiveWeapon:

    .. cpp:function:: enitity GetActiveWeapon()

