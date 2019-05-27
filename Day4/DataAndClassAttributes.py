class testPrivateMembers:
    def __init__(self, attribute="default", name="instance", sysV="sysVar"):
        self.name = name  # public attribute
        self.__attriubute = attribute  # private attribute
        self.__sysVar__ = sysV

    def __str__(self):
        return "{} has attribute {} and {}".format(
            self.name, self.__attriubute, self.__sysVar__
        )


inst = testPrivateMembers(name="testClass", attribute="member")

print(inst)

print(inst.name)

print(inst.__sysVar__)

# print(inst.__attribute)

#print(dir(inst))

print(inst._testPrivateMembers__attriubute)
