import numpy as np
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
import keras
from matplotlib import pyplot as plt
import save_arrays


def save_db(db):
    np.random.shuffle(db)
    dim = int(0.8 * len(db))
    train, test = db[:dim], db[dim:]
    save_arrays.save(train, "training_set")
    save_arrays.save(test, "test_set")


def split(set):
    set_x = [x[0] for x in set]
    set_y = [y[1] for y in set]
    set_y = np.array(set_y)
    len_action = len(set_y[0][0])
    len_type = len(set_y[0][1])
    len_param = len(set_y[0][2])

    y = [crea_output(set_y, len_action, 0), crea_output(set_y, len_type, 1), crea_output(set_y, len_param, 2), crea_output(set_y, len_type, 3),
         crea_output(set_y, len_param, 4), crea_output(set_y, len_type, 5), crea_output(set_y, len_param, 6), crea_output(set_y, len_type, 7), crea_output(set_y, len_param, 8)]

    return np.array(set_x), y


def crea_output(set, len_out, pos):
    dim = len(set)
    output = np.zeros((dim, len_out))

    for i in range(dim):
        output[i][:] = set[i, pos][:]
    return output


def get_net(dim):
    input = Input(shape=(dim,))
    d1 = Dense(100, activation="linear")(input)
    o1 = Dense(10, activation="softmax", name='action_type')(d1)
    o2 = Dense(6, activation="softmax", name='type1')(d1)
    o3 = Dense(104, activation="softmax", name='param1')(d1)
    o4 = Dense(6, activation="softmax", name='type2')(d1)
    o5 = Dense(104, activation="softmax", name='param2')(d1)
    o6 = Dense(6, activation="softmax", name='type3')(d1)
    o7 = Dense(104, activation="softmax", name='param3')(d1)
    o8 = Dense(6, activation="softmax", name='type4')(d1)
    o9 = Dense(104, activation="softmax", name='param4')(d1)
    model = Model(input=input, outputs=[o1, o2, o3, o4, o5, o6, o7, o8, o9])
    adam = keras.optimizers.Adam(learning_rate=0.1, beta_1=0.9, beta_2=0.999, amsgrad=False)
    model.compile(optimizer=adam, loss='categorical_crossentropy')
    return model


