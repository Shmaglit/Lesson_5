#Решить с помощью генераторов списка.
#1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#
#    Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['apple', 'banana', 'pear']
fruits2 = ['orange', 'pear', 'apple', 'pineapple']

result = []
result = [fruit for fruit in fruits1 if fruit in fruits2]
print(result)