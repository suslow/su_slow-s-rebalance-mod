const fs = require('fs');
const path = require('path');

// Функция для получения имени блока
function getBlockName(block) {
    // Сначала ищем name, потом PublicName
    if (block.name) return block.name;
    if (block.PublicName) return block.PublicName;
    if (block.persistentID) return `Block_${block.persistentID}`;
    return 'Unknown Block';
}

// Технические поля которые нужно игнорировать
const IGNORED_PATTERNS = [
    /^Headers$/,
    /^LastPersistentID$/,
    /^persistentID$/,
    /^internalEnabled$/,
    /EquipSequence/,
    /AimSequence/,
    /^Anim$/,
    /AnimHash/,
    /^TPAnim/,
    /^FPAnim/,
    /FrameTime$/,
    /BlendIn$/,
    /^startupShard$/,
    /^Side$/
];

// Критически важные поля (всегда показывать)
const CRITICAL_FIELDS = [
    'Damage', 'DefaultClipSize', 'DefaultReloadTime', 'CostOfBullet', 'ShotDelay',
    'StaggerDamageMulti', 'PrecisionDamageMulti', 'FireMode',
    'BurstDelay', 'BurstShotCount', 'PiercingBullets', 'PiercingDamageCountLimit',
    'ShotgunBulletCount', 'ShotgunBulletSpread', 'HipFireSpread',
    'ChargedAttackDamage', 'LightAttackDamage', 'LightStaggerMulti', 'ChargedStaggerMulti',
    'range', 'angle', 'intensity'
];

// Функция для проверки, важное ли это поле
function isImportantField(fieldPath, oldValue, newValue) {
    const fieldName = fieldPath.split('.').pop();
    const fullPath = fieldPath;
    
    // 1. Критически важные поля - всегда показывать
    if (CRITICAL_FIELDS.includes(fieldName)) {
        return true;
    }
    
    // 2. Игнорируем техническую фигню
    if (IGNORED_PATTERNS.some(pattern => pattern.test(fieldName) || pattern.test(fullPath))) {
        return false;
    }
    
    // 3. Автоматически включаем числовые поля (они обычно важны для баланса)
    if (typeof oldValue === 'number' && typeof newValue === 'number') {
        return true;
    }
    
    // 4. Булевы поля тоже важны (включение/выключение фич)
    if (typeof oldValue === 'boolean' && typeof newValue === 'boolean') {
        return true;
    }
    
    // 5. Специфические паттерны для разных типов полей
    const importantPatterns = [
        // Турели
        /^Sentry_/,
        // Отдача
        /Recoil/,
        // Урон и эффекты
        /Multi$/,
        /Multiplier$/,
        /Damage/,
        /Stagger/,
        /Precision/,
        // Дальности и углы
        /Range$/,
        /Falloff/,
        /Angle$/,
        // Боеприпасы и эффективность
        /Cost/,
        /Bullet/,
        /Ammo/,
        // Времена
        /Time$/,
        /Delay$/,
        // Цвета (для фонарей)
        /^[rgb]$/,
        // Радиусы и размеры
        /Radius$/,
        /Spread$/,
        /Size$/,
        // Параметры выносливости
        /Stamina/,
        // Параметры обнаружения
        /Detection/,
        // Скорости
        /Speed$/,
        /Rate$/
    ];
    
    if (importantPatterns.some(pattern => pattern.test(fieldName) || pattern.test(fullPath))) {
        return true;
    }
    
    // 6. Строковые изменения только если это не техническая фигня
    if (typeof oldValue === 'string' && typeof newValue === 'string') {
        // Разрешаем только короткие строки (вероятно значения, не пути к файлам)
        if (newValue.length < 50 && !newValue.includes('/') && !newValue.includes('.')) {
            return true;
        }
    }
    
    return false;
}

