# try it yourself 8-7 exercise
def make_album(name, title):
    """ Return a dictionary of information about artist and album."""
    person = {'artist_name': name, 'album_title': title}
    return person

musician = make_album('MIcheal Jackson','Thriller')
print(musician)

musician = make_album('Marshmello','alone')
print(musician)

musician = make_album('alan walker', 'faded')
print(musician)

# no. of songs as optional
def make_album(name, title, total_songs):
    """ Return a dictionary of information about artist and album."""
    person = {'artist_name': name, 'album_title': title, 'No of songs': total_songs}
    return person

musician = make_album('MIcheal Jackson','Thriller', '5')
print(musician)
