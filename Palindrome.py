#Palindrome string/phrase:
def isPalindrome(n):
    if len(n) <=1:
        return True
    elif n[0] == n[len(n)-1]:
        return isPalindrome(n[1:len(n)-1])
    else:
        return False
n = ["anna", "wolf","mom","sleep","noon", "refer", "radar", "cling", "wow", "civic", "kayak", "river"]
for word in n:
    ans = isPalindrome(word)
    if ans == 1:
        print(f'the given string: {word}, is a palindrome')
    else:
        print(f'the given string: {word}, is not a palindrome')