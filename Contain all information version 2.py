data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.0034525394439697266,
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
                "index": 24,
                "channel": 1,
                "text": "đóng xong kỳ này thì còn kỳ sau là kỳ cuối vui lòng hoàn tất đúng hạn hợp đồng trước ngày mùng 2 hàng tháng nhận ưu trả góp về sau sau ngày mùng 2 này tiền công ty em chưa nhận được thì công ty vẫn sẽ tiếp tục quy trình điện lại chị hường sau em cảm ơn chào chị ạ",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "due_date": [
                        {
                            "start": 79,
                            "end": 96,
                            "value": "trước ngày mùng 2",
                            "real_value": "trước ngày mùng 2",
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
                "index": 24,
                "channel": 1,
                "text": "đóng xong kỳ này thì còn kỳ sau là kỳ cuối vui lòng hoàn tất đúng hạn hợp đồng trước ngày mùng 2 hàng tháng nhận ưu trả góp về sau sau ngày mùng 2 này tiền công ty em chưa nhận được thì công ty vẫn sẽ tiếp tục quy trình điện lại chị hường sau em cảm ơn chào chị ạ",
                "intents": [
                    "willpay_summary"
                ],
                "entities": {
                    "due_date": [
                        {
                            "start": 79,
                            "end": 96,
                            "value": "trước ngày mùng 2",
                            "real_value": "trước ngày mùng 2",
                            "entity": "due_date",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "due_date": [
                {
                    "index": 24,
                    "value": [
                        "trước ngày mùng 2"
                    ],
                    "real_value": [
                        "trước ngày mùng 2"
                    ]
                }
            ]
        },
        "position_range_index": [
            24,
            24
        ],
        "position_condition": [
            24
        ],
        "task": "compare"
    },
    "criterias_order": [
        {
            "criteria_name": "willpaySummary",
            "decision": "yes",
            "position_range_index": [
                24,
                24
            ],
            "slots": {
                "due_date": [
                    {
                        "index": 24,
                        "value": [
                            "trước ngày mùng 2"
                        ],
                        "real_value": [
                            "trước ngày mùng 2"
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