Weapon Key Values
========================

This document provides a list of various Key Values utilized by weapons and their purposes.

Note that asset values are identical to strings in Key Value files.

These can be modified with KeyValue modding, see here: :doc:`weaponmodding`

The majority of these values are held in ``eWeaponVar`` and can be modified with attachments (named "Mods" in Key Value files).

"\*" will be used to denote values that are not in ``eWeaponVar`` and cannot be modified with attachments.

List of KeyValues
------------------------

``active_crosshair_count``: ``int``. The number of crosshairs to use from the weapon's crosshair list, starting at ``rui_crosshair_index``.

``activitymodifier``: ``string``. Used for certain weapon animations.

``ads_fov_zoomfrac_end``: ``float``. The fraction at which FoV should finish zooming in when aiming down sights.

``ads_fov_zoomfrac_start``: ``float``. The fraction at which FoV should start zooming in when aiming down sights.

``ads_move_speed_scale``: ``float``. Scalar on movement speed when aiming down sights. Does not affect acceleration.

``aimassist_adspull_weaponclass``: ``string``. Determines the aim assist class for aim assist pull on aiming down sights.

- ``none``: No aim assist pull.

- ``broad``, ``broad_sp``: Moderate aim assist pull.

- ``precise``,``precise_sp`` : High aim assist pull.

``aimassist_adspull_zoomEnd``: ``float``. The fraction during aiming down sights at which aim assist pull ends.

``aimassist_adspull_zoomStart``: ``float``. The fraction during aiming down sights at which aim assist pull starts.

``aimassist_disable_ads``: ``bool``. Disables aim assist while aiming down sights.

``aimassist_disable_ads_humansonly``: ``bool``. Disables aim assist on non-heavily armored targets while aiming down sights.

``aimassist_disable_ads_titansonly``: ``bool``. Disables aim assist on heavily armored targets while aiming down sights.

``aimassist_disable_hipfire``: ``bool``. Disables aim assist while not aiming down sights.

``aimassist_disable_hipfire_humansonly``: ``bool``. Disables aim assist on non-heavily armored targets while not aiming down sights.

``aimassist_disable_hipfire_titansonly``: ``bool``. Disables aim assist on heavily armored targets while not aiming down sights.

``allow_empty_fire``: ``bool``. Allows the weapon to fire with no ammo remaining.

``allow_headshots``: ``bool``. Allows the weapon to land headshots on non-heavily armored targets. Does not work on titan weapons.

``alt_fire_anim_count``: ``int``. Used to alternate firing animations on weapons with dual launchers (Flight Core, Salvo Core, etc.)

\* ``alwaysShow``: ``bool``. Unknown.

``ammo_clip_random_loss_on_npc_drop``: ``float``. Random fraction of ammo missing in the clip when dropped by an NPC.

``ammo_clip_random_loss_on_npc_drop_chunksize``: ``int``. Ensures that the ammo remaining in the weapon when dropped by an NPC is divisible by this value.

``ammo_clip_reload_max``: ``int``. Unknown.

``ammo_clip_size``: ``int``. Magazine size.

``ammo_default_total``: ``int``. The total amount of ammo a weapon spawns with, including the magazine.

``ammo_display``: ``string``. Unknown.

``ammo_display_as_clips``: ``bool``. Unknown.

``ammo_drains_to_empty_on_fire``: ``bool``. Forces the weapon's clip to drain to empty over ``fire_duration``.

``ammo_min_to_fire``: ``int``. The minimum amount of ammo needed to fire the weapon.

``ammo_min_to_fire_autoreloads``: ``bool``. Forces a reload when the current ammo is lower than ``ammo_min_to_fire``.

``ammo_no_remove_from_clip``: ``bool``. Enables/disables consuming ammo in the magazine on attack.

- If true while ``ammo_no_remove_from_stockpile`` is false, displays only stockpile ammo on HUD. If both are true, displays infinite ammo.

- If true and magazine size is greater than 0, ammo is not removed from stockpile.

``ammo_no_remove_from_stockpile``: ``bool``. Enables/disables consuming ammo in the stockpile when reloading or on weapons with no magazine.

- If false, displays stockpile ammo on HUD.

``ammo_per_shot``: ``int``. The amount of ammo consumed per shot.

``ammo_size_segmented_reload``: ``int``. The amount of ammo reloaded per segment on weapons with segmented reloads.

``ammo_stockpile_max``: ``int``. The maximum amount of ammo that the stockpile can hold.

``ammo_suck_behavior``: ``string``. Can be ``melee_weapons``, ``offhand_weapons``, or ``primary_weapons``. Use unknown.

``anim_alt_idleAttack``: ``int``. Unknown.

\* ``arc_switch_activator``: ``bool``. Unknown.

``attack_button_presses_ads``: ``bool``. Enables/disables the attack button triggering aim down sights when held.

``attack_button_presses_melee``: ``bool``. Enables/disables the attack button triggering melee.

\* ``battle_chatter_event``: ``string``. Unknown.

\* ``bob_``. A set of values controlling view model bobbing while moving.

``body_skin``: ``int``. Unknown.

\* ``body_type``: ``string``. Unknown.

\* ``bodygroup1_name``: ``string``. The name that body group 1 is tied to.

``bodygroup1_set``: ``bool``. Enables/disables body group 1.

- Distinct values exist for bodygroups up to ``bodygroup10``.

\* ``bodygroup_ads_scope_name``: ``string``. The name that the set of aiming down sights scopes is tied to.

``bodygroup_ads_scope_set``: ``int``. The index of the scope to use from the set while aiming down sights.

``bodygroup_ammo_index_count``: ``int``. The maximum amount of ammo visible on the viewmodel.

``bolt_bounce_frac``: ``float``. Maximum angle fraction from parallel that a bolt can still bounce off a surface at.

``bolt_gravity_enabled``: ``bool``. Enables/disables gravity on bolts fired.

``bolt_hitsize``: ``float``. The hitbox size of bolts.

- Hitbox size does not affect map collisions.
- Not 1:1 with other size measurements.

``bolt_hitsize_grow1_size``: ``float``. The hitbox size the bolt reaches at the grow1 time.

``bolt_hitsize_grow1_time``: ``float``. The time in seconds at which grow1 size is reached.

``bolt_hitsize_grow2_size``: ``float``. The hitbox size the bolt reaches at the grow2 time.

``bolt_hitsize_grow2_time``: ``float``. The time in seconds at which grow2 size is reached.

``bolt_hitsize_growfinal_lerptime``: ``float``. The hitbox size the bolt reaches at the growfinal time.

``bolt_hitsize_growfinal_size``: ``float``. The time in seconds at which growfinal size is reached.

- Time values are absolute from projectile spawn, not cumulative. Later time values must be >= the previous values.

``bounce_effect_table``: ``asset``. The effect table to use when bouncing.

``breaks_cloak``: ``bool``. Enables/disables breaking cloak on attack.

- Note: Does not appear to work for all weapons, such as titan weaponry.

``burst_fire_count``: ``int``. The number of shots fired in a burst.

``burst_fire_delay``: ``float``. The delay after a burst before another burst can be fired.

- Counts from the moment the last shot in a burst is fired.

- Also prevents other actions (e.g. holstering, melee) until finished.

``burst_or_looping_fire_sound_end``: ``string``. Deprecated. Sound effect played at the end of the burst/loop for the user.

``burst_or_looping_fire_sound_end_1p``: ``string``. Sound effect played at the end of the burst/loop for the user.

``burst_or_looping_fire_sound_end_3p``: ``string``. Sound effect played at the end of the burst/loop for others.

``burst_or_looping_fire_sound_end_npc``: ``string``. Sound effect played at the end of the burst/loop for others when an NPC is using the weapon.

``burst_or_looping_fire_sound_middle``: ``string``. Deprecated. Sound effect played on every attack in the burst/loop for the user. Ends on burst/loop end.

``burst_or_looping_fire_sound_middle_1p``: ``string``. Sound effect played on every attack in the burst/loop for the user. Ends on burst/loop end.

``burst_or_looping_fire_sound_middle_3p``: ``string``. Sound effect played on every attack in the burst/loop for others. Ends on burst/loop end.

``burst_or_looping_fire_sound_middle_npc``: ``string``. Sound effect played on every attack in the burst/loop for others when an NPC is using the weapon. Ends on burst/loop end.

``burst_or_looping_fire_sound_start``: ``string``. Deprecated. Sound effect played at the start of the burst/loop for the user.

``burst_or_looping_fire_sound_start_1p``: ``string``. Sound effect played at the start of the burst/loop for the user.

``burst_or_looping_fire_sound_start_3p``: ``string``. Sound effect played at the start of the burst/loop for others.

``burst_or_looping_fire_sound_start_npc``: ``string``. Sound effect played at the start of the burst/loop for others when an NPC is using the weapon.

``bypass_semiauto_hold_protection``: ``bool``. Unknown.

``can_attack_when_dead``: ``bool``. Unknown.

``challeng_req``: ``string``. Unknown.

``challenge_tier``: ``int``. Unknown.

``chance_for_bonus_last_shot_in_clip``: ``float``. Chance to refund a shot while on the last shot in the magazine.

``charge_allow_melee``: ``bool``. Allows the user to melee in the middle of charging the weapon.

``charge_allow_midway_charge``: ``bool``. Unknown.

``charge_cooldown_delay``: ``float``. The time in seconds since last charge before charge begins cooling down.

``charge_cooldown_time``: ``float``. The time in seconds for charge to cooldown to 0 (from full charge).

``charge_drain_sound_1p``: ``string``. Sound effect played to the user when charge begins cooling down.

``charge_drain_sound_3p``: ``string``. Sound effect played to others when charge begins cooling down.

``charge_drain_sound_seek_to_charge_fraction``: ``bool``. Enables/disables setting the starting point of the charge drain sound effect to match the charge fraction.

