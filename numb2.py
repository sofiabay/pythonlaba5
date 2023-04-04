list = [randint(1,10) for i in range(10)]
print(list)
spisok = [i for i in set(list) if list.count(i) > 1]
if len(spisok) == 0:
   print("Повторяющихся элементов нет")
else:
   print(spisok)