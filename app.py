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
                    "carousel": {
                        "type": "commerceCard",
                        "items": [
                            {
                                "title": "서브웨이",
                                "description": "서브웨이입니다",
                                "price": 1000,
                                "discount": 200,
                                "currency": "won",
                                "thumbnails": [
                                    {
                                        "imageUrl": "http://subway.co.th/en/images/menu/catering/catering-mealbox.jpg",
                                        "link": {
                                            "web": "http://subway-menu.com/subway-menu-germany/subway-to-go-box/"
                                        }
                                    }
                                ],
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
                            },
                            {
                                "title": "던킨도넛",
                                "description": "던킨도넛입니다",
                                "price": 3000,
                                "discount": 200,
                                "currency": "won",
                                "thumbnails": [
                                    {
                                        "imageUrl": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/munckin-1548961144.jpg?crop=1xw:1xh;center,top&resize=480:*",
                                        "link": {
                                            "web": "https://news.dunkindonuts.com"
                                        }
                                    }
                                ],
                                "buttons": [
                                    {
                                        "label": "공유하기",
                                        "action": "share"
                                    }

                                ]
                            }
                        ],

                    }
                }
            ]
        }
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
