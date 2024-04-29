def main():
    n = int(input())
    count = 1
    i = 1
    while i < n:
        i *= 2
        count += 1
    
    print(count)


if __name__=="__main__": 
    main()