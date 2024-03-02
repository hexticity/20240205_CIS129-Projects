def getTotalHotDogs():
    attendees = int(input("Enter the number of people attending the cookout: "))
    hotDogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))
    total_hot_dogs = attendees * hotDogs_per_person
    return total_hot_dogs

def showResults(total):
    DOGS = 10
    BUNS = 8
    
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
    
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))
    
    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)

def main():
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

if __name__ == "__main__":
    main()
