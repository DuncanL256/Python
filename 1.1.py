import time

# problem 1.1 ____________________________________________________________________________________________________________________

s = 'azcbobobegghakl' 
print("")
print("starting string: " + s)
print("")
time.sleep(1.5)
print("analyzing number of vowels...") # i added an analyzation message for a little bit of flare
time.sleep(2.5)



count = 0
i = 0  #i used "i" since it is a common variable i recognize from coding

for i in range(len(s)):  # "len" refers to the length of the string
    if (
        (s[i] == "a")
        or (s[i] == "e")
        or (s[i] == "i")
        or (s[i] == "o")
        or (s[i] == "u")
    ):
        count += 1

print("")
print("Number of vowels: ", count)
time.sleep(1)
print("_______________________________________________________________________________") #used as a visual distinction between problems in the terminal
print("")


# problem 1.2 ______________________________________________________________________________________________________________________

# string s is already estabolished

bobCount = 0
debug = 1

time.sleep(2)
print("Possible words under 3 letters:")
time.sleep(1)
for i in range (len(s)):
    time.sleep(0.2)
    if debug > 0:
        print(s[i: (i+3)])
    if s[i: (i+3)] == "bob":
        bobCount += 1

print("")
time.sleep(1.5)
print("Number of times bob occurs is: ")
print(bobCount)
print("")

