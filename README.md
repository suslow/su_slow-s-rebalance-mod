# suslow's rebalance mod

## 🎯 Overview

No more being forced into the same meta loadouts - now you can enjoy experimenting with different weapon combinations!

## ✨ Key Features

- **26 weapon archetypes rebalanced** - Every weapon type receives meaningful improvements
- **Enhanced turret systems** - All sentries get major upgrades including 70° detection angles and improved rotation speed
- **Better flashlights** - Increased range and improved visibility for all flashlight types  
- **Improved melee combat** - Reduced stamina costs and increased damage for spears and bats
- **Maintained game balance** - Changes preserve the core GTFO experience while expanding viable options

## 📋 Installation

### Automatic (Recommended)
1. Install via [Thunderstore Mod Manager](https://www.overwolf.com/app/thunderstore-thunderstore_mod_manager), [r2modman](https://gtfo.thunderstore.io/package/ebkr/r2modman/) or [Gale](https://thunderstore.io/c/gtfo/p/Kesomannen/GaleModManager/)
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

## Complete Changelog

### **MAIN WEAPONS**

#### **Malatack HXC Heavy Assault Rifle (GEAR_Rifle_Semi | ID: 1)**
- **Magazine Size**: 14 → 20 rounds
- **Reload Time**: 1.9s → 2.0s
- **Ammo Cost**: 3.8 → 3.83

#### **MALATACK CH 4 Burst Rifle (GEAR_Rifle_Burst | ID: 3)**
- **Damage**: 2.71 → 2.85
- **Ammo Cost**: 1.65 → 1.765

#### **Malatack LX Assault Rifle (GEAR_Rifle_Auto | ID: 5)**
- **Damage**: 2.19 → 2.75
- **Magazine Size**: 30 → 50 rounds
- **Reload Time**: 1.8s → 2.4s
- **Ammo Cost**: 1.47 → 2.0
- **Stagger Multiplier**: 1.0 → 1.1
- **Precision Multiplier**: 0.8 → 0.65

#### **ACCRAT ND6 Heavy SMG (GEAR_SMG_Heavy_Auto | ID: 69)**
- **Piercing**: Now pierces through enemies (3 targets max)
- **Damage Falloff**: 10m-65m → 8m-60m range

#### **ACCRAT GOLOK DA Bullpup Rifle (GEAR_Bullpup_Auto | ID: 49)**
- **Damage**: 2.1 → 2.84
- **Magazine Size**: 40 → 45 rounds
- **Fire Rate**: 0.055s → 0.0705s shot delay
- **Ammo Cost**: 1.5 → 1.87
- **Hip Fire Accuracy**: 2.5 → 2.0 spread
- **Stagger Multiplier**: 1.0 → 0.8

#### **BATALDO CUSTOM K330 Slug Shotgun (GEAR_Shotgun_Slug_Semi | ID: 81)**
- **Ammo Cost**: 12.0 → 11.5
- **Fire Rate**: 0.75s → 0.70s shot delay

#### **BUCKLAND SBS III Sawed-off Shotgun (GEAR_Sawed-Off_Shotgun_Semi | ID: 45)**
- **Magazine Size**: 4 → 3 rounds

---

### **SPECIAL WEAPONS**

#### **Drekker CLR Short RifleDrekker CLR Short Rifle (GEAR_SMG_Semi | ID: 17)**
- **Fire Mode**: Semi-Auto → **Burst Fire** (3-round burst)
- **Damage**: 4.81 → 7.0
- **Range**: 8m → 10m effective range
- **Fire Rate**: Significantly increased
- **Ammo Cost**: 1.38 → 2.32
- **Burst Delay**: Added 0.15s between bursts

#### **TR22 HANAWAY DMR (GEAR_DMR_Semi_v2 | ID: 25)**
- **Damage**: 7.51 → 8.0
- **Magazine Size**: 12 → 8 rounds
- **Range**: 50m-100m → 30m-80m effective range
- **Ammo Cost**: 5.89 → 10.9
- **Fire Rate**: 0.25s → 0.35s shot delay
- **Precision Multiplier**: 0.87 → 0.85

#### **KÖNING PR 11 Sniper Rifle (GEAR_Sniper_Semi_v2 | ID: 29)**
- **Magazine Size**: 2 → 3 rounds
- **Ammo Cost**: 17.5 → 23

#### **DREKKER DEL P1 Precision Rifle (GEAR_Precision_Rifle | ID: 79)**
- **Range**: 30m-70m → 40m-90m effective range
- **Magazine Size**: 10 → 12 rounds
- **Precision Multiplier**: 1.3 → 2.15

#### **SHELLING ARID 5 High Caliber Pistol (GEAR_HighCal_Pistol | ID: 80)**
- **Damage**: 30.1 → 33.0

#### **MASTABA R66 Revolver (GEAR_Revolver_Semi_v2 | ID: 37)**
- **Damage**: 14.21 → 15.25

#### **OMNECO LRG HEL Rifle (GEAR_HEL_Rifle_semi | ID: 65)**
- **Ammo Cost**: 10.0 → 10.8

#### **OMNECO EXP1 HEL Gun (GEAR_HEL_Gun - Mechinegun_Semi | ID: 21)**
- **Ammo Cost**: 5.74 → 6.2

#### **TECHMAN ARBALIST V Machine Gun (GEAR_MachineGun_Burst | ID: 22)**
- **Magazine Size**: 20 → 21 rounds

#### **Malatack HXC (GEAR_Rifle_Heavy_Auto_Special | ID: 73)**
- **Ammo Cost**: 1.92 → 1.84

#### **BUCKLAND S870 Shotgun (GEAR_Shotgun_Semi_v2 | ID: 33)**
- **Damage**: 3.01 → 3.1
- **Range**: 4m → 5m effective range

#### **DREKKER INEX DREI Scattergun (GEAR_Scattergun_Semi | ID: 72)**
- **Precision Multiplier**: 0.7333 → 0.6
- **Ammo Cost**: 16.3 → 20.6

#### **BUCKLAND XDIST2 Choke Mod Shotgun (GEAR_Shotgun_Choke_Mod | ID: 34)**
- **Ammo Cost**: 10.0 → 9.55

---

### **EQUIPMENT & TOOLS**

#### **AUTOTEK 51 RSG Sniper Sentry (GEAR_SentryGun_Semi_sniper | ID: 54)**
- **Damage**: 48.1 → 50.1
- **Fire Rate**: 2.6s → 1.9s shot delay
- **Ammo Cost**: 16.0 → 5.8
- **Sentry Tag Cost Multiplier**: 0.4 → 1.0
- **Piercing**: Now pierces through enemies
- **Deployment Speed**: 2.8s → 0.6s
- **Rotation Speed**: 6.0 → 10.0
- **Detection Angle**: 20° → 70°
- **Tag Bonuses**: Significantly improved performance vs tagged enemies

#### **MECHATRONIC SGB3 Burst Sentry (GEAR_SentryGun_Burst | ID: 55)**
- **Range**: 10m-40m → 20m-80m effective range
- **Ammo Cost**: 2.05 → 1.36
- **Sentry Tag Cost Multiplier**: 0.6 → 1.0
- **Piercing**: Now pierces through enemies (2 targets max)
- **Burst Delay**: 1.0s → 0.5s
- **Deployment Speed**: 1.0s → 0.5s
- **Rotation Speed**: 4.0 → 10.0
- **Detection Angle**: 30° → 70°

#### **RAD LABS MEDUZA HEL Auto Sentry (GEAR_SentryGun_Auto_staggering | ID: 57)**
- **Damage**: 0.8 → 1.0
- **Range**: 10m → 18m effective range
- **Ammo Cost**: 0.7 → 0.55
- **Sentry Tag Cost Multiplier**: 0.5 → 1.0
- **Piercing**: 2 → 3 targets max
- **Deployment Speed**: 1.0s → 0.5s
- **Rotation Speed**: 4.0 → 10.0
- **Detection Range**: 25m → 20m
- **Detection Angle**: 30° → 70°

#### **MECHATRONIC B5 LFR Shotgun Sentry (GEAR_SentryGun_Shotgun_Semi | ID: 58)**
- **Damage**: 3.01 → 2.21
- **Stagger Multiplier**: 1.0 → 2.0
- **Ammo Cost**: 1.58 → 0.85
- **Sentry Tag Cost Multiplier**: 0.5 → 1.0
- **Piercing**: Now pierces through enemies (2 targets max)
- **Pellet Count**: 5 → 10 pellets
- **Spread Pattern**: 2 → 1 spread
- **Deployment Speed**: 0.5s
- **Rotation Speed**: 8.0 → 10.0
- **Detection Range**: 10m → 12m
- **Detection Angle**: 40° → 70°

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