def main(file_name):


    import numpy as np
    import pandas as pd
    details = pd.read_csv(file_name)
    details.shape
    print(details.head())