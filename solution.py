import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp



chat_id = 250483508 # Ваш chat ID, не меняйте название переменной

def solution(sample: np.ndarray) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
       alpha = 0.04
    _, p_value = ttest_1samp(sample, 300)

    if p_value < alpha:
        return True
    else:
        return False
