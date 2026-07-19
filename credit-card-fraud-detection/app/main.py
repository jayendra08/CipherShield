from flask import Flask, render_template, request

try:
	from .predictor import predict_transaction
except ImportError:
	from predictor import predict_transaction


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
	result = predict_transaction(request.form)
	return render_template("index.html", prediction=result)


if __name__ == "__main__":
	app.run(debug=True)
