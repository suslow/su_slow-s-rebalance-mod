# suslow's rebalance mod

## 🎯 Overview

No more being forced into the same meta loadouts - now you can enjoy experimenting with different weapon combinations!

## ✨ Key Features

- **26 weapon archetypes rebalanced** - Every weapon type receives meaningful improvements
- **Enhanced turret systems** - All sentries get major upgrades including 90° detection angles and improved rotation speed
- **Better flashlights** - Increased range and improved visibility for all flashlight types  
- **Improved melee combat** - Reduced stamina costs and increased damage for spears and bats
- **Maintained game balance** - Changes preserve the core GTFO experience while expanding viable options

## 🔧 Major Changes

### Assault Rifles & SMGs
- **Auto Rifle**: Damage increased from 2.19 to 3.0, magazine size 30→50
- **Burst Rifle**: Damage boosted from 2.71 to 2.85
- **Heavy SMG**: Damage increased 2.45→2.84, magazine size 33→50, faster reload, piercing limit increased to 3

### Snipers & DMRs  
- **Sniper Rifle**: Magazine size increased 2→3, higher bullet cost for balance
- **DMR**: Damage increased 7.51→8.0, magazine reduced 12→8 for balance

### Sentries (Major Overhaul)
- **All turrets**: Detection angle increased to 90°, rotation speed improved to 10.0
- **Sniper Sentry**: Added piercing bullets, reduced fire delay
- **Burst Sentry**: Added piercing with damage limit of 2
- **Auto Sentry**: Piercing limit increased to 3

### Quality of Life
- **Flashlights**: Range increased across all types (10-30m depending on variant)
- **Melee**: Spear and bat damage increased, stamina costs reduced/eliminated

## 📋 Installation

