"""I create a list for all palindromes, iterating over the range from 1 to 1000 (the largest three-digit number is 999).
By iterating, I check if the number will be read forward [::1] and also read backward [::-1].
If the value is True, I add the number to my search. Next, I display the maximum number from my list."""

list_for_answer = []
for i in range(1,1000):
    for j in range(1,1000):
        res = i*j
        x = str(res)
        if x[::1] == x[::-1]:
            list_for_answer.append(res)

print(max(list_for_answer))










































