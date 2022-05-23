Entities
========

There are different Classes for Server and Client. Classes that start with ``C_`` are exclusive to the Client VM and classes that only have the ``C`` Prefix are only usable in the Server VM.

Each entry in the following list has three sub entries: The class available to the SERVER, the CLIENT and methods that are available on both VMs.

.. note::

	If not otherwise specified are the following Classes inherited from CBaseEntity or C_BaseEntity respectively.

	This List of Classes and their Methods is incomplete!


CBaseEntity / C_BaseEntity
--------------------------

Basic enitity that most other entities inherit from.

Shared
^^^^^^

.. cpp:class:: CBaseEntity / C_BaseEntity

	.. cpp:function:: unknown Hide( unknown )

	.. cpp:function:: unknown Destroy( unknown )

	.. cpp:function:: unknown Signal( unknown )

	.. cpp:function:: unknown GetOrigin( unknown )

	.. cpp:function:: unknown GetBossPlayer( unknown )

	.. cpp:function:: unknown GetClassName( unknown )

	.. cpp:function:: unknown IsNPC( unknown )

	.. cpp:function:: unknown IsTitan( unknown )

	.. cpp:function:: unknown IsHuman( unknown )

	.. cpp:function:: unknown IsPhaseShifted( unknown )

	.. cpp:function:: unknown IsPlayer( unknown )

	.. cpp:function:: unknown IsProjectile( unknown )

	.. cpp:function:: unknown GetModelName( unknown )

	.. cpp:function:: unknown SetParent( unknown )

	.. cpp:function:: unknown SetValueForEffectNameKey( unknown )

	.. cpp:function:: unknown CreateTableFromModelKeyValues( unknown )

	.. cpp:function:: unknown EndSignal( unknown )

	.. cpp:function:: unknown GetArmorType( unknown )

	.. cpp:function:: unknown GetMaxHealth( unknown )

	.. cpp:function:: unknown HasGibModel( unknown )

	.. cpp:function:: unknown HasKey( unknown )

	.. cpp:function:: unknown IsMarkedForDeletion( unknown )

	.. cpp:function:: unknown IsMechanical( unknown )

	.. cpp:function:: unknown SetOrigin( unknown )

	.. cpp:function:: unknown GetTargetName( unknown )

	.. cpp:function:: unknown GetTeam( unknown )

	.. cpp:function:: unknown GetAngles( unknown )

	.. cpp:function:: unknown EyePosition( unknown )

	.. cpp:function:: unknown GetValueForKey( unknown )

	.. cpp:function:: unknown WaitSignal( unknown )

	.. cpp:function:: unknown GetVelocity( unknown )

	.. cpp:function:: unknown Kill_Deprecated_UseDestroyInstead( unknown )

	.. cpp:function:: unknown GetBoundingMaxs( unknown )

	.. cpp:function:: unknown GetBoundingMins( unknown )

	.. cpp:function:: unknown SetAngles( unknown )

	.. cpp:function:: unknown ClearParent( unknown )

	.. cpp:function:: unknown SetValueForModelKey( unknown )

	.. cpp:function:: unknown Show( unknown )

	.. cpp:function:: unknown IsInvulnerable( unknown )

	.. cpp:function:: unknown GetParent( unknown )

	.. cpp:function:: unknown GetWorldSpaceCenter( unknown )

	.. cpp:function:: unknown Highlight_GetCurrentContext( unknown )

	.. cpp:function:: unknown Highlight_GetCurrentInsideOpacity( unknown )

	.. cpp:function:: unknown Highlight_GetCurrentOutlineOpacity( unknown )

	.. cpp:function:: unknown Highlight_GetInheritHighlight( unknown )

	.. cpp:function:: unknown Highlight_GetInsideFunction( unknown )

	.. cpp:function:: unknown Highlight_GetOutlineFunction( unknown )

	.. cpp:function:: unknown Highlight_GetOutlineRadius( unknown )

	.. cpp:function:: unknown Highlight_GetParam( unknown )

	.. cpp:function:: unknown Highlight_GetState( unknown )

	.. cpp:function:: unknown Highlight_HideInside( unknown )

	.. cpp:function:: unknown Highlight_HideOutline( unknown )

	.. cpp:function:: unknown Highlight_IsAfterPostProcess( unknown )

	.. cpp:function:: unknown Highlight_IsEntityVisible( unknown )

	.. cpp:function:: unknown Highlight_SetCurrentContext( unknown )

	.. cpp:function:: unknown Highlight_SetFunctions( unknown )

	.. cpp:function:: unknown Highlight_SetParam( unknown )

	.. cpp:function:: unknown Highlight_ShowInside( unknown )

	.. cpp:function:: unknown Highlight_ShowOutline( unknown )

	.. cpp:function:: unknown GetEntIndex( unknown )

	.. cpp:function:: unknown GetOwner( unknown )

	.. cpp:function:: unknown GetShieldHealth( unknown )

	.. cpp:function:: unknown GetShieldHealthMax( unknown )

	.. cpp:function:: unknown SetScriptName( unknown )

	.. cpp:function:: unknown GetLinkEntArray( unknown )

	.. cpp:function:: unknown GetLinkEnt( unknown )

	.. cpp:function:: unknown Code_SetTeam( unknown )

	.. cpp:function:: unknown GetHealth( unknown )

	.. cpp:function:: unknown IsCloaked( unknown )

	.. cpp:function:: unknown IsEntAlive( unknown )

	.. cpp:function:: unknown IsValidInternal( unknown )

	.. cpp:function:: unknown GetForwardVector( unknown )

	.. cpp:function:: unknown GetRightVector( unknown )

	.. cpp:function:: unknown GetUpVector( unknown )

	.. cpp:function:: unknown SetValueForKey( unknown )

	.. cpp:function:: unknown constructor( unknown )

	.. cpp:function:: unknown SetDoDestroyCallback( unknown )

	.. cpp:function:: unknown GetLifeState( unknown )

	.. cpp:function:: unknown DisableDraw( unknown )

	.. cpp:function:: unknown EnableDraw( unknown )

	.. cpp:function:: unknown SetCanCloak( unknown )

	.. cpp:function:: unknown GetCritsPrevented( unknown )

	.. cpp:function:: unknown IsHologram( unknown )

	.. cpp:function:: unknown IsOnGround( unknown )

	.. cpp:function:: unknown SetModel( unknown )

	.. cpp:function:: unknown MarkAsNonMovingAttachment( unknown )

	.. cpp:function:: unknown GetScriptName( unknown )

	.. cpp:function:: unknown EyeAngles( unknown )

	.. cpp:function:: unknown IsBreakableGlass( unknown )

	.. cpp:function:: unknown IsWorld( unknown )

	.. cpp:function:: unknown DispatchImpactEffects( unknown )

	.. cpp:function:: unknown IsPlayerDecoy( unknown )

	.. cpp:function:: unknown SetPassThroughDirection( unknown )

	.. cpp:function:: unknown SetPassThroughThickness( unknown )

	.. cpp:function:: unknown SetTakeDamageType( unknown )

	.. cpp:function:: unknown SetVelocity( unknown )

	.. cpp:function:: unknown EnableRenderAlways( unknown )

	.. cpp:function:: unknown GetParentAttachment( unknown )

	.. cpp:function:: unknown SetFadeDistance( unknown )

	.. cpp:function:: unknown Highlight_SetInheritHighlight( unknown )

	.. cpp:function:: unknown DisableRenderAlways( unknown )

	.. cpp:function:: unknown SetLocalOrigin( unknown )

	.. cpp:function:: unknown HasPusherRootParent( unknown )

	.. cpp:function:: unknown StopPhysics( unknown )

	.. cpp:function:: unknown SetPreventCrits( unknown )

	.. cpp:function:: unknown HighlightDisableForTeam( unknown )

	.. cpp:function:: unknown HighlightEnableForTeam( unknown )

	.. cpp:function:: unknown HighlightSetTeamBitField( unknown )

	.. cpp:function:: unknown SetLocalAngles( unknown )

	.. cpp:function:: unknown SetParentWithHitbox( unknown )

	.. cpp:function:: unknown RenderWithViewModels( unknown )

	.. cpp:function:: unknown SetValueForTextureKey( unknown )

	.. cpp:function:: unknown GetValueForModelKey( unknown )

	.. cpp:function:: unknown GetLocalAngles( unknown )

	.. cpp:function:: unknown GetLinkParent( unknown )

	.. cpp:function:: unknown GetNoTarget( unknown )

	.. cpp:function:: unknown SetForceVisibleInPhaseShift( unknown )

	.. cpp:function:: unknown GetScriptScope( unknown )

