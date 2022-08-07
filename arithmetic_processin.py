from posixpath import split


def arithmetic_sequence_elements(a, d, n):
    #Your code here!:)
    return ", ".join(str(a + i*d) for i in range(n))
        



    


print(arithmetic_sequence_elements(1,2,5))