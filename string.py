#str_one ="your"
#str_two ="face"
#str_three =str_one +""+str_two
#print(str_three)#

#interpolation of variables
#guess=8
#print(f"your guess of{guess} was incorrect")
#name="bluetheray"
#print(f"nice try,{name} but your guess of{guess} is wrong!")
#print(f"your guess of {guess+1} is correct!")


print("How many kilometers did you run today?")
kms= input()
miles = float(kms)/1.60934
#print(f"that is equal to {round(miles , 2)} miles")  #Round(thing to round,how many decimal points)
miles=round(miles,2)
print(f"that is equal to{miles}miles")