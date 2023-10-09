import unittest
import os
import pandas as pd
import pandas.testing as pd_testing
from duplicate_finder import find_duplicates

class TestFindDuplicates(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store test files
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create test input data
        data = {
            "ID": [1, 2, 3, 4, 5, 6, 7, 8],
            "Name": ["John", "Jane", "John", "John", "Jane", "Garry", "Mary", "Zack"],
            "Age": [30, 25, 30, 30, 26, 10, 11, 12],
            "Address": ["123 Main St", "456 Elm St", "789 Pine St", "123 Main St", "456 Elm St", "111 Main St", "456 Elm St", "122 Main St"],
            "Phone": ["555-1234", "555-5678", "555-1234", "555-1234", "555-5678", "111-111", "222-222", "333-333"]
        }
        self.input_df = pd.DataFrame(data)
        self.input_file = os.path.join(self.test_dir, "test_input_data.csv")
        self.input_df.to_csv(self.input_file, index=False)

    def tearDown(self):
        # Remove the temporary test directory and files
        import shutil
        shutil.rmtree(self.test_dir)

    def test_find_duplicates(self):
        output_file = os.path.join(self.test_dir, "test_output_data.csv")
        find_duplicates(self.input_file, output_file)
        
        # Read the output CSV file into a Pandas dataframe
        output_df = pd.read_csv(output_file)
        
        # Assert that the output dataframe has the correct columns
        self.assertTrue("Score" in output_df.columns)
        self.assertTrue("GroupID" in output_df.columns)
        
        # Assert that the Score and GroupID columns have the correct values
        self.assertEqual(output_df.iloc[0]["Score"], 75)
        self.assertEqual(output_df.iloc[0]["GroupID"], 3)

        self.assertEqual(output_df.iloc[1]["Score"], 100)
        self.assertEqual(output_df.iloc[1]["GroupID"], 6)

        self.assertEqual(output_df.iloc[2]["Score"], 100)
        self.assertEqual(output_df.iloc[2]["GroupID"], 6)

        self.assertEqual(output_df.iloc[3]["Score"], 75)
        self.assertEqual(output_df.iloc[3]["GroupID"], 7)

if __name__ == "__main__":
    unittest.main()