### Automatic (Recommended)
1. Install via [Thunderstore Mod Manager](https://www.overwolf.com/app/thunderstore-thunderstore_mod_manager) or [r2modman](https://gtfo.thunderstore.io/package/ebkr/r2modman/)
2. Search for "suslow rebalance mod" 
3. Click Install

### Manual Installation
1. Install [BepInEx for GTFO](https://gtfo.thunderstore.io/package/BepInEx/BepInExPack_GTFO/)
2. Install [MTFO](https://gtfo.thunderstore.io/package/dakkhuza/MTFO/) 
3. Download this mod and extract to `BepInEx/plugins/`

## ⚠️ Compatibility

- **Required**: MTFO 4.6.2+
- **Compatible**: Most mods that don't modify the same DataBlocks
- **May conflict**: Other weapon rebalance mods, custom rundowns that modify weapon stats

## 🔄 Complete Changelog

<details>
<summary>Click to expand full changelog</summary>

### Assault Rifles
- **GEAR_Rifle_Semi (Drekker PRES MOD 556 Rifle)**:
  - Magazine increased from 14 to 20
  - Reload time increased from 1.9s to 2.0s
  - Bullet cost increased from 3.8 to 3.83
- **GEAR_Rifle_Burst (Malatack CH 4 Burst Rifle)**:
  - Damage increased from 2.71 to 2.85
  - Bullet cost increased from 1.65 to 1.765
- **GEAR_Rifle_Auto (Malatack LX Assault Rifle)**:
  - Damage increased from 2.1875 to 3.0
  - Stagger damage multiplier reduced from 1.0 to 0.8
  - Precision damage multiplier reduced from 0.8 to 0.78
  - Magazine increased from 30 to 50
  - Reload time increased from 1.8s to 2.4s
  - Bullet cost increased from 1.47 to 2.0
- **GEAR_Rifle_Heavy_Auto_Special (Malatack HXC Heavy Assault Rifle)**:
  - Bullet cost reduced from 1.92 to 1.84

### SMGs
- **GEAR_SMG_Semi (Drekker CLR Short Rifle)**:
  - Fire mode changed from Semi to Burst
  - Damage increased from 4.81 to 7.0
  - Damage falloff start increased from 8.0 to 10.0
  - Bullet cost increased from 1.38 to 2.32
  - Shot delay reduced from 0.04s to 0.01s
  - Burst delay set to 0.15s
  - Burst shot count set to 3
- **GEAR_SMG_Burst (Van Auken LTC5 SMG)**:
  - Damage falloff start reduced from 10.0 to 8.0
  - Damage falloff end reduced from 65.0 to 60.0
- **GEAR_SMG_Heavy_Auto (Accrat ND6 Heavy SMG)**:
  - Damage increased from 2.45 to 2.84
  - Damage falloff start reduced from 7.0 to 6.0
  - Damage falloff end reduced from 60.0 to 55.0
  - Piercing bullets enabled
  - Piercing damage count limit set to 3
  - Precision damage multiplier increased from 0.8 to 0.91
  - Magazine increased from 33 to 50
  - Reload time reduced from 1.55s to 1.4s
  - Bullet cost reduced from 1.5 to 1.3
  - Shot delay reduced from 0.078s to 0.066s

### Snipers & DMRs
- **GEAR_DMR_Semi (TR22 Hanaway DMR)**:
  - Damage increased from 7.51 to 8.0
  - Damage falloff start reduced from 50.0 to 30.0
  - Damage falloff end reduced from 100.0 to 80.0
  - Precision damage multiplier reduced from 0.87 to 0.85
  - Magazine reduced from 12 to 8
  - Reload time increased from 2.3s to 2.4s
  - Bullet cost increased from 5.89 to 10.9
  - Shot delay increased from 0.25s to 0.35s
- **GEAR_Sniper_Semi (Köning PR 11 Sniper Rifle)**:
  - Magazine increased from 2 to 3
  - Bullet cost increased from 17.5 to 23.0

### Shotguns
- **GEAR_Shotgun_Semi (Buckland S870 Shotgun)**:
  - Damage increased from 3.01 to 3.1
  - Damage falloff start increased from 4.0 to 5.0
- **GEAR_Sawed-Off_Shotgun_Semi (Buckland SBS III Sawed-Off Shotgun)**:
  - Damage increased from 3.8 to 3.9
  - Magazine reduced from 4 to 3
- **GEAR_Shotgun_Pump (Buckland Custom K330 Slug Shotgun)**:
  - Bullet cost reduced from 12.0 to 11.5
  - Shot delay reduced from 0.75s to 0.70s
- **GEAR_Shotgun_Choke (Buckland XDIST2 Choke Mod Shotgun)**:
  - Precision damage multiplier reduced from 0.7333 to 0.6
  - Bullet cost increased from 16.3 to 20.6
- **GEAR_Shotgun_DoubleBarrel (Buckland AF6 Combat Shotgun)**:
  - Bullet cost reduced from 10.0 to 9.55

### Bullpup Rifles
- **GEAR_Bullpup_Auto (Accrat Golok DA Bullpup Rifle)**:
  - Damage increased from 2.1 to 2.84
  - Stagger damage multiplier reduced from 1.0 to 0.8
  - Magazine increased from 40 to 45
  - Bullet cost increased from 1.5 to 1.87
  - Shot delay increased from 0.055s to 0.0705s
  - Hip fire spread reduced from 2.5 to 2.0

### Sentries
- **All turrets**:
  - Detection angles increased from 20-40° to 90°
  - Rotation speed increased from 4-8 to 10
- **GEAR_SentryGun_Semi_sniper (Sniper Sentry)**:
  - Damage increased from 48.1 to 50.1
  - Damage falloff start increased from 30.0 to 40.0
  - Bullet cost reduced from 16.0 to 14.5
  - Shot delay reduced from 2.6s to 1.9s
  - Piercing bullets enabled
  - Start fire delay reduced from 2.8s to 0.6s
  - Rotation speed increased from 6.0 to 10.0
  - Detection max angle increased from 20.0 to 90.0
  - Legacy enemy detection enabled
  - Start fire delay tag multiplier increased from 0.5 to 0.8
  - Damage tag multiplier increased from 1.0 to 1.5
  - Stagger damage tag multiplier increased from 1.0 to 2.0
  - Bullet cost tag multiplier reduced from 0.7 to 0.4
  - Shot delay tag multiplier reduced from 0.7 to 0.6
- **GEAR_SentryGun_Burst (Mechatronic SGB3 Burst Sentry)**:
  - Damage falloff start increased from 10.0 to 20.0
  - Damage falloff end increased from 40.0 to 80.0
  - Bullet cost increased from 2.05 to 2.26
  - Burst delay reduced from 1.0s to 0.5s
  - Piercing bullets enabled
  - Piercing damage count limit set to 2
  - Start fire delay reduced from 1.0s to 0.5s
  - Rotation speed increased from 4.0 to 10.0
  - Detection max angle increased from 30.0 to 90.0
  - Legacy enemy detection disabled
  - Start fire delay tag multiplier set to 0.8
  - Rotation speed tag multiplier set to 1.5
  - Damage tag multiplier increased from 1.0 to 1.5
  - Stagger damage tag multiplier increased from 1.0 to 2.0
  - Bullet cost tag multiplier reduced from 1.0 to 0.6
  - Shot delay tag multiplier reduced from 1.0 to 0.8
- **GEAR_SentryGun_Auto_staggering (Rad Labs Meduza HEL Auto Sentry)**:
  - Damage increased from 0.8 to 1.0
  - Damage falloff start increased from 10.0 to 18.0
  - Bullet cost increased from 0.7 to 1.1
  - Piercing damage count limit increased from 2 to 3
  - Start fire delay reduced from 1.0s to 0.5s
  - Rotation speed increased from 4.0 to 10.0
  - Detection max range reduced from 25.0 to 20.0
  - Detection max angle increased from 30.0 to 90.0
  - Start fire delay tag multiplier set to 0.8
  - Damage tag multiplier increased from 1.0 to 2.0
  - Stagger damage tag multiplier increased from 1.0 to 3.0
  - Bullet cost tag multiplier reduced from 1.0 to 0.5
- **GEAR_SentryGun_Shotgun_Semi (Mechatronic B5 LFR Shotgun Sentry)**:
  - Damage reduced from 3.01 to 2.21
  - Stagger damage multiplier increased from 1.0 to 2.0
  - Bullet cost increased from 1.58 to 1.7
  - Piercing bullets enabled
  - Piercing damage count limit set to 2
  - Shotgun bullet count increased from 5 to 10
  - Shotgun bullet spread reduced from 2 to 1
  - Rotation speed increased from 8.0 to 10.0
  - Detection max range increased from 10.0 to 12.0
  - Detection max angle increased from 40.0 to 90.0
  - Force aim towards body enabled
  - Damage tag multiplier increased from 1.0 to 1.5
  - Stagger damage tag multiplier increased from 1.0 to 2.0

### Revolvers
- **GEAR_Revolver_Semi (Bataldo 3RB HEL Revolver)**:
  - Bullet cost increased from 5.74 to 6.2
- **GEAR_Revolver_Semi_Special (Mastaba R66 Revolver)**:
  - Magazine increased from 20 to 21

### Special Weapons
- **GEAR_Special_Semi_HighDamage (Shelling Arid 5 High Caliber Pistol)**:
  - Damage increased from 14.21 to 15.25
- **GEAR_Special_Semi_Precision (Drekker DEL P1 Precision Rifle)**:
  - Bullet cost increased from 10.0 to 10.8
- **GEAR_Special_Semi_Sniper (Drekker DEL P1 Precision Rifle - Thermal Scope)**:
  - Damage falloff start increased from 30.0 to 40.0
  - Damage falloff end increased from 70.0 to 90.0
  - Precision damage multiplier increased from 1.3 to 2.15
  - Magazine increased from 10 to 12
- **GEAR_Special_Semi_Heavy (Shelling Arid-5 High Caliber Pistol)**:
  - Damage increased from 30.1 to 33

### Equipment
- **GunLight_A (Short Range Flashlight)**:
  - Range increased from 8.0 to 10.0
  - Blue color tint increased from 0.731 to 0.831
- **GunLight_E (Medium Range #2 Flashlight)**:
  - Range increased from 13.0 to 15.0
  - Intensity reduced from 0.5 to 0.45
  - Cookie texture changed to "FlashlightRegularCookie_01.tga"
  - Color red changed from 0.86 to 1.0
  - Color green changed from 1.0 to 0.991
  - Color blue changed from 0.988 to 0.933
- **GunLight_B (Medium Range #1 Flashlight)**:
  - Range increased from 15.0 to 16.0
- **GunLight_D (Long Range #1 Flashlight)**:
  - Range increased from 16.0 to 18.0
- **GunLight_C (Long Range #2 Flashlight)**:
  - Range increased from 20.0 to 22.0
- **Consumable_MediumFlashlight (Portable Flashlight)**:
  - Range increased from 25.0 to 30.0
- **Spear**:
  - Light attack damage increased from 2.0 to 2.5
  - Charged attack stamina cost in combat reduced from 0.05 to 0.015
  - Charged attack stamina cost out of combat reduced from 0.05 to 0.015
  - Push stamina cost in combat reduced from 0.05 to 0.015
  - Push stamina cost out of combat reduced from 0.05 to 0.015
- **Bat**:
  - Light attack damage increased from 3.0 to 4.0
  - Light stagger multiplier reduced from 5.0 to 4.0

</details>

## 🐛 Known Issues

- Some weapons may feel overpowered initially - this is intentional to bring them up to viable levels
- Turret improvements may make some sections easier than intended

## 💬 Feedback & Support

Found a bug or have balance suggestions? 
- Open an issue on [GitHub](https://github.com/your-username/gtfo-suslow-rebalance-mod)

## 📄 License

This mod is available under the MIT License.

---

*Made with ❤️ for the GTFO community*