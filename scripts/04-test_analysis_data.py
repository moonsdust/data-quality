#### Preamble ####
# Purpose: Tests the cleaned dataset from Open Data Toronto 
# Author: Emily Su
# Date: 9 May 2025
# Contact: em.su@mail.utoronto.ca
# License: MIT
# Pre-requisites: Have ran 02-download_data.py and 03-clean_data.py and have installed the required packages mentioned in 
# Workspace setup by running requirements.txt.


#### Workspace setup ####
import polars as pl
import pointblank as pb

# Reference https://posit.co/blog/introducing-pointblank-for-python/
# Read in CSV file
cleaned_data = pl.read_csv("data/02-analysis_data/analysis_data.csv")

#### Test data ####
# Check columns type
schema = pb.Schema(
    columns=[
        ("package", "String"),
        ("accessibility", "Int64"),
        ("completeness", "Float64"),
        ("freshness", "Float64"),
        ("metadata", "Float64"),
        ("usability", "Float64"),
        ("grade", "String"),
    ]
)
check_columns_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check Columns Test"
    )
    .col_schema_match(schema=schema)
    .interrogate()
)

# Check if all the columns don't have a NONE/NULL value
check_for_null_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check NULL Test"
    )
     .col_vals_not_null(
      columns=["package", "accessibility", "completeness", "freshness", "metadata", "usability", "grade"]
   )
    .interrogate()
)

# None of the columns in string type columns are ""
check_for_empty_strings_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check for empty strings test"
    )
    .col_vals_regex(
        columns=["package", "grade"],# check that all string columns are non-empty strings
        pattern=r"(.|\s)*\S(.|\s)*" # Referenced: https://posit-dev.github.io/pointblank/demos/column-selector-functions/index.html
    )
    .interrogate()
)

# Check min and max for all numeric type columns except usability
check_min_max_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check Min/Max Test"
    )
    .col_vals_between(columns=["accessibility", "completeness", "freshness", "metadata"], left=0, right=1)
    .interrogate()
)

# Check if grade's value is only grade is Bronze, Silver, and Gold 
check_grade_value_test = (
    pb.Validate(
        data=cleaned_data,
        tbl_name="cleaned_data",
        label="Check Grade Value Test"
    )
    .col_vals_in_set(columns="grade", set=["Bronze", "Silver", "Gold"])
    .interrogate()
)

# RUN TESTS 
check_columns_test.get_tabular_report().show("browser")
check_for_null_test.get_tabular_report().show("browser")
check_for_empty_strings_test.get_tabular_report().show("browser")
check_min_max_test.get_tabular_report().show("browser")
check_grade_value_test.get_tabular_report().show("browser")