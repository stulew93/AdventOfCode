import os
import shutil
import subprocess


def ingest_csv_to_list(filepath: str) -> list:
    result_list = []
    with open(filepath, 'r') as input_file:
        for row in input_file:
            result_list.append(str(row.strip()))

    return result_list


def create_new_day(dir_name: str) -> None:
    # os.mkdir(dir_name)
    open(os.path.join(dir_name, "input.csv"), 'a').close()
    # open(os.path.join(dir_name, "solution.py"), 'a').close()
    shutil.copyfile("solution_template.py", os.path.join(dir_name, "solution.py"))
    # os.system("cd " + dir_name)
    os.system(f"git add {dir_name}/input.csv")
    os.system(f"git add {dir_name}/solution.py")
    return


if __name__ == "__main__":
    day_directory = "2022/day_3"
    create_new_day(day_directory)
