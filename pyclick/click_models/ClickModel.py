#
# Copyright (C) 2015  Ilya Markov
#
# Full copyright notice can be found in LICENSE.
#
from abc import abstractmethod
import json
from enum import Enum

__author__ = 'Ilya Markov'


class ClickModel(object):
    """An abstract click model."""

    param_names = Enum('ParamNames', 'param_name')
    """
    The names of the click model parameters.
    Should be defined by each subclass.
    """

    def __init__(self):
        self.params = {}
        self._inference = None

    def get_param(self, param_name):
        """Returns a container of parameters with the given name."""
        return self.params(param_name)

    def train(self, search_sessions):
        """Trains the click model using the given list of search sessions."""
        self._inference.infer_params(self, search_sessions)

    def to_json(self):
        """
        Converts the model into JSON and returns the corresponding string.

        :returns: The JSON representation of the model.
        """
        json_dict = {}
        for param_name, param in self.params.items():
            json_dict[param_name.name] = param.to_json()
        return json.dumps(json_dict)

    def from_json(self, json_str):
        """
        Initializes the model from the given JSON string.

        :param json_param: The JSON representation of the model.
        """
        json_obj = json.loads(json_str)
        for json_param_name, json_param in json_obj.items():
            param_name = self.param_names[json_param_name]
            self.params[param_name].from_json(json_param)

    def __str__(self):
        params_str = ''
        for param_name, param in self.params.items():
            params_str += '%s\n%s\n' % (param_name, param)
        return params_str

    def __repr__(self):
        return str(self)

    @abstractmethod
    def predict_click_probs(self, search_session):
        """Uses the trained parameters to predict click probabilities
        for results in the given search session."""
        pass

    @abstractmethod
    def get_session_params(self, search_session):
        """Returns click model parameters that describe the given search session.
        In particular, for each result X in the given search session
        creates a dictionary of corresponding parameters
        in the form {param1_name:param1_for_X, param2_name:param2_for_X, ...}.
        Then the list of these dictionaries is returned,
        where returned_dict_list[i] corresponds to search_session.results[i].
        """
        pass

    @abstractmethod
    def get_conditional_click_probs(self, search_session):
        """
        Returns a list of click probabilities conditioned on the observed clicks in the given search session.
        In particular, for a result at rank k calculates the following probability:
        P(C_k | C_1, C_2, ..., C_k-1),
        where C_i is 1 if there is a click on the i-th result in the given search session and 0 otherwise.
        """
        pass

    @abstractmethod
    def predict_click_probs(self, search_session):
        """
        Returns a list of predicted probabilities of click P(C = 1) for all results in the given search session.
        """
        pass

    @abstractmethod
    def predict_relevance(self, query, search_result):
        """
        Predicts the relevance of a given search result to a given query.

        :param query: The query.
        :param search_result: The identifier of the search result (NOT the SearchResult object).
        :returns: Predicted relevance.
        """
        pass