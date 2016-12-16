class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        thousand = [['MMM',3000],['MM',2000],['M',1000]]
        hundred = [['CM',900],['DCCC',800],['DCC',700],['DC',600],['CD',400],['D',500],['CCC',300],['CC',200],['C',100]]
        ten = [['XC',90],['LXXX',80],['LXX',70],['LX',60],['XL',40],['L',50],['XXX',30],['XX',20],['X',10]]
        no = [['IX',9],['VIII',8],['VII',7],['VI',6],['IV',4],['V',5],['III',3],['II',2],['I',1]]
        counter = 0
        table = [thousand,hundred,ten,no]
        for j in table:
            for i in j:
                if i[0] == s[:len(i[0])]:
                    counter += i[1]
                    s = s[len(i[0]):]
        return counter