from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/skill", methods=["POST"])
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "사용자 발화 : " + str(request.json['userRequest']['utterance'])
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "퀵리플라이1",
                    "action": "message",
                    "messageText": "퀵리플라이1 응답메세지"
                },
                {
                    "label": "퀵리플라이2",
                    "action": "message",
                    "messageText": "퀵리플라이2 응답메세지"
                },
                {
                    "label": "퀵리플라이3",
                    "action": "message",
                    "messageText": "퀵리플라이3 응답메세지"
                }
            ]
        }
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
