import re
from datetime import datetime

class Every(object):

    def __init__(self, proc):
        self.proc = proc

    def __call__(self, values):
            retList = []
            for v in values:
                ret = None
                try:
                    ret = self.proc(v)
                except Exception as _:
                    continue
                retList.append(ret)
            return retList
       
class Join(object):

    def __init__(self, separator=u' '):
        self.separator = separator

    def __call__(self, values):
        return self.separator.join(values)


class Re(object):
    def __init__(self, reStr):
        self.reStr = reStr

    def __call__(self, value):
        ret = re.findall(self.reStr, value)
        if ret:
            return ret


class Split(object):
    def __init__(self, splitter, takeIndex=None):
        self.splitter = splitter
        self.takeIndex = takeIndex

    def __call__(self, value):
        ret = value.split(self.splitter)
        if self.takeIndex:
            return ret[self.takeIndex]
        else:
            return ret


class Filter(object):
    def __init__(self, filter):
        self.filter = filter

    def __call__(self, value):
        if value:
            return list(filter(self.filter, value))


class Replace(object):
    def __init__(self, fromStr, toStr):
        self.fromStr = fromStr
        self.toStr = toStr

    def __call__(self, value):
        if value:
            return value.replace(self.fromStr, self.toStr)


class desDate2Date(object):
    def __init__(self, formatStr):
        self.formatStr = formatStr

    def __call__(self, value):
        if value:
            return datetime.strptime(value, self.formatStr)


class TakeAt(object):
    def __init__(self, index):
        self.index = index

    def __call__(self, values):
        if len(values) and len(values) > self.index:
            return values[self.index]


class Slice(object):
    def __init__(self, start=0,end=-1,step=1):
        self.start = start
        self.end = end
        self.step = step

    def __call__(self, values):
        return values[self.start:self.end:self.step]


class Have(object):
    def __init__(self, mark):
        self.mark = mark

    def __call__(self, values):
        if self.mark in values:
            return 1
        else:
            return 0



from datetime import datetime, timedelta
def desDateToDate(desDate):
    number = int(getNumberOutStr(desDate) or 1)
    timeUnit = 0
    if desDate.find("年") > 0 or desDate.find("year") > 0:
        timeUnit = 365
    elif desDate.find("月") > 0 or desDate.find("month") > 0:
        timeUnit = 30
    elif desDate.find("周") > 0 or desDate.find("week") > 0:
        timeUnit = 7
    elif desDate.find("天") > 0 or desDate.find("day") > 0:
        timeUnit = 1
    # print("number {} unit {}".format(number, timeUnit))
    _date = datetime.now() - timedelta(days=timeUnit * number)
    return _date.strftime("%Y-%m-%d")


def getNumberOutStr(s):
    ret = re.findall(r"\d+", s)
    if ret is not None and len(ret) == 1:
        return ret[0]
    else:
        return None


VOLUME_DIC = {
    "k": 10**-6,
    "K": 10**-6,
    "m": 10**-3,
    "M": 10**-3,
    "g": 10**0,
    "G": 10**0,
    "": 10**0,
}


def volumeToNumber(s):
    scale = ""
    chars = re.findall(r"[gmkGMK]", s)
    if len(chars) > 0:
        scale = chars[0]
    number = 0
    numbers = re.findall(r"\d+\.?\d*", s)
    if len(numbers) > 0:
        number = float(numbers[0])
    return number * VOLUME_DIC[scale]



if __name__ == "__main__":
    a = list(range(1,20))
    print(Slice(10,-1,3)(a))
    print(TakeAt(-1)(a))
    print(Have(10)(a))
    print(Have(20)(a))
    str_li = ["chaos"]*3
    print(Join(",")(str_li))
    print(Re(r'\d+')("chaos123"))
    print(Split(",")("choas,12,chaos"))
    print(Filter(lambda x: x > 10)(a))
    print(Replace("chaos", "***")("chaos is god"))





