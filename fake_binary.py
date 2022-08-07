

x = "45385593107843568"
result = ""
for i in x:

    if i < "5":
        i = 0
        result += str(i)
        print(i)
        
    else:
        i = 1
        result += str(i)
        print(i)
print(result)        

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

print(fake_bin(x))