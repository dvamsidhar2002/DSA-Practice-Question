import math

def area_of_tetrahedron(side):
    area = math.sqrt(3) * pow(side, 2)
    return area

if __name__ == '__main__':
    side = int(input('Enter the length of each side : '))
    area = area_of_tetrahedron(side)

    print(f'Area of tetrahedron : {area}')