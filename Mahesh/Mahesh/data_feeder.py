import csv


def feed_data(data_file):
    data = []
    with open(data_file) as file:
        rd = csv.reader(file, delimiter="\t")
        data = list(rd)
    return data


if __name__ == '__main__':
    data_file = "/home/shubham/Downloads/coding_challenge-master/data.tsv"
    print(feed_data(data_file))