
def sort_by_key(elements: list, key: str, ascending=True) -> list:
    return sorted(elements, key=lambda element: element[key], reverse=not ascending)


def group_by_key(elements: list, key: str) -> dict:
    grouped_elements = {}
    for element in elements:
        if element[key] in grouped_elements.keys():
            grouped_elements[element[key]].append(element)
        else:
            grouped_elements[element[key]] = []
            grouped_elements[element[key]].append(element)
    return grouped_elements


def group_quantities_by_key(elements: list, key: str):
    grouped_elements = group_by_key(elements, key)
    return {k: len(grouped_elements[k]) for k in grouped_elements}


def get_element_by_min_key(elements: list, key: str):
    return min(elements, key=lambda element: float(element[key]))


def get_element_by_max_key(elements: list, key: str):
    return max(elements, key=lambda element: float(element[key]))


def get_sum_by_key(elements: list, key: str):
    return sum([element[key] for element in elements])


def get_average_by_key(elements: list, key: str):
    return get_sum_by_key(elements, key) / len(elements)


def filter_by_key_value(elements: list, key: str, value: str) -> list:
    return list(filter(lambda element: element[key].capitalize() == value.capitalize(), elements))


def filter_by_higher_key_value(elements: list, key: str, target_value: float) -> list:
    return list(filter(lambda element: element[key] > target_value, elements))


def filter_by_higher_key_value(elements: list, key: str, target_value: float) -> list:
    return list(filter(lambda element: element[key] < target_value, elements))
