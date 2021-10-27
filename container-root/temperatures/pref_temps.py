import csv

with open('max.csv', encoding='shift_jis') as csvfile:
    line = csv.reader(csvfile)
    pref = '北海道'
    max_temp = -float('inf')
    for row in line:
        pref_name = row[1]
        if pref_name == '都道府県':
            # ヘッダ行は無視
            continue
        else:
            if pref_name.startswith('北海道'):
                # 北海道はpref_nameが地方名なので除去する
                pref_name = '北海道'

        pref_temp = float(row[9])
        if pref_name == pref:
            max_temp = max(max_temp, pref_temp)
        else:
            print(pref, max_temp)
            pref = pref_name
            max_temp = pref_temp

    print(pref, max_temp)
