import csv
import os

def organize(list):

    dictionary = {}

    for issue in list:

        if issue.fields.assignee is None :
            assignee = "Unsigned"
        else :
            assignee = issue.fields.assignee.displayName

        points = issue.fields.customfield_10014

        if(assignee not in dictionary.keys()) :
            if (points is not None) :
                dictionary[assignee] = float(points)

        if (assignee in dictionary.keys()):
            if (points is not None):
                dictionary[assignee] = float(points) + dictionary[assignee]

    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "..", "ext", "R", "datasets", "assigneeWorkload.csv")
    with open(path, 'w') as f:
        file = csv.DictWriter(f, dictionary.keys())
        file.writeheader()
        file.writerow(dictionary)

    return dictionary;