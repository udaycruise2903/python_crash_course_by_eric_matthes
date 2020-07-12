# try it yourself exercise 8-12 
# programmer: UDay Date: 20-apr-2020
def make_hotel_menu(*items):
    """Prepare a Hotel Menu with the following items."""
    print("\n The following items are available in the hotel menu.")
    for item in items:
        print("->" + item)
    
make_hotel_menu('Masala Dosa', 'Idly', 'Vada', 'Ricebath')
make_hotel_menu('roti dal', 'Paneer tikka', 'butter nan')
make_hotel_menu('curd rice', 'sambhar rice', 'bajji')
 
