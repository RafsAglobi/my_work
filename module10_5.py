from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
            all_data.append(line)


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = datetime.now()

for f in files:
    read_info(f)

end1 = datetime.now()
print(f'{end1 - start1} (линейный)')

if __name__ == '__main__':
    start2 = datetime.now()
    with Pool(processes=len(files)) as pool:
        pool.map(read_info, files)

    end2 = datetime.now()
    print(f'{end2 - start2} (многопроцессный)')