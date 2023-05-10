#Global Data
data_one = "process1.txt"
data_tow = "process2.txt"


class Process:
    def __init__(self, number:int, arrival:int, burst_time:int, priority):
        self.number = number
        self.arrival = arrival
        self.burst_time = burst_time
        self.priority = priority
    
    def show_self(self) -> str:
        return "" + str(self.number) + " " + str(self.arrival + " " + str(self.burst_time) + " " + str(self.priority))

def Load_Data(array:[]):
    temp:[] = []

    with open(data_one, 'r') as file:
        for line in file:
            temp.append(line.split())
    del temp[0]

    for x in temp:
        array.append(Process(x[0], x[1], x[2], x[3]))
    
    for x in array:
        print(x.show_self())

    return array
    
def main():
    process:[] = []
    Load_Data(process)

main()
    
