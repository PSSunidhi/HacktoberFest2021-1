def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes it's a palindrome")
else:
    print("No it's a palindrome")
