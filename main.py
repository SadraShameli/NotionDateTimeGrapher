import glob
import datefinder
import matplotlib.pyplot as plt
from collections import defaultdict

def parse_files():
    entries = []
    for file in glob.glob("**/*.txt"):
        with open(file, "r") as file:
            entries += (file.read().splitlines())
    return entries

start_time_counts = defaultdict(int) 
end_time_counts = defaultdict(int)
def parse_entries(entries):
    for entry in entries:
        dates = list(datefinder.find_dates(entry))
        start_time = dates[0].hour
        end_time = dates[1].hour
        start_time_counts[start_time] += 1
        end_time_counts[end_time] += 1

def find_missing_numbers(dic, boundary):
    new_dict = {}
    for number in range(boundary):
        if number in dic:
         new_dict[number] = dic[number]
        else:
         new_dict[number] = 0
    return new_dict 

def plot_graph():
    start_time_counts_sorted = dict(sorted(find_missing_numbers(start_time_counts, 24).items()))
    end_time_counts_sorted = dict(sorted(find_missing_numbers(end_time_counts, 24).items()))
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.bar(start_time_counts_sorted.keys(), start_time_counts_sorted.values(), color='blue')
    ax1.set_xlabel('Start Times')
    ax1.set_ylabel('Frequency')
    ax1.set_xticks(list(start_time_counts_sorted.keys()))
    ax1.tick_params(axis='x', rotation=45)

    ax2.bar(end_time_counts_sorted.keys(), end_time_counts_sorted.values(), color='red')
    ax2.set_xlabel('End Times')
    ax2.set_ylabel('Frequency')
    ax2.set_xticks(list(end_time_counts_sorted.keys()))
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    entries = parse_files()
    parse_entries(entries)
    plot_graph()

if __name__ == "__main__":
    main()
