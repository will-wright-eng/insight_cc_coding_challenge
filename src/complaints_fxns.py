import csv
import collections
import operator

def test_datatypes(test_dict):
    '''docstring for test_datatypes'''
    # test for OrderedDict
    if collections.OrderedDict==type(test_dict):
        pass
        if len(test_dict) == 18:
            pass
        else:
            print('Warning: OrderedDict of unexpected length')
    else:
        raise Exception('data type other than expected')
    # test for strings as values in OrderedDict
    for k in test_dict:
        if isinstance(test_dict[k],str):
            pass
        else:
            raise Exception('data type other than expected')
            break
    return

def open_and_read_csv(filepath):
    '''docstring for open_and_read_csv
    input: file and path to csv data
    output: list of OrderedDict objects'''
    my_data=[]
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_data.append(row)
    return my_data

def csv_data_to_dict(my_data):
    '''docstring for csv_data_to_dict
    input: list of OrderedDict objects
    output: return dictionary of key:value (column header: list of elements)'''
    # construct list of lists
    l = []
    keys = list(dict(my_data[0]))
    l = [[my_data[0][i]] for i in keys]
    test_datatypes(my_data[0])
    # extract remaining data into list of lists
    for i in my_data[1:]:
        for j in range(len(keys)):
            l[j].append(i[keys[j]])
    # convert list of lists to dictionary
    d = {}
    d = {i: j for (i, j) in zip(keys,l)}
    return d

def generate_results_list(d,p,x,dates):
    '''docstring for generate_results_list
    input: dictionary of complaints data, product, and set of years
    output: single row in results output'''
    date_count = collections.Counter(dates)
    # positions by date
    pos = [i for i, e in enumerate(dates) if e.split('-')[0] == x]
    # corresponding companies
    col_comp = 'Company'
    comps = [d[col_comp][i].split('-')[0] for i in pos]
    # company dict
    comp_count = collections.Counter(comps)
    comp_num = len(comp_count)
    complaint_percent_by_worst_company = round(
        max(comp_count.items(), key=operator.itemgetter(1))[1]/len(comps)
        ,2)*100
    comp_count = greater_than_one(comp_count)
    # generate row
    # product | year | complaint count | number of companies (>1) | high percentage of complaints
    return [p
            , x
            , date_count[x]
            , comp_num
            , complaint_percent_by_worst_company]

def greater_than_one(comp_count):
    '''docstring for greater_than_one
    input: dictionary of key-value pairs
    output: return dictionary with values greater than 1'''
    comp_count_mod = {}
    for x in comp_count:
        val = comp_count[x]
        if val < 1:
            comp_count_mod[x] = val
        else:
            pass
    return comp_count_mod

def write_results_to_csv(filepath,results):
    '''docstring for write_results_to_csv
    input: column headers, filepath from command line arg, and results list of lists
    output: saved csv file'''
    # writing to csv file  
    with open(filepath, 'w') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)
        # writing the data rows  
        csvwriter.writerows(results)
    return print('csv saved to '+filepath)