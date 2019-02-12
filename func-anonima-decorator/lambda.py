# Funciones anonimas (lambda)
print("Con funciones anonimas")
print((lambda: 100 * 3)())
print((lambda x, y: x + y)(8,9))
print((lambda *x: sum(x)) (8,5,12,45,21))

# Asignado funciones a variables
variable1 = lambda : 100 * 3
variable2 = lambda x, y: x + y
variable3 = lambda *x: sum(x)

print("Almacenado los resultados en variables")
print(variable1())
print(variable2(8,9))
print(variable3(8,5,12,45,21))

