import os

#Global Data
data_one = "process1.txt"
data_tow = "process2.txt"
data_a = "process3.txt"


class Process:
    def __init__(self, number:int, arrival:int, burst_time:int, priority:int, start_time:int, end_time:int):
        self.number = number
        self.arrival = arrival
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time
    
    def s(self) -> str:
        return "" + str(self.number) + " " + str(self.arrival) + " " + str(self.burst_time) + " " + str(self.priority) + " " + str(self.start_time) + " " + str(self.end_time) 

def Load_Data(fname):
    temp = []
    array = []

    with open(fname, 'r') as file:
        for line in file:
            #print(line, end = "")
            temp.append(line.split())

    del temp[0]

    for x in temp:
        array.append(Process(int(x[0]), int(x[1]), int(x[2]), int(x[3]), 0, 0))

    #for x in array:
    #   print(x.show_self())
    return array

def show_data(fname):
    with open(fname, 'r') as file:
        for line in file:
            print(line, end = "")
    print()

def pause():
    print("\nPress any key...")
    input()
    os.system("cls")

def sortthis(process, _by):
    if _by == 'num':
        return sorted(process, key=lambda process: process.number) #this syntax is from the net I cant explain it.
    elif _by == 'arv':
        return sorted(process, key=lambda process: process.arrival)
    elif _by == 'burst':
        return sorted(process, key=lambda process: process.burst_time)
    elif _by == 'prio':
        return sorted(process, key=lambda process: process.priority)

def get_from():
    try:
        data = input("?:")
        data = int(data) #error occurs here for if str is forced to become int

        if data == 1:
            return data_one
        elif data == 2:
            return data_tow
        elif data == 2:
            return data_a
        else:
            raise ValueError #error is forced to occur here because there is no file. 
    except ValueError as e:
        print("No such file") 

def ghant(process):
    count = 0
    space = 3
    print(10*9*"=")
    for x in process:
        if len(str(x.number)) == 2:
            space = 2
        count+=1
        print("|" + 2*" " + "P" + str(x.number) + space*" " + "|", end="")
        if count == 10:
            count = 0
            print()
            print(10*9*"=")

def ghant2(process):
    temp = process.copy()

    while temp:
        count = 0
        space = 3
        first_mult = 0
        if len(temp) >= 10:
            first_mult = 10
        else:
            first_mult = len(temp)

        print(first_mult*9*"=")

        for x in temp:
            if len(str(x.number)) == 2:
                space = 2
            elif len(str(x.number)) == 1:
                space = 3
            count+=1
            print("|" + 2*" " + "P" + str(x.number) + space*" " + "|", end="")
            if count == 10:
                count = 0
                print()
                print(10*9*"=")
                break
        if count != 0:
            count = 0
            print()
            print(len(temp)*9*"=")

        for x in temp:
            count+=1
            indent = 9 - len(str(x.start_time))
            print(str(x.start_time) + indent*" ", end = "")
            if count == 10:
                count = 0
                print(str(x.end_time))
                break

        if count != 0:
            count = 0
            print(str(x.end_time))

        for x in temp[:]:
            count+=1
            if x == temp[0]:  # check if the element is the first element
                temp.remove(x)
            if count == 10:
                count = 0
                break

        print()

def FCFS(fname):
    process =  Load_Data(fname)
    time = avg1 = avg2 = 0

    for x in process:
        x.start_time = time
        time = time + x.burst_time
        x.end_time = time
    
    print("First Come First Serve")

    ghant2(process)
    
    print("Process\t\tWaiting Time\t\tTurnaround Time")
    for x in process:
        print(str(x.number) + "\t\t" + str(x.start_time) + "\t\t\t" + str(x.end_time))
        avg1 = avg1 + x.start_time
        avg2 = avg2 + x.end_time

    print("\n")
    print("The average waiting time is " + str(avg1/len(process)))
    print("The average turnaround time is " + str(avg2/len(process)))
    

def SJF(fname):
    process =  Load_Data(fname)
    process = sortthis(process, 'burst')
    time = avg1 = avg2 = 0

    for x in process:
        x.start_time = time
        time = time + x.burst_time
        x.end_time = time
    
    print("Shortest Job First")

    ghant2(process)

    process = sortthis(process, 'num')
    
    print("Process\t\tWaiting Time\t\tTurnaround Time")
    for x in process:
        print(str(x.number) + "\t\t" + str(x.start_time) + "\t\t\t" + str(x.end_time))
        avg1 = avg1 + x.start_time
        avg2 = avg2 + x.end_time

    print("\n")
    print("The average waiting time is " + str(avg1/len(process)))
    print("The average turnaround time is " + str(avg2/len(process)))


