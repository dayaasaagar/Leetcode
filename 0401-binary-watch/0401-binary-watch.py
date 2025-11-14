class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:


        if turnedOn < 0 or turnedOn >10:
            return []
        
        res =[]
        hourVals =[8,4,2,1]
        minuteVals=[32,16,8,4,2,1]
        
        def comb_sum(vals,k):
            out=[]
            n =len(vals)

            def back_track(idx,chosen,curr_sum):
                if chosen==k:
                    out.append(curr_sum)
                    return
                if idx>=n:
                    return 
                back_track(idx+1,chosen+1,curr_sum+vals[idx])
                if n-(idx+1)>=(k-chosen):
                    back_track(idx+1,chosen,curr_sum)
            back_track(0,0,0)
            return out

        for h in range(max(0,turnedOn-6),min(4,turnedOn)+1):
            m  = turnedOn-h
            hours = comb_sum(hourVals,h)
            minutes = comb_sum(minuteVals,m)

            for hour in hours:
                if hour>=12:
                    continue
                for minute in minutes:
                    if minute>=60:
                        continue 
                    res.append(f"{hour}:{minute:02d}")

        return res

        