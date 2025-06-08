# su_slow's rebalance mod

## Изменения в архетипах оружия

### 1. GEAR_Rifle_Semi (Drekker PRES MOD 556 Rifle)
- **DefaultClipSize**: Увеличен с 14 до 20
- **DefaultReloadTime**: Увеличен с 1.9 до 2.0
- **CostOfBullet**: Увеличен с 3.8 до 3.83

### 2. GEAR_Rifle_Burst (Malatack CH 4 Burst Rifle)
- **Damage**: Увеличен с 2.71 до 2.85
- **CostOfBullet**: Увеличен с 1.65 до 1.765

### 3. GEAR_Rifle_Auto (Malatack LX Assault Rifle)
- **Damage**: Увеличен с 2.1875 до 3.0
- **StaggerDamageMulti**: Уменьшен с 1.0 до 0.8
- **PrecisionDamageMulti**: Уменьшен с 0.8 до 0.78
- **DefaultClipSize**: Увеличен с 30 до 50
- **DefaultReloadTime**: Увеличен с 1.8 до 2.4
- **CostOfBullet**: Увеличен с 1.47 до 2.0

### 4. GEAR_Rifle_Heavy_Auto_Special (Malatack HXC Heavy Assault Rifle)
- **CostOfBullet**: Уменьшен с 1.92 до 1.84

### 5. GEAR_SMG_Semi (Drekker CLR Short Rifle → преобразован в Burst)
- **FireMode**: Изменён с 0 (Semi) на 1 (Burst)
- **Damage**: Увеличен с 4.81 до 7.0
- **DamageFalloff.x**: Увеличен с 8.0 до 10.0
- **CostOfBullet**: Увеличен с 1.38 до 2.32
- **ShotDelay**: Уменьшен с 0.04 до 0.01
- **BurstDelay**: Установлен на 0.15
- **BurstShotCount**: Установлен на 3

### 6. GEAR_SMG_Burst (Van Auken LTC5 SMG)
- **DamageFalloff.x**: Уменьшен с 10.0 до 8.0
- **DamageFalloff.y**: Уменьшен с 65.0 до 60.0

### 7. GEAR_SMG_Heavy_Auto (Accrat ND6 Heavy SMG)
- **Damage**: Увеличен с 2.45 до 2.84
- **DamageFalloff.x**: Уменьшен с 7.0 до 6.0
- **DamageFalloff.y**: Уменьшен с 60.0 до 55.0
- **PrecisionDamageMulti**: Увеличен с 0.8 до 0.91
- **DefaultClipSize**: Увеличен с 33 до 50
- **DefaultReloadTime**: Уменьшен с 1.55 до 1.4
- **CostOfBullet**: Уменьшен с 1.5 до 1.3
- **ShotDelay**: Уменьшен с 0.078 до 0.066

### 9. GEAR_DMR_Semi (TR22 Hanaway DMR)
- **Damage**: Увеличен с 7.51 до 8.0
- **DamageFalloff.x**: Уменьшен с 50.0 до 30.0
- **DamageFalloff.y**: Уменьшен с 100.0 до 80.0
- **PrecisionDamageMulti**: Уменьшен с 0.87 до 0.85
- **DefaultClipSize**: Уменьшен с 12 до 8
- **DefaultReloadTime**: Увеличен с 2.3 до 2.4
- **CostOfBullet**: Увеличен с 5.89 до 10.9
- **ShotDelay**: Увеличен с 0.25 до 0.35

### 10. GEAR_Sniper_Semi (Köning PR 11 Sniper Rifle)
- **DefaultClipSize**: Увеличен с 2 до 3
- **CostOfBullet**: Увеличен с 17.5 до 23.0

### 11. GEAR_Shotgun_Semi (Buckland S870 Shotgun)
- **Damage**: Увеличен с 3.01 до 3.1
- **DamageFalloff.x**: Увеличен с 4.0 до 5.0

### 12. GEAR_Sawed-Off_Shotgun_Semi (Buckland SBS III Sawed-Off Shotgun)
- **Damage**: Увеличен с 3.8 до 3.9
- **DefaultClipSize**: Уменьшен с 4 до 3

### 13. GEAR_Bullpup_Auto (Accrat Golok DA Bullpup Rifle)
- **Damage**: Увеличен с 2.1 до 2.84
- **StaggerDamageMulti**: Уменьшен с 1.0 до 0.8
- **DefaultClipSize**: Увеличен с 40 до 45
- **CostOfBullet**: Увеличен с 1.5 до 1.87
- **ShotDelay**: Увеличен с 0.055 до 0.0705
- **HipFireSpread**: Уменьшен с 2.5 до 2.0

