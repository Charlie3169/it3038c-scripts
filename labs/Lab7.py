from sympy import *

# https://pypi.org/project/sympy/
# https://docs.sympy.org/latest/index.html
# Sympy is a python libray for symbolic math calculations
# You can do all this op stuff

x, y, z, c = symbols('x y z c')

#Factoring and Expansion
print(expand((((c)**2 + c)**2 + c)**2 + c))
print(factor(expand((((c)**2 + c)**2 + c)**2 + c)))

#Equality
print('\nEquality example')
eq1 = Eq(x + 1, 4)
print(eq1)
print(solve(eq1))

print('\nSystem of equations with two variables')
eq2 = Eq(5*x + 5*y - 7, 0)
eq3 = Eq(6*x - 4*y - 9, 0)
solution = solve((eq2,eq3), (x,y))
print(solution)

print('\nSum of two expressions')
equ2 = 5*x + 5*y - 7
equ3 = 6*x - 4*y - 9
equ4 = equ2 + equ3
print(equ4)

print('\nSolve for roots of x**2 = 2')
print(solve(x**2 - 2, x))

print('\nSolve for roots of x**3 = 1')
print(solve(x**3 - 1, x))

#Derivatives
print('\nNth derivatives of cosine:')
print(diff(cos(x), x))
print(diff(cos(x), x, 2))
print(diff(cos(x), x, 3))
print(diff(cos(x), x, 4))

print('\nDerivative of e^(x**2)')
print(diff(exp(x**2), x))

print('\nDerivative of cas(x) [cos(x) + sin(x)]')
expr = cos(x) + sin(x)
print(expr.diff(x))

print('\nPartial derivatives of exp(x*y*z) applied successively')
expr2 = exp(x*y*z)
print(expr2.diff(x, y, 2, z, 3))

deriv = Derivative(expr2, x, y, 2, z, 3)
print(deriv)
print(deriv.doit())

#Integrals
print('\nIndefinite integral of cos(x)')
print(integrate(cos(x), x))

print('\nDefinite integral of 1/x from 1 to 3')
print(integrate(1/x, (x, 1, 3)))

print('\nGaussian integral')
print(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))

print('\nUnevaluatable integral, returns Integral object')
print(integrate(x**x, x))

print('\nIntegral object example')
expr3 = Integral(cos(x)*exp(x),x)
print(expr3.doit())

print('\nExample of the power of integrate on sin(x**2)')
expr4 = Integral(sin(x**2), x)
print(expr4.doit())

print('\nConvert integrals to latex example')
print(latex(Integral(cos(x)**2, (x, 0, pi))))

#Limits
print('\nThe limit of sin(x)/x as x goes to 0')
print(limit(sin(x)/x, x, 0))

print('\nExample of the Limit object')
expr5 = Limit((cos(x) - 1)/x, x, 0)
print(expr5.doit)

#Series
print('\nExample of series using exp(x)')
expr6 = exp(x)
print(expr6.series(x, 0, 6).removeO())
