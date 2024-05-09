# take value from file and find the avg

def get_avg():
    with open("file\Ex_1.txt",'r') as File:
        data = File.readlines()
    value = data[1:]
    value = [float(i) for i in value]
    avg = sum(value)/len(value)
    return avg
avg = get_avg()
print(avg)