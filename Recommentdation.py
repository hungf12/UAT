data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.004727602005004883,
    "agentUnderstand": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "yes"
        },
        "decision_position": [
            {
                "index": 6,
                "channel": 1,
                "text": "em ghi nhận là tháng qua mình cũng sơ suất quên hay có gặp khó khăn gì hay sao mà để chậm hạn hơn 1 tuần lễ dữ vậy anh",
                "intents": [],
                "entities": {
                    "agent_understand": [
                        {
                            "entity": "agent_understand",
                            "value": "khó khăn",
                            "start": 59,
                            "end": 67,
                            "real_value": "em hiểu",
                            "is_required": "required"
                        }
                    ]
                }
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
                "index": 6,
                "channel": 1,
                "text": "em ghi nhận là tháng qua mình cũng sơ suất quên hay có gặp khó khăn gì hay sao mà để chậm hạn hơn 1 tuần lễ dữ vậy anh",
                "intents": [],
                "entities": {
                    "agent_understand": [
                        {
                            "entity": "agent_understand",
                            "value": "khó khăn",
                            "start": 59,
                            "end": 67,
                            "real_value": "em hiểu",
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "agent_understand": [
                {
                    "index": 6,
                    "value": [
                        "khó khăn"
                    ],
                    "real_value": [
                        "em hiểu"
                    ]
                }
            ]
        },
        "position_range_index": [
            6,
            6
        ],
        "position_condition": [
            6
        ],
        "task": "compare"
    },
    "askPaymentReceipt": {
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
    "dueDateMention": {
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
        "position_range_index": [],
        "position_condition": [],
        "task": "query"
    },
    "motivationAppear": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "no"
        },
        "decision_position": [
            {
                "index": 2,
                "channel": 1,
                "text": "dạ rồi đánh dấu nâng cao sử dụng dịch vụ cuộc gọi sẽ được ghi âm đang liên hệ hỗ trợ khoản trả góp điện thoại trễ hạn vào ngày 27 này số tiền là 842000 mình sẽ thanh toán được vào ngày nào để bên em cải thiện lịch sử tín dụng nè anh sơn",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 199,
                            "end": 225,
                            "value": "cải thiện lịch sử tín dụng",
                            "real_value": "cải thiện lịch sử tín dụng",
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
            },
            {
                "index": 10,
                "channel": 1,
                "text": "dạ rồi vậy thì vấn đề này bên em sẽ tạm thời ghi nhận trên hệ thống cũng như hỗ trợ cho mình tại vì em thấy mình được rằng là mình cũng mới sơ suất có tháng đầu tiên thôi nên em sẽ hỗ trợ nó không bị phát sinh thêm tiền lãi như tháng em cần phải đóng đúng hẹn lại cho công ty để tránh trường hợp sai sót 2 tháng tục chậm hạn thì bắt buộc tiền lãi phải phát sinh thêm và nhiều nhất có thể lên tới hơn 300000 nó sẽ ảnh hưởng tới vấn đề tài chính và bên em sẽ không thể nào hỗ trợ miễn giảm được nên là tháng công ty liên hệ ra nhắc trước cho mình luôn anh sơn ha",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 200,
                            "end": 223,
                            "value": "phát sinh thêm tiền lãi",
                            "real_value": "phát sinh thêm tiền lãi",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "motivation_result": [
                        {
                            "start": 413,
                            "end": 422,
                            "value": "ảnh hưởng",
                            "real_value": "ảnh hưởng",
                            "entity": "motivation_result",
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
                "index": 16,
                "channel": 1,
                "text": "dạ rồi xác nhận đóng 842000 qua cửa hàng chậm nhất 0 quá ngày 26 tháng tháng cùng duy trì 26 tránh trường hợp để phí lãi phát sinh thêm phải đóng thêm tiền ảnh hưởng tới tài chính nữa nhá cảm ơn chào anh ạ",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 93,
                            "end": 109,
                            "value": "tránh trường hợp",
                            "real_value": "tránh trường hợp",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 110,
                            "end": 140,
                            "value": "để phí lãi phát sinh thêm phải",
                            "real_value": "để phí lãi phát sinh thêm phải",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 156,
                            "end": 179,
                            "value": "ảnh hưởng tới tài chính",
                            "real_value": "ảnh hưởng tới tài chính",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "motivation_result": [
                        {
                            "start": 141,
                            "end": 155,
                            "value": "đóng thêm tiền",
                            "real_value": "đóng thêm tiền",
                            "entity": "motivation_result",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                },
                "evaluate": "yes",
                "entities_score": 2.0,
                "intent_score": 0.0,
                "confidence_criteria": 2.0
            }
        ],
        "decision": "yes",
        "confidence": 2.0,
        "confidence_channel": {
            "1": 2.0,
            "2": 0.0
        },
        "position": [
            {
                "index": 2,
                "channel": 1,
                "text": "dạ rồi đánh dấu nâng cao sử dụng dịch vụ cuộc gọi sẽ được ghi âm đang liên hệ hỗ trợ khoản trả góp điện thoại trễ hạn vào ngày 27 này số tiền là 842000 mình sẽ thanh toán được vào ngày nào để bên em cải thiện lịch sử tín dụng nè anh sơn",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 199,
                            "end": 225,
                            "value": "cải thiện lịch sử tín dụng",
                            "real_value": "cải thiện lịch sử tín dụng",
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
            },
            {
                "index": 10,
                "channel": 1,
                "text": "dạ rồi vậy thì vấn đề này bên em sẽ tạm thời ghi nhận trên hệ thống cũng như hỗ trợ cho mình tại vì em thấy mình được rằng là mình cũng mới sơ suất có tháng đầu tiên thôi nên em sẽ hỗ trợ nó không bị phát sinh thêm tiền lãi như tháng em cần phải đóng đúng hẹn lại cho công ty để tránh trường hợp sai sót 2 tháng tục chậm hạn thì bắt buộc tiền lãi phải phát sinh thêm và nhiều nhất có thể lên tới hơn 300000 nó sẽ ảnh hưởng tới vấn đề tài chính và bên em sẽ không thể nào hỗ trợ miễn giảm được nên là tháng công ty liên hệ ra nhắc trước cho mình luôn anh sơn ha",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 200,
                            "end": 223,
                            "value": "phát sinh thêm tiền lãi",
                            "real_value": "phát sinh thêm tiền lãi",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "motivation_result": [
                        {
                            "start": 413,
                            "end": 422,
                            "value": "ảnh hưởng",
                            "real_value": "ảnh hưởng",
                            "entity": "motivation_result",
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
                "index": 16,
                "channel": 1,
                "text": "dạ rồi xác nhận đóng 842000 qua cửa hàng chậm nhất 0 quá ngày 26 tháng tháng cùng duy trì 26 tránh trường hợp để phí lãi phát sinh thêm phải đóng thêm tiền ảnh hưởng tới tài chính nữa nhá cảm ơn chào anh ạ",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 93,
                            "end": 109,
                            "value": "tránh trường hợp",
                            "real_value": "tránh trường hợp",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 110,
                            "end": 140,
                            "value": "để phí lãi phát sinh thêm phải",
                            "real_value": "để phí lãi phát sinh thêm phải",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 156,
                            "end": 179,
                            "value": "ảnh hưởng tới tài chính",
                            "real_value": "ảnh hưởng tới tài chính",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "motivation_result": [
                        {
                            "start": 141,
                            "end": 155,
                            "value": "đóng thêm tiền",
                            "real_value": "đóng thêm tiền",
                            "entity": "motivation_result",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                },
                "evaluate": "yes",
                "entities_score": 2.0,
                "intent_score": 0.0,
                "confidence_criteria": 2.0
            }
        ],
        "slots": {
            "motivation_title": [
                {
                    "index": 2,
                    "value": "cải thiện lịch sử tín dụng"
                },
                {
                    "index": 10,
                    "value": "phát sinh thêm tiền lãi"
                },
                {
                    "index": 16,
                    "value": "tránh trường hợp"
                },
                {
                    "index": 16,
                    "value": "để phí lãi phát sinh thêm phải"
                },
                {
                    "index": 16,
                    "value": "ảnh hưởng tới tài chính"
                }
            ],
            "motivation_result": [
                {
                    "index": 10,
                    "value": "ảnh hưởng"
                },
                {
                    "index": 16,
                    "value": "đóng thêm tiền"
                }
            ]
        },
        "position_range_index": [],
        "position_condition": [],
        "task": "query"
    },
    "criterias_order": [
        {
            "criteria_name": "agentUnderstand",
            "decision": "yes",
            "position_range_index": [
                6,
                6
            ],
            "slots": {
                "agent_understand": [
                    {
                        "index": 6,
                        "value": [
                            "khó khăn"
                        ],
                        "real_value": [
                            "em hiểu"
                        ]
                    }
                ]
            }
        }
    ]
}]
result_recommentdation = []
for i in data:
    if (i["askPaymentReceipt"]["evaluate"]) and (i["askPaymentReceipt"]["decision"]) == "yes" and (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["evaluate"]) and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "1",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["askPaymentReceipt"]["evaluate"]) and (i["askPaymentReceipt"]["decision"]) == "yes" and (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "2",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["agentUnderstand"]["evaluate"]) and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["evaluate"]) and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "3",
            "file_name": i["fileName"],
            "result": "Yes"
        })
    elif (i["askPaymentReceipt"]["evaluate"]) and (i["askPaymentReceipt"]["decision"]) == "yes" or (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "4",
            "file_name": i["fileName"],
            "result": "Partially"
        })
    elif ((i["agentUnderstand"]["evaluate"]) and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"]) == "yes"
    or (i["agentUnderstand"]["evaluate"]) and (i["agentUnderstand"]["decision"]) == "yes" and (i["motivationAppear"]["evaluate"]) and (i["motivationAppear"]["decision"]) == "yes"
    or (i["dueDateMention"]["evaluate"]) and (i["dueDateMention"]["decision"])== "yes") and (i["motivationAppear"]["evaluate"]) and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "case": "5",
            "file_name": i["fileName"],
            "result": "Partially"
        })
    else:
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "No"
        })

print(f"kết qua: {result_recommentdation}")