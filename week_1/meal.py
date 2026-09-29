def main():
    input_time = input("What time is it? ")
    x = convert(input_time)
    if 7<=x<=8:
        print("breakfast time")
    elif 12<=x<=13:
        print("lunch time")
    elif 18<=x<=19:
        print("dinner time")
    
    


def convert(time):
    x,y = time.split(":")
    x=int(x)
    y=int(y)/60
    return x+y





if __name__ == "__main__":
    main()