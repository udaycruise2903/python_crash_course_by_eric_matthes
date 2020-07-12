# try it yourself 8-8 exercise
def make_album(name, title):
    """ Return a dictionary of information about artist and album."""
    person = {'artist_name': name, 'album_title': title}
    return person

while True:
    print("\n Please tell the details of artist and their album")
    print("(Press 'q' to quit the program)")
    
    name = input('artist name: ')
    if name == 'q':
        break
    title = input('album_title: ')
    if title == 'q':
        break
    details = make_album(name, title)
    print(details)
    
