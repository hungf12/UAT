data = [{
    "fileName": "",
    "agentChannel": 2,
    "time_load_info": 0.003935098648071289,
    "nopaySummary": {
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
    "paidSummary": {
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
    "willpaySummary": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 10,
                "channel": 2,
                "text": "lưu ý chuyển nhận tiền qua trung gian mất 1 ngày tránh phát sinh rủi ro có sớm trong hôm nay 26 góp giùm em còn không chậm nhất ngày mai 27 nha chị",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 85,
                            "end": 92,
                            "value": "hôm nay",
                            "real_value": "hôm nay",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 93,
                            "end": 95,
                            "value": "26",
                            "real_value": "26",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 128,
                            "end": 139,
                            "value": "ngày mai 27",
                            "real_value": "ngày mai 27",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_method": [
                        {
                            "start": 6,
                            "end": 12,
                            "value": "chuyển",
                            "real_value": "chuyển",
                            "entity": "payment_method",
                            "subentities": "null",
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 11,
                "channel": 1,
                "text": "rồi rồi rồi nhá rồi rồi",
                "intents": [],
                "entities": {}
            },
            {
                "index": 12,
                "channel": 2,
                "text": "rồi",
                "intents": [],
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
                "index": 10,
                "channel": 2,
                "text": "lưu ý chuyển nhận tiền qua trung gian mất 1 ngày tránh phát sinh rủi ro có sớm trong hôm nay 26 góp giùm em còn không chậm nhất ngày mai 27 nha chị",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 85,
                            "end": 92,
                            "value": "hôm nay",
                            "real_value": "hôm nay",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 93,
                            "end": 95,
                            "value": "26",
                            "real_value": "26",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 128,
                            "end": 139,
                            "value": "ngày mai 27",
                            "real_value": "ngày mai 27",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ],
                    "payment_method": [
                        {
                            "start": 6,
                            "end": 12,
                            "value": "chuyển",
                            "real_value": "chuyển",
                            "entity": "payment_method",
                            "subentities": "null",
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 11,
                "channel": 1,
                "text": "rồi rồi rồi nhá rồi rồi",
                "intents": [],
                "entities": {}
            },
            {
                "index": 12,
                "channel": 2,
                "text": "rồi",
                "intents": [],
                "entities": {}
            }
        ],
        "slots": {
            "payment_datetime": [
                {
                    "index": 10,
                    "value": [
                        "hôm nay",
                        "26",
                        "ngày mai 27"
                    ],
                    "real_value": [
                        "hôm nay",
                        "26",
                        "ngày mai 27"
                    ]
                }
            ],
            "payment_method": [
                {
                    "index": 10,
                    "value": [
                        "chuyển"
                    ],
                    "real_value": [
                        "chuyển"
                    ]
                }
            ]
        },
        "position_range_index": [
            10,
            12
        ],
        "position_condition": [
            10
        ],
        "task": "compare"
    },
    "callResultAI": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes"
        },
        "decision_position": [
            {
                "index": 0,
                "channel": 2,
                "text": "<agent>: dạ <agent>: dạ chị <agent>: alo <customer>: alo <agent>: chị nghe rõ tín hiệu không chị chào chị em thuộc home credit á chị hoàng thúy vân đúng không chị <customer>: ừ <agent>: đánh giá nâng cao chất lượng dịch vụ hỗ trợ xe máy honda đang vay mua trả góp tôi hẹn hồ sơ hồ sơ thanh toán hàng tháng 28 của chị số tiền thanh toán là 1624000 hôm nay 26 rồi nè chị vân <customer>: ừ ừ ừ rồi rồi rồi <agent>: ngày nào công ty luôn chị <customer>: rồi rồi rồi <agent>: lưu ý chuyển nhận tiền qua trung gian mất 1 ngày tránh phát sinh rủi ro có sớm trong hôm nay 26 góp giùm em còn không chậm nhất ngày mai 27 nha chị <customer>: rồi rồi rồi nhá rồi rồi <agent>: rồi",
                "intents": [
                    "willpay"
                ],
                "entities": {}
            }
        ],
        "decision": "willpay",
        "confidence": 1.0,
        "confidence_channel": {
            "2": 1.0
        },
        "position": [
            {
                "index": 0,
                "channel": 2,
                "text": "<agent>: dạ <agent>: dạ chị <agent>: alo <customer>: alo <agent>: chị nghe rõ tín hiệu không chị chào chị em thuộc home credit á chị hoàng thúy vân đúng không chị <customer>: ừ <agent>: đánh giá nâng cao chất lượng dịch vụ hỗ trợ xe máy honda đang vay mua trả góp tôi hẹn hồ sơ hồ sơ thanh toán hàng tháng 28 của chị số tiền thanh toán là 1624000 hôm nay 26 rồi nè chị vân <customer>: ừ ừ ừ rồi rồi rồi <agent>: ngày nào công ty luôn chị <customer>: rồi rồi rồi <agent>: lưu ý chuyển nhận tiền qua trung gian mất 1 ngày tránh phát sinh rủi ro có sớm trong hôm nay 26 góp giùm em còn không chậm nhất ngày mai 27 nha chị <customer>: rồi rồi rồi nhá rồi rồi <agent>: rồi",
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
                10,
                12
            ],
            "slots": {
                "payment_datetime": [
                    {
                        "index": 10,
                        "value": [
                            "hôm nay",
                            "26",
                            "ngày mai 27"
                        ],
                        "real_value": [
                            "hôm nay",
                            "26",
                            "ngày mai 27"
                        ]
                    }
                ],
                "payment_method": [
                    {
                        "index": 10,
                        "value": [
                            "chuyển"
                        ],
                        "real_value": [
                            "chuyển"
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
            else:
                result_contain_all_information.append({
                    "case": "faillback_1",
                    "file_name": item["fileName"],
                    "result": "No"
                })
        else:
            if ('amount' in slots_0) and ('payment_datetime' in slots_0) or ('amount' in slots_0) and ('payment_method' in slots_0) or ('payment_datetime' in slots_0) and ('payment_method' in slots_0):
                result_contain_all_information.append({
                    "case": "willpay_5",
                    "file_name": item["fileName"],
                    "result": "partially"
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