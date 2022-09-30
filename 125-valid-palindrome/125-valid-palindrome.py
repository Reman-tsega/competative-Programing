class Solution:
    def isPalindrome(self, inp: str) -> bool:
        alpnum =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        lower_str = inp.lower()
        new_str =""
        
        for s in lower_str:
            if s in alpnum:
                new_str+=s
        half_len = (len(new_str)//2)
        if new_str=="":
            return True
        # elif (len(new_str)%2==0):
        #     return False
        else:
            for i in range(half_len):
                if new_str[i]!= new_str[-(i+1)]:
                    return False
                else:
                    continue
            return True
       