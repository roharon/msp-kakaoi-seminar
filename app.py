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
                    "basicCard":{
                        "title": "카드의 제목",
                        "description": "상세 설명",
                        "thumbnail": {
                            "imageUrl": "https://t1.daumcdn.net/friends/www/talk/kakaofriends_talk_2018.png"
                            },
                        "buttons": [
                            {
                                "label": "첫번째 버튼",
                                "action": "message",
                                "messageText": "첫번째 버튼을 눌렀습니다!"
                            }
                           
                        ]
                    }
                }
            ]
        }   
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
