infile = open('wrapping-paper-dimensions.txt')
lines = infile.readlines()
square_feet = 0
for line in lines:
    l, w, h = [int(x) for x in line.removesuffix('\n').split('x')]
    square_feet += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
print(square_feet)