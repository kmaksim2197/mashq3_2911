m1 = lambda lst: list(map(lambda x: f"{x[0]}-{len(x)}", lst))

m2 = lambda lst: list(map(lambda x: f"{x.split()[0]} {x.split()[1][0]}.", lst))

m3 = lambda lst: list(map(lambda x: f"{x}{len(x)}", lst))

m4 = lambda lst: list(map(lambda x: x[:-1] + x[-1].upper(), lst))

f1 = lambda lst: list(filter(lambda x: len(x) > 5 and "a" in x, lst))

f2 = lambda lst: list(filter(lambda x: len(str(x)) == 3, lst))

f3 = lambda lst: list(filter(lambda x: x.endswith(".uz"), lst))

f4 = lambda lst: list(filter(lambda x: x % 5 == 0 or x % 7 == 0, lst))

f5 = lambda lst: list(filter(lambda x: str(x).endswith("0"), lst))

f6 = lambda lst: list(filter(lambda x: len(x) % 2 == 0, lst))
