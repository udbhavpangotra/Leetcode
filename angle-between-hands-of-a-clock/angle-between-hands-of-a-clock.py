class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        if hour == 12:
            hour =0
        minute_hand = 0
        minute_hand = minutes*6
        # print(minute_hand)
        hour_hand = (hour*30)+(minute_hand/12)
        # print(hour_hand)
        
        if (hour_hand>minute_hand):
            s =  hour_hand - minute_hand
        else: 
            s =  minute_hand-hour_hand
        
        if s>180:
            return 360-s
        else: return s