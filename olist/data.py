import os
import pandas as pd

class Olist:
    def get_data(self):
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data", "csv")

        file_names = os.listdir(csv_path)

        file_names = [file_name for file_name in file_names if file_name.endswith('.csv')]


        key_names = file_names[:]
        for index, path in enumerate(key_names):
            if "_dataset.csv" in path:
                key_names[index] = path.replace("_dataset.csv", "")
            elif ".csv" in path:
                key_names[index] = path.replace(".csv", "")
            key_names[index] = key_names[index].replace("olist_", "")


        data = {}
        for (key, path) in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path,path))

        return data






        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        pass  # YOUR CODE HERE

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")





        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        pass  # YOUR CODE HERE

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
