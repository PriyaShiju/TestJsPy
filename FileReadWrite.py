
performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}
schedule_file = open('schedule.txt','w')
for key, val in performances.items():
    schedule_file.write(key + " - " + val + "\n")
schedule_file.close()

"""   """ 
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    print(line)
schedule_file.close()

"""   """ 
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show, time) = line.split(' - ')      
    print(show , time )
schedule_file.close()


"""   """ 
performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show]= time.strip()
schedule_file.close() 
print(performances)


"""   """ 
performances = {}
try:
    schedule_file = open('schedule.txt', 'r')
except FileNotFoundError  as err:
    print(err)

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)

"""   """    