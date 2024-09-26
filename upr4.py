def triangle(size, symbol, depth = 1):
    if size % 2 != 0 and depth == (size//2 + 1):
        print(symbol*depth)
        return
    if size % 2 == 0 and depth == (size//2):
        print(symbol*depth)
        print(symbol * depth)
        return
    print(symbol*depth)

    triangle(size, symbol, depth = depth + 1)

    print(symbol*depth)
size = int(input("Введите размер треугольника:"))
symbol = input("Введите символ:")
triangle(size, symbol)