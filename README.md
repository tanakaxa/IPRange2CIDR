# IPRange2CIDR
IPアドレスのRangeが記載されたcsvを読み込み、CIDR形式に変換してcsvに出力するスクリプト

# Demo
```
$ cat import.csv
192.168.1.0, 192.168.1.127
192.168.2.33, 192.168.2.63
2001:db8::, 2001:db8::beef

$ python3 range2cidr.py

$ cat export.csv
192.168.1.0/25
192.168.2.33/32
192.168.2.34/31
192.168.2.36/30
192.168.2.40/29
192.168.2.48/28
2001:db8::/113
2001:db8::8000/115
2001:db8::a000/116
2001:db8::b000/117
2001:db8::b800/118
2001:db8::bc00/119
2001:db8::be00/121
2001:db8::be80/122
2001:db8::bec0/123
2001:db8::bee0/124
```

# Requirement
* Python 3.6
* [netaddr 0.7.19](https://github.com/drkjam/netaddr)
    ```
    $ python3 -m pip install netaddr
    ```

# Example
1. 変換したいIPアドレスの範囲を記載したCSVファイルを用意
    * 192.168.1.1 ~ 192.168.1.127 と 192.168.2.1 ～ 192.168.2.127 までのIPアドレスをCIDR形式で出力したい場合
        ```
        192.168.1.1, 192.168.1.127
        192.168.2.1, 192.168.2.127
        ```
    

1. `range2cidr.py`の下記変数にInputとOutputに用いるファイルのpathを記載
    ```
    # Import CSV File Path
    input_file_path = ''
    # Export CSV File Path
    output_file_path = ''
    ```

1. `range2cidr.py`を実行
    ```
    $ python3 range2cidr.py
    ```
