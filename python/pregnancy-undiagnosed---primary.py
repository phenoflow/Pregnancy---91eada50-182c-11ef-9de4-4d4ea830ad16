# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2024.

import sys, csv, re

codes = [{"code":"L30z100","system":"readv2"},{"code":"L061z00","system":"readv2"},{"code":"L361z00","system":"readv2"},{"code":"L06z.00","system":"readv2"},{"code":"L11yz00","system":"readv2"},{"code":"L360z00","system":"readv2"},{"code":"L221z00","system":"readv2"},{"code":"L225z00","system":"readv2"},{"code":"L18z100","system":"readv2"},{"code":"L25z000","system":"readv2"},{"code":"Q21z.00","system":"readv2"},{"code":"636Z.00","system":"readv2"},{"code":"L070z00","system":"readv2"},{"code":"L140z00","system":"readv2"},{"code":"62KZ.00","system":"readv2"},{"code":"L100z00","system":"readv2"},{"code":"L11z000","system":"readv2"},{"code":"L042z00","system":"readv2"},{"code":"L070x00","system":"readv2"},{"code":"L33z.00","system":"readv2"},{"code":"L333z00","system":"readv2"},{"code":"L212z00","system":"readv2"},{"code":"L125z00","system":"readv2"},{"code":"7F22z00","system":"readv2"},{"code":"L222z00","system":"readv2"},{"code":"L221.00","system":"readv2"},{"code":"Q2z..00","system":"readv2"},{"code":"Q21z.11","system":"readv2"},{"code":"L413z00","system":"readv2"},{"code":"L16yz00","system":"readv2"},{"code":"L10z000","system":"readv2"},{"code":"L314.15","system":"readv2"},{"code":"ZV3zz00","system":"readv2"},{"code":"62GZ.00","system":"readv2"},{"code":"L35zz00","system":"readv2"},{"code":"L07z.00","system":"readv2"},{"code":"L11z100","system":"readv2"},{"code":"7F2z.00","system":"readv2"},{"code":"62NZ.00","system":"readv2"},{"code":"L09z.00","system":"readv2"},{"code":"L052z00","system":"readv2"},{"code":"L30zz11","system":"readv2"},{"code":"L282z00","system":"readv2"},{"code":"L123z00","system":"readv2"},{"code":"L245z00","system":"readv2"},{"code":"L320z00","system":"readv2"},{"code":"L10z.00","system":"readv2"},{"code":"L309z00","system":"readv2"},{"code":"L36z.00","system":"readv2"},{"code":"L051z00","system":"readv2"},{"code":"13SZ.00","system":"readv2"},{"code":"L220z00","system":"readv2"},{"code":"L221000","system":"readv2"},{"code":"L397z00","system":"readv2"},{"code":"L33yz00","system":"readv2"},{"code":"L221100","system":"readv2"},{"code":"L281z00","system":"readv2"},{"code":"L322z00","system":"readv2"},{"code":"L33z100","system":"readv2"},{"code":"L330z00","system":"readv2"},{"code":"L30zz00","system":"readv2"},{"code":"L14z.00","system":"readv2"},{"code":"7F23z00","system":"readv2"},{"code":"L251z00","system":"readv2"},{"code":"L224z00","system":"readv2"},{"code":"L352z00","system":"readv2"},{"code":"621Z.00","system":"readv2"},{"code":"L150z00","system":"readv2"},{"code":"L040z00","system":"readv2"},{"code":"L05z.00","system":"readv2"},{"code":"L052x00","system":"readv2"},{"code":"L04z.00","system":"readv2"},{"code":"L351z00","system":"readv2"},{"code":"L041z00","system":"readv2"},{"code":"L25z.00","system":"readv2"},{"code":"L162.12","system":"readv2"},{"code":"L30z000","system":"readv2"},{"code":"L265z00","system":"readv2"},{"code":"L16z.00","system":"readv2"},{"code":"7F10z00","system":"readv2"},{"code":"L161z00","system":"readv2"},{"code":"L041x00","system":"readv2"},{"code":"L13yz00","system":"readv2"},{"code":"L060z00","system":"readv2"},{"code":"L10z200","system":"readv2"},{"code":"L071z00","system":"readv2"},{"code":"L33zz00","system":"readv2"},{"code":"L11zz00","system":"readv2"},{"code":"L236z00","system":"readv2"},{"code":"L042x00","system":"readv2"},{"code":"63BZ.00","system":"readv2"},{"code":"L303z00","system":"readv2"},{"code":"L25yz00","system":"readv2"},{"code":"L0z..00","system":"readv2"},{"code":"7F03z00","system":"readv2"},{"code":"L09yz00","system":"readv2"},{"code":"L166z00","system":"readv2"},{"code":"L35z.00","system":"readv2"},{"code":"L13zz00","system":"readv2"},{"code":"L394z00","system":"readv2"},{"code":"L264z00","system":"readv2"},{"code":"L091z00","system":"readv2"},{"code":"L25zz00","system":"readv2"},{"code":"L250z00","system":"readv2"},{"code":"639Z.00","system":"readv2"},{"code":"L10yz00","system":"readv2"},{"code":"L072z00","system":"readv2"},{"code":"L15z.00","system":"readv2"},{"code":"L305z00","system":"readv2"},{"code":"L331z00","system":"readv2"},{"code":"635Z.00","system":"readv2"},{"code":"L210z00","system":"readv2"},{"code":"L313z00","system":"readv2"},{"code":"7F25z00","system":"readv2"},{"code":"L11z.00","system":"readv2"},{"code":"L211z00","system":"readv2"},{"code":"L25z100","system":"readv2"},{"code":"L35z000","system":"readv2"},{"code":"L141z00","system":"readv2"},{"code":"L124z00","system":"readv2"},{"code":"L266z00","system":"readv2"},{"code":"L362z00","system":"readv2"},{"code":"L307z00","system":"readv2"},{"code":"L30z.00","system":"readv2"},{"code":"L350z00","system":"readv2"},{"code":"L127z00","system":"readv2"},{"code":"63AZ.00","system":"readv2"},{"code":"Q21z.12","system":"readv2"},{"code":"L33z000","system":"readv2"},{"code":"L23z100","system":"readv2"},{"code":"7F11z00","system":"readv2"},{"code":"L291z00","system":"readv2"},{"code":"L126z00","system":"readv2"},{"code":"L35z100","system":"readv2"},{"code":"L10zz00","system":"readv2"},{"code":"L336z00","system":"readv2"},{"code":"64BZ.00","system":"readv2"},{"code":"7F24z00","system":"readv2"},{"code":"L16Az00","system":"readv2"},{"code":"L168z00","system":"readv2"},{"code":"L050x00","system":"readv2"},{"code":"L18z300","system":"readv2"},{"code":"62OZ.00","system":"readv2"},{"code":"L050z00","system":"readv2"},{"code":"L32z.00","system":"readv2"},{"code":"632Z.00","system":"readv2"},{"code":"L353z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pregnancy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pregnancy-undiagnosed---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pregnancy-undiagnosed---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pregnancy-undiagnosed---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
