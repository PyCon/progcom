#!/usr/bin/env python

import logic as l
import csv
import sys

def main(out):
    q = "SELECT schedules.*, proposals.data->>'title' as title from schedules JOIN proposals ON proposals.id=schedules.proposal"
    keys = ('proposal', 'day', 'room', 'time', 'duration', 'title')
    with open(out, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        for row in l.fetchall(q):
            writer.writerow([str(getattr(row, k)) for k in keys])

if __name__ == "__main__":
    main(sys.argv[1])
