data = [{
    "fileName": "",
    "agentChannel": 2,
    "time_load_info": 0.004159212112426758,
    "askPaymentDatetime": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "yes",
            "1": "yes"
        },
        "decision_position": [
            [
                {
                    "index": 22,
                    "channel": 2,
                    "text": "tháng chị đóng vào ngày 29 là trễ 1 ngày á chị nhi hợp đồng là ngày 28 nha chị",
                    "intents": [
                        "ask_payment_info"
                    ],
                    "entities": {
                        "payment_datetime": [
                            {
                                "start": 19,
                                "end": 26,
                                "value": "ngày 29",
                                "real_value": "ngày 29",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            },
                            {
                                "start": 63,
                                "end": 70,
                                "value": "ngày 28",
                                "real_value": "ngày 28",
                                "entity": "payment_datetime",
                                "subentities": [],
                                "is_required": "required"
                            }
                        ]
                    }
                },
                {
                    "index": 25,
                    "channel": 1,
                    "text": "còn chị còn để coi",
                    "intents": [
                        "customer_willpay"
                    ],
                    "entities": {}
                }
            ],
            [
                {
                    "index": 7,
                    "channel": 1,
                    "text": "ngày mai",
                    "intents": [
                        "customer_willpay"
                    ],
                    "entities": {
                        "customer_datetime": [
                            {
                                "start": 0,
                                "end": 8,
                                "value": "ngày mai",
                                "real_value": "ngày mai",
                                "entity": "customer_datetime",
                                "subentities": [],
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
            "2": 1.0,
            "1": 1.0
        },
        "position": [
            {
                "index": 22,
                "channel": 2,
                "text": "tháng chị đóng vào ngày 29 là trễ 1 ngày á chị nhi hợp đồng là ngày 28 nha chị",
                "intents": [
                    "ask_payment_info"
                ],
                "entities": {
                    "payment_datetime": [
                        {
                            "start": 19,
                            "end": 26,
                            "value": "ngày 29",
                            "real_value": "ngày 29",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        },
                        {
                            "start": 63,
                            "end": 70,
                            "value": "ngày 28",
                            "real_value": "ngày 28",
                            "entity": "payment_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            },
            {
                "index": 25,
                "channel": 1,
                "text": "còn chị còn để coi",
                "intents": [
                    "customer_willpay"
                ],
                "entities": {}
            },
            {
                "index": 7,
                "channel": 1,
                "text": "ngày mai",
                "intents": [
                    "customer_willpay"
                ],
                "entities": {
                    "customer_datetime": [
                        {
                            "start": 0,
                            "end": 8,
                            "value": "ngày mai",
                            "real_value": "ngày mai",
                            "entity": "customer_datetime",
                            "subentities": [],
                            "is_required": "required"
                        }
                    ]
                }
            }
        ],
        "slots": {
            "payment_datetime": [
                {
                    "index": 22,
                    "value": [
                        "ngày 29",
                        "ngày 28"
                    ]
                }
            ],
            "customer_datetime": [
                {
                    "index": 7,
                    "value": [
                        "ngày mai"
                    ]
                }
            ]
        },
        "task": "compare_beta"
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
                "text": "<agent>: xin chào em cần cám ơn đợi máy xin phép tiếp tục hỗ trợ thông tin nha gọi bên home credit là chị phạm thị thanh nhi nghe máy đúng không chị <customer>: dạ <agent>: chị là chị nhi hả <customer>: ừ <agent>: chào chị nhi để đánh giá nâng cao chất lượng dịch vụ cuộc gọi được ghi âm lại nha chị nhi em đang thông báo kỳ góp cuối cùng hợp đồng của chị mua máy điều hòa trả góp đến hạn thanh toán ngày 28 là 671000 đảm bảo quyền lợi lợi về sau cũng như là tránh phát sinh thêm tiền phí phạt á chị nhiên góp được ngày nào sớm trước 28 giờ <customer>: rồi <agent>: lâu lâu <customer>: ngày mai <agent>: cám ơn chị hợp đồng của chị em thấy những kỳ lúc trước chị đang đóng rất là tốt nhưng mà có tháng là tháng 8 chị đóng ngày 29 có trễ 1 ngày nên công ty mới thông báo sớm hỗ trợ đóng đúng cải thiện lại lịch sử tín dụng và tránh rủi ro hợp đồng về sau á tháng là có gặp khó khăn gì không mà mình góp trễ ngày vậy chị nhi <customer>: à chị đi a <agent>: công ty á <customer>: đi đi chơi á xong rồi quên <agent>: dạ em hiểu nếu như mà sau này mình sợ quên á chị mình có thể cài đặt trong điện thoại để mà nhắc ngày mình đi thanh toán giùm em nha còn ở đây à dạ <customer>: nó cứ rồi á <agent>: dạ <customer>: không công ty có nhắn tin rồi <agent>: dạ dạ <customer>: chị nhớ <agent>: nhưng mà dạ nhưng mà tháng vẫn quên ngày rất là tiếc nha chị nhi tại vì hợp đồng mình mua trả góp á là mình phải dựa vào uy tín và trách nhiệm <customer>: đúng <agent>: dạ <customer>: tháng chị đóng đúng mà đâu có quên đâu <agent>: tháng chị đóng vào ngày 29 là trễ 1 ngày á chị nhi hợp đồng là ngày 28 nha chị <customer>: tháng đóng trễ anh tâm <agent>: cái này dạ đúng rồi chị còn giữ cái biên lai đó không <customer>: còn chị còn để coi <agent>: chị mở à chị mở lại cái biên lai kiểm tra lại giùm em nha tại vì bên em có nhận tiền trễ cho nên mới gọi ra báo cho chị do là tháng cuối cùng á bên em sẽ đánh giá lại toàn bộ cái khả năng chi trả của mình trong 6 tháng qua là dựa trên kỳ góp cuối <customer>: ừ <agent>: cho nên là cố gắng đóng tốt để hồ sơ mình được cập nhật lại nha sau này có uy tín trách nhiệm á mình đi vay đi mua dịch vụ <customer>: ok rồi rồi <agent>: dễ dàng cho hợp đồng tại vì tránh đóng trễ có thể là phát sinh thêm tiền lãi phạt ảnh hưởng đến tài chính về sau tiền góp là 671000 nha chị nhi <customer>: rồi rồi rồi <agent>: cám ơn chị nhi đóng tiền ở cửa hàng hay là chị chuyển qua app dạ <customer>: đâu đóng tiền cửa hàng không à <agent>: cám ơn chị đóng tiền xong nhớ giữ lại biên lai thu tiền giùm em nha tránh sai sót bên em liên hệ lại kiểm tra <customer>: rồi <agent>: em ghi nhận hợp đồng trong ngày mai 27 chị nhi đóng 671000 qua cửa hàng chị cấp cứu sắp xếp đóng sớm trước 28 để nhận các khoản vay ưu đãi tránh đóng tiền trễ phát sinh lãi ảnh hưởng lịch sử tín dụng nha chị cám ơn dạ xin chào",
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
                "text": "<agent>: xin chào em cần cám ơn đợi máy xin phép tiếp tục hỗ trợ thông tin nha gọi bên home credit là chị phạm thị thanh nhi nghe máy đúng không chị <customer>: dạ <agent>: chị là chị nhi hả <customer>: ừ <agent>: chào chị nhi để đánh giá nâng cao chất lượng dịch vụ cuộc gọi được ghi âm lại nha chị nhi em đang thông báo kỳ góp cuối cùng hợp đồng của chị mua máy điều hòa trả góp đến hạn thanh toán ngày 28 là 671000 đảm bảo quyền lợi lợi về sau cũng như là tránh phát sinh thêm tiền phí phạt á chị nhiên góp được ngày nào sớm trước 28 giờ <customer>: rồi <agent>: lâu lâu <customer>: ngày mai <agent>: cám ơn chị hợp đồng của chị em thấy những kỳ lúc trước chị đang đóng rất là tốt nhưng mà có tháng là tháng 8 chị đóng ngày 29 có trễ 1 ngày nên công ty mới thông báo sớm hỗ trợ đóng đúng cải thiện lại lịch sử tín dụng và tránh rủi ro hợp đồng về sau á tháng là có gặp khó khăn gì không mà mình góp trễ ngày vậy chị nhi <customer>: à chị đi a <agent>: công ty á <customer>: đi đi chơi á xong rồi quên <agent>: dạ em hiểu nếu như mà sau này mình sợ quên á chị mình có thể cài đặt trong điện thoại để mà nhắc ngày mình đi thanh toán giùm em nha còn ở đây à dạ <customer>: nó cứ rồi á <agent>: dạ <customer>: không công ty có nhắn tin rồi <agent>: dạ dạ <customer>: chị nhớ <agent>: nhưng mà dạ nhưng mà tháng vẫn quên ngày rất là tiếc nha chị nhi tại vì hợp đồng mình mua trả góp á là mình phải dựa vào uy tín và trách nhiệm <customer>: đúng <agent>: dạ <customer>: tháng chị đóng đúng mà đâu có quên đâu <agent>: tháng chị đóng vào ngày 29 là trễ 1 ngày á chị nhi hợp đồng là ngày 28 nha chị <customer>: tháng đóng trễ anh tâm <agent>: cái này dạ đúng rồi chị còn giữ cái biên lai đó không <customer>: còn chị còn để coi <agent>: chị mở à chị mở lại cái biên lai kiểm tra lại giùm em nha tại vì bên em có nhận tiền trễ cho nên mới gọi ra báo cho chị do là tháng cuối cùng á bên em sẽ đánh giá lại toàn bộ cái khả năng chi trả của mình trong 6 tháng qua là dựa trên kỳ góp cuối <customer>: ừ <agent>: cho nên là cố gắng đóng tốt để hồ sơ mình được cập nhật lại nha sau này có uy tín trách nhiệm á mình đi vay đi mua dịch vụ <customer>: ok rồi rồi <agent>: dễ dàng cho hợp đồng tại vì tránh đóng trễ có thể là phát sinh thêm tiền lãi phạt ảnh hưởng đến tài chính về sau tiền góp là 671000 nha chị nhi <customer>: rồi rồi rồi <agent>: cám ơn chị nhi đóng tiền ở cửa hàng hay là chị chuyển qua app dạ <customer>: đâu đóng tiền cửa hàng không à <agent>: cám ơn chị đóng tiền xong nhớ giữ lại biên lai thu tiền giùm em nha tránh sai sót bên em liên hệ lại kiểm tra <customer>: rồi <agent>: em ghi nhận hợp đồng trong ngày mai 27 chị nhi đóng 671000 qua cửa hàng chị cấp cứu sắp xếp đóng sớm trước 28 để nhận các khoản vay ưu đãi tránh đóng tiền trễ phát sinh lãi ảnh hưởng lịch sử tín dụng nha chị cám ơn dạ xin chào",
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
    "criterias_order": []
}]

result_Date = []
for i in data:
    if (i["askPaymentDatetime"]["evaluate"]) and (i["askPaymentDatetime"]["decision"]) == "yes":
        result_Date.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    else:
        result_Date.append({
            "file_name": i["fileName"],
            "result": "No"
        })
print(f"kết quả {result_Date}")