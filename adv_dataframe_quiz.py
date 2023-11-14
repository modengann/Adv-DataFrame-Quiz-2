import pandas as pd

def remove_empty_col(df):
    pass
    
def remove_any_missing_row(df):
    pass

def max_score(df):
    pass

def merge_data(left, right):
    pass

def main():
    test_data = pd.read_csv("student_test_data.csv")
    test_data = remove_empty_col(test_data)
    test_data = remove_any_missing_row(test_data)
    largest = max_score(test_data)
    print(f"Largest score: {largest}")

    demographic_data = pd.read_csv("student_demo_data.csv")
    merged_data = merge_data(test_data, demographic_data)

if __name__ == "__main__":
    main()