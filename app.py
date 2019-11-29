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
                    "listCard": {
                        "header": {
                            "title": "한국외대 사이트모음",
                            "imageUrl": "http://builder.hufs.ac.kr/user/hufs/mycodyimages/main_new/main190829.jpg""
                        },
                        "items": [
                            {
                                "title": "메인 사이트",
                                "description": "학교 메인 웹사이트로 이동",
                                "imageUrl": "http://builder.hufs.ac.kr/user/hufs/mycodyimages/new/goimg_navy.png",
                                "link": {
                                    "web": "http://hufs.ac.kr/"
                                }
                            },
                            {
                                "title": "E-Class",
                                "description": "e-Class / 사이버강의 System"",
                                "imageUrl": "http://eclass2.hufs.ac.kr:8181/ilos/images/osms/hufs/ko/logo.gif",
                                "link": {
                                    "web": "http://eclass2.hufs.ac.kr:8181/ilos/main/main_form.acl"
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "강의실 대실하러가기,
                                "action": "webLink",
                                "webLinkUrl": "https://rs.hufs.ac.kr/"
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
