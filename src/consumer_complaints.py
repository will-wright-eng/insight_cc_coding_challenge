'''ETL for consumer complaints data table'''

import sys
from complaints_fxns import open_and_read_csv, csv_data_to_dict, generate_results_list, greater_than_one, write_results_to_csv

def main():
	# command line arguments
	filename, csv_input, csv_output = sys.argv

	## EXTRACT ##
	# create dictionary from csv data
	d = csv_data_to_dict(open_and_read_csv(csv_input))

	## TRANSFORM ##
	# selection of columns for analysis
	col_prod = 'Product'
	col_date = 'Date received'
	# loop through product and year instances and calculate complaint and company metrics
	results = []
	r = []
	# product loop
	prods = list(set(d[col_prod]))
	prods.sort()
	for p in prods:
	    # positions
	    pos = [i for i, e in enumerate(d[col_prod]) if e == p]
	    # corresponding dates
	    dates = [d[col_date][i].split('-')[0] for i in pos]
	    # date loop
	    years = list(set(dates))
	    years.sort()
	    for x in years:
	        results.append(generate_results_list(d,p.lower(),x,dates))

	## LOAD ##
	# write file
	return write_results_to_csv(csv_output,results)

if __name__ == '__main__':
    main()