// Функция для сравнения значений  
function compareValues(oldVal, newVal, fieldPath) {
    // Сначала проверяем, есть ли реальное изменение
    if (oldVal === newVal) {
        return null; // Нет изменений
    }
    
    // Проверяем, важное ли это поле
    if (!isImportantField(fieldPath, oldVal, newVal)) {
        return null;
    }
    
    // Для чисел показываем с точностью
    if (typeof oldVal === 'number' && typeof newVal === 'number') {
        if (Math.abs(oldVal - newVal) < 0.001) return null; // Игнорируем микроизменения
        
        // Форматируем числа красиво
        const oldFormatted = oldVal % 1 === 0 ? oldVal.toString() : oldVal.toFixed(3).replace(/\.?0+$/, '');
        const newFormatted = newVal % 1 === 0 ? newVal.toString() : newVal.toFixed(3).replace(/\.?0+$/, '');
        
        return {
            oldValue: oldVal,
            newValue: newVal,
            formatted: `${oldFormatted} → ${newFormatted}`
        };
    }
    
    // Для булевых значений
    if (typeof oldVal === 'boolean' && typeof newVal === 'boolean') {
        return {
            oldValue: oldVal,
            newValue: newVal,
            formatted: `${oldVal} → ${newVal}`
        };
    }
    
    // Для строк и других примитивов
    return {
        oldValue: oldVal,
        newValue: newVal,
        formatted: `${oldVal} → ${newVal}`
    };
}

// Рекурсивное сравнение объектов
function compareObjects(oldObj, newObj, path = '', changes = []) {
    for (const key in newObj) {
        const currentPath = path ? `${path}.${key}` : key;
        const oldValue = oldObj[key];
        const newValue = newObj[key];
        
        if (!(key in oldObj)) {
            // Новое поле - только если важное
            if (isImportantField(currentPath, null, newValue) && (typeof newValue !== 'object' || newValue === null)) {
                changes.push({
                    path: currentPath,
                    type: 'added',
                    property: key,
                    newValue: newValue
                });
            }
        } else if (typeof newValue === 'object' && newValue !== null && !Array.isArray(newValue)) {
            // Рекурсивно сравниваем объекты
            compareObjects(oldValue, newValue, currentPath, changes);
        } else {
            // Сравниваем примитивы
            const change = compareValues(oldValue, newValue, currentPath);
            if (change) {
                changes.push({
                    path: currentPath,
                    type: 'changed',
                    property: key,
                    ...change
                });
            }
        }
    }
    
    return changes;
}

// Функция для анализа блоков
function analyzeBlocks(oldBlocks, newBlocks, fileName) {
    const changes = [];
    
    // Создаем карту блоков по persistentID
    const oldMap = {};
    const newMap = {};
    
    if (oldBlocks) {
        oldBlocks.forEach(block => {
            if (block.persistentID) {
                oldMap[block.persistentID] = block;
            }
        });
    }
    
    if (newBlocks) {
        newBlocks.forEach(block => {
            if (block.persistentID) {
                newMap[block.persistentID] = block;
            }
        });
    }
    
    // Сравниваем соответствующие блоки
    Object.keys(newMap).forEach(id => {
        const oldBlock = oldMap[id];
        const newBlock = newMap[id];
        
        if (oldBlock) {
            const blockName = getBlockName(newBlock);
            const blockChanges = compareObjects(oldBlock, newBlock, '', [], fileName);
            
            if (blockChanges.length > 0) {
                changes.push({
                    blockName: blockName,
                    blockId: id,
                    changes: blockChanges
                });
            }
        }
    });
    
    return changes;
}

// Функция для форматирования changelog
function formatChangelog(blockChanges, fileName) {
    if (blockChanges.length === 0) return '';
    
    const fileDisplayName = fileName
        .replace('GameData_', '')
        .replace('_bin.json', '')
        .replace('ArchetypeDataBlock', 'Weapons')
        .replace('FlashlightSettingsDataBlock', 'Flashlights')
        .replace('MeleeArchetypeDataBlock', 'Melee Weapons');
        
    let output = `\n## ${fileDisplayName}\n\n`;
    
    blockChanges.forEach(block => {
        output += `### ${block.blockName}\n\n`;
        
        block.changes.forEach(change => {
            const propertyName = change.property || change.path.split('.').pop();
            
            if (change.type === 'changed') {
                output += `- **${propertyName}**: ${change.formatted}\n`;
            } else if (change.type === 'added') {
                output += `- **${propertyName}**: Added (${change.newValue})\n`;
            }
        });
        
        output += '\n';
    });
    
    return output;
}