### 14. GEAR_SentryGun_Semi_sniper (Sniper Sentry)
- **Damage**: Увеличен с 48.1 до 50.1
- **DamageFalloff.x**: Увеличен с 30.0 до 40.0
- **CostOfBullet**: Уменьшен с 16.0 до 14.5
- **ShotDelay**: Уменьшен с 2.6 до 1.9
- **PiercingBullets**: Изменён с false на true
- **Sentry_StartFireDelay**: Уменьшен с 2.8 до 0.6
- **Sentry_RotationSpeed**: Увеличен с 6.0 до 10.0
- **Sentry_DetectionMaxAngle**: Увеличен с 20.0 до 90.0
- **Sentry_LegacyEnemyDetection**: Изменён с false на true
- **Sentry_StartFireDelayTagMulti**: Изменён с 0.5 на 0.8
- **Sentry_DamageTagMulti**: Увеличен с 1.0 до 1.5
- **Sentry_StaggerDamageTagMulti**: Увеличен с 1.0 до 2.0
- **Sentry_CostOfBulletTagMulti**: Уменьшен с 0.7 до 0.4
- **Sentry_ShotDelayTagMulti**: Уменьшен с 0.7 до 0.6

### 15. GEAR_SentryGun_Burst (Mechatronic SGB3 Burst Sentry)
- **DamageFalloff.x**: Увеличен с 10.0 до 20.0
- **DamageFalloff.y**: Увеличен с 40.0 до 80.0
- **CostOfBullet**: Увеличен с 2.05 до 2.26
- **BurstDelay**: Уменьшен с 1.0 до 0.5
- **PiercingBullets**: Изменён с false на true
- **PiercingDamageCountLimit**: Установлен на 2
- **Sentry_StartFireDelay**: Уменьшен с 1.0 до 0.5
- **Sentry_RotationSpeed**: Увеличен с 4.0 до 10.0
- **Sentry_DetectionMaxAngle**: Увеличен с 30.0 до 90.0
- **Sentry_LegacyEnemyDetection**: Изменён с true на false
- **Sentry_StartFireDelayTagMulti**: Изменён с 1.0 на 0.8
- **Sentry_RotationSpeedTagMulti**: Изменён с 1.0 на 1.5
- **Sentry_DamageTagMulti**: Увеличен с 1.0 до 1.5
- **Sentry_StaggerDamageTagMulti**: Увеличен с 1.0 до 2.0
- **Sentry_CostOfBulletTagMulti**: Уменьшен с 1.0 до 0.6
- **Sentry_ShotDelayTagMulti**: Уменьшен с 1.0 до 0.8

### 16. GEAR_SentryGun_Auto_staggering (Rad Labs Meduza HEL Auto Sentry)
- **Damage**: Увеличен с 0.8 до 1.0
- **DamageFalloff.x**: Увеличен с 10.0 до 18.0
- **CostOfBullet**: Увеличен с 0.7 до 1.1
- **PiercingDamageCountLimit**: Увеличен с 2 до 3
- **Sentry_StartFireDelay**: Уменьшен с 1.0 до 0.5
- **Sentry_RotationSpeed**: Увеличен с 4.0 до 10.0
- **Sentry_DetectionMaxRange**: Уменьшен с 25.0 до 20.0
- **Sentry_DetectionMaxAngle**: Увеличен с 30.0 до 90.0
- **Sentry_StartFireDelayTagMulti**: Изменён с 1.0 на 0.8
- **Sentry_DamageTagMulti**: Увеличен с 1.0 до 2.0
- **Sentry_StaggerDamageTagMulti**: Увеличен с 1.0 до 3.0
- **Sentry_CostOfBulletTagMulti**: Уменьшен с 1.0 до 0.5

### 17. GEAR_SentryGun_Shotgun_Semi (Mechatronic B5 LFR Shotgun Sentry)
- **Damage**: Уменьшен с 3.01 до 2.21
- **StaggerDamageMulti**: Увеличен с 1.0 до 2.0
- **CostOfBullet**: Увеличен с 1.58 до 1.7
- **PiercingBullets**: Изменён с false на true
- **PiercingDamageCountLimit**: Установлен на 2
- **ShotgunBulletCount**: Увеличен c 5 до 10
- **ShotgunBulletSpread**: Уменьшен с 2 до 1
- **Sentry_RotationSpeed**: Увеличен с 8.0 до 10.0
- **Sentry_DetectionMaxRange**: Увеличен с 10.0 до 12.0
- **Sentry_DetectionMaxAngle**: Увеличен с 40.0 до 90.0
- **Sentry_ForceAimTowardsBody**: Изменён с false на true
- **Sentry_DamageTagMulti**: Увеличен с 1.0 до 1.5
- **Sentry_StaggerDamageTagMulti**: Увеличен с 1.0 до 2.0

