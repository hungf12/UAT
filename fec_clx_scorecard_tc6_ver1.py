data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.004020214080810547,
    "askPaymentAmount": {
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
        "task": "compare_beta"
    },
    "askPaymentDatetime": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "yes"
        },
        "decision_position": [
            [
                {
                    "index": 9,
                    "channel": 1,
                    "text": "từ tháng 6 trở đi là mình cũng chưa có thanh toán",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 3,
                                "end": 10,
                                "value": "tháng 6",
                                "real_value": "tháng 6",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 10,
                    "channel": 2,
                    "text": "dạ",
                    "intents": [],
                    "entities": {
                        "customer_confirm_word": [
                            {
                                "entity": "customer_confirm_word",
                                "value": "dạ",
                                "start": 0,
                                "end": 2,
                                "real_value": "dạ",
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            [
                {
                    "index": 13,
                    "channel": 1,
                    "text": "chị cố gắng sắp xếp từ giờ đến trễ nhất là 23 tây giùm em là bây giờ bên em hỗ trợ cho chị trong tuần này tới thứ 6 á hỗ trợ chị tới ngày đó vui lòng mình bổ sung được tối thiểu không được những kỳ đang trễ là 3 kỳ hiện tại của tháng 6 tháng 7 tháng 8 thì mình vui lòng cố gắng bổ sung được ít nhất từ 1 đến 2 kỳ để hồ sơ của mình có phát sinh giao dịch trong 3 tháng tiếp nếu mà không á chị vì cái hồ sơ mình mua trả góp góp thành hồ sơ nợ xấu đó",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 43,
                                "end": 49,
                                "value": "23 tây",
                                "real_value": "23 tây",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 14,
                    "channel": 2,
                    "text": "dạ",
                    "intents": [],
                    "entities": {
                        "customer_confirm_word": [
                            {
                                "entity": "customer_confirm_word",
                                "value": "dạ",
                                "start": 0,
                                "end": 2,
                                "real_value": "dạ",
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            [
                {
                    "index": 27,
                    "channel": 1,
                    "text": "nên có gì cố gắng giùm em trễ nhất là 23 tây mình thu xếp được tối thiểu 1 đến 2 kỳ là mình chạy ra mình thanh toán cho phía công ty rồi tháng mình cố gắng mình thanh toán luôn các kỳ trễ còn lại để hồ sơ tránh kiểm tra tình trạng hồ sơ đánh giá lại hồ sơ nợ xấu tại vì giờ mình đã chú ý hồ sơ nhắc nhở khách hàng để lên sắp lên nợ xấu nhóm 3 rồi chị ha",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 38,
                                "end": 44,
                                "value": "23 tây",
                                "real_value": "23 tây",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 28,
                    "channel": 2,
                    "text": "dạ",
                    "intents": [],
                    "entities": {
                        "customer_confirm_word": [
                            {
                                "entity": "customer_confirm_word",
                                "value": "dạ",
                                "start": 0,
                                "end": 2,
                                "real_value": "dạ",
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
                "index": 9,
                "channel": 1,
                "text": "từ tháng 6 trở đi là mình cũng chưa có thanh toán",
                "intents": [
                    "ask_payment_info"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 3,
                            "end": 10,
                            "value": "tháng 6",
                            "real_value": "tháng 6",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 10,
                "channel": 2,
                "text": "dạ",
                "intents": [],
                "entities": {
                    "customer_confirm_word": [
                        {
                            "entity": "customer_confirm_word",
                            "value": "dạ",
                            "start": 0,
                            "end": 2,
                            "real_value": "dạ",
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 13,
                "channel": 1,
                "text": "chị cố gắng sắp xếp từ giờ đến trễ nhất là 23 tây giùm em là bây giờ bên em hỗ trợ cho chị trong tuần này tới thứ 6 á hỗ trợ chị tới ngày đó vui lòng mình bổ sung được tối thiểu không được những kỳ đang trễ là 3 kỳ hiện tại của tháng 6 tháng 7 tháng 8 thì mình vui lòng cố gắng bổ sung được ít nhất từ 1 đến 2 kỳ để hồ sơ của mình có phát sinh giao dịch trong 3 tháng tiếp nếu mà không á chị vì cái hồ sơ mình mua trả góp góp thành hồ sơ nợ xấu đó",
                "intents": [
                    "ask_payment_info"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 43,
                            "end": 49,
                            "value": "23 tây",
                            "real_value": "23 tây",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 14,
                "channel": 2,
                "text": "dạ",
                "intents": [],
                "entities": {
                    "customer_confirm_word": [
                        {
                            "entity": "customer_confirm_word",
                            "value": "dạ",
                            "start": 0,
                            "end": 2,
                            "real_value": "dạ",
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 27,
                "channel": 1,
                "text": "nên có gì cố gắng giùm em trễ nhất là 23 tây mình thu xếp được tối thiểu 1 đến 2 kỳ là mình chạy ra mình thanh toán cho phía công ty rồi tháng mình cố gắng mình thanh toán luôn các kỳ trễ còn lại để hồ sơ tránh kiểm tra tình trạng hồ sơ đánh giá lại hồ sơ nợ xấu tại vì giờ mình đã chú ý hồ sơ nhắc nhở khách hàng để lên sắp lên nợ xấu nhóm 3 rồi chị ha",
                "intents": [
                    "ask_payment_info"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 38,
                            "end": 44,
                            "value": "23 tây",
                            "real_value": "23 tây",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 28,
                "channel": 2,
                "text": "dạ",
                "intents": [],
                "entities": {
                    "customer_confirm_word": [
                        {
                            "entity": "customer_confirm_word",
                            "value": "dạ",
                            "start": 0,
                            "end": 2,
                            "real_value": "dạ",
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "payment_datetime": [
                {
                    "index": 9,
                    "value": [
                        "tháng 6"
                    ]
                },
                {
                    "index": 13,
                    "value": [
                        "23 tây"
                    ]
                },
                {
                    "index": 27,
                    "value": [
                        "23 tây"
                    ]
                }
            ],
            "customer_confirm_word": [
                {
                    "index": 10,
                    "value": [
                        "dạ"
                    ]
                },
                {
                    "index": 14,
                    "value": [
                        "dạ"
                    ]
                },
                {
                    "index": 28,
                    "value": [
                        "dạ"
                    ]
                }
            ]
        },
        "task": "compare_beta"
    },
    "askPaymentMethod": {
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
        "task": "compare_beta"
    },
    "cusProvidePaymentAmount": {
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
    "cusProvidePaymentDatetime": {
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
    "cusProvidePaymentMethod": {
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
    "callClassifyAI": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<customer>: alo <agent>: alo <customer>: alo <agent>: dạ số điện thoại chị bạch thị thu hà đây đúng không <customer>: dạ dạ <agent>: hồ sơ vay trả góp bên fe của mình á mua sản phẩm điện máy á đóng tiền được vậy chị <customer>: dạ tại em chạy tiền chưa ra nên em đóng chưa có được <agent>: là mình đang gặp khó khăn nhưng mà từ lúc mà mình nhận cái sản phẩm về tới giờ là mình mới đóng được đúng 1 lần của tháng 5 thôi <customer>: dạ <agent>: từ tháng 6 trở đi là mình cũng chưa có thanh toán",
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
                "text": "<customer>: alo <agent>: alo <customer>: alo <agent>: dạ số điện thoại chị bạch thị thu hà đây đúng không <customer>: dạ dạ <agent>: hồ sơ vay trả góp bên fe của mình á mua sản phẩm điện máy á đóng tiền được vậy chị <customer>: dạ tại em chạy tiền chưa ra nên em đóng chưa có được <agent>: là mình đang gặp khó khăn nhưng mà từ lúc mà mình nhận cái sản phẩm về tới giờ là mình mới đóng được đúng 1 lần của tháng 5 thôi <customer>: dạ <agent>: từ tháng 6 trở đi là mình cũng chưa có thanh toán",
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
                "text": "<agent>: dạ đi làm kiểu như công việc của mình lúc cói hay là công ty nó nó giảm cắt giảm nhân sự hay sao chị <customer>: tại em mới đi làm đây á <agent>: à vậy là 3 tháng rồi là mình chưa có đi làm 2 tháng rồi chưa đi làm tháng bắt đầu mình mới đi làm lại <customer>: dạ <agent>: đúng không rồi mình cố gắng giúp em nha tại vì hồ sơ của mình đã trễ rồi mà để 90 ngày quá 90 ngày trễ rồi chắc chắn hồ sơ lên nợ xấu mà hồ sơ này là gần đến 90 ngày rồi ha <customer>: dạ dạ <agent>: nên có gì cố gắng giùm em trễ nhất là 23 tây mình thu xếp được tối thiểu 1 đến 2 kỳ là mình chạy ra mình thanh toán cho phía công ty rồi tháng mình cố gắng mình thanh toán luôn các kỳ trễ còn lại để hồ sơ tránh kiểm tra tình trạng hồ sơ đánh giá lại hồ sơ nợ xấu tại vì giờ mình đã chú ý hồ sơ nhắc nhở khách hàng để lên sắp lên nợ xấu nhóm 3 rồi chị ha <customer>: dạ <agent>: rồi em chốt hồ sơ của chị ở đây trễ nhất năm giờ chiều của ngày 2 3 tây <customer>: dạ dạ <agent>: tháng 8 này thế giới di động hoặc điện máy xanh thì vui lòng ra thanh toán tối thiểu những kỳ trễ của mình không được tất cả 3 kỳ thì mình ráng cố gắng 1 đến 2 kỳ trễ <customer>: dạ <agent>: để bên em báo cáo hồ sơ nhá <customer>: dạ dạ dạ dạ dạ <agent>: rồi em cảm ơn chào chị",
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
                "text": "<agent>: dạ đi làm kiểu như công việc của mình lúc cói hay là công ty nó nó giảm cắt giảm nhân sự hay sao chị <customer>: tại em mới đi làm đây á <agent>: à vậy là 3 tháng rồi là mình chưa có đi làm 2 tháng rồi chưa đi làm tháng bắt đầu mình mới đi làm lại <customer>: dạ <agent>: đúng không rồi mình cố gắng giúp em nha tại vì hồ sơ của mình đã trễ rồi mà để 90 ngày quá 90 ngày trễ rồi chắc chắn hồ sơ lên nợ xấu mà hồ sơ này là gần đến 90 ngày rồi ha <customer>: dạ dạ <agent>: nên có gì cố gắng giùm em trễ nhất là 23 tây mình thu xếp được tối thiểu 1 đến 2 kỳ là mình chạy ra mình thanh toán cho phía công ty rồi tháng mình cố gắng mình thanh toán luôn các kỳ trễ còn lại để hồ sơ tránh kiểm tra tình trạng hồ sơ đánh giá lại hồ sơ nợ xấu tại vì giờ mình đã chú ý hồ sơ nhắc nhở khách hàng để lên sắp lên nợ xấu nhóm 3 rồi chị ha <customer>: dạ <agent>: rồi em chốt hồ sơ của chị ở đây trễ nhất năm giờ chiều của ngày 2 3 tây <customer>: dạ dạ <agent>: tháng 8 này thế giới di động hoặc điện máy xanh thì vui lòng ra thanh toán tối thiểu những kỳ trễ của mình không được tất cả 3 kỳ thì mình ráng cố gắng 1 đến 2 kỳ trễ <customer>: dạ <agent>: để bên em báo cáo hồ sơ nhá <customer>: dạ dạ dạ dạ dạ <agent>: rồi em cảm ơn chào chị",
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
            "criteria_name": "askPaymentDatetime",
            "decision": "yes",
            "position_range_index": "",
            "slots": {
                "payment_datetime": [
                    {
                        "index": 9,
                        "value": [
                            "tháng 6"
                        ]
                    },
                    {
                        "index": 13,
                        "value": [
                            "23 tây"
                        ]
                    },
                    {
                        "index": 27,
                        "value": [
                            "23 tây"
                        ]
                    }
                ],
                "customer_confirm_word": [
                    {
                        "index": 10,
                        "value": [
                            "dạ"
                        ]
                    },
                    {
                        "index": 14,
                        "value": [
                            "dạ"
                        ]
                    },
                    {
                        "index": 28,
                        "value": [
                            "dạ"
                        ]
                    }
                ]
            }
        }
    ]
}]

result_data = []

for i in data:
    # nếu đi vào nhánh EC thì chấm full điểm
    if (i["callClassifyAI"]["decision"]) == "ec":
        result_data.append({
            "Type": "EC",
            "file_name": i["fileName"],
            "result": "Yes_30"
        })
    # nếu đi vào nhánh wrong_contact thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "wrongnumber":
        result_data.append({
            "Type": "Wrong",
            "file_name": i["fileName"],
            "result": "Yes_30"
        })
    # nếu đi vào nhánh silent thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "silent":
        result_data.append({
            "Type": "silent",
            "file_name": i["fileName"],
            "result": "No"
        })
    else:
        if (i["callClassifyAI"]["decision"]) == "client":
            if (i["callResultAI"]["decision"]) == "willpay" or (i["callResultAI"]["decision"]) == "paid":
                if (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["cusProvidePaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 3/3 cus",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 2/3 cus - 1/3 agent.1",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["cusProvidePaymentMethod"]["decision"]) == "yes" and (i["askPaymentDatetime"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 2/3 cus - 1/3 agent.2",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["cusProvidePaymentMethod"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 2/3 cus - 1/3 agent.3",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["askPaymentDatetime"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 1/3 cus - 2/3 agent.1",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 1/3 cus - 2/3 agent.2",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentMethod"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes" and (i["askPaymentDatetime"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 30 - 1/3 cus - 2/3 agent.3",
                        "file_name": i["fileName"],
                        "result": "Yes_30"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["cusProvidePaymentDatetime"]["decision"]) == "yes" or (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["cusProvidePaymentMethod"]["decision"]) == "yes" or (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["cusProvidePaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 2/3 cus - 0/3 agent",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["askPaymentDatetime"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.1",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.2",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.3",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentDatetime"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.4",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentMethod"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.5",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentMethod"]["decision"]) == "yes" and (i["askPaymentDatetime"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 20 - 1/3 cus - 1/3 agent.6",
                        "file_name": i["fileName"],
                        "result": "Yes_20"
                    })
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" or (i["cusProvidePaymentDatetime"]["decision"]) == "yes" or (i["cusProvidePaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 10 - 1/3 cus - 0/3 agent",
                        "file_name": i["fileName"],
                        "result": "Yes_10"
                    })
                else:
                    if (i["askPaymentDatetime"]["decision"]) == "no":
                        result_data.append({
                            "type": "No - không nhắc ngày thanh toán",
                            "file_name": i["fileName"],
                            "result": "No"
                        })
                    else:
                        if (i["askPaymentDatetime"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                            result_data.append({
                                "type": "yes 30 - 3/3 agent",
                                "file_name": i["fileName"],
                                "result": "Yes_30"
                            })
                        elif (i["askPaymentDatetime"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes":
                            result_data.append({
                                "type": "yes 20 - 2/3 agent.1",
                                "file_name": i["fileName"],
                                "result": "Yes_20"
                            })
                        elif (i["askPaymentDatetime"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == "yes":
                            result_data.append({
                                "type": "yes 20 - 2/3 agent.2",
                                "file_name": i["fileName"],
                                "result": "Yes_20"
                            })
                        elif (i["askPaymentDatetime"]["decision"]) == "yes":
                            result_data.append({
                                "type": "yes 20 - 2/3 agent",
                                "file_name": i["fileName"],
                                "result": "Yes_10"
                            })
                        else:
                            result_data.append({
                                "type": "fall_back",
                                "file_name": i["fileName"],
                                "result": "No"
                            })
            else:
                result_data.append({
                    "type": "fall_back_nopay_&_paid",
                    "file_name": i["fileName"],
                    "result": "Yes_30"
                })
print(f"result: {result_data}")