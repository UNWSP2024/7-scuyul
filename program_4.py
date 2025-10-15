# Program #4: Coordinate caculator, 10/15/25
import math


def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist


def get_coordinate(prompt):
    print(prompt)
    x = float(input(" Enter x coordinate: "))
    y = float(input(" Enter y coordinate: "))
    z = float(input(" Enter z coordinate: "))
    return (x, y, z)


def main():
    print("3D Coordinate Distance Calculator")
    print("")
    
    try:
        coord1 = get_coordinate("Enter the first coordinate: ")
        coord2 = get_coordinate("Enter the second coordinate: ")
        dist = distance(coord1, coord2)
        
        print("")
        print(f"Coordinate 1: {coord1}")
        print(f"Coordinate 2: {coord2}")
        print(f"Distance: {dist:.4f}")
        
    except:
        print("An error occurred")


if __name__ == "__main__":
    main()
