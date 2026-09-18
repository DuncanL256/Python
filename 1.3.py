import time #for better termial organization


s = 'azcbobobegghakl'
print("")
print("starting string: " + s)
print("")
time.sleep(1.5)
print("calculating longest string...") 
time.sleep(2.5)

#i found a method where i iterate over s
longest = s[0]
present = s[0]

for p in s[1:]:
    if p >= present[-1]:
        present += p
        if len(present) > len(longest):
            longest = present
    else:
        present = p

print("")
print ("Longest substring in alphabetical order is: " + longest)