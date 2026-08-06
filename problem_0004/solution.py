def reverse_str(string):
    n_reverse = [string[i] for i in range(len(string)-1,-1,-1)]
    return ''.join(n_reverse)


def is_palindrome(n):
    n_string = str(n)
    n_reverse = reverse_str(n_string)
    if int(n_string) == int(n_reverse):
        return True

palindromes = list()
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        n = i * j
        if is_palindrome(n):
            palindromes.append(n)

print(max(palindromes))
