# coding = utf-8
# @Author : AYY

import pandas as pd
import os

pd.set_option('display.expand_frame_repr', False)


def get_batch_filepath():
    batch_paths = []
    for root, dirs, files in os.walk('data'):
        print(root, dirs, files)

        for file_name in files:
            file_path = os.path.join(root, file_name)

            file_abs_path = os.path.abspath(file_path)
            print(file_abs_path)
            batch_paths.append(file_abs_path)
    return batch_paths


def batch_read_data(file_batch_path):
    all_data = pd.DataFrame()
    for file_name in file_batch_path:
        temp_data = pd.read_csv(file_name, encoding='gbk', skiprows=1)
        all_data = all_data.append(temp_data, ignore_index=True)
    print('all_data', all_data)


if __name__ == "__main__":

    file_path = get_batch_filepath()
    print(file_path)
    batch_read_data(file_path)