CBaseEntity
^^^^^^^^^^^

.. cpp:class:: CBaseEntity

	.. cpp:function:: unknown SetHealth( unknown )

	.. cpp:function:: unknown SetMaxHealth( unknown )

	.. cpp:function:: unknown SetOwner( unknown )

	.. cpp:function:: unknown GetSpawner( unknown )

	.. cpp:function:: unknown Die( unknown )

	.. cpp:function:: unknown NotSolid( unknown )

	.. cpp:function:: unknown MoveTo( unknown )

	.. cpp:function:: unknown RotateTo( unknown )

	.. cpp:function:: unknown ClearInvulnerable( unknown )

	.. cpp:function:: unknown SetInvulnerable( unknown )

	.. cpp:function:: unknown SetNextThinkNow( unknown )

	.. cpp:function:: unknown SetNoTarget( unknown )

	.. cpp:function:: unknown SetNoTargetSmartAmmo( unknown )

	.. cpp:function:: unknown Minimap_SetClampToEdge( unknown )

	.. cpp:function:: unknown Minimap_SetCustomState( unknown )

	.. cpp:function:: unknown Minimap_SetZOrder( unknown )

	.. cpp:function:: unknown Minimap_SetAlignUpright( unknown )

	.. cpp:function:: unknown Minimap_SetObjectScale( unknown )

	.. cpp:function:: unknown SetShieldHealth( unknown )

	.. cpp:function:: unknown SetShieldHealthMax( unknown )

	.. cpp:function:: unknown GetEncodedEHandle( unknown )

	.. cpp:function:: unknown SetUsable( unknown )

	.. cpp:function:: unknown SetUsableRadius( unknown )

	.. cpp:function:: unknown Solid( unknown )

	.. cpp:function:: unknown Fire( unknown )

	.. cpp:function:: unknown SetUsableByGroup( unknown )

	.. cpp:function:: unknown DisableHibernation( unknown )

	.. cpp:function:: unknown SetSize( unknown )

	.. cpp:function:: unknown SetCloakFlicker( unknown )

	.. cpp:function:: unknown TakeDamage( unknown )

	.. cpp:function:: unknown GetCenter( unknown )

	.. cpp:function:: unknown TraceAttackToTriggers( unknown )

	.. cpp:function:: unknown SetBlocksRadiusDamage( unknown )

	.. cpp:function:: unknown SetDamageNotifications( unknown )

	.. cpp:function:: unknown NextMovePeer( unknown )

	.. cpp:function:: unknown SetNameVisibleToEnemy( unknown )

	.. cpp:function:: unknown SetNameVisibleToFriendly( unknown )

	.. cpp:function:: unknown SetNameVisibleToOwner( unknown )

	.. cpp:function:: unknown FirstMoveChild( unknown )

	.. cpp:function:: unknown GetRootMoveParent( unknown )

	.. cpp:function:: unknown RemoveFromSpatialPartition( unknown )

	.. cpp:function:: unknown SetUsePrompts( unknown )

	.. cpp:function:: unknown SetAngularVelocity( unknown )

	.. cpp:function:: unknown MakeInvisible( unknown )

	.. cpp:function:: unknown MakeVisible( unknown )

	.. cpp:function:: unknown GetGroundEntity( unknown )

	.. cpp:function:: unknown GetGroundRelativePos( unknown )

	.. cpp:function:: unknown GetPhysicsSolidMask( unknown )

	.. cpp:function:: unknown SetBossPlayer( unknown )

	.. cpp:function:: unknown EnableAttackableByAI( unknown )

	.. cpp:function:: unknown SetDeathNotifications( unknown )

	.. cpp:function:: unknown SetTitle( unknown )

	.. cpp:function:: unknown LinkToEnt( unknown )

	.. cpp:function:: unknown SetAbsAngles( unknown )

	.. cpp:function:: unknown SetAbsOrigin( unknown )

	.. cpp:function:: unknown UnsetUsable( unknown )

	.. cpp:function:: unknown Minimap_AlwaysShow( unknown )

	.. cpp:function:: unknown RoundOriginAndAnglesToNearestNetworkValue( unknown )

	.. cpp:function:: unknown ConnectOutput( unknown )

	.. cpp:function:: unknown ClearBossPlayer( unknown )

	.. cpp:function:: unknown SetUsableValue( unknown )

	.. cpp:function:: unknown Minimap_DisplayDefault( unknown )

	.. cpp:function:: unknown FireNow( unknown )

