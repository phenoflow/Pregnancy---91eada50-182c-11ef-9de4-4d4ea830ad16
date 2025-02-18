# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"L21..11","system":"readv2"},{"code":"Z261.00","system":"readv2"},{"code":"62X4.00","system":"readv2"},{"code":"L161.13","system":"readv2"},{"code":"L180811","system":"readv2"},{"code":"L19..00","system":"readv2"},{"code":"L169200","system":"readv2"},{"code":"L180900","system":"readv2"},{"code":"L169300","system":"readv2"},{"code":"L16C100","system":"readv2"},{"code":"Z22C312","system":"readv2"},{"code":"L123500","system":"readv2"},{"code":"62X2.00","system":"readv2"},{"code":"L16C000","system":"readv2"},{"code":"Z261100","system":"readv2"},{"code":"62X3.00","system":"readv2"},{"code":"Z22C300","system":"readv2"},{"code":"L140200","system":"readv2"},{"code":"62X0.00","system":"readv2"},{"code":"Z261200","system":"readv2"},{"code":"62X..00","system":"readv2"},{"code":"62X1.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-gestationis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-gestationis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-gestationis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
