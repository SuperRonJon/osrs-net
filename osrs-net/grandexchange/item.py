import json
from util.file_io import read


class Item:
    def __init__(self, item_id, item_name, price_data, members):
        self.id = item_id
        self.name = item_name
        self.price_data = price_data
        self.members = members

    @staticmethod
    def _get_item_data():
        text = read('osrs-net/resources/items.json')
        return json.loads(text)

    @staticmethod
    def get_ids(name):
        item_data = Item._get_item_data()
        try:
            return item_data[name.lower()]['id']
        except KeyError:
            matches = []
            for item in item_data:
                if name in item:
                    matches.append(item_data[item]['id'])
            return matches

    @staticmethod
    def id_to_name(id_num):
        data = Item._get_item_data()
        for item in data:
            if data[item]['id'] == id_num:
                return data[item]['name']

        return None


