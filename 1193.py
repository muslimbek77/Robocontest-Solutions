def don_don_ziki(Ali,Vali,Gani):
    if Ali == "qog'oz" and Vali == Gani == "quduq":
        print("Ali")
    elif Vali == "qog'oz" and Gani == Ali == "quduq":
        print("Vali")
    elif Gani == "qog'oz" and Vali == Ali == "quduq":
        print("G'ani")

    elif Ali == "qaychi" and Vali == Gani == "qog'oz":
        print("Ali")
    elif Vali == "qaychi" and Gani == Ali == "qog'oz":
        print("Vali")
    elif Gani == "qaychi" and Vali == Ali == "qog'oz":
        print("G'ani")

    elif Ali == "quduq" and Vali == Gani == "qaychi":
        print("Ali")
    elif Vali == "quduq" and Gani == Ali == "qaychi":
        print("Vali")
    elif Gani == "quduq" and Vali == Ali == "qaychi":
        print("G'ani")
    else :
        print("?")
    
    

Ali = input()
Vali = input()
Gani = input()
don_don_ziki(Ali,Vali,Gani)