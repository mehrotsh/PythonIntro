class Shark:
    """
    Class is used for displaying class features
    """
    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")

    #def __str__(self):
    #    return self.name

    def __repr__(self):
       return '%s("%s", %s)' % (self.__class__.__name__, self.name, self.age)


    # Equlity
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.name == other.name and self.age == other.age
        return False
    
    # Hash 
    def __hash__(self):
        return hash((self.name, self.age))


def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)

    # Print out instance variable name
    print(sammy.name)

    # Print out class variable location
    print(sammy.location)

    # Second object
    stevie = Shark("Stevie", 8)

    # Print out instance variable name
    print(stevie.name)

    # Use set_followers method and pass followers instance variable
    stevie.set_followers(77)

    # Print out class variable animal_type
    print(stevie.animal_type)

    #Special methods

    #String methods
    print(stevie)
    print(repr(stevie))  # equivalent to just writing the object in Jupytr

    # __doc__
    print(stevie.__doc__)

    # __dict__ mehtod
    print(stevie.__dict__)


    # equality comparison
    stevie_n = Shark("Stevie", 8)
    print(stevie==stevie_n)

if __name__ == "__main__":
    main()
