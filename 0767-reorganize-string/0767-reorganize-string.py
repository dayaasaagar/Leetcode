class Solution:
    def reorganizeString(self, s: str) -> str:
        str_len= len(s)
        char_count = Counter(s)
        max_freq = max(char_count.values())

        if max_freq > (str_len+1)//2:
            return ''
        index =0
        newstring = [None]*str_len

        for char,count in char_count.most_common():
            while count:
                newstring[index]=char
                count-=1
                index+=2
                if index>=str_len:
                    index=1
                

        
        return ''.join(newstring)

