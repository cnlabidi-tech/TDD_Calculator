def add(n):
 if not n:
    return 0
 parts = [int(x) for x in n.split(",")]
 return  sum(parts)