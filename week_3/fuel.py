while True:
    try:
        fuel = input("Fraction: ")
        x , y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or x > y:
            continue
        z = (x/y)*100
        if z <= 1:
            print("E")
            break
        elif z >= 99:
            print("F")
            break
        else:
            print(f"{round(z)}%")
            break



    except ValueError:
        pass
    except ZeroDivisionError:
        pass