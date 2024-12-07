class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def double_speed(self):
        self.speed *= 2

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
