x=25
if x < 10:
    print('smaller')
    print('bigger')
elif x<100:print(x)
else : print(x+1)
print('bigger')
num = input("9/? = ")
try:
    ans = 9 / int(num)
    print(ans)
except:
    print("cannot be divided")
    quit()
print(ans,", this is the answer")