# http://code.activestate.com/recipes/577575-scale-rectangle-while-keeping-aspect-ratio/
def scale(w, h, x, y, maximum=True):
    nw = y * w / h
    nh = x * h / w
    if maximum ^ (nw >= x):
        return nw or 1, y
    return x, nh or 1

print(scale(50, 100, 10, 10, False))
print(scale(50, 100, 10, 10, True))


print(scale(50, 100, 10, 20, False))

print(scale(50, 100, 1, 1, True))


# print("scale(800,600,  128,128,  False) : ", scale(800, 600, 128,128,  False))

# scale so the 800/600 object will have sides of *at least* 128
# scale을 사용하여 800/600 객체의 크기가 * 적어도 128 *
print(scale(800,600,  128,128,  False))
# (170, 128)

# scale so the 800/600 object can fit in a box of 128/128
# 800/600 오브젝트가 128/128의 상자에 들어갈 수 있도록 # 스케일
print(scale(800,600,  128,128,  True))
# (128, 96)

# can scale up too
# 규모도 커질 수 있습니다.
print(scale(4,3,  900,1600, True))
# (900, 675)

print(scale(4,3,  900,1600, False))
# (2133, 1600)

print(scale(2,8,  1,8,  True))
# (1, 4)