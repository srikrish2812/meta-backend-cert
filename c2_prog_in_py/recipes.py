class Recipe:

    # def __new__(cls: type[Self]) -> Self: # responsible for creating and returning a new empty object
    #     pass

    # def __init__(self) -> None:
    #     pass

    def __init__(self,dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time= time

    def contents(self):
        print("The "+ self.dish + " has " +str(self.items)+ \
            " and takes " + str(self.time) + ' min to prepare')

#pizza = Recipe("Pizza",['cheese', 'bread'],50)
#pizza.contents()
