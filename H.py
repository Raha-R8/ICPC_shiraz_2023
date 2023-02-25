finger = int(input())
hands = int(input())
total_fingers = hands*finger
num1,num2 = int(input()),int(input())
number = num1+num2
if number ==0:
    print('0')
else:
    if number%total_fingers==0:
        print(total_fingers)
    else :
        print(number%total_fingers)
#7min        
