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
                    "commerceCard": {
                        "description": "서브웨이",
                        "price": 1000,
                        "discountRate": 10,
                        "discountedPrice": 900,
                        "currency": "won",
                        "thumbnails": [
                            {
                                "imageUrl": "http://subway.co.th/en/images/menu/catering/catering-mealbox.jpg",
                                "link": {
                                    "web": "http://subway-menu.com/subway-menu-germany/subway-to-go-box/"
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
                    }
                }
            ]
        }
        }
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
