# Diplom_3
Проект содержит в себе тесты сайта https://stellarburgers.nomoreparties.site/
Запустить тесты можно командой pytest
Просьба обратить внимание, что счётчик заказов за сутки может падать по причине того, что время, указанное программистом: текущее время минус 24 часа и если заказ формировался в это время сутки назад, то тест может упасть.
Также могут падать тесты, связанные с заказами по причине множественного тестирования заказов другими тестировщиками.

Папки проекта:
- allure_results - отчёты 
- locators - локаторы, соответствующие страницам
- pages - описанные методы для работы со страницами
- tests - файлы с тестами

Файлы:
.gitignore - игнорируемые файлы
conftest.py - файл фикстур
data.py - файл с используемыми данными
helpers.py - файл с генерацией
requirements.txt - установленные библиотеки
