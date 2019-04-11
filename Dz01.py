# coding: utf8

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.

d = dict(
    [('разработка', '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'),
     ('сокет', '\u0441\u043e\u043a\u0435\u0442'),
     ('декоратор', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')])

for i, k in d.items():
    print(f"value = {i}, {k}, {i == k}")
    print(f"type = type={type(i)}, type={type(k)}, {type(i) == type(k)}")
    print(f"length = {len(i)}, {len(k)}, {len(i) == len(k)}")
    print()

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

c = bytes('class', 'utf-8')
f = bytes('function', 'utf-8')
m = bytes('method', 'utf-8')
print(f'value c = {c}, type = {type(c)}, length = {len(c)}')
print(f'value f = {f}, type = {type(f)}, length = {len(f)}')
print(f'value m = {m}, type = {type(m)}, length = {len(m)}')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

print('attribute'.encode("utf-8"))  # b'attribute'
print('класс'.encode("utf-8"))  # b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'
print('функция'.encode("utf-8"))  # b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
print('type'.encode("utf-8"))  # b'type'

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

s = ['разработка', 'администрирование', 'protocol', 'standard']
e = []
d = []

for i in s:
    enc = i.encode()
    dec = enc.decode()
    e.append(enc)
    d.append(dec)
    
print(e)
print(d)


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.


def ping(host):
    import subprocess
    result = subprocess.Popen(["ping", '-n', '1', host], shell=True, stdout=subprocess.PIPE, encoding='cp866')
    # return result.stdout.read().decode('cp866') # if without argument encoding='cp866'
    return result.stdout.read()


print(ping('yandex.ru'))
print(ping('youtube.com'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

file_name = 'test_file.txt'

with open(file_name, 'w') as cf:
    cf.write('сетевое программирование\n')
    cf.write('сокет\n')
    cf.write('декоратор\n')
    print(f"Кодировка файла {file_name} по умолчанию: {cf.encoding}")

with open(file_name, 'r', encoding='utf-8', errors="ignore") as rf:  # errors="ignore"
    print(rf.read())
