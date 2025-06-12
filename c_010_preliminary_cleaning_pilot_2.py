"""


"""

import numpy as np
import pandas as pd
from i7_hot_reload.hot_reload import hot_reload_a_module_from_cwd


b_000_env = hot_reload_a_module_from_cwd('b_000_env')

from b_000_env import Directory
from b_000_env import FilePath
from b_000_env import Constants
from b_000_env import Parameters



##
def main() :
    pass

    ##
    def keep_only_valid_responses() :
        pass

        ##
        d = Directory()
        fp = FilePath()
        c = Constants()

        ##
        df_raw_apps_wide = pd.read_csv(fp.all_apps_wide_csv_250301)

        ##

        print(df_raw_apps_wide.shape)

        # (47 , 296)

        ##

        # dropping rows without Introduction.1.player.MTurk_ID value
        df_raw_apps_wide = df_raw_apps_wide.dropna(subset=[c.mturk_id])

        ##


    ##



    ##



    ##


    ##



    ##



    ##


    ##


##
if __name__ == '__main__' :
    main()
