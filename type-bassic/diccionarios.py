dic = {'a':[1,2,3,4], 'b':(6,4,9), 'c': {'d': 0, 'e':100}}
dic1 = dict(clave1=10, clave2=20, clave=30)
dic2 = dict(zip('abc', '123'))
dic3 = dict(zip([1,2,4], [6,3,5]))
dic4 = dict(zip(('a', 'b', 'c'), [1,2,3]))
# print(dic['b'])
# print(dic['b'][0])
# print(dic['c']['e'])
dic['z'] = 500

# print(dic)

dic['a'] = 50
dic['c'] = 10
dic['d'] = { 'r': 1, 's': 2, 't':3 }
# print(dic)

# print(dic1)

# print(dic2)
# print(dic4)
# print(dic3)

# print(dic.fromkeys(['a', 'b', 'c'], 10))
# print(dict.fromkeys('Devcode', 1))
# print(dic.fromkeys(('a','b', 'c')))

# print(dic)
# print(dic.popitem())
# print(dic.popitem())
# print(dic)

# print(dic.items())
# print(dic.values())
# print(dic.keys())