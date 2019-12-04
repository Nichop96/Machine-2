

class LogisticDomain:
    def __init__(self, logistic_domain_description):
        f = open(logistic_domain_description, "r")
        lines = [line for line in f.readlines()]
        self.apn = lines[5].strip().split("(:objects ")[1].split(" ")
        self.cit = lines[6].strip().split(" ")
        self.tru = lines[7].strip().split(" ")
        self.loc = lines[8].strip().split(" ")
        self.obj = lines[9].strip().split(" ")
