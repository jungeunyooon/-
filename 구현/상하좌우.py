n = int(input())
plans = input().split()
x , y = 1 , 1

for i in range(len(plans)):
    if(plans[i]=='L'):
        if(y<=1):
            y = 1
        else :
            y -= 1
    elif (plans[i]=='R'):
        y += 1
    elif (plans[i]=='U'):
        if(x<=1):
            x = 1
        else :
            y -= 1
    elif (plans[i]=='D'):
        x += 1
print(x,y)