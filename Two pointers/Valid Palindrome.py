class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointers, begine
        begin = 0
        end = len(s) - 1
        def isValid(char):
            print(char)
            if char and (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
                return True
            return False

        while begin <= end:
            #skip the white space
            if isValid(s[begin]) and isValid(s[end]):
                # print(s[begin], s[end])
                if s[begin].lower() == s[end].lower():
                    begin += 1
                    end -= 1
                else:
                    return False
            elif not isValid(s[begin]):
                begin += 1
            elif not isValid(s[end]):
                end -= 1
            
        return True