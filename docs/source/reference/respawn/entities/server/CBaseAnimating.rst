.. _CBaseAnimating:

CBaseAnimating
==============

.. cpp:class:: CBaseAnimating extends CBaseEntity

    Inherits all properties from :ref:`CBaseEntity <CBaseEntity>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`CProjectile <CProjectile>`
    - :ref:`CFirstPersonProxy <CFirstPersonProxy>`
    - :ref:`CDynamicProp <CDynamicProp>`
    - :ref:`CPlayerDecoy <CPlayerDecoy>`
    - :ref:`CBaseCombatWeapon <CBaseCombatWeapon>`
    - :ref:`CBaseCombatCharacter <CBaseCombatCharacter>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _CBaseAnimating-Anim-IsActive:

    .. cpp:function:: bool Anim_IsActive()

    .. _CBaseAnimating-GetAttachmentForward:

    .. cpp:function:: vector GetAttachmentForward(int attachID)

    .. _CBaseAnimating-Code-Anim-Stop:

    .. cpp:function:: unknown Code_Anim_Stop(unknown)

    .. _CBaseAnimating-Anim-DisableAnimDelta:

    .. cpp:function:: unknown Anim_DisableAnimDelta(unknown)

    .. _CBaseAnimating-Anim-DisableSequenceTransition:

    .. cpp:function:: unknown Anim_DisableSequenceTransition(unknown)

    .. _CBaseAnimating-Anim-EnablePlanting:

    .. cpp:function:: void Anim_EnablePlanting()

    .. _CBaseAnimating-SetPoseParameter:

    .. cpp:function:: void SetPoseParameter(int pose, float offset)

    .. _CBaseAnimating-GetAnimEndPos:

    .. cpp:function:: unknown GetAnimEndPos(unknown)

    .. _CBaseAnimating-Anim-GetStartForRefPoint-Old:

    .. cpp:function:: vector Anim_GetStartForRefPoint_Old(animation, origin, angles)

    .. _CBaseAnimating-ClearDoomed:

    .. cpp:function:: unknown ClearDoomed(unknown)

    .. _CBaseAnimating-Anim-GetStartForRefEntity:

    .. cpp:function:: unknown Anim_GetStartForRefEntity(unknown)

    .. _CBaseAnimating-Anim-NonScriptedPlay:

    .. cpp:function:: void Anim_NonScriptedPlay(string animation)

    .. _CBaseAnimating-DissolveStop:

    .. cpp:function:: unknown DissolveStop(unknown)

    .. _CBaseAnimating-SetDoFaceAnimations:

    .. cpp:function:: unknown SetDoFaceAnimations(unknown)

    .. _CBaseAnimating-PlayRecordedAnimation:

    .. cpp:function:: void PlayRecordedAnimation(asset animation, vector unknown_purpose1, vecor unknown_purpose2, float blendTime, entity ref)

    .. _CBaseAnimating-Anim-Play:

    .. cpp:function:: void Anim_Play(string anim)

    .. _CBaseAnimating-Anim-GetStartForRefEntity-Old:

    .. cpp:function:: vector Anim_GetStartForRefEntity_Old(string anim, vector reference, string optionalTag)

    .. _CBaseAnimating-Anim-GetStartForRefPoint:

    .. cpp:function:: AnimRefPoint Anim_GetStartForRefPoint(string anim, vector origin, vector angles)

    .. _CBaseAnimating-SetPlaybackRate:

    .. cpp:function:: void SetPlaybackRate(float rate)

    .. _CBaseAnimating-GetCycle:

    .. cpp:function:: unknown GetCycle(unknown)

    .. _CBaseAnimating-SetRecordedAnimationPlaybackRate:

    .. cpp:function:: void SetRecordedAnimationPlaybackRate(float rate)

    .. _CBaseAnimating-LerpSkyScale:

    .. cpp:function:: void LerpSkyScale(float skyScale, float time)

    .. _CBaseAnimating-GetAnimEventCycleFrac:

    .. cpp:function:: unknown GetAnimEventCycleFrac(unknown)

    .. _CBaseAnimating-DisableFastPathRendering:

    .. cpp:function:: unknown DisableFastPathRendering(unknown)

    .. _CBaseAnimating-IsDissolving:

    .. cpp:function:: unknown IsDissolving(unknown)

    .. _CBaseAnimating-DissolveNonLethal:

    .. cpp:function:: unknown DissolveNonLethal(unknown)

    .. _CBaseAnimating-Dissolve:

    .. cpp:function:: void Dissolve(int dissolveID, vector normal, int unknown_purpose)

    .. _CBaseAnimating-Gib:

    .. cpp:function:: void Gib(vector forceVec)

    .. _CBaseAnimating-SetContinueAnimatingAfterRagdoll:

    .. cpp:function:: void SetContinueAnimatingAfterRagdoll(bool cont)

    .. _CBaseAnimating-SetRagdollImpactFX:

    .. cpp:function:: unknown SetRagdollImpactFX(unknown)

    .. _CBaseAnimating-GetDecal:

    .. cpp:function:: unknown GetDecal(unknown)

    .. _CBaseAnimating-SetDecal:

    .. cpp:function:: unknown SetDecal(unknown)

    .. _CBaseAnimating-SetCamo:

    .. cpp:function:: unknown SetCamo(unknown)

    .. _CBaseAnimating-GetCamo:

    .. cpp:function:: unknown GetCamo(unknown)

    .. _CBaseAnimating-SetSkin:

    .. cpp:function:: void SetSkin(int skin)

    .. _CBaseAnimating-LookupPoseParameterIndex:

    .. cpp:function:: int LookupPoseParameterIndex(string poseParam)

    .. _CBaseAnimating-Anim-IgnoreParentRotation:

    .. cpp:function:: unknown Anim_IgnoreParentRotation(unknown)

    .. _CBaseAnimating-SequenceTransitionFromEntity:

    .. cpp:function:: unknown SequenceTransitionFromEntity(unknown)

    .. _CBaseAnimating-Anim-SetStartTime:

    .. cpp:function:: void Anim_SetStartTime(float time)

    .. _CBaseAnimating-SetPoseParameterOverTime:

    .. cpp:function:: unknown SetPoseParameterOverTime(unknown)

    .. _CBaseAnimating-Anim-SetInitialTime:

    .. cpp:function:: void Anim_SetInitialTime(float time)

    .. _CBaseAnimating-Anim-EnableUseAnimatedRefAttachmentInsteadOfRootMotion:

    .. cpp:function:: unknown Anim_EnableUseAnimatedRefAttachmentInsteadOfRootMotion(unknown)

    .. _CBaseAnimating-GetSkin:

    .. cpp:function:: int GetSkin()

    .. _CBaseAnimating-FindBodyGroup:

    .. cpp:function:: int FindBodyGroup(string group)

    .. _CBaseAnimating-Anim-GetActivity:

    .. cpp:function:: unknown Anim_GetActivity(unknown)

    .. _CBaseAnimating-SetDoomed:

    .. cpp:function:: unknown SetDoomed(unknown)

    .. _CBaseAnimating-Anim-HasActivity:

    .. cpp:function:: unknown Anim_HasActivity(unknown)

    .. _CBaseAnimating-Anim-HasSequence:

    .. cpp:function:: bool Anim_HasSequence(string animation)

    .. _CBaseAnimating-GetAttachmentOrigin:

    .. cpp:function:: vector GetAttachmentOrigin()

    .. _CBaseAnimating-SetPoseParametersSameAs:

    .. cpp:function:: unknown SetPoseParametersSameAs(unknown)

    .. _CBaseAnimating-GetPoseParameter:

    .. cpp:function:: unknown GetPoseParameter(unknown)

    .. _CBaseAnimating-Anim-Stop:

    .. cpp:function:: void Anim_Stop()

    .. _CBaseAnimating-GetBodyGroupModelCount:

    .. cpp:function:: int GetBodyGroupModelCount(int bodyGroupIndex)

    .. _CBaseAnimating-GetBodyGroupState:

    .. cpp:function:: int GetBodyGroupState(int bodyGroupIndex)

    .. _CBaseAnimating-Anim-DisableUpdatePosition:

    .. cpp:function:: void Anim_DisableUpdatePosition()

    .. _CBaseAnimating-GetFullBodygroup:

    .. cpp:function:: int GetFullBodygroup()

    .. _CBaseAnimating-SetFullBodygroup:

    .. cpp:function:: void SetFullBodygroup(int group)

    .. _CBaseAnimating-IsSequenceFinished:

    .. cpp:function:: unknown IsSequenceFinished(unknown)

    .. _CBaseAnimating-GetAnimDeltas:

    .. cpp:function:: unknown GetAnimDeltas(unknown)

    .. _CBaseAnimating-LookupSequence:

    .. cpp:function:: int LookupSequence(string sequence)

    .. _CBaseAnimating-GetAttachmentAngles:

    .. cpp:function:: vector GetAttachmentAngles()

    .. _CBaseAnimating-LookupAttachment:

    .. cpp:function:: int LookupAttachment(string attachment)

    .. _CBaseAnimating-GetScriptedAnimEventCycleFrac:

    .. cpp:function:: float GetScriptedAnimEventCycleFrac(string anim, string event)

    .. _CBaseAnimating-Anim-GetRefLocalOffset:

    .. cpp:function:: unknown Anim_GetRefLocalOffset(unknown)

    .. _CBaseAnimating-BecomeRagdoll:

    .. cpp:function:: void BecomeRagdoll(vector push, bool skipAnim)

    .. _CBaseAnimating-Anim-PlayWithRefPoint:

    .. cpp:function:: void Anim_PlayWithRefPoint(string animation, vector origin, vector angles, float blendTime)

    .. _CBaseAnimating-Anim-GetAttachmentAtTime:

    .. cpp:function:: Attachment Anim_GetAttachmentAtTime(string animation, string attachmentName, float time)

    .. _CBaseAnimating-SetBodygroup:

    .. cpp:function:: void SetBodygroup(int groupIndex, int newIndex)

    .. _CBaseAnimating-GetSequenceDuration:

    .. cpp:function:: float GetSequenceDuration(string anim)

