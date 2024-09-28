data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.1970810890197754,
    "askCusDifficult": {
        "evaluate": "no",
        "evaluate_channel": {
            "1": "no",
            "2": "no"
        },
        "decision_position": [],
        "decision": "no",
        "confidence": 0.0,
        "confidence_channel": {
            "1": 0.0,
            "2": 0.0
        },
        "position": [],
        "slots": {},
        "position_range_index": "null",
        "position_condition": [],
        "task": "compare"
    },
    "askLateReason": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "yes"
        },
        "decision_position": [
            [
                {
                    "index": 56,
                    "channel": 1,
                    "text": "à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha",
                    "intents": [
                        "ask_cus_reason"
                    ],
                    "entities": {}
                }
            ],
            [
                {
                    "index": 58,
                    "channel": 1,
                    "text": "ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha",
                    "intents": [
                        "ask_cus_reason"
                    ],
                    "entities": {}
                }
            ]
        ],
        "decision": "yes",
        "confidence": 1.0,
        "confidence_channel": {
            "1": 1.0,
            "2": 1.0
        },
        "position": [
            {
                "index": 56,
                "channel": 1,
                "text": "à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha",
                "intents": [
                    "ask_cus_reason"
                ],
                "entities": {}
            },
            {
                "index": 58,
                "channel": 1,
                "text": "ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha",
                "intents": [
                    "ask_cus_reason"
                ],
                "entities": {}
            }
        ],
        "slots": {},
        "task": "compare_beta"
    },
    "callClassifyAI": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<customer>: bận chờ tí <agent>: 1 giờ là chắc là 5 giờ con mới đi học về phải không <customer>: dạ đúng rồi <agent>: à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha <customer>: dạ đúng rồi <agent>: ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha <customer>: dạ dạ <agent>: ừ vậy thôi cứ cảm ơn nhiều nhá <customer>: dạ <agent>: ừ <customer>: cúp máy cái chú <agent>: à hả <customer>: cúp máy chứ <agent>: ờ ừ ừ văn quốc anh phúc <customer>: dạ",
                "intents": [
                    "ec"
                ],
                "entities": {}
            }
        ],
        "decision": "ec",
        "confidence": 1.0,
        "confidence_channel": {
            "1": 1.0
        },
        "position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<customer>: bận chờ tí <agent>: 1 giờ là chắc là 5 giờ con mới đi học về phải không <customer>: dạ đúng rồi <agent>: à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha <customer>: dạ đúng rồi <agent>: ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha <customer>: dạ dạ <agent>: ừ vậy thôi cứ cảm ơn nhiều nhá <customer>: dạ <agent>: ừ <customer>: cúp máy cái chú <agent>: à hả <customer>: cúp máy chứ <agent>: ờ ừ ừ văn quốc anh phúc <customer>: dạ",
                "intents": [
                    "ec"
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
                "text": "<customer>: bận chờ tí <agent>: 1 giờ là chắc là 5 giờ con mới đi học về phải không <customer>: dạ đúng rồi <agent>: à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha <customer>: dạ đúng rồi <agent>: ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha <customer>: dạ dạ <agent>: ừ vậy thôi cứ cảm ơn nhiều nhá <customer>: dạ <agent>: ừ <customer>: cúp máy cái chú <agent>: à hả <customer>: cúp máy chứ <agent>: ờ ừ ừ văn quốc anh phúc <customer>: dạ",
                "intents": [
                    "nopay"
                ],
                "entities": {}
            }
        ],
        "decision": "nopay",
        "confidence": 1.0,
        "confidence_channel": {
            "1": 1.0
        },
        "position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<customer>: bận chờ tí <agent>: 1 giờ là chắc là 5 giờ con mới đi học về phải không <customer>: dạ đúng rồi <agent>: à rồi thì học đi học về nha thì nhờ chú nhờ con nha là bảo với bố mẹ là à à bố mẹ đi làm về xong rồi ra thế giới di động hoặc là điện máy xanh gì ấy thanh toán cái khoản tiền trả góp cho bên chú nha <customer>: dạ đúng rồi <agent>: ừ bảo bố mẹ là bố mẹ có khoản nợ là bị chán hạn bị quá hạn của bên chú rồi nha bảo bố mẹ là đi làm về ra thanh toán luôn nha <customer>: dạ dạ <agent>: ừ vậy thôi cứ cảm ơn nhiều nhá <customer>: dạ <agent>: ừ <customer>: cúp máy cái chú <agent>: à hả <customer>: cúp máy chứ <agent>: ờ ừ ừ văn quốc anh phúc <customer>: dạ",
                "intents": [
                    "nopay"
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
    "criterias_order": [
        {
            "criteria_name": "askLateReason",
            "decision": "yes",
            "position_range_index": "",
            "slots": {}
        }
    ]
}]

result_data = []

for i in data:
    # nếu đi vào nhánh EC thì chấm full điểm
    if (i["callClassifyAI"]["decision"]) == "ec":
        result_data.append({
            "Type": "EC",
            "file_name": i["fileName"],
            "result": "Yes_10"
        })
    # nếu đi vào nhánh wrong_contact thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "wrong_contact":
        result_data.append({
            "Type": "Wrong",
            "file_name": i["fileName"],
            "result": "Yes_10"
        })
    # nếu đi vào nhánh silent thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "silent":
        result_data.append({
            "Type": "silent",
            "file_name": i["fileName"],
            "result": "N/A"
        })
    else:
        if (i["callClassifyAI"]["decision"]) == "client":
            if (i["callResultAI"]["decision"]) == "willpay":
                if (i["askLateReason"]["evaluate"]) and (i["askLateReason"]["decision"]) == "yes":
                    result_data.append({
                        "Type": "client",
                        "file_name": i["fileName"],
                        "result": "Yes_5"
                    })
                else:
                    result_data.append({
                        "Type": "client",
                        "file_name": i["fileName"],
                        "result": "No"
                    })
            elif (i["callResultAI"]["decision"]) == "nopay":
                if (i["askLateReason"]["evaluate"]) and (i["askLateReason"]["decision"]) == "yes":
                    result_data.append({
                        "Type": "client",
                        "file_name": i["fileName"],
                        "result": "Yes_10"
                    })
                else:
                    result_data.append({
                        "Type": "client",
                        "file_name": i["fileName"],
                        "result": "No"
                    })
            elif (i["callResultAI"]["decision"]) == "paid":
                result_data.append({
                    "Type": "client",
                    "file_name": i["fileName"],
                    "result": "Yes_5"
                })
            else:
                result_data.append({
                    "Type": "client",
                    "file_name": i["fileName"],
                    "result": "No"
                })

print(f"result: {result_data}")