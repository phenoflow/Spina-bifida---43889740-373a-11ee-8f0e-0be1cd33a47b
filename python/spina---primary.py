# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"P1...00","system":"readv2"},{"code":"101013.0","system":"med"},{"code":"101493.0","system":"med"},{"code":"102628.0","system":"med"},{"code":"103284.0","system":"med"},{"code":"104943.0","system":"med"},{"code":"105767.0","system":"med"},{"code":"106579.0","system":"med"},{"code":"107144.0","system":"med"},{"code":"107377.0","system":"med"},{"code":"109243.0","system":"med"},{"code":"109893.0","system":"med"},{"code":"21802.0","system":"med"},{"code":"31775.0","system":"med"},{"code":"3336.0","system":"med"},{"code":"3947.0","system":"med"},{"code":"42497.0","system":"med"},{"code":"43593.0","system":"med"},{"code":"46790.0","system":"med"},{"code":"47288.0","system":"med"},{"code":"47827.0","system":"med"},{"code":"48609.0","system":"med"},{"code":"50365.0","system":"med"},{"code":"50565.0","system":"med"},{"code":"52683.0","system":"med"},{"code":"5306.0","system":"med"},{"code":"53471.0","system":"med"},{"code":"53578.0","system":"med"},{"code":"53929.0","system":"med"},{"code":"5431.0","system":"med"},{"code":"56362.0","system":"med"},{"code":"56386.0","system":"med"},{"code":"57113.0","system":"med"},{"code":"57243.0","system":"med"},{"code":"57611.0","system":"med"},{"code":"59218.0","system":"med"},{"code":"59380.0","system":"med"},{"code":"60623.0","system":"med"},{"code":"61862.0","system":"med"},{"code":"63513.0","system":"med"},{"code":"64717.0","system":"med"},{"code":"65246.0","system":"med"},{"code":"65936.0","system":"med"},{"code":"66516.0","system":"med"},{"code":"67351.0","system":"med"},{"code":"67708.0","system":"med"},{"code":"67878.0","system":"med"},{"code":"68221.0","system":"med"},{"code":"6866.0","system":"med"},{"code":"69370.0","system":"med"},{"code":"69397.0","system":"med"},{"code":"70923.0","system":"med"},{"code":"71525.0","system":"med"},{"code":"72018.0","system":"med"},{"code":"72928.0","system":"med"},{"code":"73085.0","system":"med"},{"code":"73608.0","system":"med"},{"code":"73712.0","system":"med"},{"code":"90482.0","system":"med"},{"code":"91600.0","system":"med"},{"code":"93902.0","system":"med"},{"code":"94598.0","system":"med"},{"code":"95018.0","system":"med"},{"code":"95478.0","system":"med"},{"code":"96407.0","system":"med"},{"code":"96709.0","system":"med"},{"code":"9722.0","system":"med"},{"code":"98280.0","system":"med"},{"code":"98298.0","system":"med"},{"code":"98811.0","system":"med"},{"code":"99281.0","system":"med"},{"code":"99299.0","system":"med"},{"code":"99332.0","system":"med"},{"code":"99894.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spina-bifida-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["spina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["spina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["spina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
