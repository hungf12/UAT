data = [{
    "fileName": "009403631b6caf3a.mp3",
    "agentChannel": 1,
    "time_load_info": 0.4165160655975342,
    "nopaySummary": {
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
    "paidSummary": {
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
    "willpaySummary": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "yes"
        },
        "decision_position": [
            {
                "index": 16,
                "channel": 1,
                "text": "cảm ơn xác nhận đóng 1110000 trong ngày 12 trong ngày mai có chuyển khoản các chị góp tiếp theo như chị trước ngày 13 để hưởng các ưu đãi về sau cảm ơn chào anh ạ",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "amount": [
                        {
                            "start": 21,
                            "end": 28,
                            "value": "1110000",
                            "real_value": "1110000",
                            "entity": "amount",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_datetime": [
                        {
                            "start": 35,
                            "end": 42,
                            "value": "ngày 12",
                            "real_value": "ngày 12",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 49,
                            "end": 57,
                            "value": "ngày mai",
                            "real_value": "ngày mai",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_method": [
                        {
                            "start": 61,
                            "end": 73,
                            "value": "chuyển khoản",
                            "real_value": "chuyển khoản",
                            "entity": "payment_method",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "due_date": [
                        {
                            "start": 104,
                            "end": 117,
                            "value": "trước ngày 13",
                            "real_value": "trước ngày 13",
                            "entity": "due_date",
                            "subentities": [],
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
                "index": 16,
                "channel": 1,
                "text": "cảm ơn xác nhận đóng 1110000 trong ngày 12 trong ngày mai có chuyển khoản các chị góp tiếp theo như chị trước ngày 13 để hưởng các ưu đãi về sau cảm ơn chào anh ạ",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "amount": [
                        {
                            "start": 21,
                            "end": 28,
                            "value": "1110000",
                            "real_value": "1110000",
                            "entity": "amount",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_datetime": [
                        {
                            "start": 35,
                            "end": 42,
                            "value": "ngày 12",
                            "real_value": "ngày 12",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 49,
                            "end": 57,
                            "value": "ngày mai",
                            "real_value": "ngày mai",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_method": [
                        {
                            "start": 61,
                            "end": 73,
                            "value": "chuyển khoản",
                            "real_value": "chuyển khoản",
                            "entity": "payment_method",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "due_date": [
                        {
                            "start": 104,
                            "end": 117,
                            "value": "trước ngày 13",
                            "real_value": "trước ngày 13",
                            "entity": "due_date",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "amount": [
                {
                    "index": 16,
                    "value": [
                        "1110000"
                    ],
                    "real_value": [
                        "1110000"
                    ]
                }
            ],
            "payment_datetime": [
                {
                    "index": 16,
                    "value": [
                        "ngày 12",
                        "ngày mai"
                    ],
                    "real_value": [
                        "ngày 12",
                        "ngày mai"
                    ]
                }
            ],
            "payment_method": [
                {
                    "index": 16,
                    "value": [
                        "chuyển khoản"
                    ],
                    "real_value": [
                        "chuyển khoản"
                    ]
                }
            ],
            "due_date": [
                {
                    "index": 16,
                    "value": [
                        "trước ngày 13"
                    ],
                    "real_value": [
                        "trước ngày 13"
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
    "callResultAI": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<agent>: alo xin chào em là <customer>: alo <agent>: phạm đức cường đang nghe máy đúng không ạ <customer>: chị ơi <agent>: em gọi từ home credit việt nam á dạ anh là phạm đức cường đúng không ạ <customer>: ờ đúng rồi anh <agent>: đánh giá nâng cao chất lượng dịch vụ cuộc gọi này sẽ được ghi âm em gọi hỗ trợ thông tin thanh toán kỳ tiếp theo hợp đồng anh đang vay vốn số tiền là 1110000 đóng tiền ngày 13 đúng hạn trả góp này và duy trì lịch sử thanh toán anh đóng ngày nào đúng hạn trước ngày 13 ạ <customer>: dạ mai mai hoặc 1 em báo cho anh <agent>: cảm ơn hợp đồng đóng tiền rất tốt á tháng gọi hỗ trợ duy trì lịch sử thanh toán tốt của anh trên ngân hàng nhà nước ngoài ra kỳ này công ty cũng đang hỗ trợ việc thanh lý sớm á anh có nhu cầu tất toán dư nợ còn lại được hỗ trợ giảm lãi không ạ <customer>: dạ không dạ không không em em nên tại em đang đi đi xe á anh <agent>: dạ <agent>: dạ vậy tiền kỳ của anh vẫn là 1110000 nhé <customer>: em đang bận <customer>: rồi rồi rồi rồi <agent>: anh vẫn thanh toán chuyển khoản đúng không anh <customer>: rồi rồi rồi dạ dạ dạ <agent>: cảm ơn xác nhận đóng 1110000 trong ngày 12 trong ngày mai có chuyển khoản các chị góp tiếp theo như chị trước ngày 13 để hưởng các ưu đãi về sau cảm ơn chào anh ạ <customer>: rồi rồi rồi",
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
                "text": "<agent>: alo xin chào em là <customer>: alo <agent>: phạm đức cường đang nghe máy đúng không ạ <customer>: chị ơi <agent>: em gọi từ home credit việt nam á dạ anh là phạm đức cường đúng không ạ <customer>: ờ đúng rồi anh <agent>: đánh giá nâng cao chất lượng dịch vụ cuộc gọi này sẽ được ghi âm em gọi hỗ trợ thông tin thanh toán kỳ tiếp theo hợp đồng anh đang vay vốn số tiền là 1110000 đóng tiền ngày 13 đúng hạn trả góp này và duy trì lịch sử thanh toán anh đóng ngày nào đúng hạn trước ngày 13 ạ <customer>: dạ mai mai hoặc 1 em báo cho anh <agent>: cảm ơn hợp đồng đóng tiền rất tốt á tháng gọi hỗ trợ duy trì lịch sử thanh toán tốt của anh trên ngân hàng nhà nước ngoài ra kỳ này công ty cũng đang hỗ trợ việc thanh lý sớm á anh có nhu cầu tất toán dư nợ còn lại được hỗ trợ giảm lãi không ạ <customer>: dạ không dạ không không em em nên tại em đang đi đi xe á anh <agent>: dạ <agent>: dạ vậy tiền kỳ của anh vẫn là 1110000 nhé <customer>: em đang bận <customer>: rồi rồi rồi rồi <agent>: anh vẫn thanh toán chuyển khoản đúng không anh <customer>: rồi rồi rồi dạ dạ dạ <agent>: cảm ơn xác nhận đóng 1110000 trong ngày 12 trong ngày mai có chuyển khoản các chị góp tiếp theo như chị trước ngày 13 để hưởng các ưu đãi về sau cảm ơn chào anh ạ <customer>: rồi rồi rồi",
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
            "criteria_name": "willpaySummary",
            "decision": "yes",
            "position_range_index": [
                16,
                16
            ],
            "slots": {
                "amount": [
                    {
                        "index": 16,
                        "value": [
                            "1110000"
                        ],
                        "real_value": [
                            "1110000"
                        ]
                    }
                ],
                "payment_datetime": [
                    {
                        "index": 16,
                        "value": [
                            "ngày 12",
                            "ngày mai"
                        ],
                        "real_value": [
                            "ngày 12",
                            "ngày mai"
                        ]
                    }
                ],
                "payment_method": [
                    {
                        "index": 16,
                        "value": [
                            "chuyển khoản"
                        ],
                        "real_value": [
                            "chuyển khoản"
                        ]
                    }
                ],
                "due_date": [
                    {
                        "index": 16,
                        "value": [
                            "trước ngày 13"
                        ],
                        "real_value": [
                            "trước ngày 13"
                        ]
                    }
                ]
            }
        }
    ]
}]

# Initialize result array
result_contain_all_information = []

# Loop through each item in the data
for item in data:
    slots_0 = item['willpaySummary']['slots']
    slots_1 = item['nopaySummary']['slots']
    slots_2 = item['paidSummary']['slots']
    # Check case willpay
    if (item["callResultAI"]["decision"]) == "willpay":
        if 'due_date' in slots_0:
            if ('amount' in slots_0) and ('payment_datetime' in slots_0) and ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_1",
                    "file_name": item["fileName"],
                    "result": "Yes"
                })
            elif ('amount' in slots_0) and ('payment_datetime' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_2",
                    "file_name": item["fileName"],
                    "result": "Yes"
                })
            elif ('amount' in slots_0) and ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_3",
                    "file_name": item["fileName"],
                    "result": "Yes"
                })
            elif ('payment_datetime' in slots_0) and ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_4",
                    "file_name": item["fileName"],
                    "result": "Yes"
                })
            elif ('amount' in slots_0) or ('payment_datetime' in slots_0) or ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_5",
                    "file_name": item["fileName"],
                    "result": "partially"
                })
            else:
                result_contain_all_information.append({
                    "case": "willpay_5",
                    "file_name": item["fileName"],
                    "result": "partially"
                })
        elif 'due_date' not in slots_0:
            if ('amount' in slots_0) and ('payment_datetime' in slots_0) or ('amount' in slots_0) and ('payment_method' in slots_0) or ('payment_datetime' in slots_0) and ('payment_method' in slots_0) or ('amount' in slots_0) and ('payment_datetime' in slots_0) and ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_6",
                    "file_name": item["fileName"],
                    "result": "partially"
                })
            else:
                result_contain_all_information.append({
                    "case": "faillback_willpay",
                    "file_name": item["fileName"],
                    "result": "No"
                })
        else:
            result_contain_all_information.append({
                "case": "faillback_willpay",
                "file_name": item["fileName"],
                "result": "No"
            })
    elif (item["callResultAI"]["decision"]) == "nopay":
        if 'due_date' in slots_1:
            result_contain_all_information.append({
                "case": "Nopay",
                "file_name": item["fileName"],
                "result": "Yes"
            })
        else:
            result_contain_all_information.append({
                "case": "faillback_nonpay",
                "file_name": item["fileName"],
                "result": "No"
            })
    else:
        if ('receipt' in slots_2) and ('hotline' in slots_2):
            result_contain_all_information.append({
                "case": "paid",
                "file_name": item["fileName"],
                "result": "Yes"
            })
        elif ('receipt' in slots_2) or ('hotline' in slots_2):
            result_contain_all_information.append({
                "case": "paid",
                "file_name": item["fileName"],
                "result": "partially"
            })
        else:
            result_contain_all_information.append({
                "case": "faillback_paid",
                "file_name": item["fileName"],
                "result": "No"
            })
# Output the result
print(f"result: {result_contain_all_information}")