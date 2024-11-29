data = [{
        "fileName": "B5D5P6L9J574P8VDBK9LQG9Q9C0SBUB4.mp3",
        "agentChannel": 1,
        "time_load_info": 0.005368947982788086,
        "agentAffirmBelief": {
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
            "position_range_index": "None",
            "position_condition": [],
            "task": "compare"
        },
        "agentQuoteSolution": {
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
            "position_range_index": "None",
            "position_condition": [],
            "task": "compare"
        },
        "agentSuggestiveCustomer": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes",
                "2": "yes"
            },
            "decision_position": [
                [
                    {
                        "index": 17,
                        "channel": 1,
                        "text": "ý là bây giờ mình đi vay mượn ai ra đóng trước 1 kỳ đi",
                        "intents": [
                            "agent_suggestive"
                        ],
                        "entities": {
                            "oh_solution": [
                                {
                                    "start": 18,
                                    "end": 32,
                                    "value": "đi vay mượn ai",
                                    "real_value": "đi vay mượn ai",
                                    "entity": "oh_solution",
                                    "subentities": [],
                                    "is_required": "required"
                                }
                            ]
                        }
                    }
                ],
                [
                    {
                        "index": 22,
                        "channel": 1,
                        "text": "vay mượn ai ra xử lý gấp trong ngày hôm nay nha",
                        "intents": [
                            "agent_suggestive"
                        ],
                        "entities": {
                            "oh_solution": [
                                {
                                    "start": 0,
                                    "end": 11,
                                    "value": "vay mượn ai",
                                    "real_value": "vay mượn ai",
                                    "entity": "oh_solution",
                                    "subentities": [],
                                    "is_required": "required"
                                }
                            ]
                        }
                    }
                ],
                [
                    {
                        "index": 36,
                        "channel": 1,
                        "text": "rồi vay mượn đồng nghiệp hay bạn bè gì đi người nhà người thân gì đó vay mượn đóng 1 kỳ giùm em với nha",
                        "intents": [
                            "agent_suggestive"
                        ],
                        "entities": {
                            "oh_solution": [
                                {
                                    "entity": "oh_solution",
                                    "value": "vay mượn đóng",
                                    "start": 69,
                                    "end": 82,
                                    "real_value": "vay mượn đóng",
                                    "is_required": "required"
                                }
                            ]
                        }
                    }
                ]
            ],
            "decision": "yes",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0,
                "2": 1.0
            },
            "position": [
                {
                    "index": 17,
                    "channel": 1,
                    "text": "ý là bây giờ mình đi vay mượn ai ra đóng trước 1 kỳ đi",
                    "intents": [
                        "agent_suggestive"
                    ],
                    "entities": {
                        "oh_solution": [
                            {
                                "start": 18,
                                "end": 32,
                                "value": "đi vay mượn ai",
                                "real_value": "đi vay mượn ai",
                                "entity": "oh_solution",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 22,
                    "channel": 1,
                    "text": "vay mượn ai ra xử lý gấp trong ngày hôm nay nha",
                    "intents": [
                        "agent_suggestive"
                    ],
                    "entities": {
                        "oh_solution": [
                            {
                                "start": 0,
                                "end": 11,
                                "value": "vay mượn ai",
                                "real_value": "vay mượn ai",
                                "entity": "oh_solution",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 36,
                    "channel": 1,
                    "text": "rồi vay mượn đồng nghiệp hay bạn bè gì đi người nhà người thân gì đó vay mượn đóng 1 kỳ giùm em với nha",
                    "intents": [
                        "agent_suggestive"
                    ],
                    "entities": {
                        "oh_solution": [
                            {
                                "entity": "oh_solution",
                                "value": "vay mượn đóng",
                                "start": 69,
                                "end": 82,
                                "real_value": "vay mượn đóng",
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            "slots": {
                "oh_solution": [
                    {
                        "index": 17,
                        "value": [
                            "đi vay mượn ai"
                        ]
                    },
                    {
                        "index": 22,
                        "value": [
                            "vay mượn ai"
                        ]
                    },
                    {
                        "index": 36,
                        "value": [
                            "vay mượn đóng"
                        ]
                    }
                ]
            },
            "task": "compare_beta"
        },
        "cusCantPay": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 11,
                    "channel": 2,
                    "text": "dạ em đang em đang khó khăn anh mong ừ công ty dài thời gian cho trước chứ giờ đang",
                    "intents": [
                        "cus_cant_pay"
                    ],
                    "entities": {}
                },
                {
                    "index": 12,
                    "channel": 1,
                    "text": "nhưng mà giờ cái của anh bị chậm 22 tháng đó anh",
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
                    "index": 11,
                    "channel": 2,
                    "text": "dạ em đang em đang khó khăn anh mong ừ công ty dài thời gian cho trước chứ giờ đang",
                    "intents": [
                        "cus_cant_pay"
                    ],
                    "entities": {}
                },
                {
                    "index": 12,
                    "channel": 1,
                    "text": "nhưng mà giờ cái của anh bị chậm 22 tháng đó anh",
                    "intents": [],
                    "entities": {}
                }
            ],
            "slots": {},
            "position_range_index": [
                11,
                12
            ],
            "position_condition": [
                11,
                12,
                13
            ],
            "task": "compare"
        },
        "paymentImpose": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes",
                "2": "yes"
            },
            "decision_position": [
                {
                    "index": 22,
                    "channel": 1,
                    "text": "vay mượn ai ra xử lý gấp trong ngày hôm nay nha",
                    "intents": [
                        "agent_suggestive"
                    ],
                    "entities": {
                        "payment_impose_time": [
                            {
                                "start": 36,
                                "end": 43,
                                "value": "hôm nay",
                                "real_value": "hôm nay",
                                "entity": "payment_impose_time",
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
                    "index": 22,
                    "channel": 1,
                    "text": "vay mượn ai ra xử lý gấp trong ngày hôm nay nha",
                    "intents": [
                        "agent_suggestive"
                    ],
                    "entities": {
                        "payment_impose_time": [
                            {
                                "start": 36,
                                "end": 43,
                                "value": "hôm nay",
                                "real_value": "hôm nay",
                                "entity": "payment_impose_time",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            "slots": {
                "payment_impose_time": [
                    {
                        "index": 22,
                        "value": [
                            "hôm nay"
                        ],
                        "real_value": [
                            "hôm nay"
                        ]
                    }
                ]
            },
            "position_range_index": [
                22,
                22
            ],
            "position_condition": [
                22
            ],
            "task": "compare"
        },
        "callClassifyAI": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: alo <agent>: số điện thoại của nguyễn văn cường đúng không <customer>: đúng rồi <agent>: rồi sao cái tiền fe của anh 2 tháng đóng anh cường <agent>: alo <customer>: dạ bây giờ <agent>: nói lớn giùm em xíu đi anh <customer>: ừ nghe nghe <agent>: rồi rồi anh nói lớn giùm em xíu được không bên anh nghe hơi nhỏ đó anh <customer>: chị nghe rồi",
                    "intents": [
                        "client"
                    ],
                    "entities": {}
                }
            ],
            "decision": "client",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0
            },
            "position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: alo <agent>: số điện thoại của nguyễn văn cường đúng không <customer>: đúng rồi <agent>: rồi sao cái tiền fe của anh 2 tháng đóng anh cường <agent>: alo <customer>: dạ bây giờ <agent>: nói lớn giùm em xíu đi anh <customer>: ừ nghe nghe <agent>: rồi rồi anh nói lớn giùm em xíu được không bên anh nghe hơi nhỏ đó anh <customer>: chị nghe rồi",
                    "intents": [
                        "client"
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
        "callResultAI": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: đúng rồi <customer>: 3000000 gần được không <agent>: mình phải đóng đủ 1 kỳ nó mới vô tiền trong cái hợp đồng của mình á anh chứ mình đóng lẻ nó không có vô được á bị treo tiền lên á anh <agent>: anh đóng trễ nên nó phát sinh thêm 200000 tiền phạt á anh bình thường anh đóng 4934000 đúng không <customer>: kỳ 1 kỳ đầu tiên em đóng 5100000 mà sao mà <agent>: đâu có có mấy kỳ thấy anh đóng 4900000 đây nè <customer>: ừ <agent>: coi xoay sở đóng giùm em 5134000 nha <customer>: ừ để anh cố gắng xoay sở <agent>: rồi vay mượn đồng nghiệp hay bạn bè gì đi người nhà người thân gì đó vay mượn đóng 1 kỳ giùm em với nha <customer>: ừ <customer>: ừ <agent>: nó cũng chậm hơn 2 tháng anh sau này khó giải quyết đó anh <customer>: dạ dạ em biết rồi <agent>: rồi rồi cảm ơn chị ha",
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
                    "text": "<agent>: đúng rồi <customer>: 3000000 gần được không <agent>: mình phải đóng đủ 1 kỳ nó mới vô tiền trong cái hợp đồng của mình á anh chứ mình đóng lẻ nó không có vô được á bị treo tiền lên á anh <agent>: anh đóng trễ nên nó phát sinh thêm 200000 tiền phạt á anh bình thường anh đóng 4934000 đúng không <customer>: kỳ 1 kỳ đầu tiên em đóng 5100000 mà sao mà <agent>: đâu có có mấy kỳ thấy anh đóng 4900000 đây nè <customer>: ừ <agent>: coi xoay sở đóng giùm em 5134000 nha <customer>: ừ để anh cố gắng xoay sở <agent>: rồi vay mượn đồng nghiệp hay bạn bè gì đi người nhà người thân gì đó vay mượn đóng 1 kỳ giùm em với nha <customer>: ừ <customer>: ừ <agent>: nó cũng chậm hơn 2 tháng anh sau này khó giải quyết đó anh <customer>: dạ dạ em biết rồi <agent>: rồi rồi cảm ơn chị ha",
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
                "criteria_name": "cusCantPay",
                "decision": "yes",
                "position_range_index": [
                    11,
                    12
                ],
                "slots": {}
            },
            {
                "criteria_name": "paymentImpose",
                "decision": "yes",
                "position_range_index": [
                    22,
                    22
                ],
                "slots": {
                    "payment_impose_time": [
                        {
                            "index": 22,
                            "value": [
                                "hôm nay"
                            ],
                            "real_value": [
                                "hôm nay"
                            ]
                        }
                    ]
                }
            },
            {
                "criteria_name": "agentSuggestiveCustomer",
                "decision": "yes",
                "position_range_index": "",
                "slots": {
                    "oh_solution": [
                        {
                            "index": 17,
                            "value": [
                                "đi vay mượn ai"
                            ]
                        },
                        {
                            "index": 22,
                            "value": [
                                "vay mượn ai"
                            ]
                        },
                        {
                            "index": 36,
                            "value": [
                                "vay mượn đóng"
                            ]
                        }
                    ]
                }
            }
        ]
    },]

result = []
for i in data:
    #các case dặc biệt không có tình huống từ chối chấm full điểm
    if (i["callClassifyAI"]["decision"]) == "ec":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối khách do rơi vào trường hợp EC"
        })
    # nếu đi vào nhánh wrong_contact thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "wrongnumber":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối do rơi vào nhầm máy"
        })
    elif (i["callClassifyAI"]["decision"]) == "silent":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối do rơi vào im lặng"
        })
    else:
        if (i["callResultAI"]["decision"]) == "paid":
            result.append({
                "file_name": i["fileName"],
                "result": "Yes_20",
                "reason": "không có tính huống từ chối khách hàng đã thanh toán"
            })
        else:
            if (i["cusCantPay"]["evaluate"]) == "yes" and (i["cusCantPay"]["decision"]) == "yes":
                if (i["agentSuggestiveCustomer"]["decision"]) == "suggestive_cus":
                    result.append({
                        "file_name": i["fileName"],
                        "result": "Yes_20",
                        "reason": "tình huống từ chối - khách hàng tự đưa ra giải pháp thanh toán"
                    })
                elif (i["agentSuggestiveCustomer"]["decision"]) == "suggestive_agent":
                    result.append({
                        "file_name": i["fileName"],
                        "result": "Yes_20",
                        "reason": "tình huống từ chối - agent khơi gợi khách hàng đưa ra giải pháp thanh toán"
                    })
                elif (i["agentSuggestiveCustomer"]["decision"]) == "yes":
                    if (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentAffirmBelief"]["decision"]) == "yes" and (i["paymentImpose"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (3/3 ý)"
                        })
                    elif (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentAffirmBelief"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (2/3 ý).1"
                        })
                    elif (i["agentQuoteSolution"]["decision"]) == "yes" and (i["paymentImpose"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (2/3 ý).2"
                        })
                    elif (i["agentAffirmBelief"]["decision"]) == "yes" and (i["paymentImpose"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (2/3 ý).3"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "No",
                            "reason": "agent khơi gợi nhưng chỉ thông báo 1/3 tiêu chí còn lại"
                        })
                else:
                    result.append({
                        "file_name": i["fileName"],
                        "result": "No",
                        "reason": "agent không khơi gợi khách hàng không đưa ra giải pháp"
                    })
            else:
                result.append({
                    "file_name": i["fileName"],
                    "result": "Yes_20",
                    "reason": "không có tình huống từ chối chấm full điểm"
                })
print(result)