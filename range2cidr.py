from netaddr import *
import csv
import os

# Import CSV File Path
input_file_path = ''
# Export CSV File Path
output_file_path = ''

# Exportファイルが存在する場合oldファイルにする
if os.path.isfile(output_file_path):
    os.rename(output_file_path, output_file_path + '.old')

# CSV読み込み
with open(input_file_path, 'r', newline='', encoding="utf-8") as inputcsv:
    # skipinitialspace=True : カンマの後ろのスペースを無視
    filereader = csv.reader(inputcsv, skipinitialspace=True)

    for row in filereader:
        start_ip = row[0]
        end_ip = row[1]
        
        # ipv4アドレスのリストを生成
        ip_list = list(iter_iprange(start_ip, end_ip))

        # CIDRに変換
        cidr_list = cidr_merge(ip_list)

        # CSV出力
        with open(output_file_path, 'a', newline='', encoding="utf-8") as outputcsv:
            filewriter = csv.writer(outputcsv)

            for item in cidr_list:
                filewriter.writerow([str(item)])