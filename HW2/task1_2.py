#task1
d_of_w = ['workday','day off','day off','workday','workday','workday','workday'] #2027 начинается с пятницы
d_of_y = []
b=0
for i in range(365):
    d_of_y.append(d_of_w[b])
    b+=1
    if b>6:
        b=b-7

def get_day_type(d):
    return(d_of_y[d-1])
    
print(get_day_type(2))

#task2
def join_strings(*args,sep=' '):
    rez = ''
    for word in args:
        rez += word+sep
    return rez.rstrip(sep)

    
print(join_strings("red", "green", "blue", sep=", "))
print(join_strings("Hello", "world"))
