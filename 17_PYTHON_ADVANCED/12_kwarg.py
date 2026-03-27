def marks(**kwarg):
    for i in kwarg.keys():
        print(f"{i} is having a mark of {kwarg[i]}")


marks(Anu=89,manu=90,sam=98)