import csv
def read_csv():
    
    with open("ExcelToCSV.csv", "r") as f:
        
        reader = csv.DictReader(f)

        headers = reader.fieldnames

        
        for line in reader:
            for key in headers:
                print(line[key].upper())

    

def write_csv():
    
    with open("ExcelToCSV.csv", "w") as f:
        
        fieldnames = []

        payload = {}
        
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        
        writer.writerow(payload)


read_csv()
