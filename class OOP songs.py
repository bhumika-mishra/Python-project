class Songs:
    type = "Entertainment"
    def __init__(self,name,genre,yr_of_release,artist_name):
        self.name = name
        self.genre = genre
        self.yr_of_release = yr_of_release
        self.artist_name = artist_name
    def details(self):
        print(f"Name : {self.name} \n Genre : {self.genre} \n Year of Release : {self.yr_of_release}\n Name of the Artist : {self.artist_name}")    

a = input("Enter the Song name : ")    
b = input("Enter the Genre of Song : ")    
c = input("Enter the Year of Release : ")
d = input("Enter the Name of the Artist  : ")
print("\n")

song1 = Songs(a,b,c,d)
song1.details()
print("\n")

song2 = Songs("Mere Dholna","Classical Fusion","2007","Shreya Ghoshal")
song2.details() 
print("\n")

song3 = Songs("Nainowale Ne","Semi-Classical","2018","Neeti Mohan")
song3.details()
print("\n")

song4 = Songs("Naina","Pop","2024","Diljit Dosanjh")
song4.details()
print("\n")

song5 = Songs("Softly","Hip-Hop","2023","Karan Aujla")
song5.details()
print("\n")