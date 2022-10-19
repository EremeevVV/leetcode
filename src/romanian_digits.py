# not optimal
class Solution:
    roma = ["I","V", "X", "L", "C", "D", "M"]
    deci = [1,5,10,50,100,500,1000]
    roma_deci = {key:val for key,val in zip(roma,deci)}


    def romanToInt(self, s: str) -> int:
        spicial_symbols = self.decrised_symbols()
        result = 0
        for key,val in spicial_symbols.items():
            if key in s:
                s = s.replace(key,'')
                result += val
        if s:
            for symbol in s:
                result += self.roma_deci[symbol]
        return result


    def decrised_symbols(self)->dict:
        special = {}
        decrisand = tuple([self.roma[0], 1])
        for ind, sym in enumerate(self.roma):
            if ind ==0:
                continue
            special[decrisand[0]+sym] = self.deci[ind] - decrisand[1]
            if ind % 2 == 0:
                decrisand = self.roma[ind], self.deci[ind]
        return special

