class Solution:
    def reorganizeString(self, s: str) -> str:
        str_len=len(s)
        char_count= Counter(s)
        max_freq = max(char_count.values())

        if max_freq > (str_len+1)//2:
            return ''
        
        index = 0
        rearrange=[None]*str_len

        for char,freq in char_count.most_common():
            while freq:
                rearrange[index]=char
                freq-=1
                index = index +2 

                if index >= str_len:
                    index =1 
        return ''.join(rearrange)
