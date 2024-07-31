'''import json
#import pandas as pd
with open ("Recommendation_output_api.json","r",encoding= "utf-8")as f:
    data = json.load(f)'''
data = [  {
        "fileName": "0094036ecb1adf60.mp3",
        "agentChannel": 1,
        "time_load_info": 0.0034503936767578125,
        "agentUnderstand": {
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
            "position_range_index": "None",
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
        "mentionHistory": {
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
        "motivationAppear": {
            "evaluate": "yes",
            "evaluate_channel": {
                "1": "yes",
                "2": "no"
            },
            "decision_position": [
                {
                    "index": 5,
                    "channel": 1,
                    "text": "em chào chị đánh giá nhằm nâng cao chất lượng dịch vụ và xin phép được ghi âm em gọi hỗ trợ hợp đồng chị đang tham gia trả góp tiền mặt sắp tới á số tiền đóng 2793000 hạn mức thanh toán ngày 21 tháng này để tránh",
                    "intents": [],
                    "entities": {
                        "motivation_result": [
                            {
                                "start": 26,
                                "end": 45,
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
                    "index": 21,
                    "channel": 1,
                    "text": "em đang hỏi là trong 4 ngày nữa 21 chị dự định thanh toán đúng hẹn trở lại được ngày nào để tránh hồ sơ này phát sinh lãi",
                    "intents": [],
                    "entities": {
                        "motivation_title": [
                            {
                                "start": 92,
                                "end": 121,
                                "value": "tránh hồ sơ này phát sinh lãi",
                                "real_value": "tránh hồ sơ này phát sinh lãi",
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
                    "index": 23,
                    "channel": 1,
                    "text": "rồi vậy thì em mong tháng này chị báo đúng ngày thì đúng ngày 21 công ty bên em nhận được tiền nha đừng báo đúng ngày lại tiếp tục đóng trễ nha chị tháng này tiền về trễ sau hạn thanh toán 21 có thể chị phải đóng kèm lãi quá hạn cho công ty chị thủy nha nên em mong tháng này bên em đã nhắc trước không lấy lý do chị báo quên đóng trễ nha",
                    "intents": [],
                    "entities": {
                        "motivation_result": [
                            {
                                "start": 208,
                                "end": 228,
                                "value": "đóng kèm lãi quá hạn",
                                "real_value": "đóng kèm lãi quá hạn",
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
                }
            ],
            "decision": "yes",
            "confidence": 0.5,
            "confidence_channel": {
                "1": 0.5,
                "2": 0.0
            },
            "position": [
                {
                    "index": 5,
                    "channel": 1,
                    "text": "em chào chị đánh giá nhằm nâng cao chất lượng dịch vụ và xin phép được ghi âm em gọi hỗ trợ hợp đồng chị đang tham gia trả góp tiền mặt sắp tới á số tiền đóng 2793000 hạn mức thanh toán ngày 21 tháng này để tránh",
                    "intents": [],
                    "entities": {
                        "motivation_result": [
                            {
                                "start": 26,
                                "end": 45,
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
                    "index": 21,
                    "channel": 1,
                    "text": "em đang hỏi là trong 4 ngày nữa 21 chị dự định thanh toán đúng hẹn trở lại được ngày nào để tránh hồ sơ này phát sinh lãi",
                    "intents": [],
                    "entities": {
                        "motivation_title": [
                            {
                                "start": 92,
                                "end": 121,
                                "value": "tránh hồ sơ này phát sinh lãi",
                                "real_value": "tránh hồ sơ này phát sinh lãi",
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
                    "index": 23,
                    "channel": 1,
                    "text": "rồi vậy thì em mong tháng này chị báo đúng ngày thì đúng ngày 21 công ty bên em nhận được tiền nha đừng báo đúng ngày lại tiếp tục đóng trễ nha chị tháng này tiền về trễ sau hạn thanh toán 21 có thể chị phải đóng kèm lãi quá hạn cho công ty chị thủy nha nên em mong tháng này bên em đã nhắc trước không lấy lý do chị báo quên đóng trễ nha",
                    "intents": [],
                    "entities": {
                        "motivation_result": [
                            {
                                "start": 208,
                                "end": 228,
                                "value": "đóng kèm lãi quá hạn",
                                "real_value": "đóng kèm lãi quá hạn",
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
                }
            ],
            "slots": {
                "motivation_result": [
                    {
                        "index": 5,
                        "value": "nâng cao chất lượng"
                    },
                    {
                        "index": 23,
                        "value": "đóng kèm lãi quá hạn"
                    }
                ],
                "motivation_title": [
                    {
                        "index": 21,
                        "value": "tránh hồ sơ này phát sinh lãi"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "criterias_order": []
    },]

result_recommentdation = []
for i in data:
    if (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    if (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    if (i["mentionHistory"]["decision"]) == "yes" and (i["agentUnderstand"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    if (i["mentionHistory"]["decision"] )== "yes" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    if (i["mentionHistory"]["decision"]) == "no" and (i["dueDateMention"]["decision"]) == "yes" and (i["motivationAppear"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    if (i["mentionHistory"]["decision"]) == "no" and (i["dueDateMention"]["decision"]) == "yes" and (i["askPaymentReceipt"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    if (i["mentionHistory"]["decision"]) == "no" and (i["dueDateMention"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    if (i["mentionHistory"]["decision"]) == "no" and (i["askPaymentReceipt"]["decision"]) == "yes":
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "Partially"
        })
    else:
        result_recommentdation.append({
            "file_name": i["fileName"],
            "result": "No"
        })
count = len(result_recommentdation)
print(f"count: {count}")
print(f"Result: {result_recommentdation}")