from app import model  # or just `import model` depending on structure

def test_model_output():
    # Load data and train the model
    data = model.load_data()
    df = model.prepare_data(data)
    trained_model, X_test, y_test = model.train_model(df)

    # Check predictions
    predictions = trained_model.predict(X_test)
    assert len(predictions) == len(y_test), "Prediction count should match labels"

    # Ensure output is only 0 or 1
    assert set(predictions).issubset({0, 1}), "Predictions must be 0 or 1"
