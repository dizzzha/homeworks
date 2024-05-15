def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function() # ошибка связанная с тем, что ф-ция inner_function не определена
