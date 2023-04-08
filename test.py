import json

def sorting_key(item):
    return item['price'], item['name']

def sort_by_price_ascending(json_string):
    data = json.loads(json_string)
    
    sorted_data = sorted(data, key=sorting_key)
    
    return json.dumps(sorted_data)

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
