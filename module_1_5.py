print('задание 1', 'создание кортежа')
immutable_var=1,2,3,False,'box'
print(immutable_var)
print('задание 2')
immutable_var2_=([8,6,5],101)
print(immutable_var2_,'создание кортежа со списком внутри него')
immutable_var2_[0][1]=99
print(immutable_var2_,'замена переменной в списке внутри кортежа')
print('задание 3 по замене элемента внутри списка')
mutable_list=['камень','ножницы','бумага']
print(mutable_list)
mutable_list[1]='бантики'
print(mutable_list)
print('задание по замене переменной внутри кортежа')
immutable_var[1]=78
print(immutable_var)



