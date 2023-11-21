# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import numpy as np
import random
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt

@st.cache
def some_expensive_deap():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    testVar = creator.FitnessMin # This assignment causes Streamlit to fail

resultVar = some_expensive_deap()
if __name__ == "__main__":
    run()
