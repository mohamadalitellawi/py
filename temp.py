

def to_celsius (fehrenheit):
    return (fehrenheit - 32 ) * 5/9

def to_fehrenheit (celsius):
    return celsius * 9/5 + 32


def main():
    for temp in range(0,212,40):
        print(f"Fehrenhit = {round(to_fehrenheit(temp))}\t({temp})")
    print()
    for temp in range(0,100,20):
        print(f"Celsius = {round(to_celsius(temp))}\t({temp})")

if __name__ == "__main__":
    main()