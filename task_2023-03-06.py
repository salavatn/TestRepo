dictionary_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]


def get_unique_data(data):
    unique_data = []
    for element in data:
        if element in unique_data:
            print(f"\tThe element '{element}' is duplicated!")
        else:
            unique_data.append(element)
    return unique_data


result = get_unique_data(dictionary_list)
print(f"\n{result}")
