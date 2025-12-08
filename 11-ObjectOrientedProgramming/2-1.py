class Song:
   def __init___(self,performer,title,album,year):
      self.perfomer = performer
      self.title = title
      self.album = album
      self.year = year
      self.song = [performer,title,album,year]
   def __str__(self):
      print({self.perfomer})
      print({self.title})
      print({self.album})
      print({self.year})
      

# object creation
song1 = Song('Ed Shreeran',"Hearts Don't Break Around Here",'Divide',2017)
song2 = Song('Queen','Bohemian Rhapsody','A Night at the Opera',1975)

## object usage
print(song1.__str__())
print(song2.__str__())