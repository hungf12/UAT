data = [ {
        "fileName": "007c036ae0e96b1c.mp3",
        "agentChannel": 2,
        "time_load_info": 0.004393815994262695,
        "agentUnderstand": {
            "evaluate": "no",
            "evaluate_channel": {
                "2": "no",
                "1": "no"
            },
            "decision_position": [],
            "decision": "no",
            "confidence": 0.0,
            "confidence_channel": {
                "2": 0.0,
                "1": 0.0
            },
            "position": [],
            "slots": {},
            "position_range_index": "None",
            "position_condition": [],
            "task": "compare"
        },
        "askPaymentReceipt": {
            "evaluate": "no",
            "evaluate_channel": {
                "2": "no",
                "1": "no"
            },
            "decision_position": [],
            "decision": "no",
            "confidence": 0.0,
            "confidence_channel": {
                "2": 0.0,
                "1": 0.0
            },
            "position": [],
            "slots": {},
            "position_range_index": "None",
            "position_condition": [],
            "task": "compare"
        },
        "dueDateMention": {
            "evaluate": "no",
            "evaluate_channel": {
                "2": "no",
                "1": "no"
            },
            "decision_position": [],
            "decision": "no",
            "confidence": 0.0,
            "confidence_channel": {
                "2": 0.0,
                "1": 0.0
            },
            "position": [],
            "slots": {},
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "mentionHistory": {
            "evaluate": "no",
            "evaluate_channel": {
                "2": "no",
                "1": "no"
            },
            "decision_position": [],
            "decision": "no",
            "confidence": 0.0,
            "confidence_channel": {
                "2": 0.0,
                "1": 0.0
            },
            "position": [],
            "slots": {},
            "position_range_index": "None",
            "position_condition": [],
            "task": "compare"
        },
        "motivationAppear": {
            "evaluate": "no",
            "evaluate_channel": {
                "2": "no",
                "1": "no"
            },
            "decision_position": [],
            "decision": "no",
            "confidence": 0.0,
            "confidence_channel": {
                "2": 0.0,
                "1": 0.0
            },
            "position": [],
            "slots": {},
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "nopaymentHistory": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 7,
                    "channel": 2,
                    "text": "à thứ nhất là mình tranh thủ từ giờ đến ngày 2 để đúng hẹn duy trì hồ sơ tốt",
                    "intents": [
                        "no_late_payment_history"
                    ],
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
                    "index": 7,
                    "channel": 2,
                    "text": "à thứ nhất là mình tranh thủ từ giờ đến ngày 2 để đúng hẹn duy trì hồ sơ tốt",
                    "intents": [
                        "no_late_payment_history"
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
        "criterias_order": [
            {
                "criteria_name": "nopaymentHistory",
                "decision": "yes",
                "position_range_index": [
                    7,
                    7
                ],
                "slots": {}
            }
        ]
    },]

result_recommentdation = []

for i in data:
    if (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "1",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "2",
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["mentionHistory"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "3",
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["nopaymentHistory"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "4",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["nopaymentHistory"]["decision"]) == "yes" or (i["nopaymentHistory"]["decision"]) == "no" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "5",
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["dueDateMention"]["decision"]) == "yes" and (i["askPaymentReceipt"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "6",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    else:
        result_recommentdation.append({
            "case": "7",
            "file_name": i["fileName"],
            "result": "No"
        })
print(f"kết quả: {result_recommentdation}")