``charge_drain_sound_stop_when_empty``: ``bool``. Enables/disables stopping the charge drain sound effect when charge is empty.

``charge_effect_1p``: ``string``. The particle effect played to the user when charging.

``charge_effect_3p``: ``string``. The particle effect played to others when charging.

``charge_effect_attachment``: ``string``. The weapon part to attach the charge effect to.

- An additional charge effect can be used under ``charge_effect2``.

``charge_effect_show_during_drain``: ``bool``. Determines whether to show the charge effect while cooling down.

``charge_end_forces_fire``: ``bool``. Forces the weapon to fire once charge is full.

- Always forces fire if ``charge_is_triggered_by_ADS`` is false.

``charge_full_sound_1p``: ``string``. Sound effect played to the user when charge is full.

``charge_full_sound_3p``: ``string``. Sound effect played to others when charge is full.

``charge_is_triggered_by_ADS``: ``bool``. Determines whether charge is triggered by aiming down sights.

- If false, charge is triggered by holding the attack button.
- If false, appears to break other charge systems, such as sound effects and charge level increased callbacks.

``charge_levels``: ``int``. Determines how many equally-spaced charge levels are in the charge (max charge is always the last level).

``charge_maintained_until_fired``: ``bool``. Unknown.

``charge_remain_full_when_fired``: ``bool``. Preserves current charge when the weapon is fired.

``charge_require_input``: ``bool``. Requires the user to hold attack to coninue to charge the weapon. If false, charge continues once triggered.

- Does not work if ``charge_is_triggered_by_ADS`` is true.

``charge_rumble_max``: ``int``. Controls controller rumble at max charge.

``charge_rumble_min``: ``int``. Controls controller rumble at minimum charge.

``charge_sound_1p``: ``string``. Sound effect played to the user when charging begins.

``charge_sound_3p``: ``string``. Sound effect played to the user when charging begins.

``charge_sound_seek_to_charge_fraction``: ``bool``. Enables/disables setting the starting point of the charge sound effect to match the charge fraction.

``charge_sound_stop_when_full``: ``bool``. Enables/disables stopping the charge sound effect when charge is full.

``charge_time``: ``float``. The time in seconds it takes to charge to full (from empty).

\* ``charge_wave_max_count``: ``int``. The number of steps charged wave attacks should take.

\* ``charge_wave_step_dist``: ``float``. The distance each step moves a charged wave attack forward.

\* ``chargeup_time``: ``float``. Additional time added to the active Core meter to account for charge time.

- Total Core meter time is the sum of this and ``core_duration``.

``clear_fx_on_new_view_model``: ``bool``. Unknown.

\* ``clip_bodygroup``: ``string``. The name of the magazine bodygroup to refer to.

\* ``clip_bodygroup_index_shown``: ``bool``. Unknown.

\* ``clip_bodygroup_index_hidden``: ``bool``. Unknown.

\* ``clip_bodygroup_shown_for_milestone_0``: ``bool``. Enables/disables showing the body group during the corresponding reload milestone.

- Additional milestone values exist up to ``clip_bodygroup_shown_for_milestone_4``.

``cooldown_time``: ``float``. The time in seconds after the weapon stops firing before it can fire again.

- Unlike ``fire_rate``, does not prevent other actions.

``cooldown_viewkick_adsScale``: ``float``. Scalar on cooldown recoil when aiming down sights.

``cooldown_viewkick_hardScale``: ``float``. Scalar on cooldown hard recoil, which applies recoil instantly.

``cooldown_viewkick_pitch_base``: ``float``. The base amount of vertical recoil applied when cooldown begins (positive = down).

``cooldown_viewkick_pitch_random``: ``float``. The maximum absolute value of randomness added to base cooldown vertical recoil.

``cooldown_viewkick_pitch_random_innerexclude``: ``float``. Unknown.

- The same values exist for yaw (positive = left)

``cooldown_viewkick_softScale``: ``float``. Scalar on cooldown soft recoil, which applies recoil over time.

``core_build_time``: ``float``. Unused. The number of seconds to build Core.

``core_duration``: ``float``. Duration of the Core in seconds. Does not include Core charge up time.

``critical_hit``: ``bool``. Allows the weapon to land critical hits on heavily armored targets.

``critical_hit_damage_scale``: ``float``. Scalar on critical hit damage.

``crosshair_force_sprint_fade_disabled``: ``float``. Prevents the crosshair from fading when sprinting.

``custom_bool_0``: ``bool``. Utility value with no specific purpose.

``custom_float_0``: ``float``. Utility value with no specific purpose.

``custom_int_0``: ``int``. Utility value with no specific purpose.

- These utility values go up to ``custom_[x]_7``.

``damage_additional_bullets``: ``int``. Has no native use. Used by Railgun in script to add damage per charge.

``damage_additional_bullets_titanarmor``: ``int``. Has no native use. Used by Railgun in script to add heavy armor damage per charge.

``damage_falloff_type``: ``string``. Determines the class of damage falloff to use. Only used by EVA-8.

``damage_far_distance``: ``float``. The distance at which the far damage value is reached.

- If ``headshot_distance`` is not specified, this also acts as the maximum headshot distance.

- Controls maximum range for hitscan shotgun attacks.

- Damage scales linearly between near to far distances and far to very far (if it is used) distances.

``damage_far_value``: ``float``. Damage dealt to non-heavily armored targets at ``damage_far_distance``.

``damage_far_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at ``damage_far_distance``. Optional.

- If unused, ``damage_far_value`` is applied instead.

``damage_flags``: ``int``. The damage flags used by the weapon. Only applies by default; flags be overwritten in script.

``damage_headshot_scale``: ``float``. Scalar on headshot damage.

``damage_heavyarmor_nontitan_scale``: ``float``. Unknown.

``damage_inverse_distance``: ``float``. Distance used alongside ``inverse`` damage falloff type.

``damage_near_distance``: ``float``. The farthest distance at which near damage value is applied.

- Damage scales linearly between near to far distances.

``damage_near_value``: ``float``. Damage dealt to non-heavily armored targets at or below ``damage_near_distance``.

``damage_near_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at or below ``damage_near_distance``. Optional.

- If unused, ``damage_near_value`` is applied instead.

``damage_rodeo``: ``float``. Damage dealt to the enemy titan during Rodeo. Unused normally.

``damage_very_far_distance``: ``float``. The distance at which the very far damage value is reached. Optional.

- If unused, damage does not change after far distance.

``damage_very_far_value``: ``float``. Damage dealt to non-heavily armored targets at or past ``damage_ver_far_distance``. Optional.

``damage_very_far_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at or past ``damage_ver_far_distance``. Optional.

- If unused, ``damage_very_far_value`` is applied instead.

``deploy_time``: ``float``. The time in seconds for the weapon to deploy when swapped to from a main weapon.

``deploycatch_time``: ``float``. Unknown.

``deployfirst_time``: ``float``. Unknown.

``description``: ``string``. Text displayed in weapon flyout descriptions.

``destroy_on_all_ammo_take``: ``bool``. Unknown.

``destroy_on_drop``: ``bool``. Destroys the weapon when dropped, preventing pickup.

\* ``dialog_core_online``: ``string``. Voiceline played when Core is available.

\* ``dialog_core_activated``: ``string``. Voiceline played when Core is activated.

\* ``does_not_interrupt_cloak``: ``bool``. Enables/disables not triggering cloak flickering on toss. (Grenades only)

``dof_nearDepthEnd``: ``float``. Unknown.

``dof_nearDepthStart``: ``float``. Unknown.

``dof_zoom_focusArea_Bottom``: ``float``. Unknown.

``dof_zoom_focusArea_Horizontal``: ``float``. Unknown.

``dof_zoom_focusArea_Top``: ``float``. Unknown.

``dof_zoom_nearDepthEnd``: ``float``. Unknown.

``dof_zoom_nearDepthStart``: ``float``. Unknown.

\* ``empty_reload_only``: ``bool``. Enables/disables allowing reloads only when there is no ammo in the magazine.

``enable_highlight_networking_on_creation``: ``bool``. Unknown.

``explosion_damage``: ``int``. Maximum explosion damage dealt to non-heavily armored targets.

``explosion_damage_flags``: ``int``. Unused. Likely equivalent to ``damage_flags``, but for explosions.

``explosion_damage_heavy_armor``: ``int``. Maximum explosion damage dealt to heavily armored targets. Optional.

- If unused, ``explosion_damage`` is applied instead.

``explosion_damages_owner``: ``bool``. Enables/disables damaging the user with explosions.

``explosion_inner_radius``: ``float``. The distance within which maximum explosion damage is dealt. Optional.

- If unused, assumed to be 0.

``explosion_shake_amplitude``: ``float``. Strength of screen shake caused by explosions.

``explosion_shake_duration``: ``float``. The time in seconds that the explosion screen shake lasts.

``explosion_shake_frequency``: ``float``. Frequency of the explosion screen shake pattern.

``explosion_shake_radius``: ``float``. The radius in which the explosion screen shake applies to enemies.

``explosionradius``: ``float``. The maximum distance within which explosion damage can be dealt.

``fast_swap_to``: ``bool``. Enables/disables fast swap when swapping to the weapon.

\* ``fire_anim_rate``: ``float``. Unknown.

``fire_duration``: ``float``. Duration in seconds that an ability lasts for. Used by offhand weapons.

- Also determines ammo drain time for weapons with ``ammo_drains_to_empty_on_fire`` enabled.

``fire_mode``: ``string``. Determines weapon attack and holster behavior.

- ``auto``, ``full-auto``: Attacks as long as the trigger is held. (Default)

- ``semi-auto``: Attacks once per trigger pull.

- ``offhand``: Swapped to when triggered, attacks as soon as possible, and holsters once fired.

- ``offhand_instant``: Immediately attacks without being swapped to.

- ``offhand_melee``: Used by melee weapons.

