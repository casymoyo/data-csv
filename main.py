from core.backend import DataExtractor

if __name__ == '__main__':
    data = DataExtractor(['Late-shifts.csv', 'Missed-meds.csv', 'Missed-Shifts.csv'])
    print(data.reader())
    print(data.filter())