def SRPT(fname):
    process =  Load_Data(fname)
    tasks = []
    for_ghant = []
    process = sortthis(process, 'arv')
    time = -1
    avg1 = avg2 = 0


    for x in process:
        time+=1
        if len(tasks) == 0: 
            for_ghant.append(Process(x.number, x.arrival, x.burst_time, x.priority, time, 0)) 
            
        if len(tasks) != 0:
            tasks[0].burst_time-=1

        tasks.append(Process(x.number, x.arrival, x.burst_time, x.priority, time, 0))
        tasks = sortthis(tasks, 'burst')

        #print(str(for_ghant[(len(for_ghant))-1].number) + "||" + str(tasks[0].number))
        if for_ghant[(len(for_ghant))-1].number != tasks[0].number:
            for_ghant[(len(for_ghant))-1].end_time = time
            #print("here" + str(time))
            for_ghant.append(Process(x.number, x.arrival, x.burst_time, x.priority, time, 0))

        #print("testing attention please -> t" + str(time))
        #print("task1")
        #for x in tasks:
        #    print(x.s())
        #print()
        #
        #print("ghant1")
        #for x in for_ghant:
        #    print(x.s())
        #print()
        #
        #print(100*"==")

    time = time + tasks[0].burst_time
    for_ghant[(len(for_ghant))-1].end_time = time
    del tasks[0]
    
    for x in tasks:
        for_ghant.append(x)
        for_ghant[(len(for_ghant))-1].start_time = time
        time = time + x.burst_time
        for_ghant[(len(for_ghant))-1].end_time = time

    for x in process:
        yes = 0
        for y in reversed(for_ghant):
            if x.number == y.number:
                yes+=1
                if yes == 1:
                    x.start_time+=y.start_time
                    x.end_time+=y.end_time
                else:
                    subtract = y.start_time - y.end_time
                    x.start_time+=subtract
        x.start_time-=x.arrival
    
    print("Shortest Remaining Processing Time")

    ghant2(for_ghant)

    print("Process\t\tWaiting Time\t\tTurnaround Time")
    for x in process:
        
        
        print(str(x.number) + "\t\t" + str(x.start_time) + "\t\t\t" + str(x.end_time))
        avg1 = avg1 + x.start_time
        avg2 = avg2 + x.end_time

    print("\n")
    print("The average waiting time is " + str(avg1/len(process)))
    print("The average turnaround time is " + str(avg2/len(process)))
    

def Priority(fname):
    process =  Load_Data(fname)
    process = sortthis(process, 'prio')
    time = avg1 = avg2 = 0

    for x in process:
        x.start_time = time
        time = time + x.burst_time
        x.end_time = time
    
    print("Priority")

    ghant2(process)

    process = sortthis(process, 'num')
    
    print("Process\t\tWaiting Time\t\tTurnaround Time")
    for x in process:
        print(str(x.number) + "\t\t" + str(x.start_time) + "\t\t\t" + str(x.end_time))
        avg1 = avg1 + x.start_time
        avg2 = avg2 + x.end_time

    print("\n")
    print("The average waiting time is " + str(avg1/len(process)))
    print("The average turnaround time is " + str(avg2/len(process)))


def RoundRobin(fname):
    process =  Load_Data(fname)
    for_ghant = []
    time = avg1 = avg2 = total_time = 0
    time_slice = 4

    for x in process:
        total_time+=x.burst_time

   
    while time != total_time:
        for x in process:
            if x.burst_time != 0:
                for_ghant.append(Process(x.number, x.arrival, x.burst_time, x.priority, time, 0))
                if x.burst_time > time_slice:
                    #print("im here")
                    time = time + time_slice
                    x.burst_time-=time_slice
                else:
                    time = time + x.burst_time
                    x.burst_time-=x.burst_time
                for_ghant[len(for_ghant)-1].end_time = time

    for x in process:
        yes = 0
        for y in reversed(for_ghant):
            if x.number == y.number:
                yes+=1
                if yes == 1:
                    x.start_time+=y.start_time
                    x.end_time+=y.end_time
                else:
                    subtract = y.start_time - y.end_time
                    x.start_time+=subtract

    print("Round Robin")

    ghant2(for_ghant)
    
    print("Process\t\tWaiting Time\t\tTurnaround Time")
    for x in process:
        print(str(x.number) + "\t\t" + str(x.start_time) + "\t\t\t" + str(x.end_time))
        avg1 = avg1 + x.start_time
        avg2 = avg2 + x.end_time

    print("\n")
    print("The average waiting time is " + str(avg1/len(process)))
    print("The average turnaround time is " + str(avg2/len(process)))

def main():
    File_name = get_from()
    os.system("cls")

    #show_data(File_name)
    #pause()

    #FCFS(File_name)
    #pause()

    #SJF(File_name)
    #pause()

    #SRPT(File_name)
    #pause()

    #Priority(File_name)
    #pause()

    #RoundRobin(File_name)
    #pause()
main()
    