- ``offhand_melee_hybrid``: Used by held melee weapons. Triggers a melee attack by attacking with the weapon.

``fire_rate``: ``float``. The fire rate of the weapon in attacks per second.

- For burst weapons, determines the fire rate of the burst.
- For weapons with accelerating fire rate, determines the minimum fire rate.
- Also prevents other actions (e.g. holstering, melee) until the shot cooldown (1/``fire_rate``) has passed.

``fire_rate_max``: ``float``. The maximum fire rate of the weapon in attacks per second. Used for accelerating fire rate.

``fire_rate_max_time_cooldown``: ``float``. The time in seconds for the fire rate to decrease to minimum. Used for accelerating fire rate.

``fire_rate_max_time_speedup``: ``float``. The time in seconds for the fire rate to increase to maximum. Used for accelerating fire rate.

``fire_rate_max_use_ads``: ``bool``. Enables/disables setting fire rate to ``fire_rate_max`` when aiming down sights.

- Disables acceleration defined by ``fire_rate_max_time_cooldown`` and ``fire_rate_max_time_speedup``.

``fire_rumble``: ``string``. Determines the class used for controller rumble.

``fire_sound_1``: ``string``. Deprecated. Sound effect played to user on attack.

``fire_sound_1_npc``: ``string``. Sound effect played to others on NPC attack.

``fire_sound_1_player_1p``: ``string``. Sound effect played to user on attack.

``fire_sound_1_player_3p``: ``string``. Sound effect played to others on attack.

- Additional fire sound effects exist up to ``fire_sound_3``.

``fire_sound_first_shot``: ``string``. Deprecated. Sound effect played for the user on the first attack per trigger pull.

``fire_sound_first_shot_npc``: ``string``. Deprecated. Sound effect played for others on the first attack per trigger pull done by an NPC.

``fire_sound_first_shot_player_1p``: ``string``. Deprecated. Sound effect played for the user on the first attack per trigger pull.

``fire_sound_first_shot_player_3p``: ``string``. Deprecated. Sound effect played for others on the first attack per trigger pull.

- This functionality is done with looping sound effects now.

\* ``flyoutEnabled``: ``bool``. Enables/disables weapon flyouts for this weapon.

``fx_muzzle_flash_attach``: ``string``. The weapon part to attach the muzzle flash effect to.

``fx_muzzle_flash_attach_scoped``: ``string``. The weapon part to attach the muzzle flash effect to while aiming down sights.

``fx_muzzle_flash_view``: ``string``. The muzzle flash effect shown to the user on attack.

``fx_muzzle_flash_world``: ``string``. The muzzle flash effect shown to others on attack.

- An additional muzzle flash effect can be used under ``fx_muzzle_flash2``.

``fx_shell_eject_attach``: ``string``. The weapon part to attach the shell eject effect to.

``fx_shell_eject_attach_scoped``: ``string``. The weapon part to attach the shell eject effect to while aiming down sights.

``fx_shell_eject_view``: ``asset``. The shell eject effect shown to the user on attack.

``fx_shell_eject_world``: ``asset``. The shell eject effect shown to others on attack.

- An additional shell eject effect can be used under ``fx_shell_eject2``.

``gamepad_use_yaw_speed_for_pitch_ads``: ``bool``. Uses yaw sensitivity for pitch sensitivity on controllers (normally, pitch is lower).

\* ``gesture_attack_anim``: ``bool``. Unknown.

``grapple_maxLength``: ``float``. The maximum horizontal length of grapple (x/y axis).

``grapple_maxLengthVert``: ``float``. The maximum vertical length of grapple (z axis).

``grapple_power_required``: ``float``. The minimum amount of power required to use grapple.

``grapple_power_use_rate``: ``float``. The power drained per second while grapple is in use.

``grapple_weapon``: ``bool``. Identifies that the weapon is a grapple.

``grenade_arc_impact_indicator_effect``: ``asset``. The visual effect where the grenade arc indicator touches terrain.

``grenade_arc_indicator_bounce_count``: ``int``. The number of bounces the grenade arc indicator shows.

``grenade_arc_indicator_effect``: ``asset``. The particle effect used to create the grenade arc indicator.

``grenade_arc_indicator_effect_first``: ``asset``. Unknown.

``grenade_arc_indicator_show_from_hip``: ``bool``. Enables/disables the grenade arc indicator to be shown while not aiming down sights.

``grenade_bounce_extra_vertical_randomness``: ``float``. Scalar on the maximum random vertical velocity added to grenade velocity on bounce. (Grenades only)

``grenade_bounce_randomness``: ``float``. Scalar on the maximum random horizontal velocity added to grenade velocity on bounce. (Grenades only)

``grenade_bounce_vel_frac_along_normal``: ``float``. The fraction of velocity preserved when bouncing off a surface parallel to velocity. (Grenades only)

``grenade_bounce_vel_frac_shallow``: ``float``. The fraction of velocity preserved when bouncing off a surface at a shallow angle to velocity. (Grenades only)

``grenade_bounce_vel_frac_sharp``: ``float``. The fraction of velocity preserved when bouncing off a surface at a sharp angle to velocity. (Grenades only)

``grenade_death_drop_velocity_extraUp``: ``float``. The fraction of velocity applied upward when the grenade is released by dying. (Grenades only)

``grenade_death_drop_velocity_scale``: ``float``. The fraction of velocity applied forwards (in current direction) when the grenade is released by dying. (Grenades only)

\* ``grenade_disc_throw``: ``bool``. Unknown.

``grenade_fuse_time``: ``float``. The time in seconds after being pulled out that a grenade will last before exploding. (Grenades only)

``grenade_ignition_time``: ``float``. The time in seconds in time after ignition that a grenade will last before expiring. Ignition is triggered in script. (Grenades only)

``grenade_orient_to_velocity``: ``bool``. Unknown.

``grenade_radius_horizontal``: ``float``. Horizontal distance a grenade will shift by when bouncing horizontally. (Grenades only)

``grenade_radius_vertical``: ``float``. Bonus vertical distance on the grenade hitbox. (Grenades only)

``grenade_roll_vel_frac_per_second``: ``float``. The fraction of velocity preserved per second of rolling. (Grenades only)

\* ``grenade_show_indicator_to_owner``: ``bool``. Enables/disables the nearby grenade indicator for the user on grenades fired.

\* ``headshot_distance``: ``float``. The distance within which headshots can occur. Optional.

- If unused, ``damage_far_distance`` is applied instead.

``hide_holstered_sidearm_when_active``: ``bool``. Hides the holstered weapon while this weapon is active. Primarily used by offhands.

``holster_time``: ``float``. The time in seconds for the weapon to holster when swapping to a main weapon.

- ``burst_fire_delay`` and ``fire_rate`` can cause a weapon to take longer to holster than this time.

``holster_type``: ``string``. Determines where the weapon is holstered on the player model.

``holstermodel``: ``asset``. The weapon viewmodel while holstered.

``hud_icon``: ``string``. The icon shown for the weapon on HUD.

``idle_sound_player_1p``: ``string``. Sound effect played while the weapon is idle.

``ignition_distance``: ``float``. The distance at which the missile is ignited and ``pre_ignition`` values no longer apply. (Missiles only)

``ignition_effect``: ``float``. The visual effect played upon ignition. (Missiles only)

``ignition_sound``: ``float``. The sound effect played upon ignition. (Missiles only)

``impact_effect_table``: ``asset``. The effect table referenced for collisions.

- Includes both visuals and sound effects.

``impulse_force``: ``int``. The impulse force applied on damage.

``impulse_force_explosions``: ``int``. The impulse force applied on explosion damage. (Optional)

- If unused, ``impulse_force`` is applied instead.

``instant_swap_from``: ``bool``. Instantly swaps when swapping from this weapon to another.

``instant_swap_to``: ``bool``. Instantly swaps when swapping to this weapon from another.

``is_burn_mod``: ``bool``. Used to identify Amped attachments and trigger related flags.

\* ``item_flags``: ``int``. Unknown.

\* ``leveled_pickup``: ``bool``. Unknown.

``lifetime_shots_default``: ``int``. Unknown.

``loadout_child_ref``: ``string``. Unknown.

``loadout_parent_ref``: ``string``. Unknown.

``loadout_selectable``: ``bool``. Unknown.

``loadout_type``: ``string``. Unknown.

``looping_sounds``: ``bool``. Enables/disables ``burst_or_looping_fire_sound`` effects.

- Does not disable ``fire_sound`` effects.

``low_ammo_fraction``: ``float``. Unknown.

``low_ammo_sound_name_1``: ``string``. Sound effect played to the user on the last shot in the magazine.

- Additional values exist for the i-th to last shot up to ``low_ammo_sound_name_15``.

``low_ammo_sound_range_name_1``: ``string``. Unknown.

``low_ammo_sound_range_start_1``: ``int``. Unknown.

- Additional values for these exist up to ``low_ammo_sound_range_[x]_3``.

``lower_time``: ``float``. The time in seconds it takes to lower the weapon when swapping to an offhand weapon.

``melee_angle``: ``float``. The angle of the cone used for melee hit detection.

``melee_anim_1p_number``: ``int``. ID used to determine the first person animation of a melee weapon.

``melee_anim_3p``: ``string``. Determines the third person animation of a melee weapon.

``melee_attack_animtime``: ``float``. The time in seconds it takes for the whole first person melee animation to play.

- Also affects the timing of the melee hitbox (both startup and duration).

- Does not change the length of time the user is locked to their melee weapon.

``melee_can_hit_humansized``: ``bool``. Enables/disables the melee weapon to hit non-heavily armored targets.

``melee_can_hit_titans``: ``bool``. Enables/disables the melee weapon to hit heavily armored targets.

``melee_damage``: ``int``. Melee damage dealt to non-heavily armored targets.

``melee_damage_heavyarmor``: ``int``. Melee damage dealt to heavily armored targets.

