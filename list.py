


def main():
    lo = ["A","B","C"]
    li = [lo] * 10
    lo[1]=5
    lo[-1] = 0
    li[0] = "start"
    li.append("end")

    while True:
        try:
            li.remove(lo)
        except:
            break
    li.insert(1,lo)
    li.insert(1,lo)

    li.pop(1)

    print (li)
    
    print (li[::-1])
    print(f"start word index is {li.index('start')}")
    print(f"list length is {len(li)}")

    for item in li:
        print(item)
    i = 0
    while i < len(li):
        print(li[i])
        i +=1

if __name__ == "__main__":
    main()