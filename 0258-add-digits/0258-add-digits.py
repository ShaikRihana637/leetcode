class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num>=10:
             temp=0
             while num>0:
                d=num%10
                temp+=d
                num//=10
             num=temp
        return num

        