"""Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию)."""


def introspection_info(obj):
    # Получаем тип объекта и сохраняем его имя в переменной obj_type
    obj_type = type(obj).__name__

    # Получаем список всех атрибутов и методов объекта с помощью dir() и сохраняем в attributes
    attributes = dir(obj)

    # Фильтруем атрибуты, чтобы оставить только методы (вызываемые объекты), и сохраняем их в methods
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем имя модуля, к которому принадлежит объект, и сохраняем его в переменной module
    module = obj.__module__ if hasattr(obj, '__module__') else None

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,  # Тип объекта
        'attributes': attributes,  # Атрибуты объекта
        'methods': methods,  # Методы объекта
        'module': module,  # Модуль, к которому принадлежит объект
    }

    # Возвращаем собранную информацию в виде словаря
    return info


# Пример использования функции с целым числом 42
number_info = introspection_info(42)
# Выводим информацию о числе 42
print(number_info)
