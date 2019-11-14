from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "200"

if __name__ == "__main__":
    app.run()