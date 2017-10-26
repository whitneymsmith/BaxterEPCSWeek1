def main():
    age = int(raw_input("what is your age?"))
    if age < 17:
        parentalGuidance = get_bool("Is there Adult suppervision?")
        #parentalGuidance = int(raw_input("Is there adult suppervision?"))
    else:
        parentalGuidance = True
    print(getMovieByAge(age, parentalGuidance))

def get_bool(prompt):
    while True:
        try:
           return {"yes":True,"no":False}[raw_input(prompt).lower()]
        except KeyError:
           print "Invalid input please enter yes or no!"

def get_int(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print "can not watch movie without Adult!"

class Movie():
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    def __repr__(self):
        return str(self.name) + ", " + str(self.year) + ", " + str(self.rating)

    def isAgeAppropriate(self, age, parentalGuidance ):
        rating = self.rating

        if rating == "NR":
            if age > 16:
                return True
            elif parentalGuidance is True:
                return True
            else:
                 return False
        #'NR' and age < 17 and not parentalGuidance :
        #else
          #return False
        if rating == "PG":
            if age >= 13:
                return True
            elif parentalGuidance is True:
                return True
            else:
                 return False

        if rating == "G":
                 return True


movies = [
    Movie("Moana",2016,"PG"),
    Movie("Snow White",1937,"G"),
    Movie("The Reluctant Dragon",1941,"NR"),
    Movie("Dumbo",1941,"G"),
    Movie("Bambi",1942,"G"),
    Movie("So Dear To My Heart",1948,"G"),
    Movie("Cinderella",1950,"G"),
    Movie("Alice And Wonderland",2010,"PG"),
    Movie("Peter Pan",2003,"PG"),
    Movie("Lady And The Tramp",1955,"NR"),
    Movie("Old Yeller",1957,"G"),
    Movie("Sleeping Beauty",1959,"PG"),
    Movie("101 Dalmatians",1996,"G"),
    Movie("The Parent Trap",1998,"PG"),
    Movie("The Jungel Book",2016,"PG"),
    Movie("The Rescuers",1977,"G"),
    Movie("Never Cry Wolf",1983,"PG"),
    Movie("Beauty And The Beast",2017,"PG"),
    Movie("Aladin",1992,"G"),
    Movie("A Far Off Place",1993,"PG"),
    Movie("The Lion King",1994,"G"),
    Movie("Pocahontas",1995,"G"),
    Movie("Freaky Friday",2003,"PG"),
    Movie("Mulan",1998,"G"),
    Movie("A Bugs Life",1998,"G"),
    Movie("Dont Look Under The Bed",1999,"NR"),
    Movie("Endurance",1999,"G"),
    Movie("The Ugly Duckling",1939,"NR")
]

def getMovieByAge(age, parentalGuidance) :
    outputMovies = []
    for movie in movies:
        if(movie.isAgeAppropriate(age, parentalGuidance)) :
            outputMovies.append(movie)
    return outputMovies



main()
