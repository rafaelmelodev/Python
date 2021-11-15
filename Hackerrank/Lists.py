if __name__ == '__main__':
    n = int(input())
    
arr = []

for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("arr."+cmd)
    else:
        print (arr)