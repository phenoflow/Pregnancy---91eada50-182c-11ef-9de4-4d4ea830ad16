# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"Z257.12","system":"readv2"},{"code":"Z254900","system":"readv2"},{"code":"62O6.00","system":"readv2"},{"code":"L296.00","system":"readv2"},{"code":"7F22700","system":"readv2"},{"code":"7F18.00","system":"readv2"},{"code":"L247300","system":"readv2"},{"code":"L340600","system":"readv2"},{"code":"Z257.13","system":"readv2"},{"code":"L247111","system":"readv2"},{"code":"7F22711","system":"readv2"},{"code":"L354100","system":"readv2"},{"code":"L354000","system":"readv2"},{"code":"L411512","system":"readv2"},{"code":"L354.12","system":"readv2"},{"code":"7F19000","system":"readv2"},{"code":"14Y3.00","system":"readv2"},{"code":"L354.11","system":"readv2"},{"code":"L354.00","system":"readv2"},{"code":"62O6.11","system":"readv2"},{"code":"L20..11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-vagin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-vagin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-vagin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
