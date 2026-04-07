def capitalize(string: str):
    return string.title()

def manual_capitalize(string: str):
    arr = list(string)
    for i in range(len(arr)):
        if i==0:
            arr[i] = chr(ord(arr[i]) - 32)
        elif arr[i] == " " and i + 1 < len(arr) and arr[i+1].isalpha():
            arr[i+1] = chr(ord(arr[i+1]) - 32)
    
    return "".join(arr)

string = 'hello world'
#print(capitalize(string))
print(manual_capitalize(string))