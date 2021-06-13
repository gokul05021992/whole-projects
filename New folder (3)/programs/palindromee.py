#from string import punctuation, ascii_lowercase

def palindrome(string):
    new = ""
    for char in string:
        lc=char.lower()
        for x in lc:
            #if x in ascii_lowercase:
                new +=x
 #   return new[::-1] == new


class palindrome(object):
    def ispalindrome(self,s):
        x=''
        diff =ord('a') - ord('A')
        for i in s:
            if ord(i)>=ord()
