# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_data(line):
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def sort_by_age(data: list[dict]):
    return sorted(data, key=lambda x: x['age'])


def filter_by_age(data):
    return [person for person in data if person['age'] > 9]


def get_users_list():
    # Чтение данных из строки
    data = read_data(csv)

    sorted_data = sort_by_age(data)

    # Фильтрация
    result_data = filter_by_age(sorted_data)
    return result_data


if __name__ == '__main__':
    print(get_users_list())
