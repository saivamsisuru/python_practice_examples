wkn=input("Enter week name: ")
if (wkn.isalnum() and wkn.upper() not in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]):
    print("given week name is not a week")
else:
    match(wkn.upper()[:3]):
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is working Day".format(wkn))
        case "SAT":
            print("{} is week end".format(wkn))
        case "SUN":
            print("{} is HOLIDAY".format(wkn))
        case _:
            print("given week name is not week day")
