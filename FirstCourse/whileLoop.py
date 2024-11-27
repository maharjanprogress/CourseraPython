x=5
y=2
while x<10:
    print(x)
    x=x+1
print("exit")
print(x,y)
while True:
    ok = input(">")
    if(ok == 'done'):
        
        print("Finally done")
        break
    if(ok[0]=='#'):
        continue
    print(ok)