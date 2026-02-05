# Problem: pythagoreanTriplet
side = list(map(int,input("Enter a side: ").split()))

if side[0]**2 + side[1]**2 == side[2]**2 \
    or side[1]**2 + side[2]**2 == side[0]**2 \
    or side[0]**2 + side[2]**2 == side[1]**2:
    print("It can form a Pythagorean triplet.")
else:
    print("It cannot form a Pythagorean triplet.")