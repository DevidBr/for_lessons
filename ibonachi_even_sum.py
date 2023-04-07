
# create a sequence. this will be the new list_fib.
list_fib = [0, 1, 2]
a = 0
new_num = 0
while new_num < 4000000:
    new_num = list_fib[1+a] + list_fib[2+a]
    list_fib.append(new_num)
    a += 1

# here i am making a list of even numbers from my sequence by looping through "for"
list_enen_fib = []
for i in list_fib[0:-1]:
    if i % 2 == 0:
        list_enen_fib.append(i)

# and display the sum of all even numbers from the list_enen_fib list
print(sum(list_enen_fib))








































