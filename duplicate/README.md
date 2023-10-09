# Duplicate Finder

This Python script reads a CSV file, identifies duplicate records based on specified columns, assigns scores to duplicates, and groups them using a GroupID. The script is designed to work with a CSV file containing the following columns: `ID, Name, Age, Address, Phone`.

## Usage

1. Install the required dependencies:

```
pip install pandas
```


2. Run the script by executing the following command:

```
python duplicate_finder.py
```


3. The script will read the input data from `input_data.csv` and produce the output in `output_data.csv`.

## Customization

You can customize the script by modifying the `find_duplicates` function in the `duplicate_finder.py` script. For example, you can change the columns used for grouping or adjust the scoring logic.

## How it Works

- The script first reads the input CSV file into a Pandas dataframe.
- It assigns a default score of 0 to all rows and initializes a GroupID.
- The columns to consider for grouping are specified in the `columns_to_group` list.
- The script loops through each column for grouping, and for each group, it calculates scores based on the number of identical fields and assigns a GroupID to each group.
- Rows with a GroupID of 0 are given unique GroupIDs.
- Finally, the dataframe is sorted based on GroupID and Score, and the results are saved in `output_data.csv`.

## Test

To run unit tests for the script, use the following command:

```
python -m unittest test_find_duplicates.py
```


The test script `test_find_duplicates.py` includes test cases to verify the functionality of the `find_duplicates` function.
