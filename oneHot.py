import numpy as np

NUMBER_ACTIONS = 10
MAX_OBJECTS = 104
ACTIONS = ["LOAD-TRUCK", "UNLOAD-TRUCK", "DRIVE-TRUCK", "LOAD-AIRPLANE", "UNLOAD-AIRPLANE", "FLY-AIRPLANE", "at", "in", "not at", "not in"]
TYPES_OBJECT = ["APN", "CIT", "OBJ", "LOC", "TRU", "EMPTY"]


def split_name_action(action):
    array = action.strip().split(" ")
    return array


def oneHot_parameter(parameter, apn_list, cit_list, obj_list, loc_list, tru_list):
    type = np.zeros(len(TYPES_OBJECT))
    if "APN" in parameter:
        type[0] = 1
        return np.concatenate([type, oneHot(parameter, apn_list, MAX_OBJECTS)])
    if "CIT" in parameter:
        type[1] = 1
        return np.concatenate([type, oneHot(parameter, cit_list, MAX_OBJECTS)])
    if "OBJ" in parameter:
        type[2] = 1
        return np.concatenate([type, oneHot(parameter, obj_list, MAX_OBJECTS)])
    if "LOC" in parameter:
        type[3] = 1
        return np.concatenate([type, oneHot(parameter, loc_list, MAX_OBJECTS)])
    if "TRU" in parameter:
        type[4] = 1
        return np.concatenate([type, oneHot(parameter, tru_list, MAX_OBJECTS)])


def invalid_encode():
    array = np.zeros(len(TYPES_OBJECT)+MAX_OBJECTS)
    array[len(TYPES_OBJECT)-1] = 1
    array[len(TYPES_OBJECT)+MAX_OBJECTS - 1] = 1
    return array

def oneHot(parameter, array, max_length):
    index = -1
    for id, val in enumerate(array):
        if parameter == val:
            index = id
    if index != -1:
        array = np.zeros(max_length)
        array[index] = 1
        return array
    return -1

def oneHotToVect(code, array):
    code = approximate(code)
    for i in range(len(code)):
        if code[i]==1:
            if(i >= len(array)):
                return "SBAGLIATO"
            return array[i]
    return -1

def oneHotObjectToVect(object, apn_list, cit_list, obj_list, loc_list, tru_list):
    type = ""
    temp = approximate(object[0:(len(TYPES_OBJECT))])
    for i in range(len(TYPES_OBJECT)):
        if temp[i]==1:
            type = TYPES_OBJECT[i]
    if "APN" in type:
        return str(oneHotToVect(object[len(TYPES_OBJECT):], apn_list))
    if "CIT" in type:
        return str(oneHotToVect(object[len(TYPES_OBJECT):], cit_list))
    if "OBJ" in type:
        return str(oneHotToVect(object[len(TYPES_OBJECT):], obj_list))
    if "LOC" in type:
        return str(oneHotToVect(object[len(TYPES_OBJECT):], loc_list))
    if "TRU" in type:
        return str(oneHotToVect(object[len(TYPES_OBJECT):], tru_list))
    if "EMPTY" in type:
        return "EMPTY"

def approximate(code):
    index = np.where(code == np.amax(code))[0][0]
    app = np.zeros(len(code))
    app[index] = 1
    return app

