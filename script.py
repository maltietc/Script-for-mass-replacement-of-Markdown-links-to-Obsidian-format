import os
import re

# Укажите путь к вашей папке с заметками
vault_path = './vault'  # например, ./vault
log_path = 'obsidian_link_update.log'

def process_file(filepath, log_file):
    try:
        log_file.write(f'Открываю файл: {filepath}\n')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        log_file.write(f'Ошибка чтения файла {filepath}: {e}\n')
        return 0

    # Основная замена ссылок [название](...md) и [[название](...md)]
    pattern = re.compile(r'(\[\[)?\[([^\[\]]+?)\]\([^\)]+?\.md\)\]?')
    new_content = pattern.sub(lambda m: f'[[{m.group(2)}]]', content)

    # Удаляем лишние открывающие скобки (три и более)
    new_content = re.sub(r'\[{3,}', '[[', new_content)

    # Логирование
    matches = list(pattern.finditer(content))
    log_file.write(f'Найдено ссылок для замены: {len(matches)}\n')
    for match in matches:
        old = match.group(0)
        new = f'[[{match.group(2)}]]'
        log_file.write(f'{filepath}: {old} -> {new}\n')

    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            log_file.write(f'Файл перезаписан: {filepath}\n')
        except Exception as e:
            log_file.write(f'Ошибка записи файла {filepath}: {e}\n')
    return len(matches)

total_files = 0
total_links = 0

with open(log_path, 'w', encoding='utf-8') as log_file:
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                total_files += 1
                links = process_file(full_path, log_file)
                total_links += links
    log_file.write(f'Обработано файлов: {total_files}\n')
    log_file.write(f'Всего заменено ссылок: {total_links}\n')

print("Готово. Все ссылки обновлены на формат [[название]]. Лог изменений: obsidian_link_update.log")