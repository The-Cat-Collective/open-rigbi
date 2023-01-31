"""
Generate country regional codes to pass to each node.

Written by Ed Oughton.

August 2022.

"""
import os
import sys
import configparser
# import pandas as pd
# import numpy as np
# import geopandas as gpd
import random

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), 'script_config.ini'))
BASE_PATH = CONFIG['file_locations']['base_path']

sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from misc import get_tropical_storm_scenarios #get_scenarios

DATA_RAW = os.path.join(BASE_PATH, 'raw')
DATA_PROCESSED = os.path.join(BASE_PATH, 'processed')


if __name__ == "__main__":

    scenarios = get_tropical_storm_scenarios()

    scenarios = [os.path.basename(i) for i in scenarios]#[:12]

    scenarios = [i.replace('.tif','') for i in scenarios]

    print(*scenarios, sep='\n')