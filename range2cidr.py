from netaddr import *
import csv
import os

# Import CSV File Path
import_file_path = ''
# Export CSV File Path
export_file_path = ''

# Exportファイルが存在する場合oldファイルにする
if os.path.isfile(export_file_path):
    os.rename(export_file_path, export_file_path + '.old')

# CSV読み込み
with open(import_file_path, 'r', newline='', encoding="utf-8") as importcsv:
    # skipinitialspace=True : カンマの後ろのスペースを無視
    filereader = csv.reader(importcsv, skipinitialspace=True)

    for row in filereader:
        start_ip = row[0]
        end_ip = row[1]
        
        # ipv4アドレスのリストを生成
        ip_list = list(iter_iprange(start_ip, end_ip))

        # CIDRに変換
        cidr_list = cidr_merge(ip_list)

        # CSV出力
        with open(export_file_path, 'a', newline='', encoding="utf-8") as exportcsv:
            filewriter = csv.writer(exportcsv)

            for item in cidr_list:
                filewriter.writerow([str(item)])