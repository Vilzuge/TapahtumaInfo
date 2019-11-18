
import Api
import UI

def main():
    
    UI.MainMenu()
    TypeChoice = input("Valitse: ")

    if TypeChoice == "1":
        Type = "activities"

    elif TypeChoice == "2":
        Type = "events"

    elif TypeChoice == "3":
        Type = "places"

    else:
        print("Et valinnut mitään, lopetetaan.")
        exit()

    Amount = input("Montako tulosta haluat?: ")
    print("\n")
    print("Tehdään haku.\n\n")

    #Searching data
    Content = Api.Search( Type, Amount )

    #Listing data
    Api.Listing( Content, Amount )

    #More info of certain activity
    UI.AdditionalInfo()
    AdditionalChoice = input("Monennestako?: ")
    Api.AdditionalInfo( Content, AdditionalChoice )


main()
