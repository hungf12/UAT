data = [{
    "fileName": "007c035a71fff701.mp3",
    "agentChannel": 2,
    "time_load_info": 0.0031557083129882812,
    "requestPayment": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 16,
                "channel": 2,
                "text": "dạ thì em gọi hỗ trợ cho mình cái khoản trả góp thì nhằm nâng cao chất lượng dịch vụ hậu quả em cũng xin phép được ghi âm cuộc gọi em gọi hỗ trợ cho mình cái khoản trả góp số tiền kỳ thanh toán là 1000000 em xin lỗi 832000 vào ngày thanh toán của mình là ngày 9 tháng 10 thì từ đây tới 9 tây chị sẽ thanh toán vào ngày nào chị ha",
                "intents": [
                    "inform_loan",
                    "ask_payment_info"
                ],
                "entities": {
                    "ask_payment_datetime": [
                        {
                            "start": 314,
                            "end": 322,
                            "value": "ngày nào",
                            "real_value": "ngày nào",
                            "entity": "ask_payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "agent_support": [
                        {
                            "start": 14,
                            "end": 20,
                            "value": "hỗ trợ",
                            "real_value": "hỗ trợ",
                            "entity": "agent_support",
                            "subentities": "null",
                            "is_required": "required"
                        },
                        {
                            "start": 138,
                            "end": 144,
                            "value": "hỗ trợ",
                            "real_value": "hỗ trợ",
                            "entity": "agent_support",
                            "subentities": "null",
                            "is_required": "required"
                        }
                    ]
                }
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
                "index": 16,
                "channel": 2,
                "text": "dạ thì em gọi hỗ trợ cho mình cái khoản trả góp thì nhằm nâng cao chất lượng dịch vụ hậu quả em cũng xin phép được ghi âm cuộc gọi em gọi hỗ trợ cho mình cái khoản trả góp số tiền kỳ thanh toán là 1000000 em xin lỗi 832000 vào ngày thanh toán của mình là ngày 9 tháng 10 thì từ đây tới 9 tây chị sẽ thanh toán vào ngày nào chị ha",
                "intents": [
                    "inform_loan",
                    "ask_payment_info"
                ],
                "entities": {
                    "ask_payment_datetime": [
                        {
                            "start": 314,
                            "end": 322,
                            "value": "ngày nào",
                            "real_value": "ngày nào",
                            "entity": "ask_payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "agent_support": [
                        {
                            "start": 14,
                            "end": 20,
                            "value": "hỗ trợ",
                            "real_value": "hỗ trợ",
                            "entity": "agent_support",
                            "subentities": "null",
                            "is_required": "required"
                        },
                        {
                            "start": 138,
                            "end": 144,
                            "value": "hỗ trợ",
                            "real_value": "hỗ trợ",
                            "entity": "agent_support",
                            "subentities": "null",
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "ask_payment_datetime": [
                {
                    "index": 16,
                    "value": [
                        "ngày nào"
                    ],
                    "real_value": [
                        "ngày nào"
                    ]
                }
            ],
            "agent_support": [
                {
                    "index": 16,
                    "value": [
                        "hỗ trợ",
                        "hỗ trợ"
                    ],
                    "real_value": [
                        "hỗ trợ",
                        "hỗ trợ"
                    ]
                }
            ]
        },
        "position_range_index": [
            16,
            16
        ],
        "position_condition": [
            16
        ],
        "task": "compare"
    },
    "criterias_order": [
        {
            "criteria_name": "requestPayment",
            "decision": "yes",
            "position_range_index": [
                16,
                16
            ],
            "slots": {
                "ask_payment_datetime": [
                    {
                        "index": 16,
                        "value": [
                            "ngày nào"
                        ],
                        "real_value": [
                            "ngày nào"
                        ]
                    }
                ],
                "agent_support": [
                    {
                        "index": 16,
                        "value": [
                            "hỗ trợ",
                            "hỗ trợ"
                        ],
                        "real_value": [
                            "hỗ trợ",
                            "hỗ trợ"
                        ]
                    }
                ]
            }
        }
    ]
}]

resutl_have_you_paid_yet = []
for i in data:
    if (i["requestPayment"]["evaluate"]) and (i["requestPayment"]["decision"]) == "yes":
        resutl_have_you_paid_yet.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    else:
        resutl_have_you_paid_yet.append({
            "file_name": i["fileName"],
            "result": "No"
        })
print(f"kết quả: {resutl_have_you_paid_yet}")