``melee_freezelook_on_hit``: ``float``. Unknown.

``melee_lunge_target_angle``: ``float``. The angle of the cone used for melee lunge. 

``melee_lunge_target_range``: ``float``. The range of the cone used for melee lunge.

``melee_lunge_time``: ``float``. The time in seconds a melee lunge takes to complete its travel.

``melee_raise_recovery_animtime_normal``: ``float``. Scalar on the time it takes to raise the held weapon after a melee.

``melee_raise_recovery_animtime_quick``: ``float``. Unknown.

``melee_range``: ``float``. The range of the cone used for melee hit detection.

``melee_respect_next_attack_time``: ``bool``. Unknown.

``melee_rumble_on_hit``: ``string``. Determines the class used for controller rumble on melee hit.

``melee_rumble_on_hit_partial``: ``string``. Unknown.

``melee_sound_attack_1p``: ``string``. Sound effect played to the user on melee attack.

``melee_sound_attack_3p``: ``string``. Sound effect played to others on melee attack.

``menu_alt_icon``: ``string``. Unknown.

``menu_icon``: ``string``. Icon shown for this weapon in menus (e.g. loadout screen).

``menu_image``: ``string``. Unknown.

``minimap_reveal_distance``: ``float``. Unknown.

``mod_description``: ``string``. Unknown.

``mod_print_name``: ``string``. Unknown.

``mod_short_print_name``: ``string``. Unknown.

``move_speed_modifier``: ``float``. Scalar on user movement speed.

``move_speed_modifier_when_out_of_ammo``: ``float``. Scalar on user movement speed while the weapon is out of ammo (both stockpile and magazine).

``net_bullet_fix``: ``bool``. Unknown.

\* ``net_optimize``: ``bool``. Used to improve performance of hitscans. Should always be true for hitscan weapons.

- Projectiles fired with this on will have no third person sound effect and will not ping radar.

``never_drop``: ``bool``. Makes the weapon unable to be dropped.

``npc_accuracy_multiplier_heavy_armor``: ``float``. Scalar on NPC accuracy when targeting a heavily armored target. (Higher = better)

``npc_accuracy_multiplier_npc``: ``float``. Scalar on NPC accuracy when targeting a non-heavily armored NPC. (Higher = better)

``npc_accuracy_multiplier_pilot``: ``float``. Scalar on NPC accuracy when targeting a non-heavily armored player. (Higher = better)

``npc_aim_at_feet``: ``bool``. Enables/disables NPCs aiming at the feet of targets.

``npc_aim_at_feet_vs_heavy_armor``: ``bool``. Enables/disables NPCs aiming at the feet of heavily armored targets.

``npc_attack_cone_angle``: ``float``. Unknown.

``npc_burst_secondary``: ``int``. Unknown.

``npc_charge_time_max``: ``float``. Maximum time in seconds that the NPC will charge the weapon for.

``npc_charge_time_min``: ``float``. Minimum time in seconds that the NPC will charge the weapon for.

``npc_clear_charge_if_not_fired``: ``bool``. Enables/disables clearing weapon charge for NPCs if they do not fire when it finishes.

``npc_damage_far_distance``: ``float``. The distance at which the far damage value is reached for NPCs. Optional.

- Controls maximum range for hitscan shotgun attacks.

- Damage scales linearly between near to far distances and far to very far (if it is used) distances.

``npc_damage_far_value``: ``float``. Damage dealt to non-heavily armored targets at ``npc_damage_far_distance`` for NPCs. Optional.

``npc_damage_far_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at ``npc_damage_far_distance`` for NPCs. Optional.

``npc_damage_near_distance``: ``float``. The farthest distance at which near damage value is applied for NPCs. Optional.

- Damage scales linearly between near to far distances.

``npc_damage_near_value``: ``float``. Damage dealt to non-heavily armored targets at or below ``npc_damage_near_distance`` for NPCs. Optional

``npc_damage_near_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at or below ``npc_damage_near_distance`` for NPCs. Optional.

``npc_damage_very_far_distance``: ``float``. The distance at which the very far damage value is reached for NPCs. Optional.

``npc_damage_very_far_value``: ``float``. Damage dealt to non-heavily armored targets at or past ``npc_damage_ver_far_distance`` for NPCs. Optional.

``npc_damage_very_far_value_titanarmor``: ``float``. Damage dealt to heavily armored targets at or past ``npc_damage_ver_far_distance``. Optional.

- For each ``npc_damage`` value, if it is unused, the corresponding player value is applied instead.

``npc_dangerous_to_heavy_armor``: ``bool``. Unknown.

``npc_dangerous_to_normal_armor``: ``bool``. Unknown.

``npc_directed_fire_ang_limit_cos``: ``float``. Unknown.

``npc_explosion_damage``: ``int``. Maximum explosion damage dealt to non-heavily armored targets for NPCs. Optional.

``npc_explosion_damage_heavy_armor``: ``int``. Maximum explosion damage dealt to heavily armored targets for NPCs. Optional.

- For each ``npc_explosion_damage`` value, if it is unused, the corresponding player value is applied instead.

``npc_fire_at_enemy_defense_time``: ``float``. The time in seconds that an NPC will fire at a defensive before holding their shots.

``npc_full_auto_vs_heavy_armor``: ``bool``. Unknown.

``npc_lead_time_max_dist``: ``float``. Unknown.

``npc_lead_time_min_dist``: ``float``. Unknown.

``npc_lead_time_scale``: ``float``. Unknown.

``npc_max_burst``: ``int``. The maximum number of shots an NPC will fire in a burst. Weapon need not be a burst weapon.

``npc_max_engage_range``: ``float``. The maximum range within which an NPC will move towards a non-heavily armored target.

``npc_max_engage_range_heavy_armor``: ``float``. The maximum range within which an NPC will move towards a heavily armored target.

``npc_max_range``: ``float``. The maximum range within which an NPC will attack a target.

``npc_max_range_secondary``: ``float``. Unknown.

``npc_min_burst``: ``int``. The minimum number of shots an NPC will fire in a burst. Weapon need not be a burst weapon.

``npc_min_engage_range``: ``float``. The range within which an NPC will stop moving towards a non-heavily armored target.

``npc_min_engage_range_heavy_armor``: ``float``. The range within which an NPC will stop moving towards a heavily armored target.

``npc_min_range``: ``float``. The minimum range before an NPC will attack a target.

``npc_min_range_secondary``: ``float``. Unknown.

``npc_miss_fast_player``: ``bool``. Unknown.

``npc_pre_fire_delay``: ``float``. Time in seconds before an NPC can fire the weapon once a target is chosen.

``npc_pre_fire_delay_interval``: ``float``. Time in seconds before ``npc_pre_fire_delay`` triggers again.

``npc_reload_enabled``: ``bool``. Allows NPCs to reload the weapon. Optional.

- If unused, ``reload_enabled`` is applied instead.

``npc_rest_time_between_bursts_expedite``: ``float``. Time in seconds before an NPC will fire another burst if staggered during rest time.

``npc_rest_time_between_bursts_max``: ``float``. Maximum time in seconds before an NPC will fire another burst.

``npc_rest_time_between_bursts_min``: ``float``. Minimum time in seconds before an NPC will fire another burst. 

``npc_rest_time_secondary``: ``float``. Unknown.

``npc_self_explosion_safety``: ``bool``. Unknown.

``npc_spread_cone_focus_time``: ``float``. Unknown.

``npc_spread_defocused_cone_multiplier``: ``float``. Unknown.

``npc_spread_pattern_focus_time``: ``float``. Unknown.

``npc_spread_pattern_not_in_fov_factor``: ``float``. Unknown.

``npc_spread_pattern_not_in_fov_time``: ``float``. Unknown.

``npc_suppress_lsp_allowed``: ``bool``. Unknown.

\* ``npc_titan_ability``: ``string``. Unknown.

``npc_use_ads_move_speed_scale``: ``bool``. Unknown.

\* ``npc_use_check_type``: ``string``. Unknown.

``npc_use_long_duration``: ``float``. Unknown.

``npc_use_max_damage``: ``float``. Maximum amount of damage taken before an NPC will use this weapon.

``npc_use_min_damage``: ``float``. Minimum amount of damage taken before an NPC will use this weapon.

``npc_use_min_projectile_damage``: ``float``. Minimum amount of damage taken by projectiles before an NPC will use this weapon.

\* ``npc_use_normal_duration``: ``float``. Time in seconds that an NPC will use this weapon.

``npc_use_short_duration``: ``float``. Unknown.

``npc_use_strict_muzzle_dir``: ``bool``. Unknown.

``npc_vortex_block``: ``bool``. Unknown.

``offhand_blocks_sprint``: ``bool``. Prevents the user from sprinting while this offhand weapon is in use.

``offhand_default_inventory_slot``: ``int``. Determines the inventory slot this offhand is inserted into with the ``give`` cheat command.

``offhand_hold_enabled``: ``bool``. Enables/disables holding the offhand weapon while it is pressed and attacking on release.

``offhand_interupts_weapon_anims``: ``bool``. Enables/disables interrupting any currently active weapon and immediately starting deployment when activating the weapon.

``offhand_switch_force_draw``: ``bool``. Unknown.

``offhand_transition_has_attach_detach_anim_events``: ``bool``. Unknown.

\* ``OnClientAnimEvent``: ``void functionref( entity weapon, string name )``. Unknown. (Client only)

\* ``OnProjectileCollision``: ``void functionref( entity projectile, vector pos, vector normal, entity hitEnt, int hitbox, bool isCritical )``. Callback ran when projectiles collide with terrain or entities.

\* ``OnProjectileIgnite``: ``void functionref( entity projectile )``. Callback ran when grenades ignite.

\* ``OnWeaponActivate``: ``void functionref( entity weapon )``. Callback ran when the weapon becomes active (e.g. when the crosshair becomes visible).

