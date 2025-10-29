def add(n):
 if n == "":
    return 0
 if "," in n:
     parts = n.split(",")
     return int(parts[0]) + int(parts[1])
 return int(n)
