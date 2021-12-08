x=eval(input("请输入一个三位数"))
if x>=100 and x<=999:
    b=int(x/100)
    s=int(x%100/10)
    g=x%10
    print("你输入的三位数是{}，其中百位、十位、个位数分别书{}，{}，{}".format(x,b,s,g))
    if x==b**3+s**3+g**3:
        print("{}是水仙花书".format(x))
    else:
         print("{}不是水仙花书".format(x))
else:
     print("数据输入无效")
    
