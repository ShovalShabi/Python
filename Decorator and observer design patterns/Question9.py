z = 4
class a():
    global z
    def __init__(self, y):
        self.y = y

    def __call__(self, z):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z

class b(a):
    def __call__(self, *args):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


print(a(5)(b(6)()))  #should return 3
print(a(6)(b(5)(6)))  #should return 5
