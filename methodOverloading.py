class Arthi:
    def sum(x, y, z = None):
        s= x + y
        if z == None:
            return s
        else:
            return s+z



print(Arthi.sum(10, 20))