// Основная функция генерации changelog
function generateChangelog() {
    const previousDir = 'previous'; // Вместо vanilla - предыдущая версия
    const currentDir = 'BepInEx/plugins/suslow_rebalance_mod';
    
    if (!fs.existsSync(previousDir)) {
        console.log('❌ Папка previous/ не найдена.');
        console.log('💡 Создайте папку previous/ и скопируйте туда файлы предыдущей версии.');
        console.log('💡 Или запустите скрипт с флагом --init для первого запуска:');
        console.log('   node scripts/generate-changelog.js --init');
        return;
    }
    
    let fullChangelog = `# Changelog\n\n*Changes since previous version - ${new Date().toISOString().split('T')[0]}*\n\n`;
    
    // Получаем список JSON файлов
    const jsonFiles = fs.readdirSync(currentDir).filter(file => file.endsWith('.json'));
    let totalChanges = 0;
    
    jsonFiles.forEach(fileName => {
        const previousPath = path.join(previousDir, fileName);
        const currentPath = path.join(currentDir, fileName);
        
        if (fs.existsSync(previousPath)) {
            try {
                const previousData = JSON.parse(fs.readFileSync(previousPath, 'utf8'));
                const currentData = JSON.parse(fs.readFileSync(currentPath, 'utf8'));
                
                const blockChanges = analyzeBlocks(previousData.Blocks, currentData.Blocks, fileName);
                const formattedChanges = formatChangelog(blockChanges, fileName);
                
                if (formattedChanges) {
                    fullChangelog += formattedChanges;
                    totalChanges += blockChanges.reduce((sum, block) => sum + block.changes.length, 0);
                }
            } catch (error) {
                console.error(`❌ Ошибка при обработке ${fileName}:`, error.message);
            }
        } else {
            console.log(`⚠️  Предыдущая версия не найдена: ${previousPath}`);
        }
    });
    
    if (totalChanges === 0) {
        fullChangelog += '\n*No significant changes detected.*\n';
        console.log('ℹ️  Изменений не обнаружено.');
    } else {
        // Добавляем статистику в начало
        const statsLine = `**Total changes: ${totalChanges}**\n\n---\n\n`;
        fullChangelog = fullChangelog.replace('*Changes since', statsLine + '*Changes since');
    }
    
    // Сохраняем changelog
    fs.writeFileSync('CHANGELOG.md', fullChangelog);
    console.log(`✅ Changelog сгенерирован: CHANGELOG.md`);
    console.log(`📊 Найдено изменений: ${totalChanges}`);
    
    // Показываем краткую статистику
    if (totalChanges > 0) {
        console.log('\n📋 Краткая сводка изменений:');
        const lines = fullChangelog.split('\n');
        lines.forEach(line => {
            if (line.startsWith('### ') || line.startsWith('- **')) {
                console.log(line);
            }
        });
    }
}

// Функция для инициализации - копирует текущие файлы в previous
function initPrevious() {
    const currentDir = 'BepInEx/plugins/suslow_rebalance_mod';
    const previousDir = 'previous';
    
    if (!fs.existsSync(previousDir)) {
        fs.mkdirSync(previousDir, { recursive: true });
    }
    
    const jsonFiles = fs.readdirSync(currentDir).filter(file => file.endsWith('.json'));
    
    jsonFiles.forEach(fileName => {
        const sourcePath = path.join(currentDir, fileName);
        const destPath = path.join(previousDir, fileName);
        fs.copyFileSync(sourcePath, destPath);
        console.log(`✅ Скопирован: ${fileName}`);
    });
    
    console.log(`\n✅ Инициализация завершена. Папка previous/ создана.`);
    console.log(`💡 При следующих изменениях запускайте: node scripts/generate-changelog.js`);
}

// Проверяем аргументы командной строки
if (process.argv.includes('--init')) {
    initPrevious();
} else {
    generateChangelog();
}