class Birds: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Chicken', 'Turkey', 'Duck']
        self.type = 'harmless'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Birds class') 
        for member in self.members: 
           print('\t%s ' % member)

class Mammals: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Cow', 'Goat', 'Elephant']
        self.type = 'harmless'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Mammals class') 
        for member in self.members: 
            print('\t%s ' % member)
            
class Fish: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Salmon', 'Tuna', 'Goldfish']
        self.type = 'harmless'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Fish class') 
        for member in self.members: 
            print('\t%s ' % member)