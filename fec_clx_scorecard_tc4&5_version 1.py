data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.005299091339111328,
    "agentMotivation": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes",
            "2": "yes"
        },
        "decision_position": [
            {
                "index": 4,
                "channel": 1,
                "text": "em chào anh hiệu em thúy liên hệ bên fe nè hợp đồng tín dụng nhà mình á hôm nay trễ hạn rồi anh thu xếp ra thanh toán giùm em với",
                "intents": [
                    "motivation"
                ],
                "entities": {}
            },
            {
                "index": 59,
                "channel": 1,
                "text": "ra thanh toán đi chứ để lát nữa chuyển qua bộ phận xử lý nợ rồi nha em cám ơn anh",
                "intents": [
                    "motivation"
                ],
                "entities": {}
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
                "index": 4,
                "channel": 1,
                "text": "em chào anh hiệu em thúy liên hệ bên fe nè hợp đồng tín dụng nhà mình á hôm nay trễ hạn rồi anh thu xếp ra thanh toán giùm em với",
                "intents": [
                    "motivation"
                ],
                "entities": {}
            },
            {
                "index": 59,
                "channel": 1,
                "text": "ra thanh toán đi chứ để lát nữa chuyển qua bộ phận xử lý nợ rồi nha em cám ơn anh",
                "intents": [
                    "motivation"
                ],
                "entities": {}
            }
        ],
        "slots": {},
        "position_range_index": [
            4,
            59
        ],
        "position_condition": [
            4
        ],
        "task": "lookup"
    },
    "agentQuoteRules": {
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
        "position_range_index": "null",
        "position_condition": [],
        "task": "compare"
    },
    "agentSuggestiveCustomer": {
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
    "cusCantPay": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "no",
            "1": "no"
        },
        "decision_position": [],
        "decision": "yes",
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
    "cusPayBenefitConsequence": {
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
    "cusRefuseUnfriendly": {
        "evaluate": "yes",
        "evaluate_channel": {
            "2": "no",
            "1": "no"
        },
        "decision_position": [],
        "decision": "yes",
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
    "paymentImpose": {
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
    "callClassifyAI": {
        "evaluate": "yes",
        "evaluate_channel": {
            "1": "yes"
        },
        "decision_position": [
            {
                "index": 0,
                "channel": 1,
                "text": "<agent>: alo <customer>: alo <agent>: dạ anh thấy nhiều lắm anh ơi <customer>: đúng rồi <agent>: em chào anh hiệu em thúy liên hệ bên fe nè hợp đồng tín dụng nhà mình á hôm nay trễ hạn rồi anh thu xếp ra thanh toán giùm em với <customer>: ừ <agent>: để em cầm hồ sơ 2526000 <customer>: rồi rồi rồi đang chuẩn bị đóng đang đóng đang chuẩn bị đi đóng đi <agent>: à đang chuẩn bị đi đóng <customer>: đóng đóng luôn 2 tháng em",
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
                "text": "<agent>: alo <customer>: alo <agent>: dạ anh thấy nhiều lắm anh ơi <customer>: đúng rồi <agent>: em chào anh hiệu em thúy liên hệ bên fe nè hợp đồng tín dụng nhà mình á hôm nay trễ hạn rồi anh thu xếp ra thanh toán giùm em với <customer>: ừ <agent>: để em cầm hồ sơ 2526000 <customer>: rồi rồi rồi đang chuẩn bị đóng đang đóng đang chuẩn bị đi đóng đi <agent>: à đang chuẩn bị đi đóng <customer>: đóng đóng luôn 2 tháng em",
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
                "text": "<customer>: ừ <agent>: nha anh <customer>: tháng người ta đóng rồi tháng người ta rảnh ta không đóng cũng không được nữa trời <agent>: không không không được anh <customer>: ví dụ tháng rồi không <agent>: thì anh phải để dành <customer>: xài hết tiền tiền không khả năng rồi sao <agent>: anh anh phải để dành tiền anh ra anh chuẩn bị anh đóng chứ làm sao được anh bây giờ quy định nó như vậy rồi em biết làm sao bây giờ <customer>: ủa ngộ vậy ta <customer>: trời ơi đóng trước cũng không được mà <agent>: rồi <customer>: đóng sớm cũng không được mà đóng trễ cũng không được nữa <agent>: đúng rồi cái này nó có quy định có ngày có giờ hết rồi nên anh thu xếp giùm em <customer>: kỳ vậy <agent>: ra thanh toán đi chứ để lát nữa chuyển qua bộ phận xử lý nợ rồi nha em cám ơn anh",
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
                "text": "<customer>: ừ <agent>: nha anh <customer>: tháng người ta đóng rồi tháng người ta rảnh ta không đóng cũng không được nữa trời <agent>: không không không được anh <customer>: ví dụ tháng rồi không <agent>: thì anh phải để dành <customer>: xài hết tiền tiền không khả năng rồi sao <agent>: anh anh phải để dành tiền anh ra anh chuẩn bị anh đóng chứ làm sao được anh bây giờ quy định nó như vậy rồi em biết làm sao bây giờ <customer>: ủa ngộ vậy ta <customer>: trời ơi đóng trước cũng không được mà <agent>: rồi <customer>: đóng sớm cũng không được mà đóng trễ cũng không được nữa <agent>: đúng rồi cái này nó có quy định có ngày có giờ hết rồi nên anh thu xếp giùm em <customer>: kỳ vậy <agent>: ra thanh toán đi chứ để lát nữa chuyển qua bộ phận xử lý nợ rồi nha em cám ơn anh",
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
# ghép full tiêu chí xử lí từ chối cho các trường hợp xuất hiện 2 tình huống từ chối và 1 trong 2 tình huống từ chối
result = []
for i in data:
    # đi vào nhánh ec chấm full điểm
    if (i["callClassifyAI"]["decision"]) == "ec":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối khách do rơi vào trường hợp EC"
        })
    # nếu đi vào nhánh wrongnumber thì chấm full điểm
    elif (i["callClassifyAI"]["decision"]) == "wrongnumber":
        result.append({
            "file_name": i["fileName"],
            "result": "Yes_20",
            "reason": "không có tính huống từ chối do rơi vào nhầm máy"
        })
    # đi vào nhánh silent chấm full điểm sau đấy chuyển thành N/A
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
            # truường hợp xuất hiện đồng thời 2 tình huống từ chối
            if (i["cusCantPay"]["evaluate"]) == "yes" and (i["cusCantPay"]["decision"]) == "yes" and (i["cusRefuseUnfriendly"]["evaluate"]) == "yes" and (i["cusRefuseUnfriendly"]["decision"]) == "yes":
                # xử lý từ chối do không có thiện chí thanh toán
                if (i["agentQuoteRules"]["decision"]) == "yes":
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason": "2/2 ý và có dẫn luật (call trễ hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "có nói dẫn luật nhưng k nói lợi ích hoặc hậu quả (xem lại)"
                        })
                else:
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "1/2 ý và không có dẫn luật (call trễ hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "No_Refuse",
                            "reason": "không nói dẫn luật + không nói lợi ích hoặc hậu quả"
                        })
                # xử lý từ chối do không có khả năng thanh toán
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
                    if (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentMotivation"]["decision"]) == "yes" and (i["paymentImpose"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (3/3 ý)"
                        })
                    elif (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentMotivation"]["decision"]) == "yes":
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
                    elif (i["agentMotivation"]["decision"]) and (i["paymentImpose"]["decision"]) == "yes":
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
                        "result": "No_CantPay",
                        "reason": "agent không khơi gợi khách hàng không đưa ra giải pháp"
                    })
            elif (i["cusRefuseUnfriendly"]["evaluate"]) == "yes" and (i["cusRefuseUnfriendly"]["decision"]) == "yes":
                if (i["agentQuoteRules"]["decision"]) == "yes":
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason": "2/2 ý và có dẫn luật (call trễ hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "có nói dẫn luật nhưng k nói lợi ích hoặc hậu quả (xem lại)"
                        })
                else:
                    if (i["cusPayBenefitConsequence"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_10",
                            "reason": "1/2 ý và không có dẫn luật (call trễ hạn & chưa đến hạn)"
                        })
                    else:
                        result.append({
                            "file_name": i["fileName"],
                            "result": "No",
                            "reason": "không nói dẫn luật + không nói lợi ích hoặc hậu quả"
                        })
            elif (i["cusCantPay"]["evaluate"]) == "yes" and (i["cusCantPay"]["decision"]) == "yes":
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
                    if (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentMotivation"]["decision"]) == "yes" and (i["paymentImpose"]["decision"]) == "yes":
                        result.append({
                            "file_name": i["fileName"],
                            "result": "Yes_20",
                            "reason": "tình huống từ chối - agent khơi gợi khách hàng không đưa ra giải pháp (3/3 ý)"
                        })
                    elif (i["agentQuoteSolution"]["decision"]) == "yes" and (i["agentMotivation"]["decision"]) == "yes":
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
                    elif (i["agentMotivation"]["decision"]) and (i["paymentImpose"]["decision"]) == "yes":
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