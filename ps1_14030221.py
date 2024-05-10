#تابعی بنویسید که آرایه‌ای از اعداد را دریافت کند 
# و کوچکترین عنصر را به عنوان نتیجه بدهد
#def min_finder(a)
def min_finder(arr):  
    minimum = arr[0]
    for item in arr[1:]:
        if (item<minimum):
            minimum = item
    return minimum


x = min_finder(arr= [1,2,3,4])
print(x)

#Write a function that returns the number 
# of 'True' and 'False' values in an array.

def sheep_counter(arr):
    count = 0
    for item in arr:
            if item == 'True':
                count +=1
    print(count)


sheep_counter(['True', 'True', 'True', 'True',
            'False','False', 'True', 'False'
            'True', 'False', 'True', 'True'])


x = ['True', 'True', 'True', 'True',
            'False','False', 'True', 'False'
            'True', 'False', 'True', 'True']

dir(x)
x.count('True')
def sheep_count(sheep):
    return sheep.count('True')

def sheep_counts(sheep):
    return sum(1 for i in sheep if sheep)
sum(1 for i in [True, False, True] if i==True)
sum(1 for i in [True, False, True] if i)
sum (3 for i in range(10) if i<5)

s= "hello"
s.upper()
x = 1
y = 1
x.__add__(y)

number = [0,1,2,3]
number[0]
number.__getitem__(0)