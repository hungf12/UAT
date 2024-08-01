data = [ {
    "fileName": "",
    "agentChannel": 2,
    "time_load_info": 0.5883722305297852,
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
        "position_range_index": "null",
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
        "position_range_index": "null",
        "position_condition": [],
        "task": "compare"
    },
    "dueDateMention": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "no"
        },
        "decision_position": [
            {
                "index": 15,
                "channel": 2,
                "text": "rồi cám ơn em ghi nhận về trước ngày 19 anh ra cửa hàng đóng 3082000 ngày nữa là kỳ cuối của anh nha đóng đúng hạn để cà vẹt",
                "intents": [],
                "entities": {
                    "due_date": [
                        {
                            "start": 26,
                            "end": 39,
                            "value": "trước ngày 19",
                            "real_value": "trước ngày 19",
                            "entity": "due_date",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                },
                "evaluate": "yes",
                "entities_score": 1.0,
                "intent_score": 0.0,
                "confidence_criteria": 1.0
            }
        ],
        "decision": "yes",
        "confidence": 1.0,
        "confidence_channel": {
            "2": 1.0,
            "1": 0.0
        },
        "position": [
            {
                "index": 15,
                "channel": 2,
                "text": "rồi cám ơn em ghi nhận về trước ngày 19 anh ra cửa hàng đóng 3082000 ngày nữa là kỳ cuối của anh nha đóng đúng hạn để cà vẹt",
                "intents": [],
                "entities": {
                    "due_date": [
                        {
                            "start": 26,
                            "end": 39,
                            "value": "trước ngày 19",
                            "real_value": "trước ngày 19",
                            "entity": "due_date",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                },
                "evaluate": "yes",
                "entities_score": 1.0,
                "intent_score": 0.0,
                "confidence_criteria": 1.0
            }
        ],
        "slots": {
            "due_date": [
                {
                    "index": 15,
                    "value": "trước ngày 19"
                }
            ]
        },
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
        "position_range_index": "null",
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
        "position_range_index": "null",
        "position_condition": [],
        "task": "compare"
    },
    "criterias_order": []
}]

result_recommentdation = []

for i in data:
    if (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["mentionHistory"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["nopaymentHistory"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["nopaymentHistory"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["nopaymentHistory"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif (i["dueDateMention"]["decision"]) and (i["askPaymentReceipt"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    else:
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "No"
        })
print(f"kết quả: {result_recommentdation}")