# Задание №7

import json
profit = []
firms = {}
result = []
with open('test_6.txt') as test_file:
    for line in test_file:
        line = line.split()
        profit.append(int(line[2]) - int(line[3]))
        average_profit = sum([i for i in profit if i > 0])
        firms.update({line[0]: int(line[2]) - int(line[3])})
    result.extend([firms, {'average_profit': average_profit}])
with open('test_6.json', 'w') as test_json:
    json.dump(result, test_json)
    js_str = json.dumps(result)
    print(js_str)