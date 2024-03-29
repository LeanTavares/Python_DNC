import pickle
import pandas as pd

#load data
def load_data():
    new_data = pd.DataFrame([[5.6,9.5,5,6]])
    return new_data

#load model
def load_model():
    with open("trained_classifier.pkl", "rb") as file:
        model = pickle.load(file)
    return model

#make predictions
def make_predictions(data, model):
    return model.predict(data)

#Write results
def write_results(predictions):
    print(predictions)

#orchestration
def run():
    new_data = load_data()
    model = load_model()
    predictions = make_predictions(data = new_data, model = model)
    write_results(predictions = predictions)

if __name__ == "__main__":
    run()