def oneHotActionToVect(code, apn_list, cit_list, obj_list, loc_list, tru_list):
    temp = approximate(code[0:(len(ACTIONS))])
    for i in range(len(ACTIONS)):
        if temp[i] == 1:
            string = ACTIONS[i]
            break
    for i in range((len(code)-len(ACTIONS))//MAX_OBJECTS):
        string += " " + oneHotObjectToVect(code[(len(ACTIONS)+((MAX_OBJECTS+len(TYPES_OBJECT))*i)) : (len(ACTIONS) + (MAX_OBJECTS+len(TYPES_OBJECT))*(i+1)-1)], apn_list, cit_list, obj_list, loc_list, tru_list) + " "
    return string

def check_output_test(output, test, apn_list, cit_list, obj_list, loc_list, tru_list):
    match= np.zeros(9)
    if np.array_equal(approximate(output[:10]), approximate(test[:10])):
        match[0] = 1
    if np.array_equal(approximate(output[10: 16]), approximate(test[10: 16])):
        match[1] = 1
    if np.array_equal(approximate(output[16: 120]), approximate(test[16: 120])):
        match[2] = 1
    if np.array_equal(approximate(output[120: 126]), approximate(test[120: 126])):
        match[3] = 1
    if np.array_equal(approximate(output[126: 230]), approximate(test[126: 230])):
        match[4] = 1
    if np.array_equal(approximate(output[230: 236]), approximate(test[230: 236])):
        match[5] = 1
    if np.array_equal(approximate(output[236: 340]), approximate(test[236: 340])):
        match[6] = 1
    if np.array_equal(approximate(output[340: 346]), approximate(test[340: 346])):
        match[7] = 1
    if np.array_equal(approximate(output[346: 450]), approximate(test[346: 450])):
        match[8] = 1
    return match

def oneHotAction(action, apn_list, cit_list, obj_list, loc_list, tru_list):
    array = split_name_action(action)
    code = oneHot(array[0], ACTIONS, NUMBER_ACTIONS)
    for i in range(1, len(array)):
        code = np.concatenate((code, oneHot_parameter(array[i], apn_list, cit_list, obj_list, loc_list, tru_list)))
    for i in range(len(array) - 1, 4):
        code = np.concatenate([code, invalid_encode()])
    return code


def oneHotPredicate(pred, apn_list, cit_list, obj_list, loc_list, tru_list):
    array = split_name_action(pred)
    code = oneHot(array[0], ACTIONS, NUMBER_ACTIONS)
    for i in range(1, len(array)):
        code = np.concatenate((code, oneHot_parameter(array[i].upper(), apn_list, cit_list, obj_list, loc_list, tru_list)))
    for i in range(len(array) - 1, 4):
        code = np.concatenate([code, invalid_encode()])
    return code


def oneHotPredicateNeg(negEff, apn_list, cit_list, obj_list, loc_list, tru_list):
    array = split_name_action(negEff)
    if array[0] == "in":
        array[0] = "not in"
    if array[0] == "at":
        array[0] = "not at"
    code = oneHot(array[0], ACTIONS, NUMBER_ACTIONS)
    for i in range(1, len(array)):
        code = np.concatenate((code, oneHot_parameter(array[i].upper(), apn_list, cit_list, obj_list, loc_list, tru_list)))
    for i in range(len(array) - 1, 4):
        code = np.concatenate([code, invalid_encode()])
    return code


def init(plans, apn_list, cit_list, obj_list, loc_list, tru_list):
    for p in plans:
        for action in p.actions:
            action.code_action(oneHotAction(action.name, apn_list, cit_list, obj_list, loc_list, tru_list))
            pos = []
            for posEff in action.positiveEffects:
                pos.append(oneHotPredicate(posEff, apn_list, cit_list, obj_list, loc_list, tru_list))
            precond = []
            for prec in action.precondition:
                precond.append(oneHotPredicate(prec, apn_list, cit_list, obj_list, loc_list, tru_list))
            neg = []
            for negEff in action.negativeEffects:
                neg.append(oneHotPredicateNeg(negEff, apn_list, cit_list, obj_list, loc_list, tru_list))
            action.code_positiveEffects(np.asarray(pos))
            action.code_precondition(np.asarray(precond))
            action.code_negativeEffects(np.asarray(neg))

    
    # for p in plans:
    #     for action in p.actions:
    #         print(action.name, oneHotActionToVect(oneHotAction(action.name, apn_list, cit_list, obj_list, loc_list, tru_list), apn_list, cit_list, obj_list, loc_list, tru_list))
    #         for posEff in action.positiveEffects:
    #             print(posEff, oneHotActionToVect(oneHotPredicate(posEff, apn_list, cit_list, obj_list, loc_list, tru_list), apn_list, cit_list, obj_list, loc_list, tru_list))
    #         for prec in action.precondition:
    #             print(prec, oneHotActionToVect(oneHotPredicate(prec, apn_list, cit_list, obj_list, loc_list, tru_list), apn_list, cit_list, obj_list, loc_list, tru_list))
    #         neg = []
    #         for negEff in action.negativeEffects:
    #             print(negEff,oneHotActionToVect(oneHotPredicateNeg(negEff, apn_list, cit_list, obj_list, loc_list, tru_list), apn_list, cit_list, obj_list, loc_list, tru_list))
    #

