#### Preamble ####
# Purpose: Cleans the raw data from Open Data Toronto
# Author: Emily Su
# Date: 9 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: Have ran 02-download_data.py and have installed the required packages mentioned in 
# Workspace setup by running requirements.txt.

#### Workspace setup ####
import polars as pl
import datetime

#### Clean data ####
# Read in CSV file
the_raw_data = pl.read_csv("data/01-raw_data/raw_data.csv")

# Select specific columns
selected_columns = ["package", "accessibility", "completeness", "freshness", "metadata", "usability", "score", "grade", "recorded_at"]

selected_df = the_raw_data.select(selected_columns)

# # Filter to only rows that have data
# filtered_df = selected_df.filter(the_raw_data["OCCUPIED_BEDS"].is_not_null())

# print(filtered_df.head())

# renamed_df = filtered_df.rename({"OCCUPANCY_DATE": "date",
#                                  "SHELTER_ID": "Shelters",
#                                  "CAPACITY_ACTUAL_BED": "Capacity",
#                                  "OCCUPIED_BEDS": "Usage"
#                                  })

# # print(renamed_df.head())

# #### Save data ####
# renamed_df.write_csv("outputs/data/analysis_data.csv")