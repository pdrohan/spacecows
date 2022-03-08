import numpy as np
#this can read a csv file, and execute a greedy algorithm but it cant do it multiple times while updating a list. idk how to figure that out
f = open('ps1_cow_data.txt', 'r')
read_data = f.read()
#print(read_data)
f.close()

#class Cows:
def loadCows(read_data):
    cow_data = read_data.split('\n')
    i = 0
    l = len(cow_data)
    the_cow_list = []
    while i < l:
        txt = cow_data[i]
        name, weight = txt.split(',')
        # this produces the individual dictionaries for every cow
        # cow_dict = {'name': name, 'weight': int(weight)}
        # print(cow_dict)
        cow_list = (name, int(weight))
        the_cow_list.append(cow_list)
        i += 1
    return the_cow_list

cow_list = loadCows(read_data)
#print(cow_list)
#print(type(cow_list))

def getWeight(cow_string):
    weight = cow_string[1]
    return weight

#print(getWeight(cow_list[9]))
#print(type(getWeight(cow_list[9])))

def sort_Cows(cow_list):
    cow_list.sort(key = lambda x: x[1], reverse= True)
    return cow_list

#print(sort_Cows(cow_list))

def greedy_Algo(cow_list, maxCost):
    cow_copy = sort_Cows(cow_list)
    result = []
    trip_num = 0
    totalWeight = 0.0
    #we need a layer that takes the below loop and does it for every trip
    #so we need a way to increment the trips and hold that data for all the trips
    #an issue is that this for loop
    #im going to takle this by making a new function and calls greedy_algo
    #this finds the heaviest cows and puts them in list result and
    for i in range(len(cow_copy)):
        cur_weight = getWeight(cow_copy[i])
        # if the heaviest cow fits in the availible room select it, else go to next cow(increment i)
        if (totalWeight + cur_weight) <= maxCost:
            result.append(cow_copy[i])
            totalWeight += cur_weight
            i += 1
        else:
            i += 1
    return result, totalWeight


print(greedy_Algo(cow_list, 22))
#greedy_algo returns a tuple

#print(type(greedy_Algo(cow_list, 22)))

def getlist(cow_string):
    list = cow_string[0]
    return list

c = getlist(greedy_Algo(cow_list, 22))
print(c)
print(cow_list)


def trip_Tracker(trips_avail, cow_list, maxCost):
    trips_avail = trips_avail
    trip_num = []

    for i in range(len(trips_avail)):
        trip_num[i] = i
        greedy_Algo(cow_list, maxCost)

    # for i in range(0, 10):


#     if len(cow_list_copy) == 0:
#        break
#    else:
#       trip_num += 1
#      trip_list = trip_list.append(getlist(greedy_Algo(cow_list_copy, maxCost)))
#     trip_weight = trip_weight.append(getWeight(greedy_Algo(cow_list_copy, maxCost)))
#    cow_list_copy = cow_list_copy.remove(trip_list)
#   i += 1
# return trip_num, trip_list, trip_weight


+++++++++++++++++++ +=


def trip_Tracker(cow_list, maxCost):
    cow_list_copy = cow_list
    data_tuple = greedy_Algo(cow_list, maxCost)
    print(data_tuple)
    # print(type(data_tuple))
    trip_list = getlist(data_tuple)
    # now we have a list of the cows that have been used, and we need to remove them
    i = 0
    for j in range(trip_list):
        for i in range(cow_list):
            if cow_list[]



