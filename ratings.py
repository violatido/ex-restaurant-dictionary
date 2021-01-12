"""Restaurant rating lister."""

'''
define a function: provide_ratings(text_file):
create: restaurant_dict = {}
open text file: rest_file = open('scores.txt')
create a variable (restaurant_name), equal to input(ask for retaurant name)
create a variable (restaurant_score), equal to input(ask for a score)
add restaurant_name and restaurant_score to restaurant_dict
    restaurant_dict[restaurant_name] = restaurant_score
itertate through file line by line using for loop
    create a variable restaurant_ratings = rstrip().split(':') 
        populate restaurant_dict with [restaurant_ratings[0] = restaurant_ratings[1]
print values of the dictionary using a f string
'''

rest_file = open('scores.txt')

def provide_ratings(text_file):
    ''' Prints out sorted rest ratings from text file '''

    restaurant_dict = {}

    restaurant_name = input("What is the name of the restaurant? >")
    restaurant_score = input("What score do you give the restaurant? >")
    restaurant_dict[restaurant_name] = restaurant_score

    for line in text_file:
        restaurant_ratings = line.rstrip().split(':')
        restaurant_dict[restaurant_ratings[0]] = restaurant_ratings[1]
   
    for key in sorted(restaurant_dict):
        print(f'{key} is rated at {restaurant_dict[key]}')

provide_ratings(rest_file)

#---------------------------------------------------------------------------
