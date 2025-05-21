a=[1,2,3]
b=3
try:
    def Index(val1,val2):
        if isinstance(val1,str) and isinstance(val2,str)==False:
            raise Exception("Provide val1 and val2 as str only")
        if isinstance(val1,list):
            if not isinstance (val2,str) and not isinstance(val2,int):
                raise Exception("Val1 and val2 both are not str or not int provide string or integer")
        return val1.index(val2)
    print(Index(a,b))
except Exception as e:
    print(e)