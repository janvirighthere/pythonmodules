def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number: "))
        except:
            print("I wa not a number")
            continue
        else:
            print("Yes that was a number")
            break
        finally:
            print("End")

