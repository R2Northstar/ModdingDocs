.. _C-BaseEntity:

C_BaseEntity
============

.. cpp:class:: C_BaseEntity

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`C_TitanSoul <C-TitanSoul>`
    - :ref:`C_AmbientGeneric <C-AmbientGeneric>`
    - :ref:`C_BaseAnimating <C-BaseAnimating>`
    - :ref:`C_DynamicLight <C-DynamicLight>`
    - :ref:`C_CascadeLight <C-CascadeLight>`
    - :ref:`C_PointCamera <C-PointCamera>`
    - :ref:`C_RopeKeyframe <C-RopeKeyframe>`
    - :ref:`C_HardPointEntity <C-HardPointEntity>`
    - :ref:`C_VGuiScreen <C-VGuiScreen>`
    - :ref:`C_WindowHint <C-WindowHint>`
    - :ref:`C_VortexSphere <C-VortexSphere>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_BaseEntity-GetLocalOrigin:

    .. cpp:function:: unknown GetLocalOrigin(unknown)

    .. _C_BaseEntity-GetNoTargetSmartAmmo:

    .. cpp:function:: unknown GetNoTargetSmartAmmo(unknown)

    .. _C_BaseEntity-IsMarkedForDeletion:

    .. cpp:function:: bool IsMarkedForDeletion()

    .. _C_BaseEntity-HideHUD:

    .. cpp:function:: void HideHUD()

    .. _C_BaseEntity-EyePosition:

    .. cpp:function:: vector EyePosition()

    .. _C_BaseEntity-GetValueForKey:

    .. cpp:function:: var GetValueForKey(string key)

    .. _C_BaseEntity-Highlight-GetCurrentOutlineOpacity:

    .. cpp:function:: float Highlight_GetCurrentOutlineOpacity()

    .. _C_BaseEntity-Highlight-GetState:

    .. cpp:function:: int Highlight_GetState(int contextID)

    .. _C_BaseEntity-DisableRenderWithViewModels:

    .. cpp:function:: unknown DisableRenderWithViewModels(unknown)

    .. _C_BaseEntity-HighlightEnableForTeam:

    .. cpp:function:: void HighlightEnableForTeam(int team)

    .. _C_BaseEntity-GetCloakFadeFactor:

    .. cpp:function:: float GetCloakFadeFactor()

    .. _C_BaseEntity-SetAttachOffsetAngles:

    .. cpp:function:: void SetAttachOffsetAngles(vector angles)

    .. _C_BaseEntity-GetInstanceName:

    .. cpp:function:: unknown GetInstanceName(unknown)

    .. _C_BaseEntity-SetAttachOffsetOrigin:

    .. cpp:function:: void SetAttachOffsetOrigin(vector origin)

    .. _C_BaseEntity-ForceShadowVisible:

    .. cpp:function:: void ForceShadowVisible(bool visible)

    .. _C_BaseEntity-SetValueForKey:

    .. cpp:function:: void SetValueForKey(var key, var val)

    .. _C_BaseEntity-ValidateScriptScope:

    .. cpp:function:: unknown ValidateScriptScope(unknown)

    .. _C_BaseEntity-SetVisibleForLocalPlayer:

    .. cpp:function:: void SetVisibleForLocalPlayer(int visible)

    .. _C_BaseEntity-Show:

    .. cpp:function:: void Show()

    .. _C_BaseEntity-scope:

    .. cpp:function:: unknown scope(unknown)

    .. _C_BaseEntity-HasKey:

    .. cpp:function:: bool HasKey(string key)

    .. _C_BaseEntity-DisableRenderWithCockpit:

    .. cpp:function:: unknown DisableRenderWithCockpit(unknown)

    .. _C_BaseEntity-GetBossPlayerName:

    .. cpp:function:: string GetBossPlayerName()

    .. _C_BaseEntity-EnableRenderWithViewModels:

    .. cpp:function:: unknown EnableRenderWithViewModels(unknown)

    .. _C_BaseEntity-GetLinkParent:

    .. cpp:function:: entity GetLinkParent()

    .. _C_BaseEntity-DisableRenderWithViewModelsNoZoom:

    .. cpp:function:: void DisableRenderWithViewModelsNoZoom()

    .. _C_BaseEntity-Highlight-GetOutlineFunction:

    .. cpp:function:: int Highlight_GetOutlineFunction(int contextID)

    .. _C_BaseEntity-SetLocalOrigin:

    .. cpp:function:: void SetLocalOrigin(vector origin)

    .. _C_BaseEntity-WaitSignal:

    .. cpp:function:: void WaitSignal(string signal)

    .. _C_BaseEntity-SetForceVisibleInPhaseShift:

    .. cpp:function:: void SetForceVisibleInPhaseShift(bool visible)

    .. _C_BaseEntity-IsPlayerDecoy:

    .. cpp:function:: void IsPlayerDecoy()

    .. _C_BaseEntity-GetOwner:

    .. cpp:function:: entity GetOwner()

    .. _C_BaseEntity-IsPlayer:

    .. cpp:function:: bool IsPlayer()

    .. _C_BaseEntity-GetHealth:

    .. cpp:function:: int GetHealth()

    .. _C_BaseEntity-Get:

    .. cpp:function:: var Get(string key)

    .. _C_BaseEntity-EndSignal:

    .. cpp:function:: void EndSignal(string signal)

    .. _C_BaseEntity-IsHologram:

    .. cpp:function:: bool IsHologram()

    .. _C_BaseEntity-ClearParent:

    .. cpp:function:: void ClearParent(entity parent)

    .. _C_BaseEntity-CanCloak:

    .. cpp:function:: unknown CanCloak(unknown)

    .. _C_BaseEntity-GetNextKey:

    .. cpp:function:: unknown GetNextKey(unknown)

    .. _C_BaseEntity-Highlight-SetFlag:

    .. cpp:function:: void Highlight_SetFlag(int highlightFlag, bool enable)

    .. _C_BaseEntity-SetInvisibleForLocalPlayer:

    .. cpp:function:: unknown SetInvisibleForLocalPlayer(unknown)

    .. _C_BaseEntity-IsCloaked:

    .. cpp:function:: bool IsCloaked()

    .. _C_BaseEntity-SetValueForModelKey:

    .. cpp:function:: void SetValueForModelKey(asset model)

    .. _C_BaseEntity-SetModel:

    .. cpp:function:: void SetModel(asset model)

    .. _C_BaseEntity-ShipHack-PositionBetweenEyes:

    .. cpp:function:: unknown ShipHack_PositionBetweenEyes(unknown)

    .. _C_BaseEntity-AreEntityLinksNetworked:

    .. cpp:function:: unknown AreEntityLinksNetworked(unknown)

    .. _C_BaseEntity-GetArmorType:

    .. cpp:function:: int GetArmorType()

    .. _C_BaseEntity-Kill-Deprecated-UseDestroyInstead:

    .. cpp:function:: void Kill_Deprecated_UseDestroyInstead()

    .. _C_BaseEntity-GetRightVector:

    .. cpp:function:: vector GetRightVector()

    .. _C_BaseEntity-IsFuncBrush:

    .. cpp:function:: unknown IsFuncBrush(unknown)

    .. _C_BaseEntity-SetPassThroughDirection:

    .. cpp:function:: void SetPassThroughDirection(float dir)

    .. _C_BaseEntity-GetBossPlayer:

    .. cpp:function:: entity GetBossPlayer()

    .. _C_BaseEntity-SetVelocity:

    .. cpp:function:: void SetVelocity(vector vel)

    .. _C_BaseEntity-Code-SetTeam:

    .. cpp:function:: void Code_SetTeam(int team)

    .. _C_BaseEntity-Highlight-GetCurrentInsideOpacity:

    .. cpp:function:: float Highlight_GetCurrentInsideOpacity()

    .. _C_BaseEntity-EnableRenderAlways:

    .. cpp:function:: void EnableRenderAlways()

    .. _C_BaseEntity-Signal:

    .. cpp:function:: void Signal(string signal)

    .. _C_BaseEntity-EnableHealthChangedCallback:

    .. cpp:function:: void EnableHealthChangedCallback()

    .. _C_BaseEntity-ShowHUD:

    .. cpp:function:: void ShowHUD()

    .. _C_BaseEntity-GetTeam:

    .. cpp:function:: int GetTeam()

    .. _C_BaseEntity-IsClientOnly:

    .. cpp:function:: unknown IsClientOnly(unknown)

    .. _C_BaseEntity-Highlight-HideOutline:

    .. cpp:function:: void Highlight_HideOutline(float duration)

    .. _C_BaseEntity-InitHudElemGroup:

    .. cpp:function:: unknown InitHudElemGroup(unknown)

    .. _C_BaseEntity-InitHudElem:

    .. cpp:function:: void InitHudElem(var key)

    .. _C_BaseEntity-HighlightSetTeamBitField:

    .. cpp:function:: void HighlightSetTeamBitField(int bitField)

    .. _C_BaseEntity-Set:

    .. cpp:function:: var Set(string key)

    .. _C_BaseEntity-constructor:

    .. cpp:function:: entity constructor(unknown)

    .. _C_BaseEntity-GetScriptId:

    .. cpp:function:: unknown GetScriptId(unknown)

    .. _C_BaseEntity-IsProjectile:

    .. cpp:function:: bool IsProjectile()

    .. _C_BaseEntity-CreateTableFromModelKeyValues:

    .. cpp:function:: table CreateTableFromModelKeyValues()

    .. _C_BaseEntity-GetParent:

    .. cpp:function:: entity GetParent()

    .. _C_BaseEntity-SetParentWithHitbox:

    .. cpp:function:: void SetParentWithHitbox(entity parent, int hitGroup, bool unknown)

    .. _C_BaseEntity-GetParentHitbox:

    .. cpp:function:: unknown GetParentHitbox(unknown)

    .. _C_BaseEntity-SetAngles:

    .. cpp:function:: void SetAngles(vector angle)

    .. _C_BaseEntity-IsPredictedProjectile:

    .. cpp:function:: unknown IsPredictedProjectile(unknown)

    .. _C_BaseEntity-SetParent:

    .. cpp:function:: void SetParent(entity parent, ..., string type = "")

    .. _C_BaseEntity-LookupAttachment:

    .. cpp:function:: int LookupAttachment(string attachment)

    .. _C_BaseEntity-DontIncludeParentBbox:

    .. cpp:function:: unknown DontIncludeParentBbox(unknown)

    .. _C_BaseEntity-PhysicsDummyEnableMotion:

    .. cpp:function:: unknown PhysicsDummyEnableMotion(unknown)

    .. _C_BaseEntity-GetLinkEnt:

    .. cpp:function:: entity GetLinkEnt()

    .. _C_BaseEntity-GetLinkEntArray:

    .. cpp:function:: array<entity> GetLinkEntArray()

    .. _C_BaseEntity-DisableRenderAlways:

    .. cpp:function:: void DisableRenderAlways()

    .. _C_BaseEntity-SetPassThroughThickness:

    .. cpp:function:: void SetPassThroughThickness(float thickness)

    .. _C_BaseEntity-Highlight-SetVisibilityType:

    .. cpp:function:: void Highlight_SetVisibilityType(int type)

    .. _C_BaseEntity-EnableRenderWithHud:

    .. cpp:function:: void EnableRenderWithHud()

    .. _C_BaseEntity-GetAngles:

    .. cpp:function:: vector GetAngles()

    .. _C_BaseEntity-GetPreTemplateName:

    .. cpp:function:: unknown GetPreTemplateName(unknown)

    .. _C_BaseEntity-IsOperator:

    .. cpp:function:: unknown IsOperator(unknown)

    .. _C_BaseEntity-GetUpVector:

    .. cpp:function:: vector GetUpVector()

    .. _C_BaseEntity-GetPassThroughFlags:

    .. cpp:function:: unknown GetPassThroughFlags(unknown)

    .. _C_BaseEntity-GetCritsPrevented:

    .. cpp:function:: bool GetCritsPrevented()

    .. _C_BaseEntity-Highlight-SetFadeOutTime:

    .. cpp:function:: void Highlight_SetFadeOutTime(float time)

    .. _C_BaseEntity-SetPreventCrits:

    .. cpp:function:: void SetPreventCrits(bool prevent)

    .. _C_BaseEntity-SetAlive:

    .. cpp:function:: unknown SetAlive(unknown)

    .. _C_BaseEntity-SetValueForEffectNameKey:

    .. cpp:function:: void SetValueForEffectNameKey(asset effect)

    .. _C_BaseEntity-IsEntAlive:

    .. cpp:function:: bool IsEntAlive()

    .. _C_BaseEntity-GetBoundingMins:

    .. cpp:function:: vector GetBoundingMins()

    .. _C_BaseEntity-EnableDraw:

    .. cpp:function:: void EnableDraw()

    .. _C_BaseEntity-GetMaxHealth:

    .. cpp:function:: int GetMaxHealth()

    .. _C_BaseEntity-IsHuman:

    .. cpp:function:: bool IsHuman()

    .. _C_BaseEntity-GetSignifierName:

    .. cpp:function:: string GetSignifierName()

    .. _C_BaseEntity-IsOnGround:

    .. cpp:function:: bool IsOnGround()

    .. _C_BaseEntity-GetVelocity:

    .. cpp:function:: vector GetVelocity()

    .. _C_BaseEntity-SetTakeDamageType:

    .. cpp:function:: void SetTakeDamageType(int takeDamageType)

    .. _C_BaseEntity-GetShieldHealth:

    .. cpp:function:: int GetShieldHealth()

    .. _C_BaseEntity-GetLifeState:

    .. cpp:function:: int GetLifeState()

    .. _C_BaseEntity-Highlight-IsEntityVisible:

    .. cpp:function:: bool Highlight_IsEntityVisible(int contextID)

    .. _C_BaseEntity-IsNPC:

    .. cpp:function:: bool IsNPC()

    .. _C_BaseEntity-Highlight-Enable:

    .. cpp:function:: unknown Highlight_Enable(unknown)

    .. _C_BaseEntity-Minimap-GetCustomState:

    .. cpp:function:: int Minimap_GetCustomState()

    .. _C_BaseEntity-HasGibModel:

    .. cpp:function:: bool HasGibModel()

    .. _C_BaseEntity-IsMechanical:

    .. cpp:function:: bool IsMechanical()

    .. _C_BaseEntity-SetPassThroughFlags:

    .. cpp:function:: unknown SetPassThroughFlags(unknown)

    .. _C_BaseEntity-DispatchImpactEffects:

    .. cpp:function:: void DispatchImpactEffects(entity ent, vector startPos, vector endPos, vector hitNormal, enitity prop, int propIndex, int damageType, int impactIndex, entity orig, int impactEffectFlags)

    .. _C_BaseEntity-Highlight-GetOutlineRadius:

    .. cpp:function:: float Highlight_GetOutlineRadius()

    .. _C_BaseEntity-Highlight-SetLifeTime:

    .. cpp:function:: void Highlight_SetLifeTime(float time)

    .. _C_BaseEntity-EyeAngles:

    .. cpp:function:: vector EyeAngles()

    .. _C_BaseEntity-Hide:

    .. cpp:function:: void Hide()

    .. _C_BaseEntity-GetLocalAngles:

    .. cpp:function:: vector GetLocalAngles()

    .. _C_BaseEntity-IsTitan:

    .. cpp:function:: bool IsTitan()

    .. _C_BaseEntity-IsHUDVisible:

    .. cpp:function:: bool IsHUDVisible()

    .. _C_BaseEntity-GetValueForEffectNameKey:

    .. cpp:function:: unknown GetValueForEffectNameKey(unknown)

    .. _C_BaseEntity-Highlight-GetCurrentContext:

    .. cpp:function:: int Highlight_GetCurrentContext()

    .. _C_BaseEntity-GetBoundingMaxs:

    .. cpp:function:: vector GetBoundingMaxs()

    .. _C_BaseEntity-Highlight-GetNearFadeDist:

    .. cpp:function:: float Highlight_GetNearFadeDist()

    .. _C_BaseEntity-GetScriptName:

    .. cpp:function:: string GetScriptName()

    .. _C_BaseEntity-GetClassName:

    .. cpp:function:: string GetClassName()

    .. _C_BaseEntity-Highlight-StartOn:

    .. cpp:function:: void Highlight_StartOn()

    .. _C_BaseEntity-Destroy:

    .. cpp:function:: void Destroy()

    .. _C_BaseEntity-DisableRenderWithHud:

    .. cpp:function:: unknown DisableRenderWithHud(unknown)

    .. _C_BaseEntity-Highlight-GetInheritHighlight:

    .. cpp:function:: unknown Highlight_GetInheritHighlight()

    .. _C_BaseEntity-Highlight-GetFlag:

    .. cpp:function:: unknown Highlight_GetFlag(unknown)

    .. _C_BaseEntity-Highlight-ResetFlags:

    .. cpp:function:: void Highlight_ResetFlags()

    .. _C_BaseEntity-Highlight-GetParam:

    .. cpp:function:: unknown Highlight_GetParam(int contextID, int parameterNum)

    .. _C_BaseEntity-IsWorld:

    .. cpp:function:: bool IsWorld()

    .. _C_BaseEntity-Highlight-GetFarFadeDist:

    .. cpp:function:: unknown Highlight_GetFarFadeDist(unknown)

    .. _C_BaseEntity-HighlightDisableForTeam:

    .. cpp:function:: void HighlightDisableForTeam(int team)

    .. _C_BaseEntity-Highlight-SetFarFadeDist:

    .. cpp:function:: void Highlight_SetFarFadeDist(float dist)

    .. _C_BaseEntity-Highlight-SetNearFadeDist:

    .. cpp:function:: void Highlight_SetNearFadeDist(float dist)

    .. _C_BaseEntity-SetFadeDistance:

    .. cpp:function:: void SetFadeDistance(int distance)

    .. _C_BaseEntity-Highlight-SetFadeInTime:

    .. cpp:function:: void Highlight_SetFadeInTime(float time)

    .. _C_BaseEntity-Highlight-ShowOutline:

    .. cpp:function:: void Highlight_ShowOutline(float duration)

    .. _C_BaseEntity-IsPhaseShifted:

    .. cpp:function:: bool IsPhaseShifted()

    .. _C_BaseEntity-Highlight-ShowInside:

    .. cpp:function:: void Highlight_ShowInside(float duration)

    .. _C_BaseEntity-GetOrigin:

    .. cpp:function:: vector GetOrigin()

    .. _C_BaseEntity-Highlight-HideInside:

    .. cpp:function:: void Highlight_HideInside(float duration)

    .. _C_BaseEntity-SetPhysics:

    .. cpp:function:: unknown SetPhysics(unknown)

    .. _C_BaseEntity-SetDoDestroyCallback:

    .. cpp:function:: void SetDoDestroyCallback(bool doCallBack)

    .. _C_BaseEntity-Highlight-SetParam:

    .. cpp:function:: void Highlight_SetParam(int contextID, int parameterID, vector highlightColor)

    .. _C_BaseEntity-Highlight-SetFunctions:

    .. cpp:function:: void Highlight_SetFunctions(int contextID, int hightlightFillID, bool entityVisible, int colorMode, float radius, int highlightID, bool afterPostProcess)

    .. _C_BaseEntity-Highlight-SetInheritHighlight:

    .. cpp:function:: void Highlight_SetInheritHighlight(bool set)

    .. _C_BaseEntity-Highlight-SetCurrentContext:

    .. cpp:function:: void Highlight_SetCurrentContext(int contextID)

    .. _C_BaseEntity-DisableDraw:

    .. cpp:function:: void DisableDraw()

    .. _C_BaseEntity-IsInvulnerable:

    .. cpp:function:: bool IsInvulnerable()

    .. _C_BaseEntity-Highlight-IsAfterPostProcess:

    .. cpp:function:: bool Highlight_IsAfterPostProcess(int contextID)

    .. _C_BaseEntity-GetParentAttachment:

    .. cpp:function:: entity GetParentAttachment()

    .. _C_BaseEntity-IsHighlightEnabledForTeam:

    .. cpp:function:: unknown IsHighlightEnabledForTeam(unknown)

    .. _C_BaseEntity-clKill:

    .. cpp:function:: void clKill()

    .. _C_BaseEntity-GetLocalVelocity:

    .. cpp:function:: unknown GetLocalVelocity(unknown)

    .. _C_BaseEntity-SetScriptName:

    .. cpp:function:: void SetScriptName(string name)

    .. _C_BaseEntity-MarkAsNonMovingAttachment:

    .. cpp:function:: void MarkAsNonMovingAttachment()

    .. _C_BaseEntity-SetCanCloak:

    .. cpp:function:: void SetCanCloak(bool canCloak)

    .. _C_BaseEntity-Dev-GetEncodedEHandle:

    .. cpp:function:: int Dev_GetEncodedEHandle()

    .. _C_BaseEntity-GetCloakEndTime:

    .. cpp:function:: unknown GetCloakEndTime(unknown)

    .. _C_BaseEntity-GetNoTarget:

    .. cpp:function:: bool GetNoTarget()

    .. _C_BaseEntity-IsBreakableGlass:

    .. cpp:function:: bool IsBreakableGlass()

    .. _C_BaseEntity-GetTargetName:

    .. cpp:function:: string GetTargetName()

    .. _C_BaseEntity-GetEntIndex:

    .. cpp:function:: int GetEntIndex()

    .. _C_BaseEntity-SetToSameParentAs:

    .. cpp:function:: unknown SetToSameParentAs(unknown)

    .. _C_BaseEntity-StopPhysics:

    .. cpp:function:: void StopPhysics()

    .. _C_BaseEntity-GetShieldHealthMax:

    .. cpp:function:: int GetShieldHealthMax()

    .. _C_BaseEntity-SetValueForTextureKey:

    .. cpp:function:: void SetValueForTextureKey(asset texture)

    .. _C_BaseEntity-GetTarget-Deprecated:

    .. cpp:function:: unknown GetTarget_Deprecated(unknown)

    .. _C_BaseEntity-GetWorldSpaceCenter:

    .. cpp:function:: vector GetWorldSpaceCenter()

    .. _C_BaseEntity-RenderWithViewModels:

    .. cpp:function:: void RenderWithViewModels(bool renderWith)

    .. _C_BaseEntity-IsRenderingWithViewModels:

    .. cpp:function:: unknown IsRenderingWithViewModels(unknown)

    .. _C_BaseEntity-Minimap-GetZOrder:

    .. cpp:function:: int Minimap_GetZOrder()

    .. _C_BaseEntity-Highlight-GetInsideFunction:

    .. cpp:function:: int Highlight_GetInsideFunction(int contextID)

    .. _C_BaseEntity-GetModelName:

    .. cpp:function:: asset GetModelName()

    .. _C_BaseEntity-GetValueForTextureKey:

    .. cpp:function:: unknown GetValueForTextureKey(unknown)

    .. _C_BaseEntity-IsIgnoredByAimAssist:

    .. cpp:function:: unknown IsIgnoredByAimAssist(unknown)

    .. _C_BaseEntity-GetValueForModelKey:

    .. cpp:function:: asset GetValueForModelKey()

    .. _C_BaseEntity-IsSpottedByTeam:

    .. cpp:function:: unknown IsSpottedByTeam(unknown)

    .. _C_BaseEntity-EnableRenderWithCockpit:

    .. cpp:function:: void EnableRenderWithCockpit()

    .. _C_BaseEntity-DisableHealthChangedCallback:

    .. cpp:function:: unknown DisableHealthChangedCallback(unknown)

    .. _C_BaseEntity-GetForwardVector:

    .. cpp:function:: vector GetForwardVector()

    .. _C_BaseEntity-GetScriptScope:

    .. cpp:function:: table GetScriptScope()

    .. _C_BaseEntity-HasPusherRootParent:

    .. cpp:function:: bool HasPusherRootParent()

    .. _C_BaseEntity-GetLinkParentArray:

    .. cpp:function:: unknown GetLinkParentArray(unknown)

    .. _C_BaseEntity-IsZipline:

    .. cpp:function:: unknown IsZipline(unknown)

    .. _C_BaseEntity-GetParentAttachmentIndex:

    .. cpp:function:: unknown GetParentAttachmentIndex(unknown)

    .. _C_BaseEntity-IsValidInternal:

    .. cpp:function:: bool IsValidInternal()

    .. _C_BaseEntity-GetTitleForUI:

    .. cpp:function:: string GetTitleForUI()

    .. _C_BaseEntity-SetLocalAngles:

    .. cpp:function:: void SetLocalAngles(vector angles)

    .. _C_BaseEntity-GetBodyGroupNameFromHitboxId:

    .. cpp:function:: unknown GetBodyGroupNameFromHitboxId(unknown)

    .. _C_BaseEntity-SetOrigin:

    .. cpp:function:: void SetOrigin(vector position)

    .. _C_BaseEntity-DoDeathCallback:

    .. cpp:function:: void DoDeathCallback(bool doCallback)

    .. _C_BaseEntity-EnableRenderWithViewModelsNoZoom:

    .. cpp:function:: unknown EnableRenderWithViewModelsNoZoom(unknown)