C_BaseEntity
^^^^^^^^^^^^

.. cpp:class:: C_BaseEntity

	.. cpp:function:: unknown GetSignifierName( unknown )

	.. cpp:function:: unknown LookupAttachment( unknown )

	.. cpp:function:: unknown GetBossPlayerName( unknown )

	.. cpp:function:: unknown ForceShadowVisible( unknown )

	.. cpp:function:: unknown clKill( unknown )

	.. cpp:function:: unknown Highlight_GetNearFadeDist( unknown )

	.. cpp:function:: unknown Highlight_ResetFlags( unknown )

	.. cpp:function:: unknown Highlight_SetFadeInTime( unknown )

	.. cpp:function:: unknown Highlight_SetFadeOutTime( unknown )

	.. cpp:function:: unknown Highlight_SetFarFadeDist( unknown )

	.. cpp:function:: unknown Highlight_SetFlag( unknown )

	.. cpp:function:: unknown Highlight_SetLifeTime( unknown )

	.. cpp:function:: unknown Highlight_SetNearFadeDist( unknown )

	.. cpp:function:: unknown Highlight_SetVisibilityType( unknown )

	.. cpp:function:: unknown Highlight_StartOn( unknown )

	.. cpp:function:: unknown DisableRenderWithViewModelsNoZoom( unknown )

	.. cpp:function:: unknown EnableRenderWithCockpit( unknown )

	.. cpp:function:: unknown EnableRenderWithHud( unknown )

	.. cpp:function:: unknown SetAttachOffsetAngles( unknown )

	.. cpp:function:: unknown SetAttachOffsetOrigin( unknown )

	.. cpp:function:: unknown SetVisibleForLocalPlayer( unknown )

	.. cpp:function:: unknown InitHudElem( unknown )

	.. cpp:function:: unknown GetTitleForUI( unknown )

	.. cpp:function:: unknown GetCloakFadeFactor( unknown )

	.. cpp:function:: unknown Dev_GetEncodedEHandle( unknown )

	.. cpp:function:: unknown Minimap_GetCustomState( unknown )

	.. cpp:function:: unknown Minimap_GetZOrder( unknown )

	.. cpp:function:: unknown DoDeathCallback( unknown )

	.. cpp:function:: unknown EnableHealthChangedCallback( unknown )

	.. cpp:function:: unknown HideHUD( unknown )

	.. cpp:function:: unknown ShowHUD( unknown )

	.. cpp:function:: unknown IsHUDVisible( unknown )

CWeaponX / C_WeaponX
--------------------

Weapons hold by a player or that are lying on the ground are of this type.

Shared
^^^^^^

