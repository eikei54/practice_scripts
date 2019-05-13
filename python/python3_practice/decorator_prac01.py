def document_it(func):
    def new_function(*args, **kwargs):
        print('Positional arguments:', args)
        print('Keword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
#def add_ints(a, b):
#    return a + b
#
#print(add_ints(3, 5))
#cooler_add_ints = document_it(add_ints)
#print(cooler_add_ints(3, 5))


@document_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
