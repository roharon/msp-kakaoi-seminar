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
                            "imageUrl": "https://t1.daumcdn.net/friends/www/talk/kakaofriends_talk_2018.png",
                            "link": {
                                "mobile": "https://naver.com",
                                "android": "https://google.com",
                                "web": "https://daum.net",
                                "pc": "https://github.com"
                                }
                            },
                        "buttons": [
                            {
                                "label": "Azure로 이동하기",
                                "action": "webLink",
                                "webLinkUrl": "https://portal.azure.com"
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