\* ``OnWeaponAttemptOffhandSwitch``: ``bool functionref( entity weapon )``. Callback ran when attempting to switch to an offhand weapon. Returns true if successful or false otherwise.

\* ``OnWeaponChargeBegin``: ``bool functionref( entity weapon )``. Callback ran when charging begins. Returns true if successful or returns false otherwise and denies the charge.

\* ``OnWeaponChargeEnd``: ``void functionref( entity weapon )``. Callback ran when charging ends.

\* ``OnWeaponChargeLevelIncreased``: ``bool functionref( entity weapon )``. Callback ran when charge level increases. Returns true. False conditions unknown.

\* ``OnWeaponCustomActivityStart``: ``void functionref( entity weapon )``. Unknown.

\* ``OnWeaponDeactivate``: ``void functionref( entity weapon )``. Callback ran when the weapon becomes inactive (e.g. when the crosshair disappears)

\* ``OnWeaponNpcPreAttack``: ``void functionref( entity weapon )``. Callback ran when an NPC begins the pre-fire delay. (Server only)

\* ``OnWeaponNpcPrimaryAttack``: ``var functionref( entity weapon, WeaponPrimaryAttackParams attackParams )``. Callback ran when the weapon attacks from an NPC. Returns ammo cost if successful or 0 if not. (Server only)

\* ``OnWeaponOwnerChanged``: ``void functionref( entity weapon, WeaponOwnerChangedParams changeParams )``. Callback ran when the user changes.

\* ``OnWeaponPrimaryAttack``: ``var functionref( entity weapon, WeaponPrimaryAttackParams attackParams )``. Callback ran when the weapon attacks. Returns ammo cost if successful or 0 if not.

\* ``OnWeaponPrimaryAttackAnimEvent``: ``var functionref( entity weapon, WeaponPrimaryAttackParams attackParams )``. Callback ran at a specific point in the weapon's attack animation. Returns ammo cost if successful or 0 if not.

\* ``OnWeaponReadyToFire``: ``void functionref( entity weapon )``. Callback ran when the weapon is ready to fire.

\* ``OnWeaponReload``: ``void functionref( entity weapon, int milestone )``. Callback ran when reload begins. Can have a nonzero milestone if reload was previously interrupted.

\* ``OnWeaponStartZoomIn``: ``void functionref( entity weapon )``. Callback ran when the user starts aiming down sights.

\* ``OnWeaponStartZoomOut``: ``void functionref( entity weapon )``. Callback ran when the user stops aiming down sights.

\* ``OnWeaponSustainedDischargeBegin``: ``bool functionref( entity weapon )``. Callback ran when sustained discharge begins. Returns true if successful or returns false otherwise and denies the sustained discharge.

\* ``OnWeaponSustainedDischargeEnd``: ``void functionref( entity weapon )``. Callback ran when sustained discharge emds.

\* ``OnWeaponTossCancelDrop``: ``void functionref( entity weapon, WeaponPrimaryAttackParams attackParams )``. Callback ran when a toss-able object is dropped by swapping.

\* ``OnWeaponTossPrep``: ``void functionref( entity weapon, WeaponTossPrepParams prepParams )``. Callback ran when a toss-able object is pulled out.

\* ``OnWeaponTossReleaseAnimEvent``: ``void functionref( entity weapon, WeaponPrimaryAttackParams attackParams )``. Callback ran when a toss-able object is released.

\* ``OnWeaponVortexHitBullet``: ``bool functionref( entity weapon, entity vortexSphere, var damageInfo )``. Callback ran when a vortex weapon is hit by a hitscan. Returns true if successful and deletes the bullet or false otherwise.

\* ``OnWeaponVortexHitProjectile``: ``bool functionref( entity weapon, entity vortexSphere, entity attacker, entity projectile, vector contactPos )``. Callback ran when a vortex weapon is hit by a projectile. Returns true if successful and deletes the projectile or false otherwise.

``ordnance_crosshair_always_on_start_index``: ``int``. The index of a crosshair in the weapon's crosshair list to always have on. Used to show cooldowns as Pilot.

``pass_through_damage_preserved_scale``: ``float``. Scalar on damage dealt to following targets after the shot pierces through a target.

``pass_through_depth``: ``float``. The total amount of depth a shot can pierce through, inclusive. 

\* ``passive``: ``string``. Determines what passive to give when the Core weapon starts attacking.

\* ``pickup_hold_prompt``: ``string``. Unknown.

\* ``pickup_press_prompt``: ``string``. Unknown.

\* ``play_offhand_charging_anim``: ``bool``. Enables/disables the standard charging animation of an offhand weapon for others.

\* ``play_offhand_fire_anim``: ``bool``. Unknown.

\* ``play_offhand_start_end_anim``: ``bool``. Unknown.

- Only works for ``PAS_FUSION_CORE``, ``PAS_SHIELD_BOOST``, ``PAS_BERSERKER``, ``PAS_SHIFT_CORE``, and ``PAS_SMART_CORE``.

``playermodel``: ``asset``. Model of the weapon shown to others when held.

``pre_ignition_damage``: ``int``. Damage dealt to non-heavily armored targets before ignition. (Missiles only)

``pre_ignition_damage_titanarmor``: ``int``. Damage dealt to heavily armored targets before ignition. (Missiles only)

``pre_ignition_flight_sound``: ``string``. Sound effect played on missiles in flight before ignition. (Missiles only)

``pre_ignition_impact_effect_table``: ``asset``. The effect table referenced for collisions before ignition. (Missiles only)

- Includes both visuals and sound effects.

``pre_ignition_npc_damage``: ``int``. Damage dealt to non-heavily armored targets before ignition for NPCs. Optional. (Missiles only)

- If unusued, ``pre_ignition_damage`` applies instead.

``pre_ignition_npc_damage_titanarmor``: ``int``. Damage dealt to heavily armored targets before ignition for NPCs. Optional. (Missiles only)

- If unusued, ``pre_ignition_damage_titanarmor`` applies instead.

``pre_ignition_speed``: ``float``. Speed of the missile before ignition. (Missiles only)

``pre_ignition_trail_effect``: ``string``. Trail effect shown on the missile before ignition. (Missiles only)

``primary_fire_does_not_block_sprint``: ``bool``. Allows the main weapon to fire while sprinting.

``printname``: ``string``. Name displayed on the weapon selection screen in loadout creation.

``proficiency_average_additional_rest``: ``float``. Additional rest time between uses for NPCs with average proficiency.

``proficiency_average_bias``: ``float``. Unknown.

``proficiency_average_spreadscale``: ``float``. Scalar on spread for NPCs with average proficiency.

- Additional values exist for ``poor``, ``good``, ``very_good``, and ``perfect`` proficiencies.

``projectile_airburst_on_death``: ``bool``. Unknown.

\* ``projectile_adjust_to_gun_barrel``: ``bool``. Adjusts projectiles to visually launch from the weapon's barrel.

``projectile_chasecamDistanceMax``: ``float``. Unknown.

``projectile_chasecamMaxOrbitDepth``: ``float``. Unknown.

``projectile_chasecamMaxPitchUp``: ``float``. Unknown.

``projectile_chasecamOffsetForward``: ``float``. Forward vector offset of the camera from the projectile in killcams following it.

``projectile_chasecamOffsetRight``: ``float``. Right vector offset of the camera from the projectile in killcams following it.

``projectile_chasecamOffsetUp``: ``float``. Up vector offset of the camera from the projectile in killcams following it.

``projectile_collide_with_owner``: ``bool``. Unknown.

``projectile_collide_with_owner_grace_time``: ``float``. Unknown.

``projectile_damage_reduction_per_bounce``: ``float``. Flat damage reduction per bounce.

- Unaffected by normal damage falloff.

``projectile_damages_owner``: ``bool``. Enables/disables direct hit damage to the user from projectiles fired.

``projectile_death_sound``: ``string``. Unknown.

``projectile_do_predict_impact_effects``: ``bool``. Unknown.

``projectile_drift_intensity``: ``float``. Unknown.

``projectile_drift_windiness``: ``float``. Unknown.

``projectile_first_person_offset_fraction``: ``float``. Adjusts how far projectiles fired travel at an offset angle before straightening in first person.  

``projectile_flight_sound``: ``string``. Sound effect played on projectiles in flight.

``projectile_gravity_scale``: ``float``. Scalar on gravity applied to projectiles.

\* ``projectile_ignore_owner_damage``: ``bool``. Enables/disables owner damage to projectiles fired if they can take damage.

\* ``projectile_ignores_vortex``: ``string``. Determines the bounce behavior of projectiles upon hitting vortex entities and prevents them from being deleted.

- Held vortexes (i.e. Vortex and Thermal Shield) only check for ``fall_vortex`` and still delete projectiles with other values.

- ``mirror``: Reverses horizontal velocity. (``< -1, -1, 1 >``)

- ``drop``: Reverses and reduces horizontal velocity by 75% and sets vertical velocity to 0. (``< -0.25, -0.25, 0 >``)

- ``fall``, ``fall_vortex``: Reverses and reduces all velocity by 75%. (``< -0.25, -0.25, -0.25 >``)

``projectile_inherit_owner_velocity_scale``: ``float``. Scalar on how much of the user's velocity is applied to the projectile when fired.

``projectile_killreplay_enabled``: ``bool``. Allows killcams to follow the projectile that dealt the kill.

``projectile_launch_pitch_offset``: ``float``. Pitch offset projectiles are fired at (positive = up).

``projectile_launch_speed``: ``float``. Base speed of projectiles fired.

``projectile_lifetime``: ``float``. The time in seconds projectiles last before disappearing.

``projectile_max_deployed``: ``int``. The maximum number of projectiles that this weapon can have existing at once. Only works for weapons with tracked projectiles in script.

``projectile_ricochet_max_count``: ``int``. The maximum number of ricochets projectiles can have before disappearing on terrain collision.

