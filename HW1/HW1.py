#Дан список целых чисел. Найти второе по величине число в списке.
#Дано:
#numbers = [15, 7, 28, 10, 21]
#Результат:
#21
numbers = [15, 7, 28, 10, 21]
numbers.sort(reverse=True)
print(numbers[1])

#Дан список целых чисел. Найти второе по величине число в списке.
#Дано:
#numbers = [4, 6, 2, 11, 1, 11, 5]
#Результат:
#6
numbers = [4, 6, 2, 11, 1, 11, 5]
numbers.sort(reverse=True)
c=1
for num in numbers:
    if num>numbers[c]:
        print(numbers[c])
        break
    else: c+=1