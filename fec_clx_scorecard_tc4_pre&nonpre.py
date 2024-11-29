data = [{
        "fileName": "0OIM2CTEE10C34927RKO5VTGJC06ORR9_2024-03-19_01-40-19_0.mp3",
        "agentChannel": 1,
        "callClassifyAI": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: alo <customer>: nghe <agent>: ờ anh anh đức nghe máy chào anh em bên fe nè anh ơi cái hợp đồng vay của mình hôm nay là 14 ngày trễ hẹn là 4378000 thu xếp chiều nay ra thanh toán giùm em nha <customer>: có tiền đâu <agent>: dạ alo <customer>: chưa thu xếp được tiền em ơi <agent>: anh nói sao anh <customer>: chưa có thu xếp được tiền <agent>: mình đang khó khăn nha anh 14 ngày trễ rồi mà chưa thu xếp được tiền khi nào mới có tiền đóng cho ngân hàng nữa <customer>: anh bị thất nghiệp anh đang tìm việc làm",
                    "intents": [
                        "client"
                    ],
                    "entities": {}
                }
            ],
            "decision": "client",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0
            },
            "position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: alo <customer>: nghe <agent>: ờ anh anh đức nghe máy chào anh em bên fe nè anh ơi cái hợp đồng vay của mình hôm nay là 14 ngày trễ hẹn là 4378000 thu xếp chiều nay ra thanh toán giùm em nha <customer>: có tiền đâu <agent>: dạ alo <customer>: chưa thu xếp được tiền em ơi <agent>: anh nói sao anh <customer>: chưa có thu xếp được tiền <agent>: mình đang khó khăn nha anh 14 ngày trễ rồi mà chưa thu xếp được tiền khi nào mới có tiền đóng cho ngân hàng nữa <customer>: anh bị thất nghiệp anh đang tìm việc làm",
                    "intents": [
                        "client"
                    ],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                0,
                0
            ],
            "position_condition": [
                0
            ],
            "task": "compare"
        },
        "callResultAI": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<customer>: anh bị thất nghiệp anh đang tìm việc làm <agent>: anh bị thất nghiệp hả thì giờ mình coi mình kiếm việc <customer>: ừ <agent>: mình nhờ tháng ai hỗ trợ đóng đi mình mượn đâu đỡ đóng được không <customer>: mượn 2 tháng sao cho mượn <agent>: cái hợp đồng mà để vậy hợp đồng mình nó bị ghi nhận nợ xấu hay sao hay sao anh vay vay vốn được là anh muốn mua hàng trả góp gì cũng khó khăn mình biết rồi đúng không bên em hỗ trợ cho mình rồi bây giờ là 10 <customer>: vậy nè <agent>: 4 ngày trễ rồi chị có thu xếp mình trong ngày mai hôm nay chậm nhất hôm nay trước 5 giờ được không <customer>: được <agent>: vậy hả <customer>: được rồi <agent>: dạ khi nào mình thanh toán được dạ để em biết <customer>: chưa biết nữa <agent>: đóng cho ngân hàng đi nha mà phát sinh rủi ro hợp đồng thì anh tự chịu trách nhiệm nha cảm ơn chào <customer>: ừ",
                    "intents": [
                        "willpay"
                    ],
                    "entities": {}
                }
            ],
            "decision": "willpay",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0
            },
            "position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<customer>: anh bị thất nghiệp anh đang tìm việc làm <agent>: anh bị thất nghiệp hả thì giờ mình coi mình kiếm việc <customer>: ừ <agent>: mình nhờ tháng ai hỗ trợ đóng đi mình mượn đâu đỡ đóng được không <customer>: mượn 2 tháng sao cho mượn <agent>: cái hợp đồng mà để vậy hợp đồng mình nó bị ghi nhận nợ xấu hay sao hay sao anh vay vay vốn được là anh muốn mua hàng trả góp gì cũng khó khăn mình biết rồi đúng không bên em hỗ trợ cho mình rồi bây giờ là 10 <customer>: vậy nè <agent>: 4 ngày trễ rồi chị có thu xếp mình trong ngày mai hôm nay chậm nhất hôm nay trước 5 giờ được không <customer>: được <agent>: vậy hả <customer>: được rồi <agent>: dạ khi nào mình thanh toán được dạ để em biết <customer>: chưa biết nữa <agent>: đóng cho ngân hàng đi nha mà phát sinh rủi ro hợp đồng thì anh tự chịu trách nhiệm nha cảm ơn chào <customer>: ừ",
                    "intents": [
                        "willpay"
                    ],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                0,
                0
            ],
            "position_condition": [
                0
            ],
            "task": "compare"
        },
        "cusRefuseUnfriendly": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 5,
                    "channel": 2,
                    "text": "chưa thu xếp được tiền em ơi",
                    "intents": [
                        "cus_refuse_pay"
                    ],
                    "entities": {}
                },
                {
                    "index": 6,
                    "channel": 1,
                    "text": "anh nói sao anh",
                    "intents": [],
                    "entities": {}
                }
            ],
            "decision": "yes",
            "confidence": 1.0,
            "confidence_channel": {
                "2": 1.0,
                "1": 1.0
            },
            "position": [
                {
                    "index": 5,
                    "channel": 2,
                    "text": "chưa thu xếp được tiền em ơi",
                    "intents": [
                        "cus_refuse_pay"
                    ],
                    "entities": {}
                },
                {
                    "index": 6,
                    "channel": 1,
                    "text": "anh nói sao anh",
                    "intents": [],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                5,
                6
            ],
            "position_condition": [
                5,
                6,
                7
            ],
            "task": "compare"
        }
    },]

result = []
for i in data:
    if (i["callClassifyAI"]["decision"]) == "ec":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối khách do rơi vào trường hợp EC"
        })
    # nếu đi vào nhánh wrong_contact thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "wrongnumber":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối do rơi vào nhầm máy"
        })
    elif (i["callClassifyAI"]["decision"]) == "silent":
        result.append({
            "file_name": i["fileName"],
            "result": "N/A",
            "reason": "không có tính huống từ chối do rơi vào im lặng"
        })
    else:
        if (i["callResultAI"]["decision"]) == "paid":
            result.append({
                "file_name": i["fileName"],
                "result": "Yes_20",
                "reason": "không có tính huống từ chối khách hàng đã thanh toán"
            })
        else:
            if (i["cusRefuseUnfriendly"]["evaluate"]) == "yes" and (i["cusRefuseUnfriendly"]["decision"]) == "yes":
                if (i["agentQuoteRules"]["decision"]) == "yes":
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason":"2/2 ý và có dẫn luật (call trễ hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "có nói dẫn luật nhưng k nói lợi ích hoặc hậu quả (xem lại)"
                        })
                else:
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "1/2 ý và không có dẫn luật (call trễ hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "No",
                            "reason": "không nói dẫn luật + không nói lợi ích hoặc hậu quả"
                        })
            else:
                result.append({
                    "file_name": i["fileName"],
                    "result": "Yes_20",
                    "reason": "không có tình huông từ chối"
                })
print(result)