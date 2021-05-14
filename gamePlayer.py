class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.isRunning = False

    def run(self):
        # print(f'{self.name} is running')
        self.isRunning = True
        return ''

    def stop_running(self):
        self.isRunning = False

    def action(self):
        if self.isRunning:
            print(f'{self.name} is running')
        else:
            print(f'{self.name} is not running')


p1 = PlayerCharacter("Jones", 23)
p2 = PlayerCharacter("Watson", 44)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p2.run())
p2.action()
p2.stop_running()
p2.action()

help(p2)
