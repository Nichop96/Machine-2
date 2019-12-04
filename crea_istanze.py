import plan
import numpy as np


def crea(plans):
    actions = np.concatenate([p.actions for p in plans], axis=0)
    db = []
    for action in actions:
        data = np.array([])
        i = 0
        for prec in action.oneHotprecondition:
            data = np.concatenate([data, prec])
            i += 1
        for j in range(i, 3):
            data = np.concatenate([data, np.zeros(450)])
        i = 0
        for pos in action.oneHotpositiveEffects:
            data = np.concatenate([data, pos])
            i += 1
        for j in range(i, 1):
            data = np.concatenate([data, np.zeros(450)])
        i = 0
        for neg in action.oneHotnegativeEffects:
            data = np.concatenate([data, neg])
            i+=1
        for j in range(i, 1):
            data = np.concatenate([data, np.zeros(450)])
        d1 = action.oneHotAtction[:10]
        d2 = action.oneHotAtction[10: 16]
        d3 = action.oneHotAtction[16: 120]
        d4 = action.oneHotAtction[120: 126]
        d5 = action.oneHotAtction[126: 230]
        d6 = action.oneHotAtction[230: 236]
        d7 = action.oneHotAtction[236: 340]
        d8 = action.oneHotAtction[340: 346]
        d9 = action.oneHotAtction[346: 450]
        db.append((data, [d1, d2, d3, d4, d5, d6, d7, d8, d9]))

    return db