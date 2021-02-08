dot = ". "
charp = "# "
xCount = 25
yCount = 25
xMax = xCount - 1
yMax = yCount - 1
funcs = [lambda x,y : dot,
         lambda x,y : charp,
         lambda x,y : charp if x > y else dot,
         lambda x,y : charp if x == y else dot,
         lambda x,y : charp if x == (yMax - y) else dot,
         lambda x,y : charp if y > x / 2 else dot,
         lambda x,y : dot if y > 10 and x > 10 else charp,
         lambda x,y : charp if y > 12 and x > 12 else dot,
         lambda x,y : charp if y * x == 0 else dot,
         lambda x,y : charp if y * y + x * x < 400 else dot,
         lambda x,y : charp if y*x == 0 or (yMax - y) * (xMax - x) == 0 else dot,
         lambda x,y : charp if (x + y) % 2 == 0 else dot,
         lambda x,y : charp if x % 2 == 0 and y % 2 == 0 else dot,
         lambda x,y : charp if x % 2 == 0 and y % 2 == 0 else dot,
         lambda x,y : charp if x == y or x == (yMax - y) else dot,
         ]
for func in funcs:
    for y in range(0, yCount):
        line = ""
        for x in range(0, xCount):
            line += func(x,y)
        print(line, "\n")
    print()