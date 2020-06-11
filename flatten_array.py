
test_input = [1, 3, [3, 5], 4, [[8]]]

def flatten_array(arr):
    result = []
    for value in arr:
        if type(value) is list:
            result.extend(flatten_array(value)) 
        else:
            result.append(value)
    return result

print(flatten_array(test_input))