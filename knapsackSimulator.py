def knapsackSum(x, a):
    s = 0
    a = [int(i) for i in a]
    x = [int(i) for i in x]
    for i in range(0, len(x)):
        s = s+ a[i] *x[i]
    return s


def inv_knapsackSum(s, a):
    for i in range(len(a), 1):
        if s >= a[i]:
            x[i] = 1
            s =s -a[i]

        else:
            x[i] = 0
    return x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g == 1:
        return x % m

def permute(table):
    temp = table[:]
    #리스트 복사

    for i in range(0, len(table)):
        table[i] = temp[permute_table[i]-1]
    return table


b = [7, 11, 19, 39, 79, 157, 313]
n = 900
r = 37
'''rd = 73
t = [259, 407, 703, 543, 223, 409, 781]'''
t = []
for i in range(0, len(b)):
    t.append(b[i] * r % n)

print("Bob generates keys")
print("t: ", t)

permute_table = [4, 2, 5, 3, 1, 7, 6]
a = permute(t)
print("a: ", a)

rd = modinv(r, n)
print("Bob's private (n, r, rd, b): ", n, r, rd, b)

x = list(format(ord('g'), 'b'))
print()
p_x = [int(i) for i in x]
print("Alice data: ", p_x)

s = knapsackSum(a, x)
print("Alice makes cypertext: ", s, "and sends it.")

#print("rd : ", rd)

d_s = s * rd % n
print()
print("Bob computes: ")
print("s': ", d_s)

d_x = inv_knapsackSum(d_s, b)
p_d_x = [int(i) for i in d_x]
print("x': ", p_d_x)
str_d_x = "".join(d_x)
print("x: ", p_x)
#print("x' : ", str_d_x)
#print(int(str_d_x, 2))
d = chr(int(str_d_x, 2))
#print("복호 : ", d)
