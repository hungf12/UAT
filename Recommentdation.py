data = [{
    "fileName": "",
    "agentChannel": 2,
    "time_load_info": 0.004635334014892578,
    "agentUnderstand": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 8,
                "channel": 2,
                "text": "rồi em hiểu nha ở đây thì lâu lâu sai sót bên em có thể hiểu và thông cảm được cho chị oanh á nhưng chị lưu ý giúp em nha",
                "intents": [],
                "entities": {
                    "agent_understand": [
                        {
                            "entity": "agent_understand",
                            "value": "em hiểu",
                            "start": 4,
                            "end": 11,
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
            "2": 1.0,
            "1": 1.0
        },
        "position": [
            {
                "index": 8,
                "channel": 2,
                "text": "rồi em hiểu nha ở đây thì lâu lâu sai sót bên em có thể hiểu và thông cảm được cho chị oanh á nhưng chị lưu ý giúp em nha",
                "intents": [],
                "entities": {
                    "agent_understand": [
                        {
                            "entity": "agent_understand",
                            "value": "em hiểu",
                            "start": 4,
                            "end": 11,
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
                    "index": 8,
                    "value": [
                        "em hiểu"
                    ],
                    "real_value": [
                        "em hiểu"
                    ]
                }
            ]
        },
        "position_range_index": [
            8,
            8
        ],
        "position_condition": [
            8
        ],
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
                "index": 20,
                "channel": 2,
                "text": "em cảm ơn em ghi nhận hôm nay là ngày 27 tây chậm nhất là ngày 30 trong 3 ngày nữa là ngày thứ 7 á mình thu xếp ra góp giúp em 3275000 qua cửa hàng chị ha hàng tháng sắp xếp thanh toán trước hẹn ngày 1 để nhận ưu đãi tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng nha chị oanh",
                "intents": [],
                "entities": {
                    "due_date": [
                        {
                            "start": 185,
                            "end": 190,
                            "value": "trước",
                            "real_value": "trước",
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
                "index": 20,
                "channel": 2,
                "text": "em cảm ơn em ghi nhận hôm nay là ngày 27 tây chậm nhất là ngày 30 trong 3 ngày nữa là ngày thứ 7 á mình thu xếp ra góp giúp em 3275000 qua cửa hàng chị ha hàng tháng sắp xếp thanh toán trước hẹn ngày 1 để nhận ưu đãi tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng nha chị oanh",
                "intents": [],
                "entities": {
                    "due_date": [
                        {
                            "start": 185,
                            "end": 190,
                            "value": "trước",
                            "real_value": "trước",
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
                    "index": 20,
                    "value": "trước"
                }
            ]
        },
        "position_range_index": [],
        "position_condition": [],
        "task": "query"
    },
    "motivationAppear": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "no"
        },
        "decision_position": [
            {
                "index": 2,
                "channel": 2,
                "text": "em chào chị oanh để đánh giá và nhằm nâng cao chất lượng dịch vụ cuộc gọi này xin phép bên em được ghi âm nha em gọi ra hỗ trợ hợp đồng chị oanh tham gia trả góp tiền mặt trả góp tiếp theo đó chị 3275000 hạn cuối thanh toán là ngày 1 chị oanh vui lòng cho em hỏi là trong tháng này mình có dự định góp được ngày nào cho công ty từ hôm nay đến trước hạn ngày 1 chưa chị",
                "intents": [],
                "entities": {
                    "motivation_result": [
                        {
                            "start": 37,
                            "end": 56,
                            "value": "nâng cao chất lượng",
                            "real_value": "nâng cao chất lượng",
                            "entity": "motivation_result",
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
                "channel": 2,
                "text": "dạ tại vì ở đây hiện tại là lâu lâu sai sót thôi chị nhưng mà nếu mà trường hợp á tại vì em báo trước nha hồ sơ của mình cũng còn rất là nhiều kỳ nếu mà trường hợp mà mình có số kỳ trễ của mình nó vượt quá số kỳ trễ bên em cho phép được hỗ trợ thì mình có thể phải đóng kèm thêm tiền lãi quá hạn cho công ty tại vì mình đi vay đi mượn ở đây là có ký kết hợp đồng vào ngày 1 chị oanh ha và hiện tại là",
                "intents": [],
                "entities": {
                    "motivation_result": [
                        {
                            "start": 265,
                            "end": 295,
                            "value": "đóng kèm thêm tiền lãi quá hạn",
                            "real_value": "đóng kèm thêm tiền lãi quá hạn",
                            "entity": "motivation_result",
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
                "index": 20,
                "channel": 2,
                "text": "em cảm ơn em ghi nhận hôm nay là ngày 27 tây chậm nhất là ngày 30 trong 3 ngày nữa là ngày thứ 7 á mình thu xếp ra góp giúp em 3275000 qua cửa hàng chị ha hàng tháng sắp xếp thanh toán trước hẹn ngày 1 để nhận ưu đãi tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng nha chị oanh",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 205,
                            "end": 209,
                            "value": "nhận",
                            "real_value": "nhận",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 217,
                            "end": 262,
                            "value": "tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng",
                            "real_value": "tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng",
                            "entity": "motivation_title",
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
                "index": 2,
                "channel": 2,
                "text": "em chào chị oanh để đánh giá và nhằm nâng cao chất lượng dịch vụ cuộc gọi này xin phép bên em được ghi âm nha em gọi ra hỗ trợ hợp đồng chị oanh tham gia trả góp tiền mặt trả góp tiếp theo đó chị 3275000 hạn cuối thanh toán là ngày 1 chị oanh vui lòng cho em hỏi là trong tháng này mình có dự định góp được ngày nào cho công ty từ hôm nay đến trước hạn ngày 1 chưa chị",
                "intents": [],
                "entities": {
                    "motivation_result": [
                        {
                            "start": 37,
                            "end": 56,
                            "value": "nâng cao chất lượng",
                            "real_value": "nâng cao chất lượng",
                            "entity": "motivation_result",
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
                "channel": 2,
                "text": "dạ tại vì ở đây hiện tại là lâu lâu sai sót thôi chị nhưng mà nếu mà trường hợp á tại vì em báo trước nha hồ sơ của mình cũng còn rất là nhiều kỳ nếu mà trường hợp mà mình có số kỳ trễ của mình nó vượt quá số kỳ trễ bên em cho phép được hỗ trợ thì mình có thể phải đóng kèm thêm tiền lãi quá hạn cho công ty tại vì mình đi vay đi mượn ở đây là có ký kết hợp đồng vào ngày 1 chị oanh ha và hiện tại là",
                "intents": [],
                "entities": {
                    "motivation_result": [
                        {
                            "start": 265,
                            "end": 295,
                            "value": "đóng kèm thêm tiền lãi quá hạn",
                            "real_value": "đóng kèm thêm tiền lãi quá hạn",
                            "entity": "motivation_result",
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
                "index": 20,
                "channel": 2,
                "text": "em cảm ơn em ghi nhận hôm nay là ngày 27 tây chậm nhất là ngày 30 trong 3 ngày nữa là ngày thứ 7 á mình thu xếp ra góp giúp em 3275000 qua cửa hàng chị ha hàng tháng sắp xếp thanh toán trước hẹn ngày 1 để nhận ưu đãi tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng nha chị oanh",
                "intents": [],
                "entities": {
                    "motivation_title": [
                        {
                            "start": 205,
                            "end": 209,
                            "value": "nhận",
                            "real_value": "nhận",
                            "entity": "motivation_title",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 217,
                            "end": 262,
                            "value": "tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng",
                            "real_value": "tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng",
                            "entity": "motivation_title",
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
            "motivation_result": [
                {
                    "index": 2,
                    "value": "nâng cao chất lượng"
                },
                {
                    "index": 10,
                    "value": "đóng kèm thêm tiền lãi quá hạn"
                }
            ],
            "motivation_title": [
                {
                    "index": 20,
                    "value": "nhận"
                },
                {
                    "index": 20,
                    "value": "tránh đóng trễ lãi ảnh hưởng lịch sử tín dụng"
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
                8,
                8
            ],
            "slots": {
                "agent_understand": [
                    {
                        "index": 8,
                        "value": [
                            "em hiểu"
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
    else:
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "No"
        })

print(f"kết quả: {result_recommentdation}")