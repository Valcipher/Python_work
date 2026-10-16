

# class Time:
#     def __init__(self,hr,min,sec):
#         self.hr=hr
#         self.min=min 
#         self.sec=sec 
#     def __str__(self):
#         return f"{self.hr}:{self.min}:{self.sec}"
#     def __mul__(self, other):
#         thr=self.hr*other.hr
#         tmin=self.min*other.min
#         tsec=self.sec*other.sec 
#         return Time(thr,tmin,tsec)
# t1=Time(12,33,55)
# t2=Time(22,34,55)
# print(t1 * t2)



# class Time:
#     def __init__(self,hr,min,sec):
#         self.hr=hr
#         self.min=min 
#         self.sec=sec 
#     def __str__(self):
#         return f"{self.hr}:{self.min}:{self.sec}"
#     def __sub__(self, other):
#         thr=self.hr-other.hr
#         tmin=self.min-other.min
#         tsec=self.sec-other.sec 
#         return Time(thr,tmin,tsec)
# t1=Time(43,63,55)
# t2=Time(22,34,55)
# print(t1-t2)



class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min 
        self.sec=sec 
    def __div__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __mul__(self, other):
        thr=self.hr / other.hr
        tmin=self.min / other.min
        tsec=self.sec / other.sec 
        return Time(thr,tmin,tsec)
t1=Time(12,33,55)
t2=Time(22,34,55)
print(t1 / t2)