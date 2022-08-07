# Example
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

x = "How can mirrors be real if our eyes aren't real"
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())



    
print(to_jaden_case(x))


   





    




