.. _C-BaseAnimating:

C_BaseAnimating
===============

.. cpp:class:: C_BaseAnimating extends C_BaseEntity

    Inherits all properties from :ref:`C_BaseEntity <C-BaseEntity>`

    Derived Classes
    ^^^^^^^^^^^^^^^

    - :ref:`C_BaseCombatWeapon <C-BaseCombatWeapon>`
    - :ref:`C_AI_BaseNPC <C-AI-BaseNPC>`
    - :ref:`C_Player <C-Player>`
    - :ref:`C_DynamicProp <C-DynamicProp>`
    - :ref:`C_ScriptProp <C-ScriptProp>`
    - :ref:`C_PlayerDecoy <C-PlayerDecoy>`
    - :ref:`C_Titan_Cockpit <C-Titan-Cockpit>`
    - :ref:`C_FirstPersonProxy <C-FirstPersonProxy>`
    - :ref:`C_Projectile <C-Projectile>`

    Unique Functions
    ^^^^^^^^^^^^^^^^

    .. _C_BaseAnimating-Anim-GetAttachmentAtTime:

    .. cpp:function:: Attachment Anim_GetAttachmentAtTime(string animation, string attachmentName, float time)

    .. _C_BaseAnimating-Anim-GetStartForRefEntity-Old:

    .. cpp:function:: vector Anim_GetStartForRefEntity_Old(string anim, vector reference, string optionalTag)

    .. _C_BaseAnimating-SetDoFaceAnimations:

    .. cpp:function:: unknown SetDoFaceAnimations(unknown)

    .. _C_BaseAnimating-Anim-GetStartForRefPoint-Old:

    .. cpp:function:: vector Anim_GetStartForRefPoint_Old(animation, origin, angles)

    .. _C_BaseAnimating-Anim-IsActive:

    .. cpp:function:: bool Anim_IsActive()

    .. _C_BaseAnimating-Anim-GetStartForRefPoint:

    .. cpp:function:: AnimRefPoint Anim_GetStartForRefPoint(string anim, vector origin, vector angles)

    .. _C_BaseAnimating-MakeSafeForUIScriptHack:

    .. cpp:function:: unknown MakeSafeForUIScriptHack(unknown)

    .. _C_BaseAnimating-SetPlaybackRate:

    .. cpp:function:: void SetPlaybackRate(float rate)

    .. _C_BaseAnimating-SetCycle:

    .. cpp:function:: void SetCycle(float cycle)

    .. _C_BaseAnimating-GetCycle:

    .. cpp:function:: unknown GetCycle(unknown)

    .. _C_BaseAnimating-DoModelChangeScriptCallback:

    .. cpp:function:: unknown DoModelChangeScriptCallback(unknown)

    .. _C_BaseAnimating-GetCamo:

    .. cpp:function:: unknown GetCamo(unknown)

    .. _C_BaseAnimating-GetAnimEventCycleFrac:

    .. cpp:function:: unknown GetAnimEventCycleFrac(unknown)

    .. _C_BaseAnimating-LookupSequence:

    .. cpp:function:: int LookupSequence(string sequence)

    .. _C_BaseAnimating-GetSequenceDuration:

    .. cpp:function:: float GetSequenceDuration(string anim)

    .. _C_BaseAnimating-Anim-IgnoreParentRotation:

    .. cpp:function:: unknown Anim_IgnoreParentRotation(unknown)

    .. _C_BaseAnimating-Anim-SetStartTime:

    .. cpp:function:: void Anim_SetStartTime(float time)

    .. _C_BaseAnimating-Anim-SetInitialTime:

    .. cpp:function:: void Anim_SetInitialTime(float time)

    .. _C_BaseAnimating-GetAttachmentForward:

    .. cpp:function:: vector GetAttachmentForward(int attachID)

    .. _C_BaseAnimating-Anim-EnableUseAnimatedRefAttachmentInsteadOfRootMotion:

    .. cpp:function:: unknown Anim_EnableUseAnimatedRefAttachmentInsteadOfRootMotion(unknown)

    .. _C_BaseAnimating-Anim-HasActivity:

    .. cpp:function:: unknown Anim_HasActivity(unknown)

    .. _C_BaseAnimating-Anim-HasSequence:

    .. cpp:function:: bool Anim_HasSequence(string animation)

    .. _C_BaseAnimating-Anim-SetPaused:

    .. cpp:function:: void Anim_SetPaused(bool pause)

    .. _C_BaseAnimating-Anim-Stop:

    .. cpp:function:: void Anim_Stop()

    .. _C_BaseAnimating-Anim-Play:

    .. cpp:function:: void Anim_Play(string anim)

    .. _C_BaseAnimating-SetGroundEffectTable:

    .. cpp:function:: void SetGroundEffectTable(string tableIdentifier)

    .. _C_BaseAnimating-GetBodyGroupModelCount:

    .. cpp:function:: int GetBodyGroupModelCount(int bodyGroupIndex)

    .. _C_BaseAnimating-GetBodyGroupState:

    .. cpp:function:: int GetBodyGroupState(int bodyGroupIndex)

    .. _C_BaseAnimating-SetBodygroup:

    .. cpp:function:: void SetBodygroup(int groupIndex, int newIndex)

    .. _C_BaseAnimating-FindBodyGroup:

    .. cpp:function:: int FindBodyGroup(string group)

    .. _C_BaseAnimating-GetDecal:

    .. cpp:function:: unknown GetDecal(unknown)

    .. _C_BaseAnimating-SetDecal:

    .. cpp:function:: unknown SetDecal(unknown)

    .. _C_BaseAnimating-LerpSkyScale:

    .. cpp:function:: void LerpSkyScale(float skyScale, float time)

    .. _C_BaseAnimating-SetCamo:

    .. cpp:function:: unknown SetCamo(unknown)

    .. _C_BaseAnimating-GetSkin:

    .. cpp:function:: int GetSkin()

    .. _C_BaseAnimating-SetPoseParameter:

    .. cpp:function:: void SetPoseParameter(int pose, float offset)

    .. _C_BaseAnimating-SetSkin:

    .. cpp:function:: void SetSkin(int skin)

    .. _C_BaseAnimating-IsViewModel:

    .. cpp:function:: unknown IsViewModel(unknown)

    .. _C_BaseAnimating-GetAttachmentAngles:

    .. cpp:function:: vector GetAttachmentAngles()

    .. _C_BaseAnimating-GetAttachmentOrigin:

    .. cpp:function:: vector GetAttachmentOrigin()

    .. _C_BaseAnimating-DoBodyGroupChangeScriptCallback:

    .. cpp:function:: void DoBodyGroupChangeScriptCallback(bool doCallback, int bodygroup)

    .. _C_BaseAnimating-GetHitGroupOfHitBox:

    .. cpp:function:: unknown GetHitGroupOfHitBox(unknown)

    .. _C_BaseAnimating-Anim-GetStartForRefEntity:

    .. cpp:function:: unknown Anim_GetStartForRefEntity(unknown)

    .. _C_BaseAnimating-GetScriptedAnimEventCycleFrac:

    .. cpp:function:: float GetScriptedAnimEventCycleFrac(string anim, string event)

    .. _C_BaseAnimating-Anim-PlayWithRefPoint:

    .. cpp:function:: void Anim_PlayWithRefPoint(string animation, vector origin, vector angles, float blendTime)

    .. _C_BaseAnimating-IsSequenceFinished:

    .. cpp:function:: unknown IsSequenceFinished(unknown)

    .. _C_BaseAnimating-Anim-NonScriptedPlay:

    .. cpp:function:: void Anim_NonScriptedPlay(string animation)

    .. _C_BaseAnimating-GetAttachmentOrigin-ViewModelNoFOVAdjust:

    .. cpp:function:: float GetAttachmentOrigin_ViewModelNoFOVAdjust(int index)

