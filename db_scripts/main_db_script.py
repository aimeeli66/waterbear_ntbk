import os


directory = os.path.dirname(__file__)
base_manuscript_dir = os.path.join(directory,'./')
data_dir = os.path.join(base_manuscript_dir,'./')
fig_dir = os.path.join(base_manuscript_dir,'./')

raw_db_filename = "/./" \
                  "hampt_rd_data.sqlite"
db_filename = "floodData.sqlite"