``projectile_speed_reduction_factor``: ``float``. The fraction of speed lost by projectiles on ricochet.

``projectile_straight_radius_max``: ``float``. Unknown.

``projectile_straight_radius_min``: ``float``. Unknown.

``projectile_straight_time_max``: ``float``. Unknown.

``projectile_straight_time_min``: ``float``. Unknown.

``projectile_trail_effect_0``: ``asset``. Trail effect shown on projectiles.

- Additional trail effects exist up to ``projectile_trail_effect_4``. 

``projectile_visible_to_smart_ammo``: ``bool``. Allows projectiles to be targeted by smart weapons.

``projectiles_per_shot``: ``int``. Has no native use. Used in script by some weapons to determine the number of projectiles fired per shot.

``raise_from_sprint_time``: ``float``. The time in seconds of the weapon's raise animation after sprinting.

- Not the time before firing is allowed. Animations can allow firing sooner at various fractions of the full raise time.

``raise_time``: ``float``. The time in seconds to raise the weapon when swapping from an offhand weapon.

- Does not include the time to raise the weapon after melee.
- Not the time before firing is allowed. Animations can allow firing sooner at various fractions of the full raise time.

``readyhint``: ``string``. Usage hint text shown to the user in reminders. Used by Cores and inventory offhands (e.g. e-smoke, boosts).

``readymessage``: ``string``. Large text shown to the user in reminders. Used by Cores and inventory offhands (e.g. e-smoke, boosts).

``rechamber_time``: ``float``. The time in seconds to rechamber another round. Use by bolt-action weapons.

- Rechambering only begins after other delays (e.g. ``fire_rate``, ``burst_fire_delay``) are finished.

``red_crosshair_range``: ``float``. The range within which the crosshair will turn red when aiming at an enemy.

``regen_ammo_refill_rate``: ``float``. The rate in ammo per second at which ammo is regenerated in the magazine.

``regen_ammo_refill_start_delay``: ``float``. The time in seconds since last shot fired before ammo regeneration begins.

``regen_ammo_sound_range_name_1``: ``string``. Unknown.

``regen_ammo_sound_range_start_1``: ``int``. Unknown.

- Additional values exist up to ``regen_ammo_sound_range_[x]_3``.

``regen_ammo_stockpile_drain_rate_when_charging``: ``float``. Unknown.

``regen_ammo_stockpile_max_fraction``: ``float``. Unknown.

``regen_ammo_while_firing``: ``bool``. Enables/disables incurring ``regen_ammo_refill_start_delay`` when firing a shot.

``reload_alt_anim``: ``bool``. Enables/disables a flag on certain weapons to use an alternate reload animation.

``reload_enabled``: ``bool``. Allows the weapon to be reloaded.

``reload_is_segmented``: ``bool``. Enables/disables segmented reloads for the weapon.

- Segmented reloads do not have reload milestones.

``reload_no_auto_if_ads_pressed``: ``bool``. Disables automatic reloads when the magazine is empty while aiming down sights.

``reload_time``: ``float``. The time in seconds to complete the reload animation when reloading from a non-empty magazine.

- For segmented reloads, this includes the time to start the reloading animation and load one segment.

``reload_time_late1``: ``float``. The time in seconds to complete the non-empty reload animation from the first reload milestone.

- Additional values exist for the i-th reload milestone up to ``reload_time_late5``.

``reloadempty_time``: ``float``. The time in seconds to complete the reload animation when reloading from an empty magazine.

- For segmented reloads, this includes the time to start the reloading animation and reload one segment.

``reloadempty_time_late1``: ``float``. The time in seconds to complete the empty reload animation from the first reload milestone.

- Additional values exist for the i-th reload milestone up to ``reloadempty_time_late5``.

``reloadsegment_time_end``: ``float``. The time in seconds to complete the end animation of a segmented non-empty reload.

- The end segment does not prevent any actions and ends on sprint.

``reloadsegment_time_loop``: ``float``. The time in seconds to complete one segment reload animation.

``reloadsegmentempty_time_end``: ``float``. The time in seconds to complete the end animation of a segmented empty reload.

- The end segment does not prevent any actions and ends on sprint.

``rui_crosshair_index``: ``int``. The index of a crosshair in the weapon's crosshair list to display. 

\* ``rumble``: ``int``. Unknown.

\* ``scripted_projectile_max_timestep``: ``float``. Unknown.

``shared_energy_charge_cost``: ``int``. Amount of shared energy consumed per frame (60 times per second) while charging.

``shared_energy_cost``: ``int``. Amount of shared energy consumed on attack.

``shortprintname``: ``string``. Name displayed for the weapon in most places (e.g. loadout screen, weapon flyouts, pickups).

\* ``show_grenade_indicator``: ``bool``. Disables the nearby grenade indicator shown to nearby on grenades fired. (Grenades only)

``show_pre_modded_tracer``: ``bool``. Unknown.

``silenced``: ``bool``. Unknown.

``smart_ammo_active_shot_damage_multiplier``: ``float``. Unknown.

``smart_ammo_active_shot_on_first_lock_only``: ``bool``. Unknown.

``smart_ammo_active_shot_time``: ``float``. Unknown.

``smart_ammo_alert_npc_fraction``: ``float``. The fraction of lock on at which NPCs will be alerted of the lock.

``smart_ammo_allow_ads_lock``: ``bool``. Enables/disables smart ammo to lock on while aiming down sights.

``smart_ammo_allow_hip_fire_lock``: ``bool``. Enables/disables smart ammo to lock on while hipfiring.

``smart_ammo_allow_search_while_firing``: ``bool``. Allows smart ammo to lock on while firing.

``smart_ammo_allow_search_while_inactive``: ``bool``. Allows smart ammo to lock on while the weapon is not held.

``smart_ammo_alt_lock_style``: ``bool``. Enables/disables limiting total locks by charge amount (higher = less locks).

``smart_ammo_always_do_burst``: ``bool``. Enables/disables always firing the maximum number of attacks per target.

``smart_ammo_apply_new_target_delay_to_first_target``: ``bool``. Unknown.

\* ``smart_ammo_bounds_search_tick_interval``: ``int``. Unknown.

``smart_ammo_draw_acquisition_lines``: ``bool``. Enables/disables displaying lines to target locks on the HUD.

``smart_ammo_hold_and_reset_after_all_locks``: ``float``. Unknown.

``smart_ammo_hud_lock_style``: ``string``. Determines the type of lock displayed.

``smart_ammo_hud_type``: ``string``. Determines the smart ammo layout displayed on the HUD.

\* ``smart_ammo_humans_only``: ``bool``. Enables/disables targeting only humanoids.

``smart_ammo_lock_effect_1p``: ``asset``. Visual effect displayed on the weapon to the user while acquiring locks.

``smart_ammo_lock_effect_3p``: ``asset``. Visual effect displayed on the weapon to others while acquiring locks.

``smart_ammo_lock_effect_attachment``: ``string``. The weapon part to attach the lock visual effect to.

``smart_ammo_lock_type``: ``string``. Determines which target types the smart ammo can lock.

- ``small``: Non-heavily armored targets.

- ``large``: Heavily armored targets.

- ``any``: Any target.

``smart_ammo_looping_sound_acquiring``: ``string``. Sound effect played while smart ammo is acquiring locks.

``smart_ammo_looping_sound_locked``: ``string``. Sound effect played while smart ammo is locked on to a target.

``smart_ammo_max_targeted_burst``: ``int``. The maximum burst size fired at any individual target.

``smart_ammo_max_targets``: ``int``. The maximum number of targets that can be locked simultaneously.

``smart_ammo_max_trackers_per_target``: ``int``. The maximum number of locks per target.

``smart_ammo_new_target_delay``: ``float``. Time in seconds before the smart weapon can start acquiring locks.

- Time starts from the moment the weapon is swapped to, even if it can't acquire locks due to deploy/raise time.

``smart_ammo_npc_targets_must_be_tracked``: ``bool``. Requires targets to be locked for NPCs to fire the weapon.

``smart_ammo_only_search_on_charge``: ``bool``. Enables/disables limiting lock acquisition to only while the weapon is charging.

``smart_ammo_other_targets_must_be_tracked``: ``bool``. Unknown.

``smart_ammo_player_targets_must_be_tracked``: ``bool``. Requires targets to be locked for players to fire the weapon.

\* ``smart_ammo_points_search_tick_interval``: ``int``. Unknown.

``smart_ammo_search_angle``: ``float``. The angle of the smart ammo search cone. 

``smart_ammo_search_distance``: ``float``. The range of the smart ammo search cone.

``smart_ammo_search_enemy_team``: ``bool``. Unknown.

``smart_ammo_search_friendly_team``: ``bool``. Unknown.

``smart_ammo_search_neutral_team``: ``bool``. Unknown.

``smart_ammo_search_npcs``: ``bool``. Enables/disables smart ammo searching for NPC targets.

``smart_ammo_search_phase_shift``: ``bool``. Unknown.

``smart_ammo_search_players``: ``bool``. Enables/disables smart ammo searching for player targets.

``smart_ammo_stick_to_fully_locked_targets``: ``bool``. Unknown.

``smart_ammo_target_confirmed_sound``: ``string``. Sound effect played when a target is fully locked.

``smart_ammo_target_confirming_sound``: ``string``. Sound effect played when a lock starts to be acquired.

``smart_ammo_target_found_sound``: ``string``. Sound effect played when a new target enters the search cone.

``smart_ammo_target_lost_sound``: ``string``. Sound effect played when locks on a target are lost.

``smart_ammo_target_max_locks_heavy``: ``int``. The maximum number of locks on a heavily armored target.

``smart_ammo_target_max_locks_normal``: ``int``. The maximum number of locks on a non-heavily armored target.

- If unused, acquires locks to deal enough damage to kill the target's in a single burst (up to general maximum locks).

