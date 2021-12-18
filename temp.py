
"""
this module contains functions for converting between degrees fehrenheit and degrees Celsius 
"""
def to_celsius (fehrenheit):
    """
    Accept degrees fehr.
    Return degrees cels.
    """
    return (fehrenheit - 32 ) * 5/9

def to_fehrenheit (celsius:float) -> float:
    return celsius * 9/5 + 32


def main():
    for temp in range(0,212,40):
        print(f"Fehrenhit = {round(to_fehrenheit(temp))}\t({temp})")
    print()
    for temp in range(0,100,20):
        print(f"Celsius = {round(to_celsius(temp))}\t({temp})")

if __name__ == "__main__":
    main()