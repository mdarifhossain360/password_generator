import random
number=int(input("Enter your Password length :> "))
number_password=[0,1,2,3,4,5,6,7,8,9]
lowercase_alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upercase_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_symbol=['!','@','#','%','*','~',' ']
Password=number_password+lowercase_alphabet+upercase_alphabet+special_symbol
print("Your password is :>",end=" ")
for i in range(number):
	print(random.choice(Password),end="")