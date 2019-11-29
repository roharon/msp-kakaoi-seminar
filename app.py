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
                                "label": "010-0000-0000에 전화걸기",
                                "action": "phone",
                                "phoneNumber": "010-0000-0000"
                            },
                            {
                                "label": "공유하기",
                                "action": "share"
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
