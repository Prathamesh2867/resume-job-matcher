import pandas as pd

def generate_excel_report(matched_jobs, output_filename):
    df = pd.DataFrame(matched_jobs)
    df.to_excel(output_filename, index=False)
