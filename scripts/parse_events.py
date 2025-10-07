import csv
from collections import Counter

def main(filename='docs/sanitized_events.csv'):
   with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        counts = Counter(row.get('EventType','UNKNOWN') for row in reader)
       for event, num in counts.most_common():
        print(f"{event}: {num}")

     if __name__ == "__main__":
    main()    
