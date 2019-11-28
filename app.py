from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hi! If you wanna get response about Skill server, Go to /skill"
    
@app.route("/test", methods=["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list=[
            "abc",
            "def"
        ]
    )
    return data

@app.route("/skill", methods=["POST"])
def skill():
    print(request.json)
    data = {
        {
        "version": "2.0",
        "template": {
        "outputs": [
                {
                    "simpleText": {
                    "text": "간단한 텍스트 요소입니다."
                    }
                }
                ]
            }
        }
    }
    
    return jsonify(data)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


"""
"version": "2.0",
    "template": {
        "outputs": [
            {
                "listCard": {
                    "header": {
                        "title": "카카오i 디벨로퍼스를 소개할까?.",
                        "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                    },

                }
            },
            {
                "simpleText": {
                    "text": "사용자 발화 : " + str(request.json['userRequest']['utterance']) + "\n사용자 botUser :  " + request.json['userRequest']['user']['properties']['plusfriendUserKey']
                },
            },
            {
                "simpleImage":{
                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                    "altText": "보물상자래요"
                }
            }
        ],
        "quickReplies": [
            {
                    "label": "퀵리플라이1",
                    "action": "message",
                    "messageText": "퀼리플라이1 눌렀다!"
            },
            {
                    "label": "퀵리플라이2",
                    "action": "message",
                    "messageText": "퀵리플라이2 눌렀다!"
            },
            {
                    "label": "퀵리플라이3",
                    "action": "message",
                    "messageText": "퀵리플라이3 눌렀다!"
            }
        ]

"""