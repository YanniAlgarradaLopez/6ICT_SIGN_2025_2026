import csv


with open('Temperatuur.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['spam', 'Lovely Spam', 'Wonderful Spam'])