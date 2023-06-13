.. _CBaseEntity:

CBaseEntity
===========

.. cpp:class:: CBaseEntity

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`CBaseAnimating <CBaseAnimating>`
    - :ref:`CVortexSphere <CVortexSphere>`
    - :ref:`CScriptTraceVolume <CScriptTraceVolume>`
    - :ref:`CTitanSoul <CTitanSoul>`
    - :ref:`CRopeKeyframe <CRopeKeyframe>`
    - :ref:`CBaseTrigger <CBaseTrigger>`
    - :ref:`CHardPointEntity <CHardPointEntity>`
    - :ref:`CParticleSystem <CParticleSystem>`
    - :ref:`CEnvExplosion <CEnvExplosion>`
    - :ref:`CSpawner <CSpawner>`
    - :ref:`CTeamSpawnPoint <CTeamSpawnPoint>`
    - :ref:`CAI_Hint <CAI-Hint>`
    - :ref:`CAI_SkitNode <CAI-SkitNode>`
    - :ref:`CBreakable <CBreakable>`
    - :ref:`CWindowHint <CWindowHint>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CBaseEntity-GetLocalOrigin:

    .. cpp:function:: unknown GetLocalOrigin(unknown)

    .. _CBaseEntity-GetNoTargetSmartAmmo:

    .. cpp:function:: unknown GetNoTargetSmartAmmo(unknown)

    .. _CBaseEntity-IsMarkedForDeletion:

    .. cpp:function:: bool IsMarkedForDeletion()

    .. _CBaseEntity-SetGrenadeTargetDebounce:

    .. cpp:function:: unknown SetGrenadeTargetDebounce(unknown)

    .. _CBaseEntity-DisableGrappleAttachment:

    .. cpp:function:: unknown DisableGrappleAttachment(unknown)

    .. _CBaseEntity-SetPreventCrits:

    .. cpp:function:: void SetPreventCrits(bool prevent)

    .. _CBaseEntity-IsTriggerBox:

    .. cpp:function:: unknown IsTriggerBox(unknown)

    .. _CBaseEntity-ClearBoneMerge:

    .. cpp:function:: unknown ClearBoneMerge(unknown)

    .. _CBaseEntity-GetInstanceName:

    .. cpp:function:: unknown GetInstanceName(unknown)

    .. _CBaseEntity-CreateTableFromModelKeyValues:

    .. cpp:function:: table CreateTableFromModelKeyValues()

    .. _CBaseEntity-ValidateScriptScope:

    .. cpp:function:: unknown ValidateScriptScope(unknown)

    .. _CBaseEntity-scope:

    .. cpp:function:: unknown scope(unknown)

    .. _CBaseEntity-HasKey:

    .. cpp:function:: bool HasKey(string key)

    .. _CBaseEntity-GetIndexForEntity:

    .. cpp:function:: unknown GetIndexForEntity(unknown)

    .. _CBaseEntity-Minimap-Hide:

    .. cpp:function:: unknown Minimap_Hide(unknown)

    .. _CBaseEntity-SetDamageNotifications:

    .. cpp:function:: void SetDamageNotifications(bool getNotifs)

    .. _CBaseEntity-Fire:

    .. cpp:function:: void Fire(string output, string param = "", float delay = 0, entity activator = null, entity caller = null)

    .. _CBaseEntity-SetLocalOrigin:

    .. cpp:function:: void SetLocalOrigin(vector origin)

    .. _CBaseEntity-SetForceVisibleInPhaseShift:

    .. cpp:function:: void SetForceVisibleInPhaseShift(bool visible)

    .. _CBaseEntity-SetAbsAngles:

    .. cpp:function:: void SetAbsAngles(vector angles)

    .. _CBaseEntity-GetOwner:

    .. cpp:function:: entity GetOwner()

    .. _CBaseEntity-SetTouchTriggers:

    .. cpp:function:: unknown SetTouchTriggers(unknown)

    .. _CBaseEntity-SetAngularVelocity:

    .. cpp:function:: void SetAngularVelocity(float x, float y, float z)

    .. _CBaseEntity-GetHealth:

    .. cpp:function:: int GetHealth()

    .. _CBaseEntity-MakeInvisible:

    .. cpp:function:: void MakeInvisible()

    .. _CBaseEntity-DisableNetworkedEntityLinks:

    .. cpp:function:: unknown DisableNetworkedEntityLinks(unknown)

    .. _CBaseEntity-EndSignal:

    .. cpp:function:: void EndSignal(string signal)

    .. _CBaseEntity-CanCloak:

    .. cpp:function:: unknown CanCloak(unknown)

    .. _CBaseEntity-GetNextKey:

    .. cpp:function:: unknown GetNextKey(unknown)

    .. _CBaseEntity-SetUsableByGroup:

    .. cpp:function:: void SetUsableByGroup(string group)

    .. _CBaseEntity-SetInactive:

    .. cpp:function:: unknown SetInactive(unknown)

    .. _CBaseEntity-GetValueForTextureKey:

    .. cpp:function:: unknown GetValueForTextureKey(unknown)

    .. _CBaseEntity-NotSolid:

    .. cpp:function:: bool NotSolid()

    .. _CBaseEntity-RotateTo:

    .. cpp:function:: void RotateTo(vector pos, float moveTime, float easeIn = 0, float easeOut = 0)

    .. _CBaseEntity-SetTitle:

    .. cpp:function:: void SetTitle(string title)

    .. _CBaseEntity-AreEntityLinksNetworked:

    .. cpp:function:: unknown AreEntityLinksNetworked(unknown)

    .. _CBaseEntity-SetForwardVector:

    .. cpp:function:: unknown SetForwardVector(unknown)

    .. _CBaseEntity-DisableAttackableByAI:

    .. cpp:function:: unknown DisableAttackableByAI(unknown)

    .. _CBaseEntity-DispatchImpactEffects:

    .. cpp:function:: void DispatchImpactEffects(entity ent, vector startPos, vector endPos, vector hitNormal, enitity prop, int propIndex, int damageType, int impactIndex, entity orig, int impactEffectFlags)

    .. _CBaseEntity-SetVelocity:

    .. cpp:function:: void SetVelocity(vector vel)

    .. _CBaseEntity-Highlight-GetCurrentInsideOpacity:

    .. cpp:function:: float Highlight_GetCurrentInsideOpacity()

    .. _CBaseEntity-EnableRenderAlways:

    .. cpp:function:: void EnableRenderAlways()

    .. _CBaseEntity-SetLocalForwardVector:

    .. cpp:function:: unknown SetLocalForwardVector(unknown)

    .. _CBaseEntity-SetHealth:

    .. cpp:function:: int SetHealth(int health)

    .. _CBaseEntity-DisableRenderAlways:

    .. cpp:function:: void DisableRenderAlways()

    .. _CBaseEntity-Highlight-ShowOutline:

    .. cpp:function:: void Highlight_ShowOutline(float duration)

    .. _CBaseEntity-FireNow:

    .. cpp:function:: void FireNow(string output, string param = "", float delay = 0, entity activator = null, entity caller = null)

    .. _CBaseEntity-TakeDamage:

    .. cpp:function:: void TakeDamage(int damageAmount, entity attacker_1, entity attacker_2, table { int scriptType, int damageType, int damageSourceId, vector origin, vector force })

    .. _CBaseEntity-AddOutput:

    .. cpp:function:: void AddOutput(string outputName, string | entity target, string inputName, string parameter = "", float delay = 0, float maxFires = 0)

    .. _CBaseEntity-SetAbsAnglesSmooth:

    .. cpp:function:: unknown SetAbsAnglesSmooth(unknown)

    .. _CBaseEntity-SetParentWithHitbox:

    .. cpp:function:: void SetParentWithHitbox(entity parent, int hitGroup, bool unknown)

    .. _CBaseEntity-Kill-Deprecated-UseDestroyInstead:

    .. cpp:function:: void Kill_Deprecated_UseDestroyInstead()

    .. _CBaseEntity-DontIncludeParentBbox:

    .. cpp:function:: unknown DontIncludeParentBbox(unknown)

    .. _CBaseEntity-constructor:

    .. cpp:function:: entity constructor(unknown)

    .. _CBaseEntity-GetPreTemplateName:

    .. cpp:function:: unknown GetPreTemplateName(unknown)

    .. _CBaseEntity-Highlight-ShowInside:

    .. cpp:function:: void Highlight_ShowInside(float duration)

    .. _CBaseEntity-GetUpVector:

    .. cpp:function:: vector GetUpVector()

    .. _CBaseEntity-GetPassThroughFlags:

    .. cpp:function:: unknown GetPassThroughFlags(unknown)

    .. _CBaseEntity-Hide:

    .. cpp:function:: void Hide()

    .. _CBaseEntity-RenderWithViewModels:

    .. cpp:function:: void RenderWithViewModels(bool renderWith)

    .. _CBaseEntity-GetBoundingMins:

    .. cpp:function:: vector GetBoundingMins()

    .. _CBaseEntity-Solid:

    .. cpp:function:: void Solid()

    .. _CBaseEntity-IsDraw:

    .. cpp:function:: unknown IsDraw(unknown)

    .. _CBaseEntity-SetUsePrompts:

    .. cpp:function:: void SetUsePrompts(string pc_prompt, string console_prompt)

    .. _CBaseEntity-SetLocalAngles:

    .. cpp:function:: void SetLocalAngles(vector angles)

    .. _CBaseEntity-GetCritsPrevented:

    .. cpp:function:: bool GetCritsPrevented()

    .. _CBaseEntity-HasGibModel:

    .. cpp:function:: bool HasGibModel()

    .. _CBaseEntity-Highlight-SetVisibleByPlayer:

    .. cpp:function:: unknown Highlight_SetVisibleByPlayer(unknown)

    .. _CBaseEntity-Highlight-GetOutlineRadius:

    .. cpp:function:: float Highlight_GetOutlineRadius()

    .. _CBaseEntity-TransferChildrenTo:

    .. cpp:function:: unknown TransferChildrenTo(unknown)

    .. _CBaseEntity-GetLocalAngles:

    .. cpp:function:: vector GetLocalAngles()

    .. _CBaseEntity-IsLinkedToEnt:

    .. cpp:function:: unknown IsLinkedToEnt(unknown)

    .. _CBaseEntity-GetValueForEffectNameKey:

    .. cpp:function:: unknown GetValueForEffectNameKey(unknown)

    .. _CBaseEntity-Highlight-SetCurrentContext:

    .. cpp:function:: void Highlight_SetCurrentContext(int contextID)

    .. _CBaseEntity-SnapToAbsOrigin:

    .. cpp:function:: unknown SnapToAbsOrigin(unknown)

    .. _CBaseEntity-GetScriptName:

    .. cpp:function:: string GetScriptName()

    .. _CBaseEntity-GetModelName:

    .. cpp:function:: asset GetModelName()

    .. _CBaseEntity-Destroy:

    .. cpp:function:: void Destroy()

    .. _CBaseEntity-Highlight-SetInheritHighlight:

    .. cpp:function:: void Highlight_SetInheritHighlight(bool set)

    .. _CBaseEntity-Highlight-SetParam:

    .. cpp:function:: void Highlight_SetParam(int contextID, int parameterID, vector highlightColor)

    .. _CBaseEntity-IsWorld:

    .. cpp:function:: bool IsWorld()

    .. _CBaseEntity-HighlightDisableForTeam:

    .. cpp:function:: void HighlightDisableForTeam(int team)

    .. _CBaseEntity-Minimap-AlwaysShow:

    .. cpp:function:: void Minimap_AlwaysShow(int team, entity ent)

    .. _CBaseEntity-GetOrigin:

    .. cpp:function:: vector GetOrigin()

    .. _CBaseEntity-SetPhysics:

    .. cpp:function:: unknown SetPhysics(unknown)

    .. _CBaseEntity-SetDoDestroyCallback:

    .. cpp:function:: void SetDoDestroyCallback(bool doCallBack)

    .. _CBaseEntity-EnableDebugBrokenInterpolation:

    .. cpp:function:: unknown EnableDebugBrokenInterpolation(unknown)

    .. _CBaseEntity-EnableNetworkedEntityLinks:

    .. cpp:function:: unknown EnableNetworkedEntityLinks(unknown)

    .. _CBaseEntity-DisableDraw:

    .. cpp:function:: void DisableDraw()

    .. _CBaseEntity-GetTimeSinceSpawning:

    .. cpp:function:: unknown GetTimeSinceSpawning(unknown)

    .. _CBaseEntity-IsSolid:

    .. cpp:function:: unknown IsSolid(unknown)

    .. _CBaseEntity-DisableHibernation:

    .. cpp:function:: void DisableHibernation()

    .. _CBaseEntity-SetToSameParentAs:

    .. cpp:function:: unknown SetToSameParentAs(unknown)

    .. _CBaseEntity-EnableHibernation:

    .. cpp:function:: unknown EnableHibernation(unknown)

    .. _CBaseEntity-GetShieldHealthMax:

    .. cpp:function:: int GetShieldHealthMax()

    .. _CBaseEntity-RoundOriginAndAnglesToNearestNetworkValue:

    .. cpp:function:: void RoundOriginAndAnglesToNearestNetworkValue()

    .. _CBaseEntity-ClearBossPlayer:

    .. cpp:function:: void ClearBossPlayer()

    .. _CBaseEntity-Minimap-SetHeightTracking:

    .. cpp:function:: unknown Minimap_SetHeightTracking(unknown)

    .. _CBaseEntity-GetForwardVector:

    .. cpp:function:: vector GetForwardVector()

    .. _CBaseEntity-GetLinkParentArray:

    .. cpp:function:: unknown GetLinkParentArray(unknown)

    .. _CBaseEntity-NextMovePeer:

    .. cpp:function:: entity NextMovePeer()

    .. _CBaseEntity-SetOrigin:

    .. cpp:function:: void SetOrigin(vector position)

    .. _CBaseEntity-RemoveUsableValue:

    .. cpp:function:: unknown RemoveUsableValue(unknown)

    .. _CBaseEntity-GetScriptId:

    .. cpp:function:: unknown GetScriptId(unknown)

    .. _CBaseEntity-GetLifeState:

    .. cpp:function:: int GetLifeState()

    .. _CBaseEntity-TraceAttackToTriggers:

    .. cpp:function:: void TraceAttackToTriggers(int damageAmount, entity attacker_1, entity attacker_2, table { int scriptType, int damageType, int damageSourceId, vector force }, vector startPos, vector endPos, vector direction)

    .. _CBaseEntity-MinimizeHibernation:

    .. cpp:function:: unknown MinimizeHibernation(unknown)

    .. _CBaseEntity-SetAIObstacle:

    .. cpp:function:: unknown SetAIObstacle(unknown)

    .. _CBaseEntity-SetValueForTextureKey:

    .. cpp:function:: void SetValueForTextureKey(asset texture)

    .. _CBaseEntity-SetBlocksRadiusDamage:

    .. cpp:function:: void SetBlocksRadiusDamage(bool blocks)

    .. _CBaseEntity-GetDamage:

    .. cpp:function:: unknown GetDamage(unknown)

    .. _CBaseEntity-Highlight-GetCurrentOutlineOpacity:

    .. cpp:function:: float Highlight_GetCurrentOutlineOpacity()

    .. _CBaseEntity-IsProjectile:

    .. cpp:function:: bool IsProjectile()

    .. _CBaseEntity-Minimap-DisplayDefault:

    .. cpp:function:: void Minimap_DisplayDefault(int team, entity ent)

    .. _CBaseEntity-HighlightEnableForTeam:

    .. cpp:function:: void HighlightEnableForTeam(int team)

    .. _CBaseEntity-SetBossPlayer:

    .. cpp:function:: void SetBossPlayer(entity boss)

    .. _CBaseEntity-IsZipline:

    .. cpp:function:: unknown IsZipline(unknown)

    .. _CBaseEntity-SetSize:

    .. cpp:function:: void SetSize(float width, float height)

    .. _CBaseEntity-SetValueForKey:

    .. cpp:function:: void SetValueForKey(var key, var val)

    .. _CBaseEntity-GetEncodedEHandle:

    .. cpp:function:: int GetEncodedEHandle()

    .. _CBaseEntity-SetBoneMerge:

    .. cpp:function:: unknown SetBoneMerge(unknown)

    .. _CBaseEntity-Show:

    .. cpp:function:: void Show()

    .. _CBaseEntity-GetLinkParent:

    .. cpp:function:: entity GetLinkParent()

    .. _CBaseEntity-IsValidInternal:

    .. cpp:function:: bool IsValidInternal()

    .. _CBaseEntity-Highlight-GetOutlineFunction:

    .. cpp:function:: int Highlight_GetOutlineFunction(int contextID)

    .. _CBaseEntity-Minimap-SetClampToEdge:

    .. cpp:function:: void Minimap_SetClampToEdge(bool clamp)

    .. _CBaseEntity-WaitSignal:

    .. cpp:function:: void WaitSignal(string signal)

    .. _CBaseEntity-PhysicsDummyEnableMotion:

    .. cpp:function:: unknown PhysicsDummyEnableMotion(unknown)

    .. _CBaseEntity-IsPlayerDecoy:

    .. cpp:function:: void IsPlayerDecoy()

    .. _CBaseEntity-HasOutput:

    .. cpp:function:: unknown HasOutput(unknown)

    .. _CBaseEntity-UnlinkFromEnt:

    .. cpp:function:: unknown UnlinkFromEnt(unknown)

    .. _CBaseEntity-LinkToEnt:

    .. cpp:function:: void LinkToEnt(entity ent)

    .. _CBaseEntity-SetKillNPCOnPush:

    .. cpp:function:: unknown SetKillNPCOnPush(unknown)

    .. _CBaseEntity-Get:

    .. cpp:function:: var Get(string key)

    .. _CBaseEntity-SetLocalForwardVectorWithUp:

    .. cpp:function:: unknown SetLocalForwardVectorWithUp(unknown)

    .. _CBaseEntity-IsHologram:

    .. cpp:function:: bool IsHologram()

    .. _CBaseEntity-Highlight-SetFunctions:

    .. cpp:function:: void Highlight_SetFunctions(int contextID, int hightlightFillID, bool entityVisible, int colorMode, float radius, int highlightID, bool afterPostProcess)

    .. _CBaseEntity-Die:

    .. cpp:function:: void Die()

    .. _CBaseEntity-Minimap-SetObjectScale:

    .. cpp:function:: void Minimap_SetObjectScale(float scale)

    .. _CBaseEntity-AddVar:

    .. cpp:function:: unknown AddVar(unknown)

    .. _CBaseEntity-IsCloaked:

    .. cpp:function:: bool IsCloaked()

    .. _CBaseEntity-SetValueForModelKey:

    .. cpp:function:: void SetValueForModelKey(asset model)

    .. _CBaseEntity-UseHitBoxForTraceCheck:

    .. cpp:function:: unknown UseHitBoxForTraceCheck(unknown)

    .. _CBaseEntity-SetForwardVectorWithUp:

    .. cpp:function:: unknown SetForwardVectorWithUp(unknown)

    .. _CBaseEntity-ShipHack-PositionBetweenEyes:

    .. cpp:function:: unknown ShipHack_PositionBetweenEyes(unknown)

    .. _CBaseEntity-MoveTo:

    .. cpp:function:: void MoveTo(vector pos, float moveTime, float easeIn = 0, float easeOut = 0)

    .. _CBaseEntity-DisconnectOutput:

    .. cpp:function:: void DisconnectOutput(string event, void functionref( entity trigger, entity activator, entity caller, var value)

    .. _CBaseEntity-GetArmorType:

    .. cpp:function:: int GetArmorType()

    .. _CBaseEntity-SetInvulnerable:

    .. cpp:function:: void SetInvulnerable()

    .. _CBaseEntity-ConnectOutput:

    .. cpp:function:: void ConnectOutput(string event, void functionref( entity trigger, entity activator, entity caller, var value)

    .. _CBaseEntity-SetUsePromptSize:

    .. cpp:function:: unknown SetUsePromptSize(unknown)

    .. _CBaseEntity-SetPassThroughDirection:

    .. cpp:function:: void SetPassThroughDirection(float dir)

    .. _CBaseEntity-Code-SetTeam:

    .. cpp:function:: void Code_SetTeam(int team)

    .. _CBaseEntity-SetShieldHealthMax:

    .. cpp:function:: void SetShieldHealthMax(int)

    .. _CBaseEntity-SetUsableRadius:

    .. cpp:function:: void SetUsableRadius(float distance)

    .. _CBaseEntity-entindex:

    .. cpp:function:: unknown entindex(unknown)

    .. _CBaseEntity-GetTeam:

    .. cpp:function:: int GetTeam()

    .. _CBaseEntity-GetGroundEntity:

    .. cpp:function:: entity GetGroundEntity()

    .. _CBaseEntity-HighlightSetTeamBitField:

    .. cpp:function:: void HighlightSetTeamBitField(int bitField)

    .. _CBaseEntity-ClearInvulnerable:

    .. cpp:function:: void ClearInvulnerable()

    .. _CBaseEntity-SetGroundEntity:

    .. cpp:function:: unknown SetGroundEntity(unknown)

    .. _CBaseEntity-SetNameVisibleToOwner:

    .. cpp:function:: void SetNameVisibleToOwner(bool visible)

    .. _CBaseEntity-GetParent:

    .. cpp:function:: entity GetParent()

    .. _CBaseEntity-SetAbsOriginSmooth:

    .. cpp:function:: unknown SetAbsOriginSmooth(unknown)

    .. _CBaseEntity-GetParentHitbox:

    .. cpp:function:: unknown GetParentHitbox(unknown)

    .. _CBaseEntity-GetShieldHealth:

    .. cpp:function:: int GetShieldHealth()

    .. _CBaseEntity-GetBoundingMaxs:

    .. cpp:function:: vector GetBoundingMaxs()

    .. _CBaseEntity-EnableAttackableByAI:

    .. cpp:function:: void EnableAttackableByAI(int ai_priority_no_threat, int unknown, int ai_ap_flag)

    .. _CBaseEntity-GetLinkEnt:

    .. cpp:function:: entity GetLinkEnt()

    .. _CBaseEntity-GetLinkEntArray:

    .. cpp:function:: array<entity> GetLinkEntArray()

    .. _CBaseEntity-SetNoTarget:

    .. cpp:function:: void SetNoTarget(bool noTarget)

    .. _CBaseEntity-SetPassThroughThickness:

    .. cpp:function:: void SetPassThroughThickness(float thickness)

    .. _CBaseEntity-ClearHitboxAttachedChildren:

    .. cpp:function:: unknown ClearHitboxAttachedChildren(unknown)

    .. _CBaseEntity-GetAngles:

    .. cpp:function:: vector GetAngles()

    .. _CBaseEntity-SetMaxHealth:

    .. cpp:function:: int SetMaxHealth(int health)

    .. _CBaseEntity-EyeAngles:

    .. cpp:function:: vector EyeAngles()

    .. _CBaseEntity-GetGroundRelativePos:

    .. cpp:function:: vector GetGroundRelativePos()

    .. _CBaseEntity-SetUsableFOVByDegrees:

    .. cpp:function:: unknown SetUsableFOVByDegrees(unknown)

    .. _CBaseEntity-CreateStringForFunction:

    .. cpp:function:: string CreateStringForFunction(function func)

    .. _CBaseEntity-SetShieldHealth:

    .. cpp:function:: void SetShieldHealth(int)

    .. _CBaseEntity-IsSpottedByTeam:

    .. cpp:function:: unknown IsSpottedByTeam(unknown)

    .. _CBaseEntity-IsEntAlive:

    .. cpp:function:: bool IsEntAlive()

    .. _CBaseEntity-GetValueForKey:

    .. cpp:function:: var GetValueForKey(string key)

    .. _CBaseEntity-SetNoTargetSmartAmmo:

    .. cpp:function:: void SetNoTargetSmartAmmo(bool noTarget)

    .. _CBaseEntity-GetMaxHealth:

    .. cpp:function:: int GetMaxHealth()

    .. _CBaseEntity-GetBossPlayer:

    .. cpp:function:: entity GetBossPlayer()

    .. _CBaseEntity-SetScriptName:

    .. cpp:function:: void SetScriptName(string name)

    .. _CBaseEntity-IsOnGround:

    .. cpp:function:: bool IsOnGround()

    .. _CBaseEntity-GetVelocity:

    .. cpp:function:: vector GetVelocity()

    .. _CBaseEntity-GetSpawner:

    .. cpp:function:: entity GetSpawner()

    .. _CBaseEntity-GetBlocksRadiusDamage:

    .. cpp:function:: unknown GetBlocksRadiusDamage(unknown)

    .. _CBaseEntity-SetValueForKey:

    .. cpp:function:: void SetValueForKey(var key, var val)

    .. _CBaseEntity-Highlight-IsEntityVisible:

    .. cpp:function:: bool Highlight_IsEntityVisible(int contextID)

    .. _CBaseEntity-IsNPC:

    .. cpp:function:: bool IsNPC()

    .. _CBaseEntity-SetParent:

    .. cpp:function:: void SetParent(entity parent, ..., string type = "")

    .. _CBaseEntity-SetTakeDamageType:

    .. cpp:function:: void SetTakeDamageType(int takeDamageType)

    .. _CBaseEntity-IsMechanical:

    .. cpp:function:: bool IsMechanical()

    .. _CBaseEntity-SetPassThroughFlags:

    .. cpp:function:: unknown SetPassThroughFlags(unknown)

    .. _CBaseEntity-RemoveFromSpatialPartition:

    .. cpp:function:: void RemoveFromSpatialPartition()

    .. _CBaseEntity-GetTitle:

    .. cpp:function:: unknown GetTitle(unknown)

    .. _CBaseEntity-SetBoundingBox:

    .. cpp:function:: unknown SetBoundingBox(unknown)

    .. _CBaseEntity-MakeVisible:

    .. cpp:function:: void MakeVisible()

    .. _CBaseEntity-IsChild:

    .. cpp:function:: unknown IsChild(unknown)

    .. _CBaseEntity-SetUsableFOV:

    .. cpp:function:: unknown SetUsableFOV(unknown)

    .. _CBaseEntity-HasPusherRootParent:

    .. cpp:function:: bool HasPusherRootParent()

    .. _CBaseEntity-GetEntIndex:

    .. cpp:function:: int GetEntIndex()

    .. _CBaseEntity-Minimap-SetCustomState:

    .. cpp:function:: void Minimap_SetCustomState(int state)

    .. _CBaseEntity-GetTargetName:

    .. cpp:function:: string GetTargetName()

    .. _CBaseEntity-GetWorldSpaceCenter:

    .. cpp:function:: vector GetWorldSpaceCenter()

    .. _CBaseEntity-SetOwner:

    .. cpp:function:: void SetOwner(entity owner)

    .. _CBaseEntity-Minimap-SetZOrder:

    .. cpp:function:: void Minimap_SetZOrder(int order)

    .. _CBaseEntity-GetParentAttachment:

    .. cpp:function:: entity GetParentAttachment()

    .. _CBaseEntity-SetCloakFlicker:

    .. cpp:function:: void SetCloakFlicker(float intensity, float duration)

    .. _CBaseEntity-SetAbsForwardVector:

    .. cpp:function:: unknown SetAbsForwardVector(unknown)

    .. _CBaseEntity-GetRootMoveParent:

    .. cpp:function:: entity GetRootMoveParent()

    .. _CBaseEntity-Signal:

    .. cpp:function:: void Signal(string signal)

    .. _CBaseEntity-GetSmoothedVelocity:

    .. cpp:function:: unknown GetSmoothedVelocity(unknown)

    .. _CBaseEntity-SetModel:

    .. cpp:function:: void SetModel(asset model)

    .. _CBaseEntity-GetRightVector:

    .. cpp:function:: vector GetRightVector()

    .. _CBaseEntity-GetBodyGroupNameFromHitboxId:

    .. cpp:function:: unknown GetBodyGroupNameFromHitboxId(unknown)

    .. _CBaseEntity-SetBlocksLOS:

    .. cpp:function:: unknown SetBlocksLOS(unknown)

    .. _CBaseEntity-GetClassName:

    .. cpp:function:: string GetClassName()

    .. _CBaseEntity-GetUsableValue:

    .. cpp:function:: unknown GetUsableValue(unknown)

    .. _CBaseEntity-SetValueForKey:

    .. cpp:function:: void SetValueForKey(var key, var val)

    .. _CBaseEntity-SetPusher:

    .. cpp:function:: unknown SetPusher(unknown)

    .. _CBaseEntity-AllowMantle:

    .. cpp:function:: unknown AllowMantle(unknown)

    .. _CBaseEntity-SetNameVisibleToEnemy:

    .. cpp:function:: void SetNameVisibleToEnemy(bool visible)

    .. _CBaseEntity-GetScriptScope:

    .. cpp:function:: table GetScriptScope()

    .. _CBaseEntity-IsPhaseShifted:

    .. cpp:function:: bool IsPhaseShifted()

    .. _CBaseEntity-SetFadeDistance:

    .. cpp:function:: void SetFadeDistance(int distance)

    .. _CBaseEntity-IsRenderingWithViewModels:

    .. cpp:function:: unknown IsRenderingWithViewModels(unknown)

    .. _CBaseEntity-GetAngularVelocity:

    .. cpp:function:: unknown GetAngularVelocity(unknown)

    .. _CBaseEntity-UnsetUsable:

    .. cpp:function:: void UnsetUsable()

    .. _CBaseEntity-SetDeathNotifications:

    .. cpp:function:: void SetDeathNotifications(bool notifs)

    .. _CBaseEntity-SetAbsOrigin:

    .. cpp:function:: void SetAbsOrigin(void origin)

    .. _CBaseEntity-GetTarget-Deprecated:

    .. cpp:function:: unknown GetTarget_Deprecated(unknown)

    .. _CBaseEntity-GetPusher:

    .. cpp:function:: unknown GetPusher(unknown)

    .. _CBaseEntity-SetUsableValue:

    .. cpp:function:: void SetUsableValue(int val)

    .. _CBaseEntity-GetValueForModelKey:

    .. cpp:function:: asset GetValueForModelKey()

    .. _CBaseEntity-IsInvulnerable:

    .. cpp:function:: bool IsInvulnerable()

    .. _CBaseEntity-SetAimAssistAllowed:

    .. cpp:function:: unknown SetAimAssistAllowed(unknown)

    .. _CBaseEntity-StopPhysics:

    .. cpp:function:: void StopPhysics()

    .. _CBaseEntity-IsHighlightEnabledForTeam:

    .. cpp:function:: unknown IsHighlightEnabledForTeam(unknown)

    .. _CBaseEntity-GetCenter:

    .. cpp:function:: vector GetCenter()

    .. _CBaseEntity-GetLocalVelocity:

    .. cpp:function:: unknown GetLocalVelocity(unknown)

    .. _CBaseEntity-AddToSpatialPartition:

    .. cpp:function:: unknown AddToSpatialPartition(unknown)

    .. _CBaseEntity-AddUsableValue:

    .. cpp:function:: unknown AddUsableValue(unknown)

    .. _CBaseEntity-SetCanCloak:

    .. cpp:function:: void SetCanCloak(bool canCloak)

    .. _CBaseEntity-SetNameVisibleToFriendly:

    .. cpp:function:: void SetNameVisibleToFriendly(bool visible)

    .. _CBaseEntity-GetCloakEndTime:

    .. cpp:function:: unknown GetCloakEndTime(unknown)

    .. _CBaseEntity-IsFuncBrush:

    .. cpp:function:: unknown IsFuncBrush(unknown)

    .. _CBaseEntity-IsTitan:

    .. cpp:function:: bool IsTitan()

    .. _CBaseEntity-IsOperator:

    .. cpp:function:: unknown IsOperator(unknown)

    .. _CBaseEntity-IsHuman:

    .. cpp:function:: bool IsHuman()

    .. _CBaseEntity-SetCloakDuration:

    .. cpp:function:: unknown SetCloakDuration(unknown)

    .. _CBaseEntity-IsBreakableGlass:

    .. cpp:function:: bool IsBreakableGlass()

    .. _CBaseEntity-SetUsablePriority:

    .. cpp:function:: unknown SetUsablePriority(unknown)

    .. _CBaseEntity-Minimap-SetAlignUpright:

    .. cpp:function:: void Minimap_SetAlignUpright(bool align)

    .. _CBaseEntity-MarkAsNonMovingAttachment:

    .. cpp:function:: void MarkAsNonMovingAttachment()

    .. _CBaseEntity-DumpParentingState:

    .. cpp:function:: unknown DumpParentingState(unknown)

    .. _CBaseEntity-Set:

    .. cpp:function:: var Set(string key)

    .. _CBaseEntity-SetValueForEffectNameKey:

    .. cpp:function:: void SetValueForEffectNameKey(asset effect)

    .. _CBaseEntity-SetNameVisibleToNeutral:

    .. cpp:function:: unknown SetNameVisibleToNeutral(unknown)

    .. _CBaseEntity-Highlight-GetCurrentContext:

    .. cpp:function:: int Highlight_GetCurrentContext()

    .. _CBaseEntity-LagCompensate:

    .. cpp:function:: unknown LagCompensate(unknown)

    .. _CBaseEntity-Highlight-GetInheritHighlight:

    .. cpp:function:: unknown Highlight_GetInheritHighlight()

    .. _CBaseEntity-Highlight-GetInsideFunction:

    .. cpp:function:: int Highlight_GetInsideFunction(int contextID)

    .. _CBaseEntity-SetAngles:

    .. cpp:function:: void SetAngles(vector angle)

    .. _CBaseEntity-Highlight-GetParam:

    .. cpp:function:: unknown Highlight_GetParam(int contextID, int parameterNum)

    .. _CBaseEntity-Highlight-GetState:

    .. cpp:function:: int Highlight_GetState(int contextID)

    .. _CBaseEntity-Highlight-IsAfterPostProcess:

    .. cpp:function:: bool Highlight_IsAfterPostProcess(int contextID)

    .. _CBaseEntity-Highlight-HideOutline:

    .. cpp:function:: void Highlight_HideOutline(float duration)

    .. _CBaseEntity-FirstMoveChild:

    .. cpp:function:: entity FirstMoveChild()

    .. _CBaseEntity-SetNextThinkNow:

    .. cpp:function:: void SetNextThinkNow()

    .. _CBaseEntity-GetNoTarget:

    .. cpp:function:: bool GetNoTarget()

    .. _CBaseEntity-Highlight-HideInside:

    .. cpp:function:: void Highlight_HideInside(float duration)

    .. _CBaseEntity-Highlight-Enable:

    .. cpp:function:: unknown Highlight_Enable(unknown)

    .. _CBaseEntity-GetParentAttachmentIndex:

    .. cpp:function:: unknown GetParentAttachmentIndex(unknown)

    .. _CBaseEntity-SetUsable:

    .. cpp:function:: void SetUsable(bool usable)

    .. _CBaseEntity-GetPhysicsSolidMask:

    .. cpp:function:: int GetPhysicsSolidMask()

    .. _CBaseEntity-ClearParent:

    .. cpp:function:: void ClearParent(entity parent)

    .. _CBaseEntity-IsPlayer:

    .. cpp:function:: bool IsPlayer()

    .. _CBaseEntity-EnableDraw:

    .. cpp:function:: void EnableDraw()

    .. _CBaseEntity-GetBlocksLOS:

    .. cpp:function:: unknown GetBlocksLOS(unknown)

    .. _CBaseEntity-EyePosition:

    .. cpp:function:: vector EyePosition()

