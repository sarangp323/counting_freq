import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from xgboost import XGBRegressor
from tpot.export_utils import set_param_recursive

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=42)

# Average CV score on the training set was: -5.526585316898924
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=ExtraTreesRegressor(bootstrap=True, max_features=1.0, min_samples_leaf=4, min_samples_split=16, n_estimators=100)),
    StackingEstimator(estimator=GradientBoostingRegressor(alpha=0.75, learning_rate=0.1, loss="quantile", max_depth=3, max_features=0.1, min_samples_leaf=5, min_samples_split=12, n_estimators=100, subsample=1.0)),
    StackingEstimator(estimator=ElasticNetCV(l1_ratio=1.0, tol=1e-05)),
    XGBRegressor(learning_rate=0.01, max_depth=8, min_child_weight=5, n_estimators=100, n_jobs=1, objective="reg:squarederror", subsample=0.4, verbosity=0)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
