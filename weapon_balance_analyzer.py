#!/usr/bin/env python3
"""
GTFO Weapon Balance Analyzer
Сравнивает ванильную и модифицированную версии оружия для анализа баланса
"""

import json
import os
from typing import Dict, List, Tuple, Any

class WeaponBalanceAnalyzer:
    def __init__(self, vanilla_path: str, mod_path: str):
        self.vanilla_path = vanilla_path
        self.mod_path = mod_path
        self.vanilla_data = None
        self.mod_data = None
        
        # Ключевые параметры для анализа
        self.key_params = [
            'Damage',
            'DefaultClipSize', 
            'CostOfBullet',
            'ShotDelay',
            'StaggerDamageMulti',
            'PrecisionDamageMulti',
            'Sentry_DetectionMaxAngle',
            'Sentry_DetectionMaxRange',
            'Sentry_RotationSpeed',
            'Sentry_StartFireDelay'
        ]
        
        # Пороги для определения имбовых изменений
        self.imba_thresholds = {
            'Damage': 50,  # >50% увеличения урона
            'DefaultClipSize': 100,  # >100% увеличения магазина
            'StaggerDamageMulti': 50,  # >50% увеличения оглушения
            'PrecisionDamageMulti': 30,  # >30% изменения точного урона
            'ShotDelay': -30,  # >30% уменьшения задержки (отрицательное значение)
            'CostOfBullet': -50  # >50% уменьшения стоимости пули
        }

    def load_data(self):
        """Загружает данные из JSON файлов"""
        try:
            with open(self.vanilla_path, 'r', encoding='utf-8') as f:
                self.vanilla_data = json.load(f)
            with open(self.mod_path, 'r', encoding='utf-8') as f:
                self.mod_data = json.load(f)
            print("✓ Данные успешно загружены")
        except Exception as e:
            print(f"✗ Ошибка загрузки данных: {e}")
            return False
        return True

    def get_weapon_name(self, weapon_block: Dict) -> str:
        """Получает имя оружия из блока"""
        if 'name' in weapon_block:
            return weapon_block['name']
        return f"Unknown_ID_{weapon_block.get('persistentID', 'NoID')}"

    def extract_weapons(self, data: Dict) -> Dict[str, Dict]:
        """Извлекает все оружие из данных"""
        weapons = {}
        if 'Blocks' in data:
            for block in data['Blocks']:
                weapon_name = self.get_weapon_name(block)
                weapons[weapon_name] = block
        return weapons

    def calculate_percentage_change(self, vanilla_val: float, mod_val: float) -> float:
        """Вычисляет процентное изменение"""
        if vanilla_val == 0:
            return 0 if mod_val == 0 else float('inf')
        return ((mod_val - vanilla_val) / vanilla_val) * 100

    def analyze_weapon_changes(self, vanilla_weapons: Dict, mod_weapons: Dict) -> Dict:
        """Анализирует изменения в оружии"""
        analysis = {
            'changed_weapons': {},
            'unchanged_weapons': [],
            'new_weapons': [],
            'removed_weapons': [],
            'imba_changes': [],
            'summary': {}
        }

        # Найти изменения
        for weapon_name, vanilla_weapon in vanilla_weapons.items():
            if weapon_name in mod_weapons:
                mod_weapon = mod_weapons[weapon_name]
                changes = {}
                
                for param in self.key_params:
                    if param in vanilla_weapon and param in mod_weapon:
                        vanilla_val = vanilla_weapon[param]
                        mod_val = mod_weapon[param]
                        
                        if vanilla_val != mod_val:
                            percentage_change = self.calculate_percentage_change(vanilla_val, mod_val)
                            changes[param] = {
                                'vanilla': vanilla_val,
                                'mod': mod_val,
                                'change_percent': percentage_change
                            }
                            
                            # Проверка на имбовость
                            if param in self.imba_thresholds:
                                threshold = self.imba_thresholds[param]
                                if (threshold > 0 and percentage_change > threshold) or \
                                   (threshold < 0 and percentage_change < threshold):
                                    analysis['imba_changes'].append({
                                        'weapon': weapon_name,
                                        'parameter': param,
                                        'change_percent': percentage_change,
                                        'vanilla': vanilla_val,
                                        'mod': mod_val
                                    })
                
                if changes:
                    analysis['changed_weapons'][weapon_name] = changes
                else:
                    analysis['unchanged_weapons'].append(weapon_name)
            else:
                analysis['removed_weapons'].append(weapon_name)

        # Найти новое оружие
        for weapon_name in mod_weapons:
            if weapon_name not in vanilla_weapons:
                analysis['new_weapons'].append(weapon_name)

        return analysis

    def generate_weapon_categories(self, weapons: Dict) -> Dict[str, List[str]]:
        """Категоризирует оружие по типам"""
        categories = {
            'Rifles': [],
            'SMGs': [],
            'Shotguns': [],
            'Snipers': [],
            'DMRs': [],
            'Machine Guns': [],
            'Pistols': [],
            'Revolvers': [],
            'Bullpup': [],
            'SentryGuns': [],
            'Other': []
        }
        
        for weapon_name in weapons.keys():
            weapon_lower = weapon_name.lower()
            if 'rifle' in weapon_lower:
                categories['Rifles'].append(weapon_name)
            elif 'smg' in weapon_lower:
                categories['SMGs'].append(weapon_name)
            elif 'shotgun' in weapon_lower:
                categories['Shotguns'].append(weapon_name)
            elif 'sniper' in weapon_lower:
                categories['Snipers'].append(weapon_name)
            elif 'dmr' in weapon_lower:
                categories['DMRs'].append(weapon_name)
            elif 'machinegun' in weapon_lower:
                categories['Machine Guns'].append(weapon_name)
            elif 'pistol' in weapon_lower:
                categories['Pistols'].append(weapon_name)
            elif 'revolver' in weapon_lower:
                categories['Revolvers'].append(weapon_name)
            elif 'bullpup' in weapon_lower:
                categories['Bullpup'].append(weapon_name)
            elif 'sentry' in weapon_lower:
                categories['SentryGuns'].append(weapon_name)
            else:
                categories['Other'].append(weapon_name)
        
        # Удаляем пустые категории
        return {k: v for k, v in categories.items() if v}

    def print_analysis_report(self, analysis: Dict, vanilla_weapons: Dict, mod_weapons: Dict):
        """Выводит детальный отчет анализа"""
        print("\n" + "="*80)
        print("🔫 АНАЛИЗ БАЛАНСА ОРУЖИЯ GTFO МОДА")
        print("="*80)
        
        # Общая статистика
        print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
        print(f"├─ Общее количество оружия в ванили: {len(vanilla_weapons)}")
        print(f"├─ Общее количество оружия в моде: {len(mod_weapons)}")
        print(f"├─ Изменено оружия: {len(analysis['changed_weapons'])}")
        print(f"├─ Не изменено оружия: {len(analysis['unchanged_weapons'])}")
        print(f"├─ Новое оружие: {len(analysis['new_weapons'])}")
        print(f"├─ Удаленное оружие: {len(analysis['removed_weapons'])}")
        print(f"└─ Потенциально имбовых изменений: {len(analysis['imba_changes'])}")
        
        # Категории оружия
        print(f"\n🗂️ КАТЕГОРИИ ОРУЖИЯ:")
        categories = self.generate_weapon_categories(vanilla_weapons)
        for category, weapons in categories.items():
            print(f"├─ {category}: {len(weapons)} единиц")
        
        # Имбовые изменения
        if analysis['imba_changes']:
            print(f"\n⚠️ ПОТЕНЦИАЛЬНО ИМБОВЫЕ ИЗМЕНЕНИЯ:")
            for change in analysis['imba_changes']:
                sign = "+" if change['change_percent'] > 0 else ""
                print(f"├─ {change['weapon']}")
                print(f"│  └─ {change['parameter']}: {change['vanilla']} → {change['mod']} ({sign}{change['change_percent']:.1f}%)")
        else:
            print(f"\n✅ ИМБОВЫХ ИЗМЕНЕНИЙ НЕ ОБНАРУЖЕНО")
        
        # Детальный анализ изменений
        print(f"\n🔧 ДЕТАЛЬНЫЙ АНАЛИЗ ИЗМЕНЕНИЙ:")
        
        for weapon_name, changes in analysis['changed_weapons'].items():
            print(f"\n🔸 {weapon_name}:")
            
            for param, change_data in changes.items():
                vanilla_val = change_data['vanilla']
                mod_val = change_data['mod']
                percent_change = change_data['change_percent']
                
                # Определяем тип изменения
                if percent_change > 0:
                    change_type = "УСИЛЕН"
                    color = "🔥" if percent_change > 30 else "📈"
                else:
                    change_type = "ОСЛАБЛЕН"
                    color = "❄️" if percent_change < -30 else "📉"
                
                print(f"   {color} {param}: {vanilla_val} → {mod_val} ({change_type} на {abs(percent_change):.1f}%)")
        
        # Неизмененное оружие
        if analysis['unchanged_weapons']:
            print(f"\n🔒 НЕИЗМЕНЕННОЕ ОРУЖИЕ ({len(analysis['unchanged_weapons'])} единиц):")
            for weapon in analysis['unchanged_weapons'][:10]:  # Показываем первые 10
                print(f"├─ {weapon}")
            if len(analysis['unchanged_weapons']) > 10:
                print(f"└─ ... и еще {len(analysis['unchanged_weapons']) - 10} единиц")
        
        # Новое оружие
        if analysis['new_weapons']:
            print(f"\n🆕 НОВОЕ ОРУЖИЕ:")
            for weapon in analysis['new_weapons']:
                print(f"├─ {weapon}")
        
        # Удаленное оружие  
        if analysis['removed_weapons']:
            print(f"\n🗑️ УДАЛЕННОЕ ОРУЖИЕ:")
            for weapon in analysis['removed_weapons']:
                print(f"├─ {weapon}")
        
        print(f"\n" + "="*80)
        print("🎯 ЗАКЛЮЧЕНИЕ:")
        
        # Анализ общего направления баланса
        total_damage_changes = 0
        damage_weapons = 0
        
        for weapon_name, changes in analysis['changed_weapons'].items():
            if 'Damage' in changes:
                total_damage_changes += changes['Damage']['change_percent']
                damage_weapons += 1
        
        if damage_weapons > 0:
            avg_damage_change = total_damage_changes / damage_weapons
            if avg_damage_change > 10:
                print("├─ 🔥 Мод в целом УСИЛИВАЕТ оружие")
            elif avg_damage_change < -10:
                print("├─ ❄️ Мод в целом ОСЛАБЛЯЕТ оружие")
            else:
                print("├─ ⚖️ Мод поддерживает БАЛАНС оружия")
        
        if len(analysis['imba_changes']) > 3:
            print("├─ ⚠️ ВНИМАНИЕ: Обнаружено много потенциально имбовых изменений!")
        elif len(analysis['imba_changes']) == 0:
            print("├─ ✅ Изменения выглядят сбалансированными")
        
        changed_percentage = (len(analysis['changed_weapons']) / len(vanilla_weapons)) * 100
        print(f"└─ 📊 Затронуто {changed_percentage:.1f}% от всего оружия")
        
        print("="*80)

    def run_analysis(self):
        """Запускает полный анализ"""
        print("🔍 Запуск анализа баланса оружия GTFO мода...")
        
        if not self.load_data():
            return False
        
        print("🔄 Извлечение данных об оружии...")
        vanilla_weapons = self.extract_weapons(self.vanilla_data)
        mod_weapons = self.extract_weapons(self.mod_data)
        
        print("⚡ Анализ изменений...")
        analysis = self.analyze_weapon_changes(vanilla_weapons, mod_weapons)
        
        self.print_analysis_report(analysis, vanilla_weapons, mod_weapons)
        
        return True

def main():
    # Пути к файлам
    vanilla_path = "/home/vlad/Документы/suslow-rebalance-mod/vanilla/GameData_ArchetypeDataBlock_bin.json"
    mod_path = "/home/vlad/Документы/suslow-rebalance-mod/BepInEx/plugins/suslow_rebalance_mod/GameData_ArchetypeDataBlock_bin.json"
    
    # Проверяем существование файлов
    if not os.path.exists(vanilla_path):
        print(f"❌ Ванильный файл не найден: {vanilla_path}")
        return
    
    if not os.path.exists(mod_path):
        print(f"❌ Файл мода не найден: {mod_path}")
        return
    
    # Запускаем анализ
    analyzer = WeaponBalanceAnalyzer(vanilla_path, mod_path)
    analyzer.run_analysis()

if __name__ == "__main__":
    main()