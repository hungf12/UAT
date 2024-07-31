'''
data = [{
        "fileName": "007c035a71f040c6.mp3",
        "agentChannel": 2,
        "time_load_info": 0.004044055938720703,
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
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "no"
            },
            "decision_position": [
                {
                    "index": 38,
                    "channel": 2,
                    "text": "vậy thì em ghi nhận chậm nhất tháng 27 tây sắp xếp 2 ngày nữa mình đóng cho bên em đóng 1964000 và không có chuyển khoản luôn nha hàng tháng trước ngày 26 hổng ưu đãi về sau",
                    "intents": [],
                    "entities": {
                        "due_date": [
                            {
                                "start": 141,
                                "end": 154,
                                "value": "trước ngày 26",
                                "real_value": "trước ngày 26",
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
                },
                {
                    "index": 40,
                    "channel": 2,
                    "text": "hàng tháng toán trước 27 tại về sau cám ơn em chào chị ạ",
                    "intents": [],
                    "entities": {
                        "due_date": [
                            {
                                "start": 16,
                                "end": 24,
                                "value": "trước 27",
                                "real_value": "trước 27",
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
                    "index": 38,
                    "channel": 2,
                    "text": "vậy thì em ghi nhận chậm nhất tháng 27 tây sắp xếp 2 ngày nữa mình đóng cho bên em đóng 1964000 và không có chuyển khoản luôn nha hàng tháng trước ngày 26 hổng ưu đãi về sau",
                    "intents": [],
                    "entities": {
                        "due_date": [
                            {
                                "start": 141,
                                "end": 154,
                                "value": "trước ngày 26",
                                "real_value": "trước ngày 26",
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
                },
                {
                    "index": 40,
                    "channel": 2,
                    "text": "hàng tháng toán trước 27 tại về sau cám ơn em chào chị ạ",
                    "intents": [],
                    "entities": {
                        "due_date": [
                            {
                                "start": 16,
                                "end": 24,
                                "value": "trước 27",
                                "real_value": "trước 27",
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
                        "index": 38,
                        "value": "trước ngày 26"
                    },
                    {
                        "index": 40,
                        "value": "trước 27"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "mentionHistory": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 13,
                    "channel": 2,
                    "text": "em cám ơn chị hợp đồng này em thấy chị cũng có cải thiện rất là tốt cho công ty rồi tại vì trước đó của mình á em thấy là có kỳ tháng 6 là mình đóng trễ có ngày à chắc là do quên chắc là giờ mình quên thôi đúng không",
                    "intents": [
                        "late_payment_history"
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
                    "index": 13,
                    "channel": 2,
                    "text": "em cám ơn chị hợp đồng này em thấy chị cũng có cải thiện rất là tốt cho công ty rồi tại vì trước đó của mình á em thấy là có kỳ tháng 6 là mình đóng trễ có ngày à chắc là do quên chắc là giờ mình quên thôi đúng không",
                    "intents": [
                        "late_payment_history"
                    ],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                13,
                13
            ],
            "position_condition": [
                13
            ],
            "task": "compare"
        },
        "motivationAppear": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "no"
            },
            "decision_position": [
                {
                    "index": 38,
                    "channel": 2,
                    "text": "vậy thì em ghi nhận chậm nhất tháng 27 tây sắp xếp 2 ngày nữa mình đóng cho bên em đóng 1964000 và không có chuyển khoản luôn nha hàng tháng trước ngày 26 hổng ưu đãi về sau",
                    "intents": [],
                    "entities": {
                        "motivation_title": [
                            {
                                "start": 155,
                                "end": 173,
                                "value": "hổng ưu đãi về sau",
                                "real_value": "hổng ưu đãi về sau",
                                "entity": "motivation_title",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.5,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.5
                }
            ],
            "decision": "yes",
            "confidence": 0.5,
            "confidence_channel": {
                "2": 0.5,
                "1": 0.0
            },
            "position": [
                {
                    "index": 38,
                    "channel": 2,
                    "text": "vậy thì em ghi nhận chậm nhất tháng 27 tây sắp xếp 2 ngày nữa mình đóng cho bên em đóng 1964000 và không có chuyển khoản luôn nha hàng tháng trước ngày 26 hổng ưu đãi về sau",
                    "intents": [],
                    "entities": {
                        "motivation_title": [
                            {
                                "start": 155,
                                "end": 173,
                                "value": "hổng ưu đãi về sau",
                                "real_value": "hổng ưu đãi về sau",
                                "entity": "motivation_title",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.5,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.5
                }
            ],
            "slots": {
                "motivation_title": [
                    {
                        "index": 38,
                        "value": "hổng ưu đãi về sau"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "criterias_order": [
            {
                "criteria_name": "mentionHistory",
                "decision": "yes",
                "position_range_index": [
                    13,
                    13
                ],
                "slots": {}
            }
        ]
    }]
'''


import json
#import pandas as pd
with open ("Recommendation_output_api.json","r",encoding= "utf-8")as f:
    data = json.load(f)
result_recommentdation = []
for i in data:
    if (i["mentionHistory"]["decision"]) == "yes":
        if (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
            result_recommentdation.append({
                "case:": "1",
                "file_name": i["fileName"],
                "result": "Yes"
            })
        elif (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" or (i["agentUnderstand"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes" or (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
            result_recommentdation.append({
                "case": "2",
                "file_name": i["fileName"],
                "result": "Partially"
            })
        else:
            result_recommentdation.append({
                "case": "fallback_1",
                "file_name": i["fileName"],
                "result": "No"
            })
    elif (i["mentionHistory"]["decision"]) == "no":
        if (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
            result_recommentdation.append({
                "case": "3",
                "file_name": i["fileName"],
                "result": "Yes"
            })
        elif (i["askPaymentReceipt"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes":
            result_recommentdation.append({
                "case": "4",
                "file_name": i["fileName"],
                "result": "Yes"
            })
        elif (i["dueDateMention"]["decision"]) == "yes" or (i["motivationAppear"]["decision"]) == "yes" or (i["askPaymentReceipt"]["decision"]) == "yes":
            result_recommentdation.append({
                "case": "5",
                "file_name": i["fileName"],
                "result": "Partially"
            })
        else:
            result_recommentdation.append({
                "case": "fallback_2",
                "file_name": i["fileName"],
                "result": "No"
            })
    else:
        result_recommentdation.append({
            "case": "fallback_3",
            "file_name": i["fileName"],
            "result": "No"
        })
count = len(result_recommentdation)
print(f"count: {count}")
print(f"Result: {result_recommentdation}")