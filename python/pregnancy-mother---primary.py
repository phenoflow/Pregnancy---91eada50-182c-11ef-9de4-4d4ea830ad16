# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"Lyu0200","system":"readv2"},{"code":"L11y.00","system":"readv2"},{"code":"7F24y00","system":"readv2"},{"code":"L35y.00","system":"readv2"},{"code":"7Fy..00","system":"readv2"},{"code":"7F2..00","system":"readv2"},{"code":"L13y.00","system":"readv2"},{"code":"L253.00","system":"readv2"},{"code":"7F24.00","system":"readv2"},{"code":"7F2y.00","system":"readv2"},{"code":"L35..00","system":"readv2"},{"code":"L10y.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-mother---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-mother---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-mother---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
