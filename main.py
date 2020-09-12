import csv
import datetime
import os

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

count = 0
with open("employee_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # could also use Dictreader method,  just access via keys instead
    rows = list(csv_reader)
    # remove header for loop
    # header = rows[0]
    rows.pop(0)
    count = 0
    new_header = ['Emp ID', 'First Name', 'Last Name', 'Date', 'SSN', 'State']
    new_emp_id = []
    new_first = []
    new_last = []
    new_date = []
    new_ss = []
    new_state = []

    for row in rows:
        # acquiring
        emp_id = rows[count][0]
        name = rows[count][1]
        date = rows[count][2]
        ss = rows[count][3]
        state = rows[count][4]

        # ID carries over
        new_emp_id.append(emp_id)

        # Name separation
        name = name.split(' ')
        new_first.append(name[0])
        new_last.append(name[1])
        # DATE
        new_date.append(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y'))
        # SSN
        new_ss.append('***-**' + ss[-5:])

        # STATE
        # Easier way
        abbreviation = us_state_abbrev[state]
        new_state.append(abbreviation)
        # Long way via a for loop
        # for k, v in us_state_abbrev.items():
        #     if k == state:
        #         new_state.append(v)
        count += 1

cleaned_data = zip(new_emp_id, new_first, new_last, new_date, new_ss, new_state)

output_file = os.path.join("cleaned_employee_data.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(new_header)

    writer.writerows(cleaned_data)
