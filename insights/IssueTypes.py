import csv
import os

def organize(list):

    dictionary = {}

    for issue in list:

        type = issue.fields.issuetype.name
        points = issue.fields.customfield_10014

        if( type not in dictionary.keys()) :
            if (points is not None) :
                dictionary[type] = float(points)

        if (type in dictionary.keys()):
            if (points is not None):
                dictionary[type] = float(points) + dictionary[type]

    path = os.path.dirname(os.path.realpath(__file__))
    with open( path + "\\..\\ext\\R\\datasets\\issueTypesWorkload.csv", 'w') as f:
        file = csv.DictWriter(f, dictionary.keys())
        file.writeheader()
        file.writerow(dictionary)

    return dictionary;