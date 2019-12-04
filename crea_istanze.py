import plan
import numpy as np


def crea(plans):

    num_train_actions = 3
    db = []

    for plan in plans:
        actions = np.concatenate([plan.actions], axis=0)
        for i in range(len(actions)):
            data = np.array([])
            if (i+num_train_actions) >= len(actions):
                break

            for j in range(num_train_actions):
                data = np.concatenate([data, actions[i+j].oneHotAtction])
            d1 = actions[i+num_train_actions].oneHotAtction[:10]
            d2 = actions[i+num_train_actions].oneHotAtction[10: 16]
            d3 = actions[i+num_train_actions].oneHotAtction[16: 120]
            d4 = actions[i+num_train_actions].oneHotAtction[120: 126]
            d5 = actions[i+num_train_actions].oneHotAtction[126: 230]
            d6 = actions[i+num_train_actions].oneHotAtction[230: 236]
            d7 = actions[i+num_train_actions].oneHotAtction[236: 340]
            d8 = actions[i+num_train_actions].oneHotAtction[340: 346]
            d9 = actions[i+num_train_actions].oneHotAtction[346: 450]
            db.append((data, [d1, d2, d3, d4, d5, d6, d7, d8, d9]))
    return db