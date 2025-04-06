import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import model
import numpy as np

def test_model_output_shape():
    # Call train_model() which returns the trained model and feature names
    trained_model, feature_names = model.train_model()

    # Create a fake input row with 30 feature values (same as number of features)
    dummy_input = np.array([15.0] * len(feature_names)).reshape(1, -1)

    # Make a prediction
    prediction = trained_model.predict(dummy_input)

    # Assertions to verify model behavior
    assert prediction.shape == (1,), "Prediction should return one result"
    assert prediction[0] in [0, 1], "Prediction should be 0 or 1"

