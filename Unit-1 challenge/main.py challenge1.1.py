def fact_rec(n):
  if n == 0 or n == 0:
    return 1
  else:
    return n * fact_rec(n - 1)

print ("TO FIND FACTORIAL ")
n = int(input("Enter a value:"))
result = fact_rec(n)

print('The factorial of ', n, ' is ', result)
