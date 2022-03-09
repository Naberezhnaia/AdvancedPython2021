def file_reader1(file):
    for line in file:
        yield print(line.strip())

def file_reader2(file):
    while True: 
        line = file.readline()
        if not line:
            break
        yield print(line.strip())

with open('The Dragon by Ray Bradbury.txt', 'r') as file:
    generator1 = file_reader1(file)
    next(generator1)
    next(generator1)
    generator2 = file_reader2(file)
    next(generator2)
    next(generator2)
    for i in range(100):  
        next(generator2)

def repeate(value, num_times: int = 5):
    print('Started.')
    current_num_times = 0
    while True:
        if current_num_times >= num_times:
            break
        print('Before yield.')
        yield print(value)  
        print('After yield.')
        current_num_times += 1
    print('Finished.')

generator = repeate(value=-17.5)
next(generator)
next(generator)
print(type(repeate))

cd 


