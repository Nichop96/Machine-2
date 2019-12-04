import numpy as np
import logistic_domain
import utils

def summary(array):
    print("min: "+str(min(array))+"\nmax: "+str(max(array))+"\nmean: "+str(sum(array)/len(array))+"\nmedian: "+str(np.median(array))+"\n1th quartile: "+str(np.percentile(array,25))+"\n3rd quartile: "+str(np.percentile(array,75))+"\n")

def init_statistics(domains):
    airplanes = [len(domain.apn) for domain in domains]
    cities = [len(domain.cit) for domain in domains]
    trucks = [len(domain.tru) for domain in domains]
    locations = [len(domain.loc) for domain in domains]
    objects = [len(domain.obj) for domain in domains]

    print("Airplanes")
    summary(airplanes)
    print("Cities")
    summary(cities)
    print("Trucks")
    summary(trucks)
    print("Locations")
    summary(locations)
    print("Objects")
    summary(objects)




