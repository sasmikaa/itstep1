result = []
def divider(a, b):
 if a < b:
    raise ValueError
 if b > 100:
    raise IndexError
 return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
for key in data.keys():
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)

print(result)
