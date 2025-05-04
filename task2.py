import random
import timeit
from BTrees.OOBTree import OOBTree
import pandas as pd

def load_items_from_csv(filename):
    df = pd.read_csv(filename)
    return df.to_dict(orient="records")

def add_item_to_tree(tree, item):
    price = item["Price"]
    if price in tree:
        tree[price].append(item)
    else:
        tree[price] = [item]

def add_item_to_dict(store, item):
    store[item['ID']] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"]
    }

def range_query_tree(tree, min_price, max_price):
    results = []
    for price, items in tree.items(min_price, max_price):
        results.extend(items)
    return results

def range_query_dict(store, min_price, max_price):
    return [
        (k, v) for k, v in store.items()
        if min_price <= v["Price"] <= max_price
    ]

def main():
    filename = "generated_items_data.csv"
    items = load_items_from_csv(filename)

    tree = OOBTree()
    store = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(store, item)

    test_ranges = [(random.randint(10, 500), random.randint(501, 1000)) for _ in range(100)]

    def tree_test():
        for r in test_ranges:
            range_query_tree(tree, r[0], r[1])

    tree_time = timeit.timeit(tree_test, number=1)

    def dict_test():
        for r in test_ranges:
            range_query_dict(store, r[0], r[1])

    dict_time = timeit.timeit(dict_test, number=1)

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()