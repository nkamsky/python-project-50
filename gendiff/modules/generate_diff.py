import json
import yaml


def check_bool(data):
    for key, value in data.items():
        if value is True:
            data[key] = 'true'
        elif value is False:
            data[key] = 'false'


def load_data(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported file format')


def generate_diff(file1, file2):
    data1 = load_data(file1)
    data2 = load_data(file2)
    check_bool(data1)
    check_bool(data2)
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = keys1.union(keys2)
    result = ''
    for key in sorted(all_keys):
        if key in data1 and key not in data2:
            result += f'  - {key}: {data1[key]}\n'
        elif key not in data1 and key in data2:
            result += f'  + {key}: {data2[key]}\n'
        else:
            if data1[key] != data2[key]:
                result += f'  - {key}: {data1[key]}\n'
                result += f'  + {key}: {data2[key]}\n'
            else:
                result += f'    {key}: {data2[key]}\n'
    # print('{\n' + result + '}')
    return '{\n' + result + '}'
