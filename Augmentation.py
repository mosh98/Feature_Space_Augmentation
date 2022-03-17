import copy
import numpy as np

class Augmentation():
    def __init__(self):
        pass

    def linear_delta(self):
        print("Linear Delta")

        return None

    def delta_S(self,embed_list, label_list,target = None):
        # Checks
        self.list_exceptions(embed_list)
        self.list_exceptions(label_list)
        
        #Now we do the actual things
        cpy_embed_list = copy.copy(embed_list)
        cpy_label_list = copy.copy(label_list)
        #-------------------------------------


        return None


    def add_noise(self, embed_list, label_list, noise_low= 0.0, nose_high= 0.1):
        """
        Add noise to the embedding
        :param embed_list: Pass in the embedding list
        :param label_list: Pass in the label list
        :param noise_low: The lower bound of the noise
        :param nose_high: The higher bound of the noise
        :return: extended list of embeddings and labels with added noise.
        :rtype: list, list
        """
        # Check if the list is empty
        self.list_exceptions(embed_list)
        self.list_exceptions(label_list)

        #Now we do the actual things
        cpy_embed_list = copy.copy(embed_list)
        cpy_label_list = copy.copy(label_list)
        noise =  np.random.uniform(noise_low, nose_high, size=(cpy_embed_list[0].shape[0],))

        augmented_samples = []
        augmented_labels = []

        for i in range(len(cpy_embed_list)):
            augmented_samples.append(cpy_embed_list[i])
            augmented_labels.append(cpy_label_list[i])

            sample = cpy_embed_list[i] + noise
            augmented_samples.append(sample)
            augmented_labels.append(cpy_label_list[i])

        return augmented_samples, augmented_labels

    def list_exceptions(self,list):
        if len(list) == 0:
            return Exception("List is empty")
        else:
            return None