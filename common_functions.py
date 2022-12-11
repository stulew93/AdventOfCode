def ingest_csv_to_list(filepath: str) -> list:
    result_list = []
    with open(filepath, 'r') as input_file:
        for row in input_file:
            result_list.append(str(row.strip()))

    return result_list