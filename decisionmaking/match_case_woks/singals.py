

singal = input("enter signal")

match singal:

    case "red":print("STOP")

    case "green":print("GO")

    case "yellow":print("WAIT")

    case _:print("invalid")

