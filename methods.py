# class piglet:
#     pass

# hamlet = piglet()

# -------------------------------
# class piglet:
#     def speak(self):
#         print("oin oink")


# hamlet = piglet()
# hamlet.speak()

# --------------------------------


# class piglet:
#     name = "piglet"

#     def speak(self):
#         print("oink! I'm {}! Oink!".format(self.name))


# hamlet = piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()
# petunia = piglet()
# petunia.name = "Petunia"
# petunia.speak()

# #------------------------------------


class Piglet:
    years = 0

    def pig_years(self):
        return self.years * 18


piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())
