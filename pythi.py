marks=int(input())

if marks>90 and marks<100:
    print("A+")
else:
    if marks>80 and marks<90:
        print("A")
    else:
        if marks>70 and marks<80:
            print("B+")
        else:
            if marks>60 and marks<70:
                print("B")
            else:
                if marks>50 and marks<60:
                     print("C+")
                else:
                    if marks>40 and marks<50:
                        print("C")
                    else:
                        if marks<35:
                            print("Fail")
                        else: 
                            print("Invalid number")