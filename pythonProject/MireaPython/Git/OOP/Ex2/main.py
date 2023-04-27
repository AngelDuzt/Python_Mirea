class Myclass:
    def myprint(self):
        print(123)

    def search_by_name(self, string):
        getattr(self, string)()



obj = Myclass()
obj.search_by_name("myprint")
