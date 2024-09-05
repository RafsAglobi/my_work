def test_function():

    def inner_function():
        print("я в области видимости функции test_function")
    return inner_function()

test_function()