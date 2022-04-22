
def is_palindrome(s):
    foo = [*filter(str.isalnum, str(s).lower())]
    return all(foo[i]==foo[len(foo)-1-i] 
    for i in range(len(foo)//2))  
    
    
        
print(is_palindrome('Tenet C is a basis, a basic tenet.'))


