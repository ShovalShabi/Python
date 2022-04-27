##################################################Time Generator Function###############################################
def tick_clock(lst, jump):  #helper method for function
    lst[2]=lst[2] + jump[2]
    if lst[2]>= 60:  #seconds
        lst[2]=lst[2]-60
        lst[1] += 1
    lst[1] = lst[1] + jump[1]
    if lst[1]>= 60:  #minutes
        lst[1]=lst[1]-60
        lst[0] += 1
    lst[0]=lst[0]+jump[0]
    if lst[0]>=24:  #hours
        lst[0] = lst[0] - 24


def gen_func_track_time(start, end, jump):
    current_time = start[0] + start[1] * 0.01 + start[2] * 0.0001  #converting tuple to number
    end_time = end[0] + end[1] * 0.01 + end[2] * 0.0001  #converting tuple to number
    if jump[0] == 0 and jump[1] ==0 and jump[2] == 0:  # corner case jump=(0,0,0)
        yield start
        return
    lst = list(start)  # moving forward in time
    flag=True
    while flag:
        flag=False
        while current_time >= end_time:
            sent_val = yield tuple(lst)
            if sent_val is not None:
                lst = list(sent_val)
                yield sent_val
            if current_time == end_time:
                return
            tick_clock(lst, jump)
            current_time = lst[0] + lst[1] * 0.01 + lst[2] * 0.0001
        while current_time <= end_time:
            sent_val = yield tuple(lst)
            if sent_val is not None:
                lst = list(sent_val)
                if (lst[0] + lst[1] * 0.01 + lst[2] * 0.0001)>end_time:
                    flag=True
                yield sent_val
            tick_clock(lst, jump)
            current_time = lst[0] + lst[1] * 0.01 + lst[2] * 0.0001


###############################################Time Generator Class#####################################################
class genClassTrackTime:
    def __init__(self, start, end, jump):
        self.start = start
        self.end = end
        self.jump = jump
        self.back_up_time=self.start
        self.finished=False
        self.same_day=False

    def __iter__(self):
        self.finished=False
        self.same_day = False
        self.back_up_time=self.start
        return self

    def __next__(self):
        current_time = self.back_up_time[0] + self.back_up_time[1] * 0.01 + self.back_up_time[2] * 0.0001  #converting tuple to number
        end_time = self.end[0] + self.end[1] * 0.01 + self.end[2] * 0.0001  # converting tuple to number
        if (self.jump[0]+ self.jump[1] +self.jump[2] == 0) and not self.finished:  # corner case jump=(0,0,0)
            self.finished=True
            return self.start
        lst = list(self.back_up_time)  # moving forward in time
        back_up=tuple(lst)
        while current_time >= end_time and not self.finished and not self.same_day:
            if current_time == end_time:
                self.finished=True
                return back_up
            self.tick_clock(lst, self.jump)
            self.back_up_time=tuple(lst)
            return back_up
        while current_time <= end_time and not self.finished:
            self.same_day=True
            self.tick_clock(lst, self.jump)
            self.back_up_time = tuple(lst)
            if (back_up[0] + back_up[1] * 0.01 + back_up[2] * 0.0001)>end_time:
                self.finished=True
            return back_up
        self.finished=True
        if self.finished:
            raise StopIteration

    def tick_clock(self,lst, jump):  #helper method for class
        lst[2] = lst[2] + jump[2]
        if lst[2] >= 60:
            lst[2] = lst[2] - 60
            lst[1] += 1
        lst[1] = lst[1] + jump[1]
        if lst[1] >= 60:
            lst[1] = lst[1] - 60
            lst[0] += 1
        lst[0] = lst[0] + jump[0]
        if lst[0] >= 24:
            lst[0] = lst[0] - 24


g = gen_func_track_time((16, 23, 11), (23, 30, 0), (0, 30, 10))
print(list(g))
g=genClassTrackTime((16, 23, 11), (23, 30, 0), (0, 30, 10))
print(list(g))
################sending values to generator################
g = gen_func_track_time((16, 23, 11), (23, 30, 0), (0, 30, 10))
print(next(g))
print(g.send((20,57,12)))
print(list(g))
