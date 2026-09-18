print("One Per Line, enter last names. Type '.' to stop.\n")

smallest = None   # Creation of our required variables
largest  = None
last     = None

while True:
    name = input().strip()
    if name == '.':
        break
    if not name:           # Skip any empty lines
        continue
    
    if smallest is None:   # Use the first valid name
        smallest = largest = last = name
    else:
        if name < smallest:
            smallest = name
        if name > largest:
            largest = name
        last = name

if smallest is not None:
    print("\nResults:")
    print("Smallest (lexicographically):", smallest) # Closest to the front in dictionary order
    print("Largest  (lexicographically):", largest)  # Closest to th back in dictionary order
    print("Last entered                 :", last)    # Typed in the most recent
else:
    print("\nNo names were entered.")