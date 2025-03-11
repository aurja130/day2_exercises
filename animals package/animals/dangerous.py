class Birds: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Goose', 'Eagle', 'Hawk']
        self.type = 'dangerous'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Birds class') 
        for member in self.members: 
           print('\t%s ' % member)

class Mammals: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Tiger', 'Lion', 'Human']
        self.type = 'dangerous'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Mammals class') 
        for member in self.members: 
            print('\t%s ' % member)
            
class Fish: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['Eel', 'Piranha', 'Pufferfish']
        self.type = 'dangerous'
  
  
    def printMembers(self): 
        print(f'Printing members of the {self.type} Fish class') 
        for member in self.members: 
            print('\t%s ' % member)