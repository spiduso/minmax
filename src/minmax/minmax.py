def find_min(array):
    if not isinstance(array, list):
        raise Exception('argument is not array')

    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array[0]

    min_val = array[0]

    for i in range(1, len(array)):
        if min_val > array[i]:
            min_val = array[i]

    return min_val


def find_max(array):
    if not isinstance(array, list):
        raise Exception('argument is not array')

    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array[0]

    max_val = array[0]

    for i in range(1, len(array)):
        if max_val < array[i]:
            max_val = array[i]

    return max_val


class Comparer:
    def __init__(self, array):
        if not isinstance(array, list):
            raise Exception('argument is not array')
        self.array = array

    def add_value(self, value):
        self.array.append(value)

    def get_min(self):
        return find_min(self.array)

    def get_max(self):
        return find_max(self.array)