### 18. GEAR_Revolver_Semi (Bataldo 3RB HEL Revolver)
- **CostOfBullet**: Увеличен с 5.74 до 6.2

### 19. GEAR_Revolver_Semi_Special (Mastaba R66 Revolver)
- **DefaultClipSize**: Увеличен с 20 до 21

### 20. GEAR_Shotgun_Pump (Buckland Custom K330 Slug Shotgun)
- **CostOfBullet**: Увеличен с 12.0 до 11.5
- **ShotDelay**: Уменьшен с 0.75 до 0.70

### 21. GEAR_Shotgun_Choke (Buckland XDIST2 Choke Mod Shotgun)
- **PrecisionDamageMulti**: Уменьшен с 0.7333 до 0.6
- **CostOfBullet**: Увеличен с 16.3 до 20.6

### 22. GEAR_Shotgun_DoubleBarrel (Buckland AF6 Combat Shotgun)
- **CostOfBullet**: Уменьшен с 10.0 до 9.55

### 23. GEAR_Special_Semi_HighDamage (Shelling Arid 5 High Caliber Pistol)
- **Damage**: Увеличен с 14.21 до 15.25

### 24. GEAR_Special_Semi_Precision (Drekker DEL P1 Precision Rifle)
- **CostOfBullet**: Увеличен с 10.0 до 10.8

### 25. GEAR_Special_Semi_Sniper (Drekker DEL P1 Precision Rifle - Thermal Scope)
- **DamageFalloff.x**: Увеличен с 30.0 до 40.0
- **DamageFalloff.y**: Увеличен с 70.0 до 90.0
- **PrecisionDamageMulti**: Увеличен с 1.3 до 2.15
- **DefaultClipSize**: Увеличен с 10 до 12

### 26. GEAR_Special_Semi_Heavy (Shelling Arid-5 High Caliber Pistol)
- **Damage**: Увеличен с 30.1 до 33

---

## Изменения в настройках фонарей

### 1. GunLight_A (Short Range Flashlight)
- **range**: Увеличен с 8.0 до 10.0
- **color.b**: Увеличен с 0.7311321 до 0.8311321

### 2. GunLight_E (Medium Range #2 Flashlight)
- **range**: Увеличен с 13.0 до 15.0
- **intensity**: Уменьшен с 0.5 до 0.45
- **cookie**: Изменён с "FlashlightRegularCookie_05.tga" на "FlashlightRegularCookie_01.tga"
- **color**: Полностью изменён:
  - **r**: Изменён с 0.86 до 1.0
  - **g**: Изменён с 1.0 до 0.9909915
  - **b**: Изменён с 0.987599432 до 0.9326415

### 3. GunLight_B (Medium Range #1 Flashlight)
- **range**: Увеличен с 15.0 до 16.0

### 4. GunLight_D (Long Range #1 Flashlight)
- **range**: Увеличен с 16.0 до 18.0

### 5. GunLight_C (Long Range #2 Flashlight)
- **range**: Увеличен с 20.0 до 22.0

### 6. Consumable_MediumFlashlight (Portable Flashlight)
- **range**: Увеличен с 25.0 до 30.0

---

## Изменения в архетипах ближнего боя

### 1. Spear (Копьё)
- **LightAttackDamage**: Увеличен с 2.0 до 2.5
- **ChargedAttackStaminaCost**: 
  - **baseStaminaCostInCombat**: Уменьшен с 0.05 до 0.0
  - **baseStaminaCostOutOfCombat**: Уменьшен с 0.05 до 0.0
- **PushStaminaCost**:
  - **baseStaminaCostInCombat**: Уменьшен с 0.05 до 0.0
  - **baseStaminaCostOutOfCombat**: Уменьшен с 0.05 до 0.0

### 2. Bat (Бита)
- **LightAttackDamage**: Увеличен с 3.0 до 4.0
- **LightStaggerMulti**: Уменьшен с 5.0 до 4.0

---

## Основные изменения

### Турели
- Все турели получили значительные улучшения в скорости поворота (до 10.0)
- Увеличен угол обнаружения до 90° для всех турелей
- Добавлено пробитие для всех типов турелей
- Улучшены бонусы от био-трекера

### Оружие
- Автоматическое оружие получило повышение урона и улучшенную эффективность
- Снайперское оружие стало более универсальным
- Дробовики получили улучшения в точности и эффективности
- Ближний бой стал менее затратным по выносливости

### Освещение
- Все типы фонарей получили увеличенную дальность
- Улучшена видимость и цветопередача