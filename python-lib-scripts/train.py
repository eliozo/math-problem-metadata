import gspread
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Function to load data from Google Spreadsheet
def load_data(sheet_url):
    # Authenticate without credentials (only works for public spreadsheets)
    client = gspread.authorize(None)

    # Open the spreadsheet
    sheet = client.open_by_url(sheet_url)

    # Select the first worksheet
    worksheet = sheet.get_worksheet(0)

    # Get the data from the worksheet
    english_concepts = worksheet.col_values(1)[1:]  # Assuming English concepts are in column A, starting from row 2
    latvian_concepts = worksheet.col_values(2)[1:]  # Assuming Latvian concepts are in column B, starting from row 2

    return english_concepts, latvian_concepts

# Load data from Google Spreadsheet
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pubhtml"
english_concepts, latvian_concepts = load_data(sheet_url)

# Encode labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(english_concepts)

# Manually define problem texts
problems = [
    "Solve the equation x^2 - 4 = 0",
    "Find the derivative of f(x) = sin(x)",
    "Calculate the area of a circle with radius 5"
]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(problems, encoded_labels, test_size=0.2, random_state=42)

# Build a pipeline for text classification
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy:", accuracy)

# Function to predict concepts for a given problem
def predict_concepts(problem):
    predicted_label = model.predict([problem])[0]
    predicted_concept = label_encoder.inverse_transform([predicted_label])[0]
    return predicted_concept

# Example usage
example_problem = "Solve the equation x^2 - 4 = 0"
predicted_concept = predict_concepts(example_problem)
print("Predicted concept for the problem:", predicted_concept)
