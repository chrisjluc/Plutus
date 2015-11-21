import csv

from category import CATEGORIES

def parse_csv(path):
    transactions = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append((row['Payee'], float(row['Amount'])))
    return transactions

def get_class_name(instance):
    return type(instance).__name__

def categorize(transactions):
    categorized = []

    for transaction in transactions[:]:
        transaction_matched = False

        for category in CATEGORIES:
            if category.belongs_to_category(transaction[0]):
                categorized.append(transaction + (get_class_name(category),))
                transaction_matched = True
                break

        if not transaction_matched:
            print 'Warning Uncategorized transaction: ' + transaction[0]

    return categorized

def get_summary_string(summary):
    text = ""
    for x in summary:
        text += '{}: ${:,} \n'.format(x[0], abs(float(x[1])))

    text += 'TOTAL: ${:,}'.format(abs(sum(map(lambda x: x[1], summary))))
    return text + '\n'

def get_category_transaction_string(d):
    text = ""
    for k, v in d.iteritems():
        text += k + ':\n'
        for x in v:
            text += '\t{}: ${:,} \n'.format(x[0], abs(float(x[1])))
    return text + '\n'

def finalize_summary():
    categorized_transactions = []
    categorized_transactions += categorize(parse_csv('../data/September2015_2216.csv'))
    categorized_transactions += categorize(parse_csv('../data/October2015_2216.csv'))
    categorized_transactions += categorize(parse_csv('../data/November2015_2216.csv'))

    summary = []
    category_transactions_dict = {}
    for category in CATEGORIES:
        name = get_class_name(category)
        category_transactions = filter(lambda x: x[2] == name, categorized_transactions)
        category_transactions_dict[name] = category_transactions
        category_amount = sum(map(lambda x: x[1], category_transactions))
        summary.append((name, category_amount))

    summary.sort(key=lambda x: x[1], reverse=False)

    return summary, category_transactions_dict

if __name__ == '__main__':
    summary, category_transactions = finalize_summary()
    print get_summary_string(summary)
    print get_category_transaction_string(category_transactions)
