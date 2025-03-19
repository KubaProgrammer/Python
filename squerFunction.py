import cmath

def solutions(a, b, c):
    if a == 0:
        print("a cannot be equal to 0.")
        return
    print(f"y = {a if a != 1 else ""}{"x^2" if a != 0 else ""} {"+" if b >= 0 else "-"} {abs(b)}x {"+" if c >= 0 else "-"} {abs(c)}")
    delta = cmath.sqrt(b*b-4*a*c)
    print(f"Delta = {delta}")
    if delta != 0:
        x1 = (-b - delta)/(2*a)
        x2 = (-b + delta)/(2*a)
        print(f"x1 = {x1}, x2 = {x2}.")
    else:
        x0 = (-b)/(2*a)
        print(f"x0 = {x0}.")

solutions(1, -16, 64)

