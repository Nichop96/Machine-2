import pickle
from matplotlib import pyplot as plt

if __name__ == '__main__':

        # da aggiustare i plot
        history = open("history", "rb")
        history = pickle.load(history)

        plt.plot(history.history['loss'])
        plt.plot(history.history['action_type_loss'])
        plt.plot(history.history['type1_loss'])
        plt.plot(history.history['param1_loss'])
        plt.plot(history.history['type2_loss'])
        plt.plot(history.history['param2_loss'])
        plt.plot(history.history['type3_loss'])
        plt.plot(history.history['param3_loss'])
        plt.plot(history.history['type4_loss'])
        plt.plot(history.history['param4_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train'], loc='upper left')
        plt.show()



