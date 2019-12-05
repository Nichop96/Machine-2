import pickle
import save_arrays
import crea_istanze

if __name__ == '__main__':
    training = open("train_plans", "rb")
    train_plans = pickle.load(training)

    testing = open("test_plans", "rb")
    test_plans = pickle.load(testing)

    training_set = crea_istanze.crea(train_plans)

    test_set = crea_istanze.crea(test_plans)

    save_arrays.save(training_set, "training_set")
    save_arrays.save(test_set, "test_set")