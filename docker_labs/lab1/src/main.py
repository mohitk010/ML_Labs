# Import necessary libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

if __name__ == '__main__':
    # Load the Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=21)

    # Train a Logistic Regression model
    model = LogisticRegression(max_iter=500, solver='lbfgs', multi_class='auto', random_state=21)
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, 'wine_quality_model.pkl')
    
    print("Model trained and saved successfully.")
