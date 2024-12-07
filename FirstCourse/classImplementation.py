class Character:
    character_no = 0
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        
        Character.character_no+=1
    def double_speed(self):
        self.speed *= 2
    def speed(self):
        return self.speed
    
    @classmethod
    def set_character_no(cls,amt):
        cls.character_no = int(amt)

    @staticmethod
    def ishigh(health):
        if int(health)==100:
            return True
        else:
            return False


a=input("the thing:")
a=int(a)
warrior = Character(100,50,a)
ninja = Character(80,40,40)

print("Warrior speed: ",warrior.speed)
print("Ninjaspeed: ",ninja.speed)
warrior.double_speed()

print(f"the speed was doubled for the warrior")

print(f"Warrior speed: {warrior.speed}")
print(f"Ninjaspeed: {ninja.speed}")

#print with reference
print(f"\nwith reference\n")

print(f"Warrior speed: {Character.speed(warrior)}")
print(f"Ninjaspeed: {Character.speed(ninja)}")
print(f"\n\n\nToatal no of the character made: {Character.character_no}")
Character.set_character_no(23)
print(f"\n\n\nToatal no of the character made: {Character.character_no}")
print(ninja.__dict__)

#check if the health of the characters is full
print(" Is the health of the character full???")
print(Character.ishigh(ninja.health))
