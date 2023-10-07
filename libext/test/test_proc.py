from libext import proc 
def test_Filter():
    assert proc.Filter(None)([None, 10, "str"]) == [10, "str"]
    assert proc.Filter(lambda x: x != "str")([None, 10, "str"]) == [None, 10]
    assert proc.Filter(lambda x: x != 10)([None, 10, "str"]) == [None, "str"]


def test_Replace():
    assert proc.Replace("s", "S")("str") == "Str"


def test_TakeAt():
    assert proc.TakeAt(0)(["str", "str"]) == "str"


def test_Slice():
    assert proc.Slice(0, 1, 1)([1, 2, 3, 4, 5, 6, 7, 8]) == [1]
    assert proc.Slice(0, 1)([1, 2, 3, 4, 5, 6, 7, 8]) == [1]
    assert proc.Slice(1, 2)([1, 2, 3, 4, 5, 6, 7, 8]) == [2]
    assert proc.Slice(1, 10)([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 3, 4, 5, 6, 7, 8]
    assert proc.Slice(1, 10, 2)([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


def test_Have():
    assert proc.Have(1)([1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert proc.Have(6)([1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert proc.Have(11)([1, 2, 3, 4, 5, 6, 7, 8]) == False


def test_Every():
    assert proc.Split(' ',-1)("a b c") == "c"
    li = ["a b c",'aa',None,'c b a']
    assert proc.Every(proc.Split(' ',-1))(li) == ["c",'aa','a']

