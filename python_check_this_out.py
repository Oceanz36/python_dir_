class The_mighty_ships:
    def __init__(self, name, length, width, draft, speed):
        self.name = name
                    
        self.length = 150  # in meters
        self.width = 50   # in meters
        self.draft = 10
        self.speed = 18 
           

    def calculate_displacement(self):
        # Simplified formula for displacement (in cubic meters)
        return self.length * self.width * self.draft

    def display_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Length: {self.length} m")
        print(f"Width: {self.width} m")
        print(f"Draft: {self.draft} m")
        print(f"Displacement: {self.calculate_displacement()} cubic meters")

    def sail(self):
        self.time = 5  # hours
        print(f"{self.name} is sailing at {self.speed} knots for {self.time}")
        return self.speed * self.time
    


    def stop (self):
        
        self.speed = 10 # knots
        if self.speed <= 0:
            print(f"{self.name} has stopped.")

        elif self.speed > 0:
            print(f"{self.name} is still moving at {self.speed} knots.")
            print("keep seated and wait for further instructions.")


        
        

    
Cruiser1 = The_mighty_ships("Cruiser1", 150, 50, 10, 18)
Cruiser1.display_info()
Cruiser1.sail()

Cruiser1.stop()

        
