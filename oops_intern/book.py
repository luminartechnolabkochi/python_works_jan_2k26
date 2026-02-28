


class Movie:

    def __init__(self,title,lang):

        self.title = title

        self.lang = lang

    def display(self):

        print(self.title,self.lang)


movie_intance = Movie("arm","malayalam")

movie_intance.display()

movie_intance2= Movie("kgf","telungu")

movie_intance2.display()

