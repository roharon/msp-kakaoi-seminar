from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/skill", methods=["POST"])
def skill():
    print(request.json)
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "http://builder.hufs.ac.kr/user/hufs/mycodyimages/new/goimg_navy.png",
                        "altText": "HUFS 로고"
                    }
                }
            ]
        }   
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
