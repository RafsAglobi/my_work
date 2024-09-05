def generate_password(n):
password = ''
for i in range(1, 21):
for j in range(i + 1, 21):
if n % (i + j) == 0:
password += str(i) + str(j)
return password



for i in range(3, 21):
# print(i, '-', generate_password(i))
print(f'{i} - {generate_password(i)}')