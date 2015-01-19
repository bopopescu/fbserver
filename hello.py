from flask import Flask
import numpy as np
from sklearn.svm import SVC

app = Flask(__name__)

@app.route("/")
def hello():
	print np.array([1,2,3,4])
	return 'hello world 788'

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080)
