#condition
is_old=False
is_licenced=True
if is_old:
    print("You are old enough to drive")
elif is_licenced:
    print("you can drive now")
else:
    print("check check")

#ternary
is_friend=True
can_message="message allowed" if is_friend else "not allowed to message"
print(can_message)

print(True==1) #true
print(''==1)#false
print([]==1)#false
print(10==10.0)#true
print([]==[]) #true
#== convert anyone to same type to both
print(True is 1) #is check location in memory is same