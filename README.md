# Accessible and Usable Datasets yet Majority are Bronze-Graded and not Updated Regularly: An analysis of the data quality of datasets available on the Open Data Toronto Portal (As of May 13, 2025)

## Overview
As one of the central hubs for data on the City of Toronto that are used in the media and in policy-making, we conducted analysis on the quality of Open Data Toronto's data catalogue. We found that despite Open Data Toronto's extensive dataset catalogue being accessible and usable, 56% of their datasets are graded bronze and bronze-graded datasets are less likely to be updated the more completed they are. However we also found that metadata fields were less likely to be filled for gold-graded and silver-graded datasets. These findings can help reporters, policy-makers, and anyone interested in using datasets from Open Data Toronto's catalogue make an inform decision of what datasets to choose.

## Setup
1. Install `uv` by opening your terminal and entering the following command: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Next, open to the directory where the `data-quality` folder is located. So for example, if the `data-quality` folder is located in your downloads folder, you will enter the following command into your terminal: `cd downloads/data-quality`. 
3. Install Python 3.11 using the following command: `uv python install 3.11`. 
4. Create virtual environment for your dependencies with the following command: `uv venv --python 3.11` (for MacOS).
4. Activate virtual environment: `source .venv/bin/activate` (for MacOS)
5. Install the necessary packages using the following command: `uv pip install -r requirements.txt` and then added to the project using: `uv add -r requirements.txt`. 

## File Structure

The repo is structured as:
-   `data/00-simulated_data` contains data obtained from simulation of the ideal dataset for our analysis.
-   `data/01-raw_data` contains the raw data as obtained from Open Data Toronto.
-   `data/02-analysis_data` contains the cleaned dataset in CSV form that was constructed and used in our analysis.
-   `other` contains sketches.
-   `paper` contains the files used to generate the paper, including the Quarto document and reference bibliography file, as well as the PDF of the paper. 
-   `scripts` contains the Python scripts used to install, simulate, download, clean, explore, and test our data.

## Statement on LLM usage

No LLMs were used for any aspect of this work.
