array = [0 for _ in range(10)]
for i in range(10):
  array[i] = int(input('inserisci un numero '))
cnt = 0
for i in range(9):
  if array[i] == array[9]:
    cnt += 1 
print('gli uguali sono ' + str(cnt))
for i in range(9):
  if array[i] == array[9]:
    cnt -= 1 
print('Gli uguali al ultimo che hai inserito sono' + str(cnt))