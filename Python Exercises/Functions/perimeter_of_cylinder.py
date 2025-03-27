def perimeter(diameter, height):
    return 2 * (diameter + height)

if __name__ == '__main__':
    diameter = int(input('Enter the diameter of cylinder : '))
    height = int(input('Enter the height of cylinder : '))

    peri = perimeter(diameter, height)
    print(f'Perimeter of Cylinder : {peri}')