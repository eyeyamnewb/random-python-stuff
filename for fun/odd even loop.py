while True:
    even = [0]
    n = int(input("number go here: "))
    for i in range(n):
        i=i+1
        i= i + i
        even.append(i)
    if n in even:
        print("even")
    else:
        print("odd")
    
    
    