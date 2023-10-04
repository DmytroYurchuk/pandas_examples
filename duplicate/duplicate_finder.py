import pandas as pd


def find_duplicates(input_file, output_file):
    # Read the input CSV file into a Pandas dataframe
    df = pd.read_csv(input_file)
    
    # Assign a default score of 0 to all rows
    df["Score"] = 0
    
    # List of columns to consider for grouping
    columns_to_group = ["Name", "Age", "Address", "Phone"]
    
    # Loop through each column for grouping
    for column in columns_to_group:
        # Group by the current column and 100/len to scores for rows in groups with more than one member
        groups = df.groupby(column)
        for _, group in groups:
            if len(group) > 1:
                df.loc[group.index, "Score"] += 100 / len(columns_to_group)

    # Add GroupID based on Score
    df["GroupID"] = df.groupby(["Score"]).ngroup() + 1

    # Sorting based on GroupID and Score
    df = df.sort_values(by=["GroupID", "Score"])
    
    # Write the dataframe with the "Score" column to the output CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"
    
    try:
        find_duplicates(input_file, output_file)
        print(f"Scores calculated and results saved in {output_file}")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
