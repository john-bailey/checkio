def sort_by(rawdata: list[dict], field: str, count: int) -> list:
    try:
        sorted_data = sorted(rawdata, key=lambda item: item[field], reverse=True)
        output = sorted_data[:count]
    except TypeError:
        output = ['Invalid Data']
    except KeyError:
        output = ['Invalid Field']
    except:
        output = ['Unknown Error']
    return output

data = [{"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}]

assert sort_by(data, 'price', 1) == [{"name": "wine", "price": 138}], "Top item"
assert sort_by(data, 'price', 2) == [{"name": "wine", "price": 138},
                                     {"name": "bread", "price": 100}], "Top two items"
assert sort_by(data, 'prie', 1) == ['Invalid Field'], "Bad field name"
assert sort_by({"name": "wine", "price": 138}, 'price', 1) == ['Invalid Data'], "Invalid data"
print('Success')
