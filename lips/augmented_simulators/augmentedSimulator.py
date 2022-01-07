# Copyright (c) 2021, IRT SystemX (https://www.irt-systemx.fr/en/)
# See AUTHORS.txt
# This Source Code Form is subject to the terms of the Mozilla Public License, version 2.0.
# If a copy of the Mozilla Public License, version 2.0 was not distributed with this file,
# you can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0
# This file is part of LIPS, LIPS is a python platform for power networks benchmarking

from typing import Union
from lips.dataset import DataSet


class AugmentedSimulator(object):
    """
    This class is the Base class that is used to create some "augmented simulator". These "augmented simulator" can be
    anything that emulates the behaviour of some "simulator".

    They are meant to use data coming from a `DataSet` to learn from it.
    """
    def __init__(self, name: str):
        self.name = name
        
        self._observations = dict()
        self._predictions = dict()

    def train(self, nb_iter: int, train_dataset: DataSet, val_dataset: Union[None, DataSet] = None):
        """
        Train the Augmented simulator using the provided datasets (parameters `train_dataset` and
        `val_dataset`) for a given number of iterations (`nb_iter`)
        """
        if not isinstance(train_dataset, DataSet):
            raise RuntimeError(f"The \"train_dataset\" should be an instance of DataSet. "
                               f"We found {type(train_dataset)}")
        if val_dataset is not None:
            if not isinstance(val_dataset, DataSet):
                raise RuntimeError(f"The \"val_dataset\" should be an instance of DataSet. "
                                   f"We found {type(val_dataset)}")

        if nb_iter <= 0:
            raise RuntimeError("Impossible to train a model for a negative number of iteration. Make sure that "
                               "`nb_iter` > 0.")

    def evaluate(self, dataset: DataSet):
        """
        evaluate the model on the full dataset
        """
        pass

    def init(self, **kwargs):
        """
        initialize the "augmented simulator".

        For example, this is where the model should be built in case the augmented simulator used a neural network.
        """
        pass

    def process_dataset(self, one_example):
        """
        This function transforms one state of a dataset (one row if you want) into something that can be used by
        the neural network (for example)
        """
        pass

    def data_to_dict(self):
        """
        This function should return two dictionaries in the following order 
            - the observations used for evaluation 
            - corresponding predictions
        """
        pass

    def save(self, path_out: str):
        """save the model at a given path"""
        pass

    def restore(self, path: str):
        """
        restore the model from the given path. It is expected to raise an error if it cannot be initialized
        by the data located at `path`
        """
        pass

    def save_metadata(self, path_out: str):
        """
        Saves the "metadata" of the model.

        Metadata should be, if possible, serializable to json.

        For example, this is the perfect function to save the meta parameters of a neural network
        """
        pass

    def load_metadata(self, path: str):
        """load the metada from the given path."""
        pass
