# Input data
data = [
    {
        "fileName": "",
        "agentChannel": 2,
        "time_load_info": 0.003535032272338867,
        "reasonOfCall": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "no"
            },
            "decision_position": [
                {
                    "index": 7,
                    "channel": 2,
                    "text": "em chào chị thủy nha để đánh giá nâng cao chất lượng dịch vụ cuộc gọi sẽ được ghi âm nha gọi để hỗ trợ cái hợp đồng mình đang vay tiền mặt với công ty nè số tiền đóng là 1964000 và đến hạn ngày 28 tháng 9 á",
                    "intents": [],
                    "entities": {
                        "loan_product": [
                            {
                                "start": 107,
                                "end": 138,
                                "value": "hợp đồng mình đang vay tiền mặt",
                                "real_value": "hợp đồng mình đang vay tiền mặt",
                                "entity": "loan_product",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ],
                        "amount": [
                            {
                                "start": 170,
                                "end": 177,
                                "value": "1964000",
                                "real_value": "1964000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ],
                        "loan_overdue": [
                            {
                                "start": 189,
                                "end": 204,
                                "value": "ngày 28 tháng 9",
                                "real_value": "ngày 28 tháng 9",
                                "entity": "loan_overdue",
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
                    "index": 9,
                    "channel": 2,
                    "text": "nay tới 28 tây chị thủy thanh toán ngày nào là việc đúng hẹn bên em ạ",
                    "intents": [],
                    "entities": {
                        "loan_overdue": [
                            {
                                "start": 8,
                                "end": 14,
                                "value": "28 tây",
                                "real_value": "28 tây",
                                "entity": "loan_overdue",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
                },
                {
                    "index": 25,
                    "channel": 2,
                    "text": "ừ 5000000 nay đã là 25 rồi chị",
                    "intents": [],
                    "entities": {
                        "amount": [
                            {
                                "start": 2,
                                "end": 9,
                                "value": "5000000",
                                "real_value": "5000000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
                },
                {
                    "index": 28,
                    "channel": 2,
                    "text": "chị đóng số tiền ở đây cũng là 1964000 luôn chị nha",
                    "intents": [],
                    "entities": {
                        "amount": [
                            {
                                "start": 31,
                                "end": 38,
                                "value": "1964000",
                                "real_value": "1964000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
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
                    "index": 7,
                    "channel": 2,
                    "text": "em chào chị thủy nha để đánh giá nâng cao chất lượng dịch vụ cuộc gọi sẽ được ghi âm nha gọi để hỗ trợ cái hợp đồng mình đang vay tiền mặt với công ty nè số tiền đóng là 1964000 và đến hạn ngày 28 tháng 9 á",
                    "intents": [],
                    "entities": {
                        "loan_product": [
                            {
                                "start": 107,
                                "end": 138,
                                "value": "hợp đồng mình đang vay tiền mặt",
                                "real_value": "hợp đồng mình đang vay tiền mặt",
                                "entity": "loan_product",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ],
                        "amount": [
                            {
                                "start": 170,
                                "end": 177,
                                "value": "1964000",
                                "real_value": "1964000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ],
                        "loan_overdue": [
                            {
                                "start": 189,
                                "end": 204,
                                "value": "ngày 28 tháng 9",
                                "real_value": "ngày 28 tháng 9",
                                "entity": "loan_overdue",
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
                    "index": 9,
                    "channel": 2,
                    "text": "nay tới 28 tây chị thủy thanh toán ngày nào là việc đúng hẹn bên em ạ",
                    "intents": [],
                    "entities": {
                        "loan_overdue": [
                            {
                                "start": 8,
                                "end": 14,
                                "value": "28 tây",
                                "real_value": "28 tây",
                                "entity": "loan_overdue",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
                },
                {
                    "index": 25,
                    "channel": 2,
                    "text": "ừ 5000000 nay đã là 25 rồi chị",
                    "intents": [],
                    "entities": {
                        "amount": [
                            {
                                "start": 2,
                                "end": 9,
                                "value": "5000000",
                                "real_value": "5000000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
                },
                {
                    "index": 28,
                    "channel": 2,
                    "text": "chị đóng số tiền ở đây cũng là 1964000 luôn chị nha",
                    "intents": [],
                    "entities": {
                        "amount": [
                            {
                                "start": 31,
                                "end": 38,
                                "value": "1964000",
                                "real_value": "1964000",
                                "entity": "amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 0.3333333333333333,
                    "intent_score": 0.0,
                    "confidence_criteria": 0.3333333333333333
                }
            ],
            "slots": {
                "loan_product": [
                    {
                        "index": 7,
                        "value": "hợp đồng mình đang vay tiền mặt"
                    }
                ],
                "amount": [
                    {
                        "index": 7,
                        "value": "1964000"
                    },
                    {
                        "index": 25,
                        "value": "5000000"
                    },
                    {
                        "index": 28,
                        "value": "1964000"
                    }
                ],
                "loan_overdue": [
                    {
                        "index": 7,
                        "value": "ngày 28 tháng 9"
                    },
                    {
                        "index": 9,
                        "value": "28 tây"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "criterias_order": "null"
    },
    {
        "fileName": "",
        "agentChannel": 2,
        "time_load_info": 0.0033843517303466797,
        "reasonOfCall": {
            "slots": {
                "loan_product": [
                    {
                        "index": 12,
                        "value": "hợp đồng thẻ tín dụng"
                    }
                ],
                "amount": [
                    {
                        "index": 12,
                        "value": "4301392162"
                    },
                    {
                        "index": 18,
                        "value": "78000"
                    },
                    {
                        "index": 20,
                        "value": "78000"
                    },
                    {
                        "index": 31,
                        "value": "78000"
                    },
                    {
                        "index": 36,
                        "value": "78000"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "criterias_order": "null"
    }
]

# Initialize result array
result_array = []

# Loop through each item in the data
for item in data:
    slots = item['reasonOfCall']['slots']
    # Check if all three keys exist
    if 'loan_product' in slots and 'loan_overdue' in slots and 'amount' in slots:
        result_array.append({
            "file_name": item["fileName"],
            "result": "true"
        })
    else:
        result_array.append({
            "file_name": item["fileName"],
            "result": "fail"
        })
# Output the result
print(f"result: {result_array}")

