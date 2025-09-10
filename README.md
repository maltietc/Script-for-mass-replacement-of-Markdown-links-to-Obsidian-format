# Script-for-mass-replacement-of-Markdown-links-to-Obsidian-format
This Python script is designed for bulk processing of Obsidian notes. It recursively scans all Markdown files in the selected folder (vault_path), finds links to other notes written in the format [title](path/to/note.md) or [[title](path/to/note.md)], and converts them to the standard Obsidian format [[title]].
All changes are logged in the obsidian_link_update.log file, where you can see which links were replaced and in which files.
The script is useful for migrating, standardizing, or automatically cleaning up links in large note databases.

# Before running, it is recommended that you make a backup copy of your notes!
## **Startup guide**
1. Copy the script
2. Save the code above to a file, for example:
scripts/obsidian_link_update.py

3. Prepare a folder with notes
Copy your Obsidian notes to a folder, for example:
vault/

4. Install Python
Make sure you have Python 3.x installed
 

5. Run the script
Open a terminal/command line in the root of your project and run:


python scripts/obsidian_link_update.py
or, if the script is located in the root directory:


python obsidian_link_update.py
Check the result

All links of the form [name](...md) and [[name](...md)] will be replaced with [[name]]
The entire process is logged in the obsidian_link_update.log file
Recommendation
Make a backup copy of your notes before running!

If you need to change the path to your notes, change the vault_path variable in the script.


# Скрипт для массовой замены ссылок Markdown на формат Obsidian
Этот Python-скрипт предназначен для массовой обработки заметок Obsidian. Он рекурсивно проходит по всем Markdown-файлам в выбранной папке (vault_path), находит ссылки на другие заметки, записанные в формате [название](путь/к/заметке.md) или [[название](путь/к/заметке.md)], и преобразует их в стандартный формат Obsidian [[название]].
Все изменения логируются в файл obsidian_link_update.log, где можно посмотреть, какие ссылки были заменены и в каких файлах.
Скрипт полезен для миграции, стандартизации или автоматической чистки ссылок в больших базах заметок.

# Перед запуском рекомендуется сделать резервную копию ваших заметок!
## **Гайд по запуску**
1. Скопируйте скрипт
2. Сохраните код выше в файл, например:
scripts/obsidian_link_update.py

3. Подготовьте папку с заметками
Скопируйте ваши Obsidian заметки в папку, например:
vault/

4. Установите Python
Убедитесь, что у вас установлен Python 3.x
 

5. Запустите скрипт
Откройте терминал/командную строку в корне вашего проекта и выполните:


python scripts/obsidian_link_update.py
или, если скрипт лежит в корне:


python obsidian_link_update.py
Проверьте результат

Все ссылки вида [название](...md) и [[название](...md)] будут заменены на [[название]]
Весь процесс логируется в файл obsidian_link_update.log
Рекомендация
Перед запуском сделайте резервную копию ваших заметок!

Если нужно изменить путь к заметкам — поменяйте переменную vault_path в скрипте.
