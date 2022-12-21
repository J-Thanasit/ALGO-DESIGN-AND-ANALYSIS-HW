def BrocotPath(n,m):
    n1 = 0
    n2 = 1
    m1 = 1
    m2 = 0
    BrocotPath = ""
    while(n1+n2 != n and m1+m2 != m ):
        if ((n1+n2)/(m1+m2) < n/m):
            BrocotPath += "R"
            n1+=n2
            m1+=m2
        elif((n1+n2)/(m1+m2) > n/m):
            BrocotPath += "L"
            n2+=n1
            m2+=m1
    return BrocotPath

def main():
    n, m = map(int, input().split())
    print(BrocotPath(n,m))
 
if __name__ == "__main__":
    main()