``smart_ammo_target_npc_lock_factor``: ``float``. Unknown.

``smart_ammo_targeting_time_max``: ``float``. The maximum time in seconds it takes to acquire a lock. 

``smart_ammo_targeting_time_max_npc``: ``float``. The maximum time in seconds it takes to acquire a lock on an NPC.

``smart_ammo_targeting_time_min``: ``float``. The minimum time in seconds it takes to acquire a lock.

``smart_ammo_targeting_time_min_npc``: ``float``. The minimum time in seconds it takes to acquire a lock on an NPC.

``smart_ammo_targeting_time_modifier_cloaked``: ``float``. Scalar on lock on time when locking a cloaked target.

``smart_ammo_targeting_time_modifier_projectile``: ``float``. Scalar on lock on time when locking projectiles.

``smart_ammo_targeting_time_modifier_projectile_owner``: ``float``. Scalar on lock on time when locking projectiles from the user.

\* ``smart_ammo_titan_lock_point0``: ``string``. Unknown.

- Additional values for lock point exist up to ``smart_ammo_titan_lock_point7``.

\* ``smart_ammo_titans_block_los``: ``bool``. Enables/disables titans blocking LoS for acquiring locks on other targets.

``smart_ammo_track_cloaked_targets``: ``bool``. Allows smart ammo to lock on to cloaked targets.

``smart_ammo_tracked_targets_check_visibility``: ``bool``. Unknown.

``smart_ammo_tracker_status_effects``: ``bool``. Unknown.

``smart_ammo_unlock_debounce_time``: ``float``. The time in seconds that locks on targets outside the search cone will be retained for before disappearing.

- Does not prevent locks from being cleared by looking too far away from the target.

``smart_ammo_weapon_type``: ``<special>``. Determines the type of smart ammo fired.

- If unused, defaults to hitscan bullets. The only other class is ``homing_missile``.

``sound_dryfire``: ``string``. Sound effect played on offhand weapons when an attempted use or swap fails.

``sound_pickup``: ``string``. Sound effect played when picking up the weapon.

\* ``sound_trigger_pull``: ``string``. Unknown.

``sound_weapon_ready``: ``string``. Sound effect played on offhand weapons when they have reached the next ``ammo_min_to_fire`` multiple.

\* ``special_3p_attack_anim``: ``bool``. Enables/disables playing a non-standard animation for an offhand weapon on charge.

\* ``special_3p_attack_anim_after_charge``: ``bool``. Enables/disables playing a non-standard animation for an offhand weapon after charge ends.

``spread_air_ads``: ``float``. The angle of the shot spread cone while aiming down sights in the air (includes wallrunning).

``spread_air_hip``: ``float``. The angle of the shot spread cone while hipfiring in the air (includes wallrunning).

``spread_crouch_ads``: ``float``. The angle of the shot spread cone while grounded, aiming down sights, and crouching or sliding.

``spread_crouch_hip``: ``float``. The angle of the shot spread cone while grounded, hipfiring, and crouching or sliding

``spread_decay_delay``: ``float``. The time in seconds since last shot fired before spread kick begins to decay.

``spread_decay_rate``: ``float``. The amount of spread kick regressed per second when decaying.

``spread_kick_on_fire_air_ads``: ``float``. The amount spread increases by per shot when aiming down sights in the air (includes wallrunning).

``spread_kick_on_fire_air_hip``: ``float``. The amount spread increases by per shot when hipfiring in the air (includes wallrunning).

``spread_kick_on_fire_crouch_ads``: ``float``. The amount spread increases by per shot when grounded, aiming down sights, and crouching or sliding.

``spread_kick_on_fire_crouch_hip``: ``float``. The amount spread increases by per shot when grounded, hipfiring, and crouching or sliding.

``spread_kick_on_fire_stand_ads``: ``float``. The amount spread increases by per shot when grounded, aiming down sights, and standing or sprinting.

``spread_kick_on_fire_stand_hip``: ``float``. The amount spread increases by per shot when grounded, hipfiring, and standing or sprinting.

``spread_lerp_speed``: ``float``. Unknown.

``spread_max_kick_air_ads``: ``float``. The maximum amount of additional spread kick while aiming down sights in the air (includes wallrunning).

``spread_max_kick_air_hip``: ``float``. The maximum amount of additional spread kick while hipfiring in the air (includes wallrunning).

``spread_max_kick_crouch_ads``: ``float``. The maximum amount of additional spread kick while grounded, aiming down sights, and crouching or sliding.

``spread_max_kick_crouch_hip``: ``float``. The maximum amount of additional spread kick while grounded, hipfiring, and crouching or sliding.

``spread_max_kick_stand_ads``: ``float``. The maximum amount of additional spread kick while grounded, aiming down sights, and standing or sprinting.

``spread_max_kick_stand_hip``: ``float``. The maximum amount of additional spread kick while grounded, hipfiring, and standing or sprinting.

``spread_stand_ads``: ``float``. The angle of the shot spread cone while grounded, aiming down sights, and standing or walking.

``spread_stand_hip``: ``float``. The angle of the shot spread cone while grounded, hipfiring, standing, and not moving.

``spread_stand_hip_run``: ``float``. The angle of the shot spread cone while grounded, hipfiring, standing, and walking.

``spread_stand_hip_sprint``: ``float``. The angle of the shot spread cone while grounded, hipfiring, and sprinting.

``spread_time_to_max``: ``float``. Unknown.

``spread_wallhanging``: ``float``. The angle of the shot spread cone while wallhanging. Optional.

- If unused, ``spread_stand_hip`` is applied instead.

``spread_wallrunning``: ``float``. The angle of the shot spread cone while wallrunning. Optional.

- If unused, ``spread_air`` values are applied instead.

``sprint_fractional_anims``: ``bool``. Unknown.

``sprintcycle_time``: ``float``. Unknown.

``stat_accuracy``: ``int``. The accuracy rating shown on the weapon selection screen in loadout creation.

``stat_damage``: ``int``. The damage rating shown on the weapon selection screen in loadout creation.

``stat_range``: ``int``. The range rating shown on the weapon selection screen in loadout creation.

``stat_rof``: ``int``. The fire rate rating shown on the weapon selection screen in loadout creation.

\* ``stick_pilot``: ``bool``. Enables/disables player entities sticking to projectiles fired.

- Includes player-manned titans.

\* ``stick_titan``: ``bool``. Enables/disables titan entities sticking to projectiles fired.

\* ``stick_npc``: ``bool``. Enables/disables npc entities sticking to projectiles fired.

- Includes npc/auto titans.

``sustained_discharge_allow_melee``: ``bool``. Allows the user to melee in the middle of a sustained discharge.

``sustained_discharge_duration``: ``float``. The time in seconds that a sustained discharge lasts.

``sustained_discharge_pulse_frequency``: ``float``. The number of attacks made per second during a sustained discharge.

``sustained_discharge_require_input``: ``bool``. unknown.

``sustained_discharge_want_pulse_callbacks``: ``bool``. unknown.

``sustained_laser_attachment``: ``string``. The weapon part to attach the sustained laser effect to.

``sustained_laser_effect_1p``: ``asset``. The visual effect shown to the user when the sustained laser attacks.

``sustained_laser_effect_3p``: ``asset``. The visual effect shown to others when the sustained laser attacks.

``sustained_laser_effect_loops``: ``bool``. Enables/disables looping on the sustained laser effects.

``sustained_laser_enabled``: ``bool``. Enables/disables firing the sustained laser on sustained discharge.

``sustained_laser_impact_distance``: ``float``. The minimum distance for ``sustained_laser_impact_effect`` to be applied.

``sustained_laser_impact_effect``: ``asset``. The visual effect shown where the sustained laser impacts terrain.

``sustained_laser_impact_effect_loops``: ``bool``. Enables/disables looping on ``sustained_laser_impact_effect``.

``sustained_laser_new_surface_impact_effect_table``: ``asset``. Unknown.

``sustained_laser_radial_iterations``: ``int``. The number of radial iterations the sustained laser is composed of.

``sustained_laser_radial_step``: ``int``. Scalar on the number of evenly spaced lasers created per radial iteration.

- 1 radial iteration is required for the single center beam.

- Successive iterations generate ``2 ^ (i - 2) * sustained_laser_radial_step`` evenly spaced lasers in a circle, where ``i`` is the current iteration.

  - E.g. 3 iterations and 3 step makes 1 center beam in the 1st iteration, 3 beams in the 2nd iteration, and 6 beams in the 3rd iteration.

``sustained_laser_radius``: ``float``. The radius increase in sustained laser circles as the radial iteration increases.

``sustained_laser_range``: ``float``. The maximum range of the sustained laser.

\* ``sway_``. A large set of values controlling view model sway when held. 

``threat_scope_bounds_height``: ``float``. Used instead of tagname to manually specify threat scope height.

``threat_scope_bounds_tagname1``: ``string``. Determines one corner of the threat scope.

``threat_scope_bounds_tagname2``: ``string``. Determines one corner of the threat scope.

``threat_scope_bounds_width``: ``float``. Used instead of tagname to manually specify threat scope width.

``threat_scope_enabled``: ``bool``. Enables/disables threat scope.

``threat_scope_fadeWithDistance``: ``bool``. Unknown.

``threat_scope_zoomfrac_end``: ``bool``. Unknown.

``threat_scope_zoomfrac_start``: ``bool``. Unknown.

``titanarmor_critical_hit_required``: ``bool``. Enables/disables requiring critical hits to damage titans.

``toss_overhead_time``: ``float``. Unknown.

``toss_pullout_time``: ``float``. The time in seconds to pull out the toss-able object.

``toss_time``: ``float``. The time in seconds to throw the toss-able object.

``tossholdsprintcycle_time``: ``float``. Unknown.

``tracer_effect``: ``asset``. Tracer effect shown to others when a hitscan shot is fired.

