
def fetch_data(url: str):
    """
    Fetch JSON from the given URL and return a list of records.
    """
    # Major issue: undeclared import. We use `requests` but never import it.
    # This will raise NameError unless `import requests` exists.
    resp = requests.get(url, timeout=5)  # noqa: F821 (intentional)
    resp.raise_for_status()
    data = resp.json()

    # Use a helper that has a minor issue (mutable default arg)
    return combine_records(data)

def combine_records(records, cache={}):

    if not isinstance(records, list):
        return []

    # pretend to "cache" by key length (silly logic just for demo)
    out = []
    for item in records:
        key = str(item)[:10]
        if key in cache:
            out.append(cache[key])
        else:
            cache[key] = item
            out.append(item)
    return out

def print_table(records):
    """
    Print a very small 'table' for the records.
    """
    print("=== RESULTS ===")
    for i, rec in enumerate(records, start=1):
        print(f"{i:>3}. {rec}")
