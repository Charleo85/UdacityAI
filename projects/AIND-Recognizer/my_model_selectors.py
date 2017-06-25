import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        n = len((self.lengths))
        logN = np.log(n)

        min_bic = 1000000
        best_model = None
        for nb_hidden_state in range(self.min_n_components, self.max_n_components + 1):
            try:
                hmm_model = GaussianHMM(n_components=nb_hidden_state, covariance_type="diag", n_iter=1000,
                                        random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
                bic = -2 * hmm_model.score(self.X, self.lengths) + (n*n + 2 * nb_hidden_state * n - 1) * logN
                if bic < min_bic:
                    min_bic = bic
                    best_model = hmm_model
            except:
                continue
        return best_model

class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores
        best_BIC = -1000000000
        best_model = self.base_model(self.min_n_components)
        for i in range(self.min_n_components, self.max_n_components+1):
            try:
                model1 = self.base_model(i)
                logL1 = model1.score(self.X, self.lengths)
                all_but_this_word = 0
                word_count = 0
                for word in self.hwords:
                    if word != self.this_word:
                        X, lengths = self.hwords[word]
                        all_but_this_word += model1.score(X, lengths)
                        word_count += 1
                DIC = logL1 - (all_but_this_word/ ( word_count -1))
                if DIC > best_BIC:
                    best_BIC = DIC
                    best_model = model1
            except:
                if self.verbose:
                    print("failure on {} with {} states".format(self.this_word, i))
                return best_model
        return best_model


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection using CV
        n_splits = min(3, len(self.lengths))
        max_mean_logL = -1000000
        best_hidden_state = 0
        for nb_hidden_state in range(self.min_n_components, self.max_n_components+1):
            sum_log = 0
            n_splits_done = 0
            mean_logL = -1000000
            if n_splits == 1 :
                try :
                    hmm_model = GaussianHMM(n_components=nb_hidden_state, covariance_type="diag", n_iter=1000,
                                            random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
                    mean_logL = hmm_model.score(self.X, self.lengths)
                except:
                    continue

            else :
                split_method = KFold(n_splits=n_splits)
                for cv_train_idx, cv_test_idx in split_method.split(self.sequences):
                    X_train, lengths_train = combine_sequences(cv_train_idx, self.sequences)
                    try:
                        model, logL =  self.selected_model(nb_hidden_state, X_train, lengths_train)
                        sum_log += logL
                        n_splits_done += 1
                    except:
                        continue
                if n_splits_done != 0 :
                    mean_logL = sum_log / float(n_splits_done)
                else:
                    mean_logL = -1000000
            if(mean_logL> max_mean_logL):
                max_mean_logL = mean_logL
                best_hidden_state = nb_hidden_state
        if best_hidden_state == 0:
            return self.base_model(self.n_constant)
        else:
            return self.base_model(best_hidden_state)
