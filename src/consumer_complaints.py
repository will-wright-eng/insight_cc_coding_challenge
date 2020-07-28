'''ETL for consumer complaints data table'''

import sys
from complaints_fxns import open_and_read_csv, csv_data_to_dict, generate_results_list, greater_than_one, write_results_to_csv

# command line arguments
filename, csv_input, csv_output = sys.argv

## EXTRACT ##
print('extract')
# create dictionary from csv data
d = csv_data_to_dict(open_and_read_csv(csv_input))

## TRANSFORM ##
print('transform')
# selection of columns for analysis
col_prod = 'Product'
col_date = 'Date received'
# loop through product and year instances and calculate complaint and company metrics
results = []
r = []
# product loop
for p in list(set(d[col_prod])):
    # positions
    pos = [i for i, e in enumerate(d[col_prod]) if e == p]
    # corresponding dates
    dates = [d[col_date][i].split('-')[0] for i in pos]
    # date loop
    for x in list(set(dates)):
        results.append(generate_results_list(d,p,x,dates))

## LOAD ##
print('load')
# field names
fields = ['product','year','complaint_count','company_count*','complaint_percent_by_worst_company']
# write file
write_results_to_csv(fields,csv_output,results)