data = [{
        "fileName": "R7QO3PU3BH4C15LAKVHOR5I70O0R5I0L.mp3",
        "agentChannel": 1,
        "time_load_info": 0.0032384395599365234,
        "askPaymentAmount": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 27,
                    "channel": 1,
                    "text": "như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_amount": [
                            {
                                "start": 127,
                                "end": 134,
                                "value": "1700000",
                                "real_value": "1700000",
                                "entity": "payment_amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 28,
                    "channel": 2,
                    "text": "dạ vâng ạ dạ vâng ạ",
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
                            },
                            {
                                "entity": "customer_confirm_word",
                                "value": "dạ",
                                "start": 10,
                                "end": 12,
                                "real_value": "dạ",
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
                    "index": 27,
                    "channel": 1,
                    "text": "như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_amount": [
                            {
                                "start": 127,
                                "end": 134,
                                "value": "1700000",
                                "real_value": "1700000",
                                "entity": "payment_amount",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 28,
                    "channel": 2,
                    "text": "dạ vâng ạ dạ vâng ạ",
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
                            },
                            {
                                "entity": "customer_confirm_word",
                                "value": "dạ",
                                "start": 10,
                                "end": 12,
                                "real_value": "dạ",
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            "slots": {
                "payment_amount": [
                    {
                        "index": 27,
                        "value": [
                            "1700000"
                        ],
                        "real_value": [
                            "1700000"
                        ]
                    }
                ],
                "customer_confirm_word": [
                    {
                        "index": 28,
                        "value": [
                            "dạ",
                            "dạ"
                        ],
                        "real_value": [
                            "dạ",
                            "dạ"
                        ]
                    }
                ]
            },
            "position_range_index": [
                27,
                28
            ],
            "position_condition": [
                27,
                28
            ],
            "task": "compare"
        },
        "askPaymentDatetime": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 14,
                    "channel": 1,
                    "text": "còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 19,
                                "end": 21,
                                "value": "15",
                                "real_value": "15",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 15,
                    "channel": 2,
                    "text": "ừ chắc cũng để em tất toán hết luôn chứ",
                    "intents": [],
                    "entities": {
                        "customer_confirm_word": [
                            {
                                "entity": "customer_confirm_word",
                                "value": "ừ",
                                "start": 0,
                                "end": 1,
                                "real_value": "ừ",
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
                    "index": 14,
                    "channel": 1,
                    "text": "còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 19,
                                "end": 21,
                                "value": "15",
                                "real_value": "15",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 15,
                    "channel": 2,
                    "text": "ừ chắc cũng để em tất toán hết luôn chứ",
                    "intents": [],
                    "entities": {
                        "customer_confirm_word": [
                            {
                                "entity": "customer_confirm_word",
                                "value": "ừ",
                                "start": 0,
                                "end": 1,
                                "real_value": "ừ",
                                "is_required": "required"
                            }
                        ]
                    }
                }
            ],
            "slots": {
                "payment_datetime": [
                    {
                        "index": 14,
                        "value": [
                            "15"
                        ],
                        "real_value": [
                            "15"
                        ]
                    }
                ],
                "customer_confirm_word": [
                    {
                        "index": 15,
                        "value": [
                            "ừ"
                        ],
                        "real_value": [
                            "ừ"
                        ]
                    }
                ]
            },
            "position_range_index": [
                14,
                15
            ],
            "position_condition": [
                14,
                15
            ],
            "task": "compare"
        },
        "askPaymentMethod": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "yes"
            },
            "decision_position": [
                {
                    "index": 18,
                    "channel": 1,
                    "text": "cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_method": [
                            {
                                "entity": "payment_method",
                                "value": "ngân hàng",
                                "start": 26,
                                "end": 35,
                                "real_value": "ngân hàng",
                                "is_required": "required"
                            },
                            {
                                "entity": "payment_method",
                                "value": "ngân hàng",
                                "start": 159,
                                "end": 168,
                                "real_value": "ngân hàng",
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 19,
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
            "decision": "yes",
            "confidence": 1.0,
            "confidence_channel": {
                "2": 1.0,
                "1": 1.0
            },
            "position": [
                {
                    "index": 18,
                    "channel": 1,
                    "text": "cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_method": [
                            {
                                "entity": "payment_method",
                                "value": "ngân hàng",
                                "start": 26,
                                "end": 35,
                                "real_value": "ngân hàng",
                                "is_required": "required"
                            },
                            {
                                "entity": "payment_method",
                                "value": "ngân hàng",
                                "start": 159,
                                "end": 168,
                                "real_value": "ngân hàng",
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 19,
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
                "payment_method": [
                    {
                        "index": 18,
                        "value": [
                            "ngân hàng",
                            "ngân hàng"
                        ],
                        "real_value": [
                            "ngân hàng",
                            "ngân hàng"
                        ]
                    }
                ],
                "customer_confirm_word": [
                    {
                        "index": 19,
                        "value": [
                            "dạ"
                        ],
                        "real_value": [
                            "dạ"
                        ]
                    }
                ]
            },
            "position_range_index": [
                18,
                19
            ],
            "position_condition": [
                18,
                19
            ],
            "task": "compare"
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
            "position_range_index": "None",
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
            "position_range_index": "None",
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
            "position_range_index": "None",
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
                    "text": "<agent>: còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa <customer>: ừ chắc cũng để em tất toán hết luôn chứ <agent>: là là phải xử lý tại nhà rồi <customer>: dạ <agent>: cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là <customer>: dạ <agent>: đâu đâu có chuyện mà chị đang nợ bên ngân hàng rồi đang thiếu bên ngân hàng 3 tháng chị nói chị không có tiền trả rồi tháng chị cũng không chị trả 1 lần luôn là người ta chịu đâu chị không không phải như vậy người ta đang nói về cái hợp đồng của chị là chị không còn khả năng xử lý nợ bên ngân hàng nữa hiện tại nó sẽ bắt buộc chị thanh lý luôn toàn bộ cái khoản nợ này ví dụ như em gửi đơn về địa phương cho mình là mình xử lý luôn chứ chị không có kịp tới tháng chị đi đóng nữa đâu <customer>: dạ vâng <customer>: thì bây giờ cũng khó bây giờ em vẫn chưa lấy lương được <agent>: 3 kỳ có nghĩa là chị đang nợ bên người ta 3 tháng tháng 1 triệu bảy đi mà chị kêu là chị chưa có nhận lương chẳng lẽ chị nhận lương công ty 3 tháng 1 lần <customer>: có nghĩa là tháng em mấy tháng em có việc ở nhà nên là em chưa có ấy bên cho mình được <agent>: còn chị muốn thì em vẫn có thể gửi về công ty của chị về vấn đề lương bổng của chị như thế nào em vẫn có thể hỗ trợ cho chị được <customer>: dạ thôi cái đó vấn đề có vấn đề gì em định là tháng em sẽ tất toán hết luôn vì em cũng không có khả năng trả hàng tháng nữa được á <agent>: như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ <customer>: dạ vâng ạ dạ vâng ạ",
                    "intents": [
                        "silent"
                    ],
                    "entities": {}
                }
            ],
            "decision": "silent",
            "confidence": 1.0,
            "confidence_channel": {
                "1": 1.0
            },
            "position": [
                {
                    "index": 0,
                    "channel": 1,
                    "text": "<agent>: còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa <customer>: ừ chắc cũng để em tất toán hết luôn chứ <agent>: là là phải xử lý tại nhà rồi <customer>: dạ <agent>: cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là <customer>: dạ <agent>: đâu đâu có chuyện mà chị đang nợ bên ngân hàng rồi đang thiếu bên ngân hàng 3 tháng chị nói chị không có tiền trả rồi tháng chị cũng không chị trả 1 lần luôn là người ta chịu đâu chị không không phải như vậy người ta đang nói về cái hợp đồng của chị là chị không còn khả năng xử lý nợ bên ngân hàng nữa hiện tại nó sẽ bắt buộc chị thanh lý luôn toàn bộ cái khoản nợ này ví dụ như em gửi đơn về địa phương cho mình là mình xử lý luôn chứ chị không có kịp tới tháng chị đi đóng nữa đâu <customer>: dạ vâng <customer>: thì bây giờ cũng khó bây giờ em vẫn chưa lấy lương được <agent>: 3 kỳ có nghĩa là chị đang nợ bên người ta 3 tháng tháng 1 triệu bảy đi mà chị kêu là chị chưa có nhận lương chẳng lẽ chị nhận lương công ty 3 tháng 1 lần <customer>: có nghĩa là tháng em mấy tháng em có việc ở nhà nên là em chưa có ấy bên cho mình được <agent>: còn chị muốn thì em vẫn có thể gửi về công ty của chị về vấn đề lương bổng của chị như thế nào em vẫn có thể hỗ trợ cho chị được <customer>: dạ thôi cái đó vấn đề có vấn đề gì em định là tháng em sẽ tất toán hết luôn vì em cũng không có khả năng trả hàng tháng nữa được á <agent>: như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ <customer>: dạ vâng ạ dạ vâng ạ",
                    "intents": [
                        "silent"
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
                    "text": "<agent>: còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa <customer>: ừ chắc cũng để em tất toán hết luôn chứ <agent>: là là phải xử lý tại nhà rồi <customer>: dạ <agent>: cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là <customer>: dạ <agent>: đâu đâu có chuyện mà chị đang nợ bên ngân hàng rồi đang thiếu bên ngân hàng 3 tháng chị nói chị không có tiền trả rồi tháng chị cũng không chị trả 1 lần luôn là người ta chịu đâu chị không không phải như vậy người ta đang nói về cái hợp đồng của chị là chị không còn khả năng xử lý nợ bên ngân hàng nữa hiện tại nó sẽ bắt buộc chị thanh lý luôn toàn bộ cái khoản nợ này ví dụ như em gửi đơn về địa phương cho mình là mình xử lý luôn chứ chị không có kịp tới tháng chị đi đóng nữa đâu <customer>: dạ vâng <customer>: thì bây giờ cũng khó bây giờ em vẫn chưa lấy lương được <agent>: 3 kỳ có nghĩa là chị đang nợ bên người ta 3 tháng tháng 1 triệu bảy đi mà chị kêu là chị chưa có nhận lương chẳng lẽ chị nhận lương công ty 3 tháng 1 lần <customer>: có nghĩa là tháng em mấy tháng em có việc ở nhà nên là em chưa có ấy bên cho mình được <agent>: còn chị muốn thì em vẫn có thể gửi về công ty của chị về vấn đề lương bổng của chị như thế nào em vẫn có thể hỗ trợ cho chị được <customer>: dạ thôi cái đó vấn đề có vấn đề gì em định là tháng em sẽ tất toán hết luôn vì em cũng không có khả năng trả hàng tháng nữa được á <agent>: như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ <customer>: dạ vâng ạ dạ vâng ạ",
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
                    "text": "<agent>: còn mà chị nói tới 15 tháng chị mới đóng đóng là em nghĩ là chị cũng không có kịp phải đi đóng nữa <customer>: ừ chắc cũng để em tất toán hết luôn chứ <agent>: là là phải xử lý tại nhà rồi <customer>: dạ <agent>: cái này là chị vay nợ bên ngân hàng là chị vay trả góp là tháng chị trả tiền tháng chứ không phải gộp 1 lần chị trả ví dụ như hiện tại chị đang trả đầy đủ bên ngân hàng bên em nhưng mà chị có nhu cầu chị thanh lý luôn thì ok còn đây là không có chuyện mà có nghĩa là <customer>: dạ <agent>: đâu đâu có chuyện mà chị đang nợ bên ngân hàng rồi đang thiếu bên ngân hàng 3 tháng chị nói chị không có tiền trả rồi tháng chị cũng không chị trả 1 lần luôn là người ta chịu đâu chị không không phải như vậy người ta đang nói về cái hợp đồng của chị là chị không còn khả năng xử lý nợ bên ngân hàng nữa hiện tại nó sẽ bắt buộc chị thanh lý luôn toàn bộ cái khoản nợ này ví dụ như em gửi đơn về địa phương cho mình là mình xử lý luôn chứ chị không có kịp tới tháng chị đi đóng nữa đâu <customer>: dạ vâng <customer>: thì bây giờ cũng khó bây giờ em vẫn chưa lấy lương được <agent>: 3 kỳ có nghĩa là chị đang nợ bên người ta 3 tháng tháng 1 triệu bảy đi mà chị kêu là chị chưa có nhận lương chẳng lẽ chị nhận lương công ty 3 tháng 1 lần <customer>: có nghĩa là tháng em mấy tháng em có việc ở nhà nên là em chưa có ấy bên cho mình được <agent>: còn chị muốn thì em vẫn có thể gửi về công ty của chị về vấn đề lương bổng của chị như thế nào em vẫn có thể hỗ trợ cho chị được <customer>: dạ thôi cái đó vấn đề có vấn đề gì em định là tháng em sẽ tất toán hết luôn vì em cũng không có khả năng trả hàng tháng nữa được á <agent>: như vầy như em nói cho chị như vầy em chỉ để cho mình chậm nhất trước 5 giờ chiều nay chị không đóng được 1 kỳ tương đương với 1700000 thì bên em sẽ tiến hành theo quy định gửi đơn về địa phương của mình để xử lý nợ luôn chị nha cám ơn chị ạ <customer>: dạ vâng ạ dạ vâng ạ",
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
                "position_range_index": [
                    14,
                    15
                ],
                "slots": {
                    "payment_datetime": [
                        {
                            "index": 14,
                            "value": [
                                "15"
                            ],
                            "real_value": [
                                "15"
                            ]
                        }
                    ],
                    "customer_confirm_word": [
                        {
                            "index": 15,
                            "value": [
                                "ừ"
                            ],
                            "real_value": [
                                "ừ"
                            ]
                        }
                    ]
                }
            },
            {
                "criteria_name": "askPaymentMethod",
                "decision": "yes",
                "position_range_index": [
                    18,
                    19
                ],
                "slots": {
                    "payment_method": [
                        {
                            "index": 18,
                            "value": [
                                "ngân hàng",
                                "ngân hàng"
                            ],
                            "real_value": [
                                "ngân hàng",
                                "ngân hàng"
                            ]
                        }
                    ],
                    "customer_confirm_word": [
                        {
                            "index": 19,
                            "value": [
                                "dạ"
                            ],
                            "real_value": [
                                "dạ"
                            ]
                        }
                    ]
                }
            },
            {
                "criteria_name": "askPaymentAmount",
                "decision": "yes",
                "position_range_index": [
                    27,
                    28
                ],
                "slots": {
                    "payment_amount": [
                        {
                            "index": 27,
                            "value": [
                                "1700000"
                            ],
                            "real_value": [
                                "1700000"
                            ]
                        }
                    ],
                    "customer_confirm_word": [
                        {
                            "index": 28,
                            "value": [
                                "dạ",
                                "dạ"
                            ],
                            "real_value": [
                                "dạ",
                                "dạ"
                            ]
                        }
                    ]
                }
            }
        ]
},]

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
    elif (i["callClassifyAI"]["decision"]) == "wrong_contact":
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
            if (i["callResultAI"]["decision"]) == "willpay":
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
                elif (i["cusProvidePaymentAmount"]["decision"]) == "yes" or (i["cusProvidePaymentDatetime"]["decision"]) == "yes" or (i["cusProvidePaymentMethod"]["decision"]) == "yes":
                    result_data.append({
                        "type": "yes 10 - 1/3 cus - 0/3 agent",
                        "file_name": i["fileName"],
                        "result": "Yes_10"
                    })
                else:
                    if (i["askPaymentDatetime"]["decision"]) == "yes" and (i["askPaymentAmount"]["decision"]) == "yes" and (i["askPaymentMethod"]["decision"]) == " yes":
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