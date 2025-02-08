n = [3, 2, 4, 10, 9]
print(n)
n[0] = 5
print(n)
n.append(8)
print(n)
n.sort(reverse=False)
print(n)
n.insert(0, 34)
print(n)
n.pop(5)
print(n)
if 4 in n:
    n.remove(4)
    print(n)
else:
    print('nao achei um numero quatro')
print(f'nessa lista tem {len(n)} elementos')
