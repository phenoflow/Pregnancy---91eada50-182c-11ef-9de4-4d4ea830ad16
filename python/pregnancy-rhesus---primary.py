# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"L261100","system":"readv2"},{"code":"5847","system":"readv2"},{"code":"5842","system":"readv2"},{"code":"584..12","system":"readv2"},{"code":"5849","system":"readv2"},{"code":"584Z.00","system":"readv2"},{"code":"5848","system":"readv2"},{"code":"584..11","system":"readv2"},{"code":"5843","system":"readv2"},{"code":"5845","system":"readv2"},{"code":"5846","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-rhesus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-rhesus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-rhesus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
