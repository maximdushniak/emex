Предварительное описание работы

Разработка представляет собой python-скрипт, запускаемый в командной строке.

Использование: python parse.py файл_источник целевой_файл [-proxy прокси] [-name ИмяПользователя] [-pass Пароль]

файл_источник – текстовый файл (кодировка ANSI, разделитель знак табуляции). Содержит значения артикулов/брендов.
целевой_файл – csv-файл (кодировка ANSI, разделитель - «;»). Содержит результат работы.
прокси (не обязательно) - строка, содержащая настройку прокси в формате тип://адрес:порт (например "http://188.165.141.151:80")

Файл источник содержит:

    Артикул
    Бренд (не обязательно)

Результирующий файл содержит:

    Искомый артикул
    Искомый бренд
    Найденный артикул
    Найденный бренд
    Минимальная цена
    Ошибка (описание ошибки, например если недоступен ресурс. Пусто если нет ошибок.)


Для каждого номера артикула из исходного файла совершается поиск на соответствующем интернет ресурсе и запись результата поиска в целевой файл.

Если в исходном файле указан бренд, то в результате будет получен результат только по артикулу этого бренда (поиск бренда осуществляется по подстроке. Например: В файле бренд указан "kNecht", тогда в результат попадет бренд "Knecht / Mahle").
Если бренд в исходном файле не указан -  результатом будет список брендов с одинаковым артикулом.
