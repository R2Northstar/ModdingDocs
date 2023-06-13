.. _CAI-BaseNPC:

CAI_BaseNPC
===========

.. cpp:class:: CAI_BaseNPC extends CBaseCombatCharacter

    Inherits all properties from :ref:`CBaseCombatCharacter <CBaseCombatCharacter>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`CNPC_SentryTurret <CNPC-SentryTurret>`
    - :ref:`CNPC_Titan <CNPC-Titan>`
    - :ref:`CNPC_Drone <CNPC-Drone>`
    - :ref:`CAI_BaseActor <CAI-BaseActor>`
    - :ref:`CAI_TrackPather <CAI-TrackPather>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CAI_BaseNPC-TakeActiveWeapon:

    .. cpp:function:: unknown TakeActiveWeapon(unknown)

    .. _CAI_BaseNPC-GetClosestEnemyNPC:

    .. cpp:function:: unknown GetClosestEnemyNPC(unknown)

    .. _CAI_BaseNPC-AISetting-MeleeChargeSet:

    .. cpp:function:: unknown AISetting_MeleeChargeSet(unknown)

    .. _CAI_BaseNPC-GetNPCViewUp:

    .. cpp:function:: unknown GetNPCViewUp(unknown)

    .. _CAI_BaseNPC-AssaultPoint:

    .. cpp:function:: void AssaultPoint(vector point)

    .. _CAI_BaseNPC-DisableArrivalOnce:

    .. cpp:function:: unknown DisableArrivalOnce(unknown)

    .. _CAI_BaseNPC-SetAutoSquad:

    .. cpp:function:: unknown SetAutoSquad(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedPlayWithRefPoint:

    .. cpp:function:: unknown Anim_ScriptedPlayWithRefPoint(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedAddGestureActivity:

    .. cpp:function:: unknown Anim_ScriptedAddGestureActivity(unknown)

    .. _CAI_BaseNPC-IsInsideIndoorArea:

    .. cpp:function:: unknown IsInsideIndoorArea(unknown)

    .. _CAI_BaseNPC-RemoveFromFireteam:

    .. cpp:function:: unknown RemoveFromFireteam(unknown)

    .. _CAI_BaseNPC-DisableBehavior:

    .. cpp:function:: void DisableBehavior(string behaviour)

    .. _CAI_BaseNPC-AssaultClearArrivalTolerance:

    .. cpp:function:: unknown AssaultClearArrivalTolerance(unknown)

    .. _CAI_BaseNPC-AISetting-OnLeechFunc:

    .. cpp:function:: unknown AISetting_OnLeechFunc(unknown)

    .. _CAI_BaseNPC-SetHologram:

    .. cpp:function:: unknown SetHologram(unknown)

    .. _CAI_BaseNPC-SetMoveAnim:

    .. cpp:function:: unknown SetMoveAnim(unknown)

    .. _CAI_BaseNPC-AssaultPointClampedExtents:

    .. cpp:function:: unknown AssaultPointClampedExtents(unknown)

    .. _CAI_BaseNPC-ClearAllEnemyMemory:

    .. cpp:function:: unknown ClearAllEnemyMemory(unknown)

    .. _CAI_BaseNPC-EnableNPCFlag:

    .. cpp:function:: void EnableNPCFlag(int flag)

    .. _CAI_BaseNPC-SetEngagementDistVsStrong:

    .. cpp:function:: unknown SetEngagementDistVsStrong(unknown)

    .. _CAI_BaseNPC-TestAnimPath:

    .. cpp:function:: unknown TestAnimPath(unknown)

    .. _CAI_BaseNPC-GetSettingModelName:

    .. cpp:function:: unknown GetSettingModelName(unknown)

    .. _CAI_BaseNPC-GetLookDist:

    .. cpp:function:: unknown GetLookDist(unknown)

    .. _CAI_BaseNPC-GetAIClass:

    .. cpp:function:: int GetAIClass()

    .. _CAI_BaseNPC-GetSurprisedReactionReason:

    .. cpp:function:: unknown GetSurprisedReactionReason(unknown)

    .. _CAI_BaseNPC-ForceCombat:

    .. cpp:function:: void ForceCombat()

    .. _CAI_BaseNPC-HasAISettings:

    .. cpp:function:: unknown HasAISettings(unknown)

    .. _CAI_BaseNPC-GetEnemyLKP:

    .. cpp:function:: unknown GetEnemyLKP(unknown)

    .. _CAI_BaseNPC-SetSubclass:

    .. cpp:function:: unknown SetSubclass(unknown)

    .. _CAI_BaseNPC-GetNPCFlag:

    .. cpp:function:: unknown GetNPCFlag(unknown)

    .. _CAI_BaseNPC-GetSubclass:

    .. cpp:function:: unknown GetSubclass(unknown)

    .. _CAI_BaseNPC-SetAllowMelee:

    .. cpp:function:: unknown SetAllowMelee(unknown)

    .. _CAI_BaseNPC-SetPotentialThreatPos:

    .. cpp:function:: unknown SetPotentialThreatPos(unknown)

    .. _CAI_BaseNPC-SetNPCFlag:

    .. cpp:function:: unknown SetNPCFlag(unknown)

    .. _CAI_BaseNPC-ClearPotentialThreatPos:

    .. cpp:function:: unknown ClearPotentialThreatPos(unknown)

    .. _CAI_BaseNPC-CanBeMeleeExecuted:

    .. cpp:function:: unknown CanBeMeleeExecuted(unknown)

    .. _CAI_BaseNPC-SetBehaviorSelector:

    .. cpp:function:: unknown SetBehaviorSelector(unknown)

    .. _CAI_BaseNPC-SetFollowGoalTolerance:

    .. cpp:function:: unknown SetFollowGoalTolerance(unknown)

    .. _CAI_BaseNPC-AssaultSetAngles:

    .. cpp:function:: unknown AssaultSetAngles(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedPlayActivityByName:

    .. cpp:function:: void Anim_ScriptedPlayActivityByName(string activity, bool unknown_purpose1, float unknown_purpose2)

    .. _CAI_BaseNPC-SetCanBeMeleeExecuted:

    .. cpp:function:: unknown SetCanBeMeleeExecuted(unknown)

    .. _CAI_BaseNPC-ForceCheckGroundEntity:

    .. cpp:function:: void ForceCheckGroundEntity()

    .. _CAI_BaseNPC-AssaultSetGoalHeight:

    .. cpp:function:: unknown AssaultSetGoalHeight(unknown)

    .. _CAI_BaseNPC-Dev-GetAISettingAssetByKeyField:

    .. cpp:function:: unknown Dev_GetAISettingAssetByKeyField(unknown)

    .. _CAI_BaseNPC-GetHearingSensitivity:

    .. cpp:function:: unknown GetHearingSensitivity(unknown)

    .. _CAI_BaseNPC-GetClosestEnemyPlayer:

    .. cpp:function:: unknown GetClosestEnemyPlayer(unknown)

    .. _CAI_BaseNPC-GetCapabilityFlag:

    .. cpp:function:: unknown GetCapabilityFlag(unknown)

    .. _CAI_BaseNPC-GetAIClassName:

    .. cpp:function:: unknown GetAIClassName(unknown)

    .. _CAI_BaseNPC-IsInterruptable:

    .. cpp:function:: bool IsInterruptable()

    .. _CAI_BaseNPC-EnableBehavior:

    .. cpp:function:: void EnableBehavior(string behaviour)

    .. _CAI_BaseNPC-GetDangerousAreaWeapon:

    .. cpp:function:: unknown GetDangerousAreaWeapon(unknown)

    .. _CAI_BaseNPC-SetCanBeGroundExecuted:

    .. cpp:function:: unknown SetCanBeGroundExecuted(unknown)

    .. _CAI_BaseNPC-InitFollowBehavior:

    .. cpp:function:: void InitFollowBehavior(entity followMe, string followBehaviour)

    .. _CAI_BaseNPC-ClearHologram:

    .. cpp:function:: unknown ClearHologram(unknown)

    .. _CAI_BaseNPC-SetAllowSpecialJump:

    .. cpp:function:: unknown SetAllowSpecialJump(unknown)

    .. _CAI_BaseNPC-SetGoalEnt:

    .. cpp:function:: unknown SetGoalEnt(unknown)

    .. _CAI_BaseNPC-ClearEnemyMemory:

    .. cpp:function:: unknown ClearEnemyMemory(unknown)

    .. _CAI_BaseNPC-DisableLookDistOverride:

    .. cpp:function:: unknown DisableLookDistOverride(unknown)

    .. _CAI_BaseNPC-SetFollowTargetMoveTolerance:

    .. cpp:function:: unknown SetFollowTargetMoveTolerance(unknown)

    .. _CAI_BaseNPC-CanSee:

    .. cpp:function:: bool CanSee(entity ent)

    .. _CAI_BaseNPC-GetBodyType:

    .. cpp:function:: string GetBodyType()

    .. _CAI_BaseNPC-SetFollowGoalCombatTolerance:

    .. cpp:function:: unknown SetFollowGoalCombatTolerance(unknown)

    .. _CAI_BaseNPC-TimeSinceKnown:

    .. cpp:function:: unknown TimeSinceKnown(unknown)

    .. _CAI_BaseNPC-SetAttackAnim:

    .. cpp:function:: unknown SetAttackAnim(unknown)

    .. _CAI_BaseNPC-GetNearestVisibleFriendlyPlayer:

    .. cpp:function:: unknown GetNearestVisibleFriendlyPlayer(unknown)

    .. _CAI_BaseNPC-AssaultGetGoalRadius:

    .. cpp:function:: unknown AssaultGetGoalRadius(unknown)

    .. _CAI_BaseNPC-UseSequenceBounds:

    .. cpp:function:: unknown UseSequenceBounds(unknown)

    .. _CAI_BaseNPC-GetAISettingsName:

    .. cpp:function:: string GetAISettingsName()

    .. _CAI_BaseNPC-GetSafeHint:

    .. cpp:function:: unknown GetSafeHint(unknown)

    .. _CAI_BaseNPC-IsAtShootingCoverHint:

    .. cpp:function:: unknown IsAtShootingCoverHint(unknown)

    .. _CAI_BaseNPC-SetAlert:

    .. cpp:function:: unknown SetAlert(unknown)

    .. _CAI_BaseNPC-Dev-GetAISettingByKeyField:

    .. cpp:function:: var Dev_GetAISettingByKeyField(string key)

    .. _CAI_BaseNPC-DisableNPCFlag:

    .. cpp:function:: void DisableNPCFlag(int flag)

    .. _CAI_BaseNPC-SetDangerousAreaRadius:

    .. cpp:function:: unknown SetDangerousAreaRadius(unknown)

    .. _CAI_BaseNPC-SetValidHealthBarTarget:

    .. cpp:function:: unknown SetValidHealthBarTarget(unknown)

    .. _CAI_BaseNPC-AssaultSetFightRadius:

    .. cpp:function:: unknown AssaultSetFightRadius(unknown)

    .. _CAI_BaseNPC-IsNonCombatAI:

    .. cpp:function:: unknown IsNonCombatAI(unknown)

    .. _CAI_BaseNPC-InCombat:

    .. cpp:function:: bool InCombat()

    .. _CAI_BaseNPC-SetSecondaryEnemy:

    .. cpp:function:: void SetSecondaryEnemy(entity enemy)

    .. _CAI_BaseNPC-AISetting-SummonDrone:

    .. cpp:function:: unknown AISetting_SummonDrone(unknown)

    .. _CAI_BaseNPC-GetNPCVelocity:

    .. cpp:function:: unknown GetNPCVelocity(unknown)

    .. _CAI_BaseNPC-SetCapabilityFlag:

    .. cpp:function:: void SetCapabilityFlag(int flag, bool active)

    .. _CAI_BaseNPC-SquadLastKnownPosition:

    .. cpp:function:: unknown SquadLastKnownPosition(unknown)

    .. _CAI_BaseNPC-LastSeenPosition:

    .. cpp:function:: unknown LastSeenPosition(unknown)

    .. _CAI_BaseNPC-LastKnownPosition:

    .. cpp:function:: unknown LastKnownPosition(unknown)

    .. _CAI_BaseNPC-GetMaxTurretYaw:

    .. cpp:function:: float GetMaxTurretYaw()

    .. _CAI_BaseNPC-GetMinGoalRadius:

    .. cpp:function:: unknown GetMinGoalRadius(unknown)

    .. _CAI_BaseNPC-GetMaxEnemyDistHeavyArmor:

    .. cpp:function:: float GetMaxEnemyDistHeavyArmor()

    .. _CAI_BaseNPC-GetMaxEnemyDist:

    .. cpp:function:: float GetMaxEnemyDist()

    .. _CAI_BaseNPC-GetNPCViewRight:

    .. cpp:function:: unknown GetNPCViewRight(unknown)

    .. _CAI_BaseNPC-CanBeGroundExecuted:

    .. cpp:function:: unknown CanBeGroundExecuted(unknown)

    .. _CAI_BaseNPC-GetNPCViewForward:

    .. cpp:function:: unknown GetNPCViewForward(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedRemoveAllGestures:

    .. cpp:function:: unknown Anim_ScriptedRemoveAllGestures(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedRemoveGestureActivity:

    .. cpp:function:: unknown Anim_ScriptedRemoveGestureActivity(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedAddGestureSequence:

    .. cpp:function:: unknown Anim_ScriptedAddGestureSequence(unknown)

    .. _CAI_BaseNPC-AISetting-LeechAnimSet:

    .. cpp:function:: string AISetting_LeechAnimSet()

    .. _CAI_BaseNPC-Anim-ScriptedJump:

    .. cpp:function:: unknown Anim_ScriptedJump(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedPlay:

    .. cpp:function:: void Anim_ScriptedPlay(string anim)

    .. _CAI_BaseNPC-GetMeleeDamageMaxForTarget:

    .. cpp:function:: int GetMeleeDamageMaxForTarget(entity target)

    .. _CAI_BaseNPC-AISetting-ShootableByFriendlyPlayer:

    .. cpp:function:: unknown AISetting_ShootableByFriendlyPlayer(unknown)

    .. _CAI_BaseNPC-SetAISettings:

    .. cpp:function:: void SetAISettings(string settings)

    .. _CAI_BaseNPC-AISetting-LeechAnimTag:

    .. cpp:function:: unknown AISetting_LeechAnimTag(unknown)

    .. _CAI_BaseNPC-AISetting-GetGrenadeWeapon:

    .. cpp:function:: unknown AISetting_GetGrenadeWeapon(unknown)

    .. _CAI_BaseNPC-AISetting-GetDefaultWeapon:

    .. cpp:function:: unknown AISetting_GetDefaultWeapon(unknown)

    .. _CAI_BaseNPC-AISetting-MaxFlyingSpeed:

    .. cpp:function:: float AISetting_MaxFlyingSpeed()

    .. _CAI_BaseNPC-AISetting-BaseHealth:

    .. cpp:function:: unknown AISetting_BaseHealth(unknown)

    .. _CAI_BaseNPC-IsSecondaryAttack:

    .. cpp:function:: bool IsSecondaryAttack()

    .. _CAI_BaseNPC-IsValidHealthBarTarget:

    .. cpp:function:: unknown IsValidHealthBarTarget(unknown)

    .. _CAI_BaseNPC-GetNPCMoveFlag:

    .. cpp:function:: unknown GetNPCMoveFlag(unknown)

    .. _CAI_BaseNPC-SetNPCMoveFlag:

    .. cpp:function:: unknown SetNPCMoveFlag(unknown)

    .. _CAI_BaseNPC-GetNPCState:

    .. cpp:function:: string GetNPCState()

    .. _CAI_BaseNPC-EnableNPCMoveFlag:

    .. cpp:function:: void EnableNPCMoveFlag(int flag)

    .. _CAI_BaseNPC-DisableNPCMoveFlag:

    .. cpp:function:: void DisableNPCMoveFlag(int flag)

    .. _CAI_BaseNPC-IsFrozen:

    .. cpp:function:: unknown IsFrozen(unknown)

    .. _CAI_BaseNPC-Unfreeze:

    .. cpp:function:: void Unfreeze()

    .. _CAI_BaseNPC-Freeze:

    .. cpp:function:: void Freeze()

    .. _CAI_BaseNPC-SetAimAssistForcePullPitchEnabled:

    .. cpp:function:: unknown SetAimAssistForcePullPitchEnabled(unknown)

    .. _CAI_BaseNPC-ClearDeathActivity:

    .. cpp:function:: unknown ClearDeathActivity(unknown)

    .. _CAI_BaseNPC-SetLookDistOverride:

    .. cpp:function:: unknown SetLookDistOverride(unknown)

    .. _CAI_BaseNPC-DoRodeoAttack:

    .. cpp:function:: unknown DoRodeoAttack(unknown)

    .. _CAI_BaseNPC-SetThinkEveryFrame:

    .. cpp:function:: void SetThinkEveryFrame(bool think)

    .. _CAI_BaseNPC-SetDefaultSchedule:

    .. cpp:function:: unknown SetDefaultSchedule(unknown)

    .. _CAI_BaseNPC-GetCurScheduleName:

    .. cpp:function:: unknown GetCurScheduleName(unknown)

    .. _CAI_BaseNPC-GetPrevScheduleName:

    .. cpp:function:: unknown GetPrevScheduleName(unknown)

    .. _CAI_BaseNPC-SetEnemyChangeCallback:

    .. cpp:function:: unknown SetEnemyChangeCallback(unknown)

    .. _CAI_BaseNPC-AssaultSetArrivalTolerance:

    .. cpp:function:: unknown AssaultSetArrivalTolerance(unknown)

    .. _CAI_BaseNPC-ClearEnemy:

    .. cpp:function:: void ClearEnemy(entity enemy)

    .. _CAI_BaseNPC-LockEnemy:

    .. cpp:function:: unknown LockEnemy(unknown)

    .. _CAI_BaseNPC-SetEnemy:

    .. cpp:function:: void SetEnemy(entity enemy)

    .. _CAI_BaseNPC-SetEnemyLKP:

    .. cpp:function:: unknown SetEnemyLKP(unknown)

    .. _CAI_BaseNPC-SetHullType:

    .. cpp:function:: unknown SetHullType(unknown)

    .. _CAI_BaseNPC-Anim-AdvanceCycleEveryFrame:

    .. cpp:function:: unknown Anim_AdvanceCycleEveryFrame(unknown)

    .. _CAI_BaseNPC-SetDeathActivity:

    .. cpp:function:: unknown SetDeathActivity(unknown)

    .. _CAI_BaseNPC-ClearAttackAnim:

    .. cpp:function:: unknown ClearAttackAnim(unknown)

    .. _CAI_BaseNPC-ClearIdleAnim:

    .. cpp:function:: unknown ClearIdleAnim(unknown)

    .. _CAI_BaseNPC-SetIdleAnim:

    .. cpp:function:: unknown SetIdleAnim(unknown)

    .. _CAI_BaseNPC-GetPrevNPCState:

    .. cpp:function:: unknown GetPrevNPCState(unknown)

    .. _CAI_BaseNPC-GetAllowMelee:

    .. cpp:function:: unknown GetAllowMelee(unknown)

    .. _CAI_BaseNPC-AssaultSetFinalDestination:

    .. cpp:function:: unknown AssaultSetFinalDestination(unknown)

    .. _CAI_BaseNPC-SetHearingSensitivity:

    .. cpp:function:: unknown SetHearingSensitivity(unknown)

    .. _CAI_BaseNPC-SetEngagementDistVsWeak:

    .. cpp:function:: unknown SetEngagementDistVsWeak(unknown)

    .. _CAI_BaseNPC-GetLookDistOverride:

    .. cpp:function:: unknown GetLookDistOverride(unknown)

    .. _CAI_BaseNPC-SetRodeoAllowed:

    .. cpp:function:: unknown SetRodeoAllowed(unknown)

    .. _CAI_BaseNPC-GetSquadEnemy:

    .. cpp:function:: unknown GetSquadEnemy(unknown)

    .. _CAI_BaseNPC-TimeSinceSeen:

    .. cpp:function:: unknown TimeSinceSeen(unknown)

    .. _CAI_BaseNPC-GetGoalEnt:

    .. cpp:function:: unknown GetGoalEnt(unknown)

    .. _CAI_BaseNPC-GetTimeFirstAttackAfterReacquire:

    .. cpp:function:: unknown GetTimeFirstAttackAfterReacquire(unknown)

    .. _CAI_BaseNPC-GetEnemyLSP:

    .. cpp:function:: unknown GetEnemyLSP(unknown)

    .. _CAI_BaseNPC-GetEnemy:

    .. cpp:function:: entity GetEnemy()

    .. _CAI_BaseNPC-SetSquad:

    .. cpp:function:: unknown SetSquad(unknown)

    .. _CAI_BaseNPC-GetSquadCentroid:

    .. cpp:function:: unknown GetSquadCentroid(unknown)

    .. _CAI_BaseNPC-GetClosestEnemy:

    .. cpp:function:: unknown GetClosestEnemy(unknown)

    .. _CAI_BaseNPC-SetActivityModifier:

    .. cpp:function:: unknown SetActivityModifier(unknown)

    .. _CAI_BaseNPC-AssaultGetArrivalTolerance:

    .. cpp:function:: unknown AssaultGetArrivalTolerance(unknown)

    .. _CAI_BaseNPC-AISetting-LeechDataKnifeTag:

    .. cpp:function:: string AISetting_LeechDataKnifeTag()

    .. _CAI_BaseNPC-SetDangerousAreaReactionTime:

    .. cpp:function:: unknown SetDangerousAreaReactionTime(unknown)

    .. _CAI_BaseNPC-GetSettingTitle:

    .. cpp:function:: unknown GetSettingTitle(unknown)

    .. _CAI_BaseNPC-AssaultSetGoalRadius:

    .. cpp:function:: unknown AssaultSetGoalRadius(unknown)

    .. _CAI_BaseNPC-GetFollowTarget:

    .. cpp:function:: entity GetFollowTarget()

    .. _CAI_BaseNPC-SetEfficientMode:

    .. cpp:function:: unknown SetEfficientMode(unknown)

    .. _CAI_BaseNPC-TestAnimPathFrom:

    .. cpp:function:: unknown TestAnimPathFrom(unknown)

    .. _CAI_BaseNPC-AssaultPointToAnimSetCallback:

    .. cpp:function:: unknown AssaultPointToAnimSetCallback(unknown)

    .. _CAI_BaseNPC-RequestSpecialRangeAttack:

    .. cpp:function:: unknown RequestSpecialRangeAttack(unknown)

    .. _CAI_BaseNPC-AssaultPointClamped:

    .. cpp:function:: unknown AssaultPointClamped(unknown)

    .. _CAI_BaseNPC-HasXRaySupport:

    .. cpp:function:: bool HasXRaySupport()

    .. _CAI_BaseNPC-AddToFireteam:

    .. cpp:function:: unknown AddToFireteam(unknown)

    .. _CAI_BaseNPC-IsActivityModifierActive:

    .. cpp:function:: unknown IsActivityModifierActive(unknown)

    .. _CAI_BaseNPC-InitSquadAssaultInterupt:

    .. cpp:function:: unknown InitSquadAssaultInterupt(unknown)

    .. _CAI_BaseNPC-Anim-ScriptedPlayActivityByNameWithRefPoint:

    .. cpp:function:: unknown Anim_ScriptedPlayActivityByNameWithRefPoint(unknown)

    .. _CAI_BaseNPC-GetNPCViewVector:

    .. cpp:function:: unknown GetNPCViewVector(unknown)

    .. _CAI_BaseNPC-AssaultGetGoalHeight:

    .. cpp:function:: unknown AssaultGetGoalHeight(unknown)

    .. _CAI_BaseNPC-GetEnemyLastTimeSeen:

    .. cpp:function:: unknown GetEnemyLastTimeSeen(unknown)

    .. _CAI_BaseNPC-AssaultGetFightRadius:

    .. cpp:function:: unknown AssaultGetFightRadius(unknown)

    .. _CAI_BaseNPC-SetNPCMoveSpeedScale:

    .. cpp:function:: unknown SetNPCMoveSpeedScale(unknown)

    .. _CAI_BaseNPC-IsCrouching:

    .. cpp:function:: bool IsCrouching()

    .. _CAI_BaseNPC-AssaultPointToAnim:

    .. cpp:function:: unknown AssaultPointToAnim(unknown)

    .. _CAI_BaseNPC-ClearMoveAnim:

    .. cpp:function:: unknown ClearMoveAnim(unknown)