.. cpp:class:: CWeaponX / C_WeaponX : extends CBaseEntity / C_BaseEntity

	.. cpp:function:: unknown GetAttachmentOrigin( unknown )

	.. cpp:function:: unknown LookupAttachment( unknown )

	.. cpp:function:: unknown GetWeaponOwner( unknown )

	.. cpp:function:: unknown FindBodyGroup( unknown )

	.. cpp:function:: unknown GetBodyGroupState( unknown )

	.. cpp:function:: unknown GetAllowHeadShots( unknown )

	.. cpp:function:: unknown GetMaxDamageFarDist( unknown )

	.. cpp:function:: unknown GetWeaponSettingBool( unknown )

	.. cpp:function:: unknown GetWeaponSettingFloat( unknown )

	.. cpp:function:: unknown GetWeaponSettingInt( unknown )

	.. cpp:function:: unknown GetBodyGroupModelCount( unknown )

	.. cpp:function:: unknown SetBodygroup( unknown )

	.. cpp:function:: unknown GetAttachmentAngles( unknown )

	.. cpp:function:: unknown GetAttackDirection( unknown )

	.. cpp:function:: unknown GetAttackPosition( unknown )

	.. cpp:function:: unknown Anim_GetAttachmentAtTime( unknown )

	.. cpp:function:: unknown GetScriptedAnimEventCycleFrac( unknown )

	.. cpp:function:: unknown GetSequenceDuration( unknown )

	.. cpp:function:: unknown Anim_IsActive( unknown )

	.. cpp:function:: unknown Anim_Play( unknown )

	.. cpp:function:: unknown Anim_SetInitialTime( unknown )

	.. cpp:function:: unknown Anim_Stop( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefEntity_Old( unknown )

	.. cpp:function:: unknown GetWeaponPrimaryAmmoCount( unknown )

	.. cpp:function:: unknown GetWeaponPrimaryClipCount( unknown )

	.. cpp:function:: unknown GetWeaponPrimaryClipCountMax( unknown )

	.. cpp:function:: unknown IsChargeWeapon( unknown )

	.. cpp:function:: unknown SetNextAttackAllowedTime( unknown )

	.. cpp:function:: unknown SetWeaponChargeFractionForced( unknown )

	.. cpp:function:: unknown SetWeaponPrimaryClipCount( unknown )

	.. cpp:function:: unknown GetWeaponClassName( unknown )

	.. cpp:function:: unknown GetSkin( unknown )

	.. cpp:function:: unknown LookupSequence( unknown )

	.. cpp:function:: unknown SetSkin( unknown )

	.. cpp:function:: unknown GetWeaponInfoFileKeyField( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint( unknown )

	.. cpp:function:: unknown GetCoreDuration( unknown )

	.. cpp:function:: unknown GetWeaponType( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint_Old( unknown )

	.. cpp:function:: unknown Anim_PlayWithRefPoint( unknown )

	.. cpp:function:: unknown GetMods( unknown )

	.. cpp:function:: unknown Anim_NonScriptedPlay( unknown )

	.. cpp:function:: unknown GetWeaponDescription( unknown )

	.. cpp:function:: unknown IsWeaponOffhand( unknown )

	.. cpp:function:: unknown GetWeaponChargeFraction( unknown )

	.. cpp:function:: unknown GetWeaponChargeTime( unknown )

	.. cpp:function:: unknown HasMod( unknown )

	.. cpp:function:: unknown Anim_HasSequence( unknown )

	.. cpp:function:: unknown SetPlaybackRate( unknown )

	.. cpp:function:: unknown GetWeaponCurrentEnergyCost( unknown )

	.. cpp:function:: unknown Anim_SetStartTime( unknown )

	.. cpp:function:: unknown LerpSkyScale( unknown )

	.. cpp:function:: unknown GetMeleeCanHitHumanSized( unknown )

	.. cpp:function:: unknown GetMeleeCanHitTitans( unknown )

	.. cpp:function:: unknown DoMeleeHitConfirmation( unknown )

	.. cpp:function:: unknown EmitWeaponNpcSound_DontUpdateLastFiredTime( unknown )

	.. cpp:function:: unknown GetDamageAmountForArmorType( unknown )

	.. cpp:function:: unknown GetMeleeAttackRange( unknown )

	.. cpp:function:: unknown GetMeleeLungeTargetRange( unknown )

	.. cpp:function:: unknown SetMods( unknown )

	.. cpp:function:: unknown EmitWeaponNpcSound( unknown )

	.. cpp:function:: unknown GetWeaponDamageFlags( unknown )

	.. cpp:function:: unknown SmartAmmo_IsEnabled( unknown )

	.. cpp:function:: unknown SmartAmmo_GetNumTrackersOnEntity( unknown )

	.. cpp:function:: unknown SmartAmmo_GetTrackedEntities( unknown )

	.. cpp:function:: unknown SmartAmmo_IsVisibleTarget( unknown )

	.. cpp:function:: unknown GetWeaponClass( unknown )

	.. cpp:function:: unknown SetWeaponSkin( unknown )

	.. cpp:function:: unknown FireWeaponGrenade( unknown )

	.. cpp:function:: unknown GetScriptFlags0( unknown )

	.. cpp:function:: unknown ShouldPredictProjectiles( unknown )

	.. cpp:function:: unknown GetScriptTime0( unknown )

	.. cpp:function:: unknown SetScriptTime0( unknown )

	.. cpp:function:: unknown SetPoseParameter( unknown )

	.. cpp:function:: unknown IsReloading( unknown )

	.. cpp:function:: unknown SetForcedADS( unknown )

	.. cpp:function:: unknown EmitWeaponSound_1p3p( unknown )

	.. cpp:function:: unknown GetChargeAnimIndex( unknown )

	.. cpp:function:: unknown PlayWeaponEffectNoCull( unknown )

	.. cpp:function:: unknown RegenerateAmmoReset( unknown )

	.. cpp:function:: unknown SetChargeAnimIndex( unknown )

	.. cpp:function:: unknown SetWeaponPrimaryAmmoCount( unknown )

	.. cpp:function:: unknown StopWeaponEffect( unknown )

	.. cpp:function:: unknown ClearForcedADS( unknown )

	.. cpp:function:: unknown GetReloadMilestoneIndex( unknown )

	.. cpp:function:: unknown GetAmmoPerShot( unknown )

	.. cpp:function:: unknown IsBurstFireInProgress( unknown )

	.. cpp:function:: unknown PlayWeaponEffect( unknown )

	.. cpp:function:: unknown StopWeaponSound( unknown )

	.. cpp:function:: unknown GetSustainedDischargeDuration( unknown )

	.. cpp:function:: unknown SetSustainedDischargeFractionForced( unknown )

	.. cpp:function:: unknown FireWeaponMissile( unknown )

	.. cpp:function:: unknown GetBurstFireShotsPending( unknown )

	.. cpp:function:: unknown AllowUse( unknown )

	.. cpp:function:: unknown RemoveMod( unknown )

	.. cpp:function:: unknown SmartAmmo_GetTargets( unknown )

	.. cpp:function:: unknown SmartAmmo_TrackEntity( unknown )

	.. cpp:function:: unknown EmitWeaponSound( unknown )

	.. cpp:function:: unknown GetWeaponChargeLevel( unknown )

	.. cpp:function:: unknown SetWeaponBurstFireCount( unknown )

	.. cpp:function:: unknown GetCurrentAltFireIndex( unknown )

	.. cpp:function:: unknown ForceRelease( unknown )

	.. cpp:function:: unknown SetWeaponChargeFraction( unknown )

	.. cpp:function:: unknown GetProjectilesPerShot( unknown )

	.. cpp:function:: unknown FireWeaponBolt( unknown )

	.. cpp:function:: unknown IsWeaponInAds( unknown )

	.. cpp:function:: unknown ResetWeaponToDefaultEnergyCost( unknown )

	.. cpp:function:: unknown SetWeaponEnergyCost( unknown )

	.. cpp:function:: unknown FireWeaponBullet( unknown )

	.. cpp:function:: unknown IsWeaponAdsButtonPressed( unknown )

	.. cpp:function:: unknown GetWeaponChargeLevelMax( unknown )

	.. cpp:function:: unknown IsReadyToFire( unknown )

	.. cpp:function:: unknown SetAttackKickRollScale( unknown )

	.. cpp:function:: unknown SetAttackKickScale( unknown )

	.. cpp:function:: unknown GetShotCount( unknown )

	.. cpp:function:: unknown AddMod( unknown )

	.. cpp:function:: unknown FireWeaponBullet_Special( unknown )

	.. cpp:function:: unknown GetWeaponSettingString( unknown )

	.. cpp:function:: unknown GetAttachmentForward( unknown )

	.. cpp:function:: unknown SmartAmmo_UntrackEntity( unknown )

	.. cpp:function:: unknown GetSmartAmmoWeaponType( unknown )

	.. cpp:function:: unknown GetWeaponBurstFireCount( unknown )

	.. cpp:function:: unknown SmartAmmo_Clear( unknown )

	.. cpp:function:: unknown SmartAmmo_GetFirePosition( unknown )

	.. cpp:function:: unknown SmartAmmo_GetStoredTargets( unknown )

	.. cpp:function:: unknown SmartAmmo_StoreTargets( unknown )

	.. cpp:function:: unknown IsSustainedDischargeWeapon( unknown )

	.. cpp:function:: unknown GetDamageSourceID( unknown )

	.. cpp:function:: unknown GetGrenadeFuseTime( unknown )

	.. cpp:function:: unknown SetWeaponPrimaryClipCountAbsolute( unknown )

	.. cpp:function:: unknown GetWeaponUtilityEntity( unknown )

	.. cpp:function:: unknown IsForceRelease( unknown )

	.. cpp:function:: unknown IsWeaponRegenDraining( unknown )

	.. cpp:function:: unknown SetWeaponPrimaryClipCountNoRegenReset( unknown )

CWeaponX
^^^^^^^^

.. cpp:class:: CWeaponX : extends CBaseEntity

	.. cpp:function:: unknown SetFullBodygroup( unknown )

	.. cpp:function:: unknown BecomeRagdoll( unknown )

	.. cpp:function:: unknown Dissolve( unknown )

	.. cpp:function:: unknown Gib( unknown )

	.. cpp:function:: unknown SetContinueAnimatingAfterRagdoll( unknown )

	.. cpp:function:: unknown PlayRecordedAnimation( unknown )

	.. cpp:function:: unknown SetRecordedAnimationPlaybackRate( unknown )

	.. cpp:function:: unknown Anim_EnablePlanting( unknown )

	.. cpp:function:: unknown LookupPoseParameterIndex( unknown )

	.. cpp:function:: unknown SetWeaponUtilityEntity( unknown )

	.. cpp:function:: unknown Anim_DisableUpdatePosition( unknown )

	.. cpp:function:: unknown ForceDryfireEvent( unknown )

	.. cpp:function:: unknown PlayWeaponEffectOnOwner( unknown )

	.. cpp:function:: unknown ForceReleaseFromServer( unknown )

	.. cpp:function:: unknown IsForceReleaseFromServer( unknown )

C_WeaponX
^^^^^^^^^

.. cpp:class:: C_WeaponX : extends C_BaseEntity

	.. cpp:function:: unknown SetGroundEffectTable( unknown )

	.. cpp:function:: unknown GetAttachmentOrigin_ViewModelNoFOVAdjust( unknown )

	.. cpp:function:: unknown Anim_SetPaused( unknown )

	.. cpp:function:: unknown SetCycle( unknown )

	.. cpp:function:: unknown DoBodyGroupChangeScriptCallback( unknown )

	.. cpp:function:: unknown PlayWeaponEffectReturnViewEffectHandle( unknown )

	.. cpp:function:: unknown SetViewmodelAmmoModelIndex( unknown )

CProjectile / C_Projectile
--------------------------

Projectiles.

Shared
^^^^^^

.. cpp:class:: CProjectile / C_Projectile : extends CBaseEntity / C_BaseEntity

	.. cpp:function:: unknown GetAttachmentOrigin( unknown )

	.. cpp:function:: unknown LookupAttachment( unknown )

	.. cpp:function:: unknown GetProjectileWeaponSettingBool( unknown )

	.. cpp:function:: unknown GetProjectileWeaponSettingFloat( unknown )

	.. cpp:function:: unknown FindBodyGroup( unknown )

	.. cpp:function:: unknown GetBodyGroupState( unknown )

	.. cpp:function:: unknown GetProjectileWeaponSettingInt( unknown )

	.. cpp:function:: unknown GetBodyGroupModelCount( unknown )

	.. cpp:function:: unknown SetBodygroup( unknown )

	.. cpp:function:: unknown GetAttachmentAngles( unknown )

	.. cpp:function:: unknown Anim_GetAttachmentAtTime( unknown )

	.. cpp:function:: unknown GetScriptedAnimEventCycleFrac( unknown )

	.. cpp:function:: unknown GetSequenceDuration( unknown )

	.. cpp:function:: unknown Anim_IsActive( unknown )

	.. cpp:function:: unknown Anim_Play( unknown )

	.. cpp:function:: unknown Anim_SetInitialTime( unknown )

	.. cpp:function:: unknown Anim_Stop( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefEntity_Old( unknown )

	.. cpp:function:: unknown GetSkin( unknown )

	.. cpp:function:: unknown LookupSequence( unknown )

	.. cpp:function:: unknown SetSkin( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint_Old( unknown )

	.. cpp:function:: unknown Anim_PlayWithRefPoint( unknown )

	.. cpp:function:: unknown Anim_NonScriptedPlay( unknown )

	.. cpp:function:: unknown ProjectileGetWeaponClassName( unknown )

	.. cpp:function:: unknown Anim_HasSequence( unknown )

	.. cpp:function:: unknown SetPlaybackRate( unknown )

	.. cpp:function:: unknown Anim_SetStartTime( unknown )

	.. cpp:function:: unknown LerpSkyScale( unknown )

	.. cpp:function:: unknown SetImpactEffectTable( unknown )

	.. cpp:function:: unknown SetPoseParameter( unknown )

	.. cpp:function:: unknown ProjectileGetMods( unknown )

	.. cpp:function:: unknown SetProjectilTrailEffectIndex( unknown )

	.. cpp:function:: unknown SetProjectileLifetime( unknown )

	.. cpp:function:: unknown ProjectileGetWeaponInfoFileKeyField( unknown )

	.. cpp:function:: unknown SetReducedEffects( unknown )

	.. cpp:function:: unknown GetAttachmentForward( unknown )

	.. cpp:function:: unknown GetProjectileWeaponSettingAsset( unknown )

	.. cpp:function:: unknown SetVortexRefired( unknown )

	.. cpp:function:: unknown GetProjectileCreationTime( unknown )

	.. cpp:function:: unknown ProjectileGetWeaponInfoFileKeyFieldAsset( unknown )

CProjectile
^^^^^^^^^^^

.. cpp:class:: CProjectile : extends CBaseEntity

	.. cpp:function:: unknown SetFullBodygroup( unknown )

	.. cpp:function:: unknown BecomeRagdoll( unknown )

	.. cpp:function:: unknown Dissolve( unknown )

	.. cpp:function:: unknown Gib( unknown )

	.. cpp:function:: unknown SetContinueAnimatingAfterRagdoll( unknown )

	.. cpp:function:: unknown PlayRecordedAnimation( unknown )

	.. cpp:function:: unknown SetRecordedAnimationPlaybackRate( unknown )

	.. cpp:function:: unknown Anim_EnablePlanting( unknown )

	.. cpp:function:: unknown LookupPoseParameterIndex( unknown )

	.. cpp:function:: unknown ProjectileGetDamageSourceID( unknown )

	.. cpp:function:: unknown Anim_DisableUpdatePosition( unknown )

	.. cpp:function:: unknown ProjectileSetDamageSourceID( unknown )

	.. cpp:function:: unknown SetWeaponClassName( unknown )

	.. cpp:function:: unknown SetProjectileImpactDamageOverride( unknown )

C_Projectile
^^^^^^^^^^^^

.. cpp:class:: C_Projectile : extends C_BaseEntity

	.. cpp:function:: unknown SetGroundEffectTable( unknown )

	.. cpp:function:: unknown GetAttachmentOrigin_ViewModelNoFOVAdjust( unknown )

	.. cpp:function:: unknown Anim_SetPaused( unknown )

	.. cpp:function:: unknown SetCycle( unknown )

	.. cpp:function:: unknown DoBodyGroupChangeScriptCallback( unknown )

CBaseGrenade / C_BaseGrenade
----------------------------

.. note::

	Extends CProjectile. This means methods from CProjectile / C_Projectile are available as well.

Grenades.

Shared
^^^^^^

.. cpp:class:: CBaseGrenade / C_BaseGrenade : extends CProjectile / C_Projectile

	.. cpp:function:: unknown GetDamageRadius( unknown )

	.. cpp:function:: unknown GetExplosionRadius( unknown )

	.. cpp:function:: unknown GrenadeExplode( unknown )

	.. cpp:function:: unknown GetThrower( unknown )

	.. cpp:function:: unknown GrenadeHasIgnited( unknown )

	.. cpp:function:: unknown GrenadeIgnite( unknown )

	.. cpp:function:: unknown SetDoesExplode( unknown )

	.. cpp:function:: unknown InitMagnetic( unknown )

	.. cpp:function:: unknown ExplodeForCollisionCallback( unknown )

	.. cpp:function:: unknown MarkAsAttached( unknown )

CBaseGrenade
^^^^^^^^^^^^

.. cpp:class:: CBaseGrenade : extends CProjectile

	.. cpp:function:: unknown SetGrenadeTimer( unknown )

	.. cpp:function:: unknown SetGrenadeIgnitionDuration( unknown )

C_BaseGrenade
^^^^^^^^^^^^^

.. cpp:class:: C_BaseGrenade : extends C_Projectile

CTitanSoul / C_TitanSoul
------------------------

Shared
^^^^^^

.. cpp:class:: CTitanSoul / C_TitanSoul : extends CBaseEntity / C_BaseEntity

	.. cpp:function:: unknown GetTitan( unknown )

	.. cpp:function:: unknown HasValidTitan( unknown )

	.. cpp:function:: unknown IsDoomed( unknown )

	.. cpp:function:: unknown GetTitanSoulNetFloat( unknown )

	.. cpp:function:: unknown GetInvalidHealthBarEnt( unknown )

	.. cpp:function:: unknown GetTitanSoulNetInt( unknown )

	.. cpp:function:: unknown GetLastRodeoHitTime( unknown )

	.. cpp:function:: unknown IsEjecting( unknown )

	.. cpp:function:: unknown GetStance( unknown )

	.. cpp:function:: unknown GetPlayerSettingsNum( unknown )

	.. cpp:function:: unknown GetCoreChargeExpireTime( unknown )

	.. cpp:function:: unknown GetCoreChargeStartTime( unknown )

	.. cpp:function:: unknown GetNextCoreChargeAvailable( unknown )

CTitanSoul
^^^^^^^^^^

.. cpp:class:: CTitanSoul : extends CBaseEntity

	.. cpp:function:: unknown SetEjecting( unknown )

	.. cpp:function:: unknown SetPlayerSettingsNum( unknown )

	.. cpp:function:: unknown SetStance( unknown )

	.. cpp:function:: unknown SoulDestroy( unknown )

	.. cpp:function:: unknown SetCoreChargeExpireTime( unknown )

	.. cpp:function:: unknown SetTitanSoulNetFloat( unknown )

	.. cpp:function:: unknown SetTitanSoulNetFloatOverTime( unknown )

	.. cpp:function:: unknown GetCoreUseDuration( unknown )

	.. cpp:function:: unknown SetTitanSoulNetInt( unknown )

	.. cpp:function:: unknown SetLastRodeoHitTime( unknown )

	.. cpp:function:: unknown SetCoreChargeStartTime( unknown )

	.. cpp:function:: unknown SetCoreUseDuration( unknown )

	.. cpp:function:: unknown SetNextCoreChargeAvailable( unknown )

C_TitanSoul
^^^^^^^^^^^

.. cpp:class:: C_TitanSoul : extends C_BaseEntity

CBaseCombatCharacter / C_BaseCombatCharacter
--------------------------------------------

Shared
^^^^^^

.. cpp:class:: CBaseCombatCharacter / C_BaseCombatCharacter : extends CBaseEntity / C_BaseEntity

	.. cpp:function:: unknown GetAttachmentOrigin( unknown )

	.. cpp:function:: unknown LookupAttachment( unknown )

	.. cpp:function:: unknown GetTitanSoul( unknown )

	.. cpp:function:: unknown FindBodyGroup( unknown )

	.. cpp:function:: unknown GetBodyGroupState( unknown )

	.. cpp:function:: unknown GetBodyGroupModelCount( unknown )

	.. cpp:function:: unknown SetBodygroup( unknown )

	.. cpp:function:: unknown GetAttachmentAngles( unknown )

	.. cpp:function:: unknown Anim_GetAttachmentAtTime( unknown )

	.. cpp:function:: unknown GetScriptedAnimEventCycleFrac( unknown )

	.. cpp:function:: unknown GetSequenceDuration( unknown )

	.. cpp:function:: unknown Anim_IsActive( unknown )

	.. cpp:function:: unknown Anim_Play( unknown )

	.. cpp:function:: unknown Anim_SetInitialTime( unknown )

	.. cpp:function:: unknown Anim_Stop( unknown )

	.. cpp:function:: unknown ContextAction_ClearBusy( unknown )

	.. cpp:function:: unknown ContextAction_IsActive( unknown )

	.. cpp:function:: unknown ContextAction_IsBusy( unknown )

	.. cpp:function:: unknown ContextAction_SetBusy( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefEntity_Old( unknown )

	.. cpp:function:: unknown GetMainWeapons( unknown )

	.. cpp:function:: unknown GetOffhandWeapon( unknown )

	.. cpp:function:: unknown GetActiveWeapon( unknown )

	.. cpp:function:: unknown GetLatestPrimaryWeapon( unknown )

	.. cpp:function:: unknown GetSkin( unknown )

	.. cpp:function:: unknown LookupSequence( unknown )

	.. cpp:function:: unknown SetSkin( unknown )

	.. cpp:function:: unknown GetAntiTitanWeapon( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint( unknown )

	.. cpp:function:: unknown GetPlayerOrNPCViewVector( unknown )

	.. cpp:function:: unknown Anim_GetStartForRefPoint_Old( unknown )

	.. cpp:function:: unknown Anim_PlayWithRefPoint( unknown )

	.. cpp:function:: unknown Anim_NonScriptedPlay( unknown )

	.. cpp:function:: unknown IsWeaponDisabled( unknown )

	.. cpp:function:: unknown GetActiveWeaponPrimaryAmmoLoaded( unknown )

	.. cpp:function:: unknown ContextAction_IsMeleeExecution( unknown )

	.. cpp:function:: unknown Anim_HasSequence( unknown )

	.. cpp:function:: unknown SetPlaybackRate( unknown )

	.. cpp:function:: unknown GetWeaponAmmoStockpile( unknown )

	.. cpp:function:: unknown Anim_SetStartTime( unknown )

	.. cpp:function:: unknown LerpSkyScale( unknown )

	.. cpp:function:: unknown GetMeleeWeapon( unknown )

	.. cpp:function:: unknown ContextAction_IsMeleeExecutionTarget( unknown )

	.. cpp:function:: unknown GetFirstRodeoRider( unknown )

	.. cpp:function:: unknown GetNumRodeoSlots( unknown )

	.. cpp:function:: unknown GetRodeoRider( unknown )

	.. cpp:function:: unknown PhaseShiftBegin( unknown )

	.. cpp:function:: unknown PhaseShiftCancel( unknown )

	.. cpp:function:: unknown SetPoseParameter( unknown )

	.. cpp:function:: unknown CanUseSharedEnergy( unknown )

	.. cpp:function:: unknown OffsetPositionFromView( unknown )

	.. cpp:function:: unknown AddSharedEnergy( unknown )

	.. cpp:function:: unknown GetSharedEnergyTotal( unknown )

	.. cpp:function:: unknown GetSharedEnergyCount( unknown )

	.. cpp:function:: unknown GetWeaponAmmoLoaded( unknown )

	.. cpp:function:: unknown GetWeaponAmmoMaxLoaded( unknown )

	.. cpp:function:: unknown SetSharedEnergyRegenDelay( unknown )

	.. cpp:function:: unknown GetAttackSpreadAngle( unknown )

	.. cpp:function:: unknown GetOffhandWeapons( unknown )

	.. cpp:function:: unknown GetAttachmentForward( unknown )

	.. cpp:function:: unknown ContextAction_IsLeeching( unknown )

	.. cpp:function:: unknown DisablePhaseShiftFlags( unknown )

	.. cpp:function:: unknown EnablePhaseShiftFlags( unknown )

	.. cpp:function:: unknown GetEntityAtPhaseShiftExitPosition( unknown )

	.. cpp:function:: unknown PhaseShiftTimeRemaining( unknown )

	.. cpp:function:: unknown TakeSharedEnergy( unknown )

CBaseCombatCharacter
^^^^^^^^^^^^^^^^^^^^

.. cpp:class:: CBaseCombatCharacter : extends CBaseEntity

	.. cpp:function:: unknown SetFullBodygroup( unknown )

	.. cpp:function:: unknown BecomeRagdoll( unknown )

	.. cpp:function:: unknown Dissolve( unknown )

	.. cpp:function:: unknown Gib( unknown )

	.. cpp:function:: unknown GetSettingsHeadshotFX( unknown )

	.. cpp:function:: unknown GiveOffhandWeapon( unknown )

	.. cpp:function:: unknown GiveWeapon( unknown )

	.. cpp:function:: unknown SetActiveWeaponByName( unknown )

	.. cpp:function:: unknown TakeOffhandWeapon( unknown )

	.. cpp:function:: unknown TakeWeaponNow( unknown )

	.. cpp:function:: unknown TakeWeapon( unknown )

	.. cpp:function:: unknown GetOutOfBoundsDeadTime( unknown )

	.. cpp:function:: unknown SetContinueAnimatingAfterRagdoll( unknown )

	.. cpp:function:: unknown SetNumRodeoSlots( unknown )

	.. cpp:function:: unknown SetRodeoRider( unknown )

	.. cpp:function:: unknown PlayRecordedAnimation( unknown )

	.. cpp:function:: unknown SetRecordedAnimationPlaybackRate( unknown )

	.. cpp:function:: unknown SetNPCPriorityOverride_NoThreat( unknown )

	.. cpp:function:: unknown Anim_EnablePlanting( unknown )

	.. cpp:function:: unknown SetTitanSoul( unknown )

	.. cpp:function:: unknown LookupPoseParameterIndex( unknown )

	.. cpp:function:: unknown Anim_DisableUpdatePosition( unknown )

	.. cpp:function:: unknown GetPlayerOrNPCViewRight( unknown )

	.. cpp:function:: unknown ResetHealthChangeRate( unknown )

C_BaseCombatCharacter
^^^^^^^^^^^^^^^^^^^^^

.. cpp:class:: C_BaseCombatCharacter : extends C_BaseEntity

	.. cpp:function:: unknown TraceToLocalPlayer( unknown )

	.. cpp:function:: unknown TraceToLocalPlayerSimple( unknown )

	.. cpp:function:: unknown SetGroundEffectTable( unknown )

	.. cpp:function:: unknown GetAttachmentOrigin_ViewModelNoFOVAdjust( unknown )

	.. cpp:function:: unknown Anim_SetPaused( unknown )

	.. cpp:function:: unknown SetCycle( unknown )

	.. cpp:function:: unknown DoBodyGroupChangeScriptCallback( unknown )

CAI_BaseNPC / C_AI_BaseNPC
----------------------------

Shared
^^^^^^

.. cpp:class:: CAI_BaseNPC / C_AI_BaseNPC : extends CBaseCombatCharacter

	.. cpp:function:: unknown Dev_GetAISettingByKeyField( unknown )

	.. cpp:function:: unknown IsInterruptable( unknown )

	.. cpp:function:: unknown GetAIClass( unknown )

	.. cpp:function:: unknown GetBodyType( unknown )

	.. cpp:function:: unknown GetAISettingsName( unknown )

	.. cpp:function:: unknown GetMeleeDamageMaxForTarget( unknown )

	.. cpp:function:: unknown AISetting_MaxFlyingSpeed( unknown )

	.. cpp:function:: unknown AISetting_LeechAnimSet( unknown )

	.. cpp:function:: unknown AISetting_LeechDataKnifeTag( unknown )

CAI_BaseNPC
^^^^^^^^^^^^

.. cpp:class:: CAI_BaseNPC : extends C_BaseCombatCharacter

	.. cpp:function:: unknown AssaultPoint( unknown )

	.. cpp:function:: unknown DisableBehavior( unknown )

	.. cpp:function:: unknown SetThinkEveryFrame( unknown )

	.. cpp:function:: unknown ClearEnemy( unknown )

	.. cpp:function:: unknown SetEnemy( unknown )

	.. cpp:function:: unknown Anim_ScriptedPlay( unknown )

	.. cpp:function:: unknown ForceCheckGroundEntity( unknown )

	.. cpp:function:: unknown GetNPCState( unknown )

	.. cpp:function:: unknown GetMaxEnemyDist( unknown )

	.. cpp:function:: unknown GetMaxEnemyDistHeavyArmor( unknown )

	.. cpp:function:: unknown GetMaxTurretYaw( unknown )

	.. cpp:function:: unknown SetSecondaryEnemy( unknown )

	.. cpp:function:: unknown DisableNPCMoveFlag( unknown )

	.. cpp:function:: unknown EnableNPCMoveFlag( unknown )

	.. cpp:function:: unknown SetAISettings( unknown )

	.. cpp:function:: unknown SetCapabilityFlag( unknown )

	.. cpp:function:: unknown Anim_ScriptedPlayActivityByName( unknown )

	.. cpp:function:: unknown GetEnemy( unknown )

	.. cpp:function:: unknown CanSee( unknown )

	.. cpp:function:: unknown IsCrouching( unknown )

	.. cpp:function:: unknown IsSecondaryAttack( unknown )

	.. cpp:function:: unknown EnableBehavior( unknown )

	.. cpp:function:: unknown GetFollowTarget( unknown )

	.. cpp:function:: unknown InitFollowBehavior( unknown )

	.. cpp:function:: unknown DisableNPCFlag( unknown )

	.. cpp:function:: unknown EnableNPCFlag( unknown )

	.. cpp:function:: unknown Freeze( unknown )

	.. cpp:function:: unknown Unfreeze( unknown )

C_AI_BaseNPC
^^^^^^^^^^^^^

.. cpp:class:: C_AI_BaseNPC : extends C_BaseCombatCharacter