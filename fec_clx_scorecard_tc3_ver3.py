data = [{
        "fileName": "0OIM2CTEE10C34927RKO5VTGJC061J4K_2024-03-13_02-11-58_0.mp3",
        "agentChannel": 1,
        "time_load_info": 0.0041692256927490234,
        "askCusDifficult": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes",
                "2": "yes"
            },
            "decision_position": [
                {
                    "index": 7,
                    "channel": 2,
                    "text": "hoài giờ chị mắc việc rồi để để tháng đóng đi",
                    "intents": [
                        "cus_cant_pay"
                    ],
                    "entities": {}
                }
            ],
            "decision": "yes",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0,
                "2": 1.0
            },
            "position": [
                {
                    "index": 7,
                    "channel": 2,
                    "text": "hoài giờ chị mắc việc rồi để để tháng đóng đi",
                    "intents": [
                        "cus_cant_pay"
                    ],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                7,
                7
            ],
            "position_condition": [
                7
            ],
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
                        "index": 7,
                        "channel": 2,
                        "text": "hoài giờ chị mắc việc rồi để để tháng đóng đi",
                        "intents": [
                            "cus_cant_pay"
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
                    "index": 7,
                    "channel": 2,
                    "text": "hoài giờ chị mắc việc rồi để để tháng đóng đi",
                    "intents": [
                        "cus_cant_pay"
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
                    "text": "<agent>: alo <customer>: hả em <agent>: dạ em bên phía công ty tài chính fe gọi ra ạ em chào chị à chị nga hả <customer>: alo <customer>: vâng <agent>: chị nga chị cho em hỏi cái hồ sơ vay tiền của chị nga bên fe em nè chị nga thu xếp thanh toán tiền giùm em chưa chị nga ơi <agent>: à chị nga đóng hồi nào chị nga em thấy còn thiếu 76000 chị nha <customer>: hoài giờ chị mắc việc rồi để để tháng đóng đi <agent>: chị không được chị 76 này cũng coi như là tiền kỳ của mình vậy đó chị chị mà đóng thiếu tiền kỳ nó phát sinh thêm phí phạt á chị thu xếp hôm nay chị bận á thì sáng ngày mai chị ra chị đóng giúp em nha <customer>: à à",
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
                    "text": "<agent>: alo <customer>: hả em <agent>: dạ em bên phía công ty tài chính fe gọi ra ạ em chào chị à chị nga hả <customer>: alo <customer>: vâng <agent>: chị nga chị cho em hỏi cái hồ sơ vay tiền của chị nga bên fe em nè chị nga thu xếp thanh toán tiền giùm em chưa chị nga ơi <agent>: à chị nga đóng hồi nào chị nga em thấy còn thiếu 76000 chị nha <customer>: hoài giờ chị mắc việc rồi để để tháng đóng đi <agent>: chị không được chị 76 này cũng coi như là tiền kỳ của mình vậy đó chị chị mà đóng thiếu tiền kỳ nó phát sinh thêm phí phạt á chị thu xếp hôm nay chị bận á thì sáng ngày mai chị ra chị đóng giúp em nha <customer>: à à",
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
                    "text": "<agent>: dạ 76000 thôi chị <customer>: ờ ờ <agent>: dạ vậy là ngày mai chị ra đóng được không <customer>: mệt quá á à ngày mai ngày 1 gì ha tại vì mắc việc <agent>: dạ dạ dạ trong ngày mai đi chị để em chốt hồ sơ luôn nha <customer>: ở xa chưa có về dạ được <agent>: để chậm nữa tháng nó thêm thoải nữa chị à tại vì tiền kỳ của mình á nó cũng giống như tiền kỳ của mình thôi chị đóng thiếu tiền kỳ là nó sẽ phát sinh thêm lãi nữa chị nha <customer>: ừ <customer>: ừ <customer>: ừ <agent>: cho nên trong sáng ngày mai giúp em nha <customer>: ừ <customer>: ừ <agent>: ừ em cảm ơn chị nga ạ rồi em chào chị nga <customer>: ừ",
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
                    "text": "<agent>: dạ 76000 thôi chị <customer>: ờ ờ <agent>: dạ vậy là ngày mai chị ra đóng được không <customer>: mệt quá á à ngày mai ngày 1 gì ha tại vì mắc việc <agent>: dạ dạ dạ trong ngày mai đi chị để em chốt hồ sơ luôn nha <customer>: ở xa chưa có về dạ được <agent>: để chậm nữa tháng nó thêm thoải nữa chị à tại vì tiền kỳ của mình á nó cũng giống như tiền kỳ của mình thôi chị đóng thiếu tiền kỳ là nó sẽ phát sinh thêm lãi nữa chị nha <customer>: ừ <customer>: ừ <customer>: ừ <agent>: cho nên trong sáng ngày mai giúp em nha <customer>: ừ <customer>: ừ <agent>: ừ em cảm ơn chị nga ạ rồi em chào chị nga <customer>: ừ",
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
        "criterias_order": [
            {
                "criteria_name": "askCusDifficult",
                "decision": "yes",
                "position_range_index": [
                    7,
                    7
                ],
                "slots": {}
            },
            {
                "criteria_name": "askLateReason",
                "decision": "yes",
                "position_range_index": "",
                "slots": {}
            }
        ]
    },]

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
    elif (i["callClassifyAI"]["decision"]) == "wrongnumber":
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
            if (i["callResultAI"]["decision"]) == "paid":
                result_data.append({
                    "Type": "client - nhánh đã thanh toán",
                    "file_name": i["fileName"],
                    "result": "Yes_5"
                })
            elif (i["callResultAI"]["decision"]) == "willpay":
                if (i["askLateReason"]["evaluate"]) and (i["askLateReason"]["decision"]) == "yes":
                    result_data.append({
                        "Type": "client - nhánh cam kết thanh toán.1",
                        "file_name": i["fileName"],
                        "result": "Yes_5"
                    })
                elif (i["askCusDifficult"]["evaluate"]) and (i["askCusDifficult"]["evaluate"]) == "yes":
                    result_data.append({
                        "Type": "client - nhánh cam kết thanh toán.2",
                        "file_name": i["fileName"],
                        "result": "Yes_5"
                    })
                else:
                    result_data.append({
                        "Type": "client - nhánh cam kết thanh toán.3",
                        "file_name": i["fileName"],
                        "result": "Yes_5"
                    })
            elif (i["callResultAI"]["decision"]) == "nopay":
                if (i["askLateReason"]["evaluate"]) and (i["askLateReason"]["decision"]) == "yes":
                    result_data.append({
                        "Type": "client - nhánh không cam kết thanh toán .1",
                        "file_name": i["fileName"],
                        "result": "Yes_10"
                    })
                elif (i["askCusDifficult"]["evaluate"]) and (i["askCusDifficult"]["evaluate"]) == "yes":
                    result_data.append({
                        "Type": "client - nhánh không cam kết thanh toán.2",
                        "file_name": i["fileName"],
                        "result": "Yes_10"
                    })
                else:
                    result_data.append({
                        "Type": "client - nhánh không cam kết thanh toán fallback",
                        "file_name": i["fileName"],
                        "result": "No"
                    })
            else:
                result_data.append({
                    "Type": "fallback",
                    "file_name": i["fileName"],
                    "result": "No"
                })

print(f"result: {result_data}")