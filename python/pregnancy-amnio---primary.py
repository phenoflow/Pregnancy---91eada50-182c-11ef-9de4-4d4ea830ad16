# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"Z264.12","system":"readv2"},{"code":"L27..11","system":"readv2"},{"code":"62F3.00","system":"readv2"},{"code":"L284.12","system":"readv2"},{"code":"L270100","system":"readv2"},{"code":"L280300","system":"readv2"},{"code":"L280z00","system":"readv2"},{"code":"7F05111","system":"readv2"},{"code":"Q013.11","system":"readv2"},{"code":"L431200","system":"readv2"},{"code":"L28y.13","system":"readv2"},{"code":"L284100","system":"readv2"},{"code":"62F7.00","system":"readv2"},{"code":"L270.00","system":"readv2"},{"code":"7F10100","system":"readv2"},{"code":"62F4.00","system":"readv2"},{"code":"7F05z00","system":"readv2"},{"code":"62F8.00","system":"readv2"},{"code":"7F05.00","system":"readv2"},{"code":"62F2.00","system":"readv2"},{"code":"L27z.00","system":"readv2"},{"code":"62F6.00","system":"readv2"},{"code":"L280.00","system":"readv2"},{"code":"Lyu3B00","system":"readv2"},{"code":"L431100","system":"readv2"},{"code":"L280000","system":"readv2"},{"code":"Z264500","system":"readv2"},{"code":"L280100","system":"readv2"},{"code":"7F10000","system":"readv2"},{"code":"L284.00","system":"readv2"},{"code":"L284.11","system":"readv2"},{"code":"L270000","system":"readv2"},{"code":"7F05200","system":"readv2"},{"code":"62FZ.00","system":"readv2"},{"code":"L27..00","system":"readv2"},{"code":"62F9.00","system":"readv2"},{"code":"L284z00","system":"readv2"},{"code":"L431.00","system":"readv2"},{"code":"L270z00","system":"readv2"},{"code":"62F..00","system":"readv2"},{"code":"Z264600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-amnio---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-amnio---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-amnio---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
