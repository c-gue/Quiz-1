import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
outfile = open('weapons.txt','r')


# create a csv object from the file object
#final = open('final.csv','w')


#skip the header row
next(outfile)

#create an empty dictionary named 'weapons_dict'
weapons_dict = {}



#use a for loop to iterate through every row of the csv file
for line in outfile:
    #use variables for name,speed and range (optional)
    record = line.strip()
    weapons_list = record.split(',')
    #print(weapons_list)

    wname = weapons_list[0]
    wspeed = weapons_list[1]
    wdistance = weapons_list[2]

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    weapon = w.Weapon(wname,wspeed,wdistance)

    # append the name and bullet count to 'weapons_dict'
    weapons_dict['weapon name: '] = weapon.get_name()
    weapons_dict['Number of bullets: '] = weapon.get_bullets()

    # print out the name of the weapon using the appropriate method of the object 
    print("Name:",weapon.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    print("Speed:",weapon.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    print("Range:",weapon.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print("Bullets:",weapon.get_bullets())
    
    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    while weapon.get_bullets() > 0:
        # call the appropriate method to fire a bullet
        weapon.fire_bullet()
        # print out the bullet count every time the weapon is fired
        print('bullets remaining...',weapon.get_bullets(),end='\r')

    


#using a loop print out the name and number of bullets from the dictionary

for i in weapons_dict:
    print(i)




    



