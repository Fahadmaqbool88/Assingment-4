def energy():
    c:float = 299792458
    m:float = float(input("inter kilos of Mass:"))
    print("e=m*c^2")
    print("Mass="+str(m)+"kg")
    print("c="+str(c)+"m/s")
    print("e="+ str(m*c**2)+"jules")
if __name__ == "__main__":
    energy()