``tracer_effect_first_person``: ``asset``. Tracer effect shown to the user when a hitscan shot is fired.

\* ``trap_warning_enemy_fx``: ``asset``. Has no native use. The visual effect shown to enemy players when a trap light effect is played on projectiles.

\* ``trap_warning_friendly_fx``: ``asset``. Has no native use. The visual effect shown to allied players when a trap light effect is played on projectiles.

\* ``trigger_snipercam``: ``bool``. Unknown.

``ui1_draw_cloaked``: ``bool``. Enables/disables showing ui element 1 while cloaked.

``ui1_enable``: ``bool``. Enables/disables showing ui element 1.

- Additional values exist for ui elements up to ``ui8``.

``viewdrift_ads_air_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when aiming down sights in the air. 

``viewdrift_ads_air_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when aiming down sights in the air. 

``viewdrift_ads_crouch_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when grounded, aiming down sights, and crouched or sliding. 

``viewdrift_ads_crouch_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when grounded, aiming down sights, and crouched or sliding.

``viewdrift_ads_speed_pitch``: ``float``. Scalar on how quickly pitch viewdrift shifts while aiming down sights. 

``viewdrift_ads_speed_yaw``: ``float``. Scalar on how quickly yaw viewdrift shifts while aiming down sights.

``viewdrift_ads_stand_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when grounded, aiming down sights, and standing or sprinting.

``viewdrift_ads_stand_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when grounded, aiming down sights, and standing or sprinting.

``viewdrift_hipfire_air_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when hipfiring in the air. 

``viewdrift_hipfire_air_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when hipfiring in the air. 

``viewdrift_hipfire_crouch_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when grounded, hipfiring, and crouched or sliding. 

``viewdrift_hipfire_crouch_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when grounded, hipfiring, and crouched or sliding. 

``viewdrift_hipfire_speed_pitch``: ``float``. Scalar on how quickly pitch viewdrift shifts while hipfiring. 

``viewdrift_hipfire_speed_yaw``: ``float``. Scalar on how quickly yaw viewdrift shifts while hipfiring. 

``viewdrift_hipfire_stand_scale_pitch``: ``float``. The maximum absolute value pitch the user view will drift by when grounded, hipfiring, and standing or sprinting. 

``viewdrift_hipfire_stand_scale_yaw``: ``float``. The maximum absolute value yaw the user view will drift by when grounded, hipfiring, and standing or sprinting. 

``viewkick_ads_weaponFraction``: ``float``. Scalar on how much the weapon/reticle recoils separate from viewpoint while aiming down sights (i.e. how much your viewpoint counters the recoil).

``viewkick_ads_weaponFraction_vmScale``: ``float``. Scalar on how much the weapon viewmodel recoils while aiming down sights.

``viewkick_air_scale_ads``: ``float``. Scalar on recoil generated while aiming down sights when the user is not grounded (includes wallrunning).

``viewkick_duck_scale``: ``float``. Scalar on recoil generated while crouching.

``viewkick_hipfire_weaponFraction``: ``float``. Scalar on how much the weapon/reticle recoils separate from viewpoint while hipfiring (i.e. how much your viewpoint counters the recoil).

``viewkick_hipfire_weaponFraction_vmScale``: ``float``. Scalar on how much the weapon viewmodel recoils while hipfiring.

``viewkick_hover_scale``: ``float``. Scalar on recoil generated while using pilot Hover.

``viewkick_move_scale``: ``float``. Scalar on recoil generated while moving.

``viewkick_perm_pitch_base``: ``float``. The base amount of vertical recoil (positive = down). Unaffected by ``viewkick_spring``.

``viewkick_perm_pitch_random``: ``float``. The maximum absolute value of randomness added to base vertical recoil. Unaffected by ``viewkick_spring``.

``viewkick_perm_pitch_random_innerexclude``: ``float``. Unknown.

``viewkick_pitch_base``: ``float``. The base amount of vertical recoil (positive = down).

``viewkick_pitch_random``: ``float``. The maximum absolute value of randomness added to base vertical recoil.

``viewkick_pitch_softScale``: ``float``. Scalar on soft vertical recoil, which applies recoil over time.

``viewkick_pitch_hardScale``: ``float``. Scalar on hard vertical recoil, which applies recoil instantly.

- The same values exist for yaw (positive = left)

``viewkick_roll_base``: ``float``. The absolute value base amount of roll.

``viewkick_roll_hardScale``: ``float``. Scalar on hard roll recoil.

``viewkick_roll_randomMax``: ``float``. The maximum amount of random roll added to base roll.

``viewkick_roll_randomMin``: ``float``. The minimum amount of random roll added to base roll.

``viewkick_roll_softScale``: ``float``. Scalar on soft roll recoil. Appears to simply be weaker than hard roll recoil.

- Roll values are unaffected by other scalars, such as ``viewkick_scale`` and ``weaponFraction``.

``viewkick_scale_min_hipfire``: ``float``. Scalar on recoil generated when hipfiring at minimum LERP.

``viewkick_scale_max_hipfire``: ``float``. Scalar on recoil generated when hipfiring at maximum LERP.

``viewkick_scale_min_ads``: ``float``. Scalar on recoil generated when aiming down sights at minimum LERP.

``viewkick_scale_max_ads``: ``float``. Scalar on recoil generated when aiming down sights at maximum LERP.

``viewkick_scale_valuePerShot``: ``float``. How much each shot advances the LERP.

``viewkick_scale_valueLerpStart``: ``float``. The minimum value for the LERP.

``viewkick_scale_valueLerpEnd``: ``float``. The maximum value for the LERP.

``viewkick_scale_valueDecayDelay``: ``float``. The time in seconds since last shot fired before LERP begins to decay.

``viewkick_scale_valueDecayRate``: ``float``. The amount of LERP regressed per second when decaying.

``viewkick_spring``: ``string``. Specifies the class of viewkick spring, which dampens recoil above certain values.

``viewmodel``: ``asset``. The model of the weapon shown to the user when held.

``viewmodel_offset_ads``: ``vector``. The position offset of the viewmodel while aiming down sights.

``viewmodel_offset_hip``: ``vector``. The position offset of the viewmodel while hipfiring.

\* ``viewpunch_multiplier``: ``float``. Unknown.

``vortex_absorb_effect``: ``asset``. Shot model shown to the vortex user when a vortex weapon catches this weapon's shot.

``vortex_absorb_effect_third_person``: ``asset``. Shot model shown to others when a vortex weapon catches this weapon's shot.

\* ``vortex_absorb_sound``: ``string``. Sound effect played to the vortex user when a vortex weapon catches this weapon's shot. 

\* ``vortex_absorb_sound_1p_vs_3p``: ``string``. Sound effect played to others when a vortex weapon catches this weapon's shot.

``vortex_drain``: ``float``. Fraction of charge taken from vortex weapons that catch a shot from this weapon.

- If caught by Ion's Vortex, drains a fraction of her energy instead.

``vortex_impact_effect``: ``asset``. The impact effect table referenced for vortex collisions.

- Vortex collisions refers to standard blocking vortex entities, such as Particle Wall and Gun Shield.

\* ``vortex_refire_behavior``: ``string``. Defines the behavior for this weapon's projectiles when caught/reflected by Vortex shield.

- ``absorb``: Disappears when caught.

- ``bullet``: High speed (12000) and slightly higher than moderate spread.

- ``explosive_round``: Moderate speed (8000) and moderate spread.

- ``rocket``: Low speed (1800) and low spread.

- ``grenade``: Low speed (1500) and high spread with 1.25s fuse time.

- ``grenade_long_fuse``: Low speed (1500) and high spread with 10s fuse time.

\* ``wave_max_count``: ``int``. The number of steps wave attacks should take.

\* ``wave_step_dist``: ``float``. The distance each step moves a wave attack forward.

\* ``weaponClass``: ``string``. Determines the type of entity that normally uses the weapon.

- ``human``: Humanoid entities.

- ``titan``: Titans.

- ``other``: Anything else (e.g. heavily armored NPCs, turrets)

\* ``weaponSubClass``: ``string``. Unknown.

- Takes ``rifle``, ``smg``, ``lmg``, ``sidearm``, ``sniper``, ``projectile_shotgun``, ``rocket``, ``shotgun``, or ``autolock``.

\* ``weaponType``: ``string``. Determines the type of offhand the weapon is. (Offhands/melees only)

- ``melee``: Melee weapon.

- ``shoulder``: Offhand pulled from the shoulder used as an offensive ability. (Excluding Energy Siphon)

- ``defense``: Held or instant offhand used as a defensive ability.

- ``tactical``: Held or instant offhand used as a utility ability. (Excluding Tether Trap)

- ``titan_core``: Titan Core weapon.

- ``anti_titan``: Turret weapon.

``zoom_angle_shift_pitch``: ``float``. Unknown.

``zoom_angle_shift_yaw``: ``float``. Unknown.

``zoom_effects``: ``bool``. Unknown.

``zoom_fov``: ``float``. The FoV the weapon will zoom to when aiming down sights.

- Affected by custom player FoV scale. Effectively zooms to ``( zoom FoV / base FoV * player FoV scale )``

- Base FoV is 70 for pilots and 75 for titans.

``zoom_fov_viewmodel``: ``float``. Unknown.

``zoom_scope_frac_end``: ``float``. Unknown.

``zoom_scope_frac_start``: ``float``. Unknown.

``zoom_time_in``: ``float``. The time in seconds to fully zoom in from hipfire.

``zoom_time_out``: ``float``. The time in seconds to fully zoom out from aiming down sights.

``zoom_toggle_fov``: ``float``. The FoV the weapon will zoom to when aiming down sights with a zoom toggle on.

``zoom_toggle_lerp_time``: ``float``. The time in seconds for toggleable zoom to change zoom FoV.

``zoomfrac_autoattack``: ``float``. The fraction of zoom above which the weapon will continually attack.