def sportDay(t,sport):
    for i in range(t):
        n = int(input())
        last = 0
        join = 0
        time_table = []
        for j in range (n):
            s,e = map(int,input().split())
            x = (s,e)
            time_table.append(x)
            new_table = sorted(time_table,key=lambda x: x[1])
        for final in new_table:
            if(last == 0):
                last = final[1]
                join += 1
            elif(final[0] >= last):
                last = final[1]
                join += 1
        sport.append(join)
    for k in sport:
        print(k)
        
def main():
    t = int(input())
    sport = []
    sportDay(t,sport)
    
if __name__ == "__main__":
    main()