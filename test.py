data = [     {
        "fileName": "007c035a72028426.mp3",
        "agentChannel": 2,
        "time_load_info": 0.0034716129302978516,
        "agentIntroduce": {
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
            "task": "compare_beta"
        },
        "companyName": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "no"
            },
            "decision_position": [
                {
                    "index": 2,
                    "channel": 2,
                    "text": "xin phép hỗ trợ nha bên home credit việt nam á chị anh lê hữu vợ đúng không",
                    "intents": [],
                    "entities": {
                        "company_name": [
                            {
                                "start": 24,
                                "end": 35,
                                "value": "home credit",
                                "real_value": "home credit",
                                "entity": "company_name",
                                "subentities": "None",
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 1.0,
                    "intent_score": 0.0,
                    "confidence_criteria": 1.0
                },
                {
                    "index": 4,
                    "channel": 2,
                    "text": "dạ đánh giá năng cao thất nghiệp vụ cuộc gọi ghi đảm bảo với công ty trao đổi anh vợ tháng này 1 chút nha em liên hệ hỗ trợ đợt kế tiếp theo mình có đang vay vốn bên home credit anh",
                    "intents": [],
                    "entities": {
                        "company_name": [
                            {
                                "entity": "company_name",
                                "value": "home credit",
                                "start": 166,
                                "end": 177,
                                "real_value": "home credit",
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
                    "text": "xin phép hỗ trợ nha bên home credit việt nam á chị anh lê hữu vợ đúng không",
                    "intents": [],
                    "entities": {
                        "company_name": [
                            {
                                "start": 24,
                                "end": 35,
                                "value": "home credit",
                                "real_value": "home credit",
                                "entity": "company_name",
                                "subentities": "None",
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 1.0,
                    "intent_score": 0.0,
                    "confidence_criteria": 1.0
                },
                {
                    "index": 4,
                    "channel": 2,
                    "text": "dạ đánh giá năng cao thất nghiệp vụ cuộc gọi ghi đảm bảo với công ty trao đổi anh vợ tháng này 1 chút nha em liên hệ hỗ trợ đợt kế tiếp theo mình có đang vay vốn bên home credit anh",
                    "intents": [],
                    "entities": {
                        "company_name": [
                            {
                                "entity": "company_name",
                                "value": "home credit",
                                "start": 166,
                                "end": 177,
                                "real_value": "home credit",
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
                "company_name": [
                    {
                        "index": 2,
                        "value": "home credit"
                    },
                    {
                        "index": 4,
                        "value": "home credit"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "greet": {
            "evaluate": "yes",
            "evaluate_channel": {
                "2": "yes",
                "1": "no"
            },
            "decision_position": [
                {
                    "index": 0,
                    "channel": 2,
                    "text": "alo xin chào cảm ơn giữ máy em",
                    "intents": [],
                    "entities": {
                        "greet": [
                            {
                                "entity": "greet",
                                "value": "alo",
                                "start": 0,
                                "end": 3,
                                "real_value": "alo",
                                "is_required": "required"
                            }
                        ],
                        "ciao": [
                            {
                                "entity": "ciao",
                                "value": "xin chào",
                                "start": 4,
                                "end": 12,
                                "real_value": "xin chào",
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 1.0,
                    "intent_score": 0.0,
                    "confidence_criteria": 1.0
                },
                {
                    "index": 4,
                    "channel": 2,
                    "text": "dạ đánh giá năng cao thất nghiệp vụ cuộc gọi ghi đảm bảo với công ty trao đổi anh vợ tháng này 1 chút nha em liên hệ hỗ trợ đợt kế tiếp theo mình có đang vay vốn bên home credit anh",
                    "intents": [],
                    "entities": {
                        "greet": [
                            {
                                "entity": "greet",
                                "value": "dạ",
                                "start": 0,
                                "end": 2,
                                "real_value": "dạ",
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
            "confidence": 1.0,
            "confidence_channel": {
                "2": 1.0,
                "1": 0.0
            },
            "position": [
                {
                    "index": 0,
                    "channel": 2,
                    "text": "alo xin chào cảm ơn giữ máy em",
                    "intents": [],
                    "entities": {
                        "greet": [
                            {
                                "entity": "greet",
                                "value": "alo",
                                "start": 0,
                                "end": 3,
                                "real_value": "alo",
                                "is_required": "required"
                            }
                        ],
                        "ciao": [
                            {
                                "entity": "ciao",
                                "value": "xin chào",
                                "start": 4,
                                "end": 12,
                                "real_value": "xin chào",
                                "is_required": "required"
                            }
                        ]
                    },
                    "evaluate": "yes",
                    "entities_score": 1.0,
                    "intent_score": 0.0,
                    "confidence_criteria": 1.0
                },
                {
                    "index": 4,
                    "channel": 2,
                    "text": "dạ đánh giá năng cao thất nghiệp vụ cuộc gọi ghi đảm bảo với công ty trao đổi anh vợ tháng này 1 chút nha em liên hệ hỗ trợ đợt kế tiếp theo mình có đang vay vốn bên home credit anh",
                    "intents": [],
                    "entities": {
                        "greet": [
                            {
                                "entity": "greet",
                                "value": "dạ",
                                "start": 0,
                                "end": 2,
                                "real_value": "dạ",
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
                "greet": [
                    {
                        "index": 0,
                        "value": "alo"
                    },
                    {
                        "index": 4,
                        "value": "dạ"
                    }
                ],
                "ciao": [
                    {
                        "index": 0,
                        "value": "xin chào"
                    }
                ]
            },
            "position_range_index": [],
            "position_condition": [],
            "task": "query"
        },
        "criterias_order": []
    },]
import json
#import pandas as pd
result_greeting = []

for i in data:
    if (i["agentIntroduce"]["evaluate"]) and (i["agentIntroduce"]["decision"]) == "yes" and (i["greet"]["evaluate"]) and (i["greet"]["decision"]) == "yes" and (i["companyName"]["evaluate"]) and (i["companyName"]["decision"]) == "yes":
        result_greeting.append({
            "file_name": i["fileName"],
            "result": "Yes"
            })
    elif (i["agentIntroduce"]["evaluate"]) and (i["agentIntroduce"]["decision"]) == "yes" and (i["greet"]["evaluate"]) and (i["greet"]["decision"]) == "yes":
        result_greeting.append({
            "file_name": i["fileName"],
            "result": "Yes"
            })
    elif (i["agentIntroduce"]["evaluate"]) and (i["agentIntroduce"]["decision"]) == "yes" and (i["companyName"]["evaluate"]) and (i["companyName"]["decision"]) == "yes":
        result_greeting.append({
            "file_name": i["fileName"],
            "result": "Yes"
            })
    elif (i["greet"]["evaluate"]) and (i["greet"]["decision"]) == "yes" and (i["companyName"]["evaluate"]) and (i["companyName"]["decision"]) == "yes":
        result_greeting.append({
            "file_name": i["fileName"],
            "result": "Yes"
        })
    else:
        result_greeting.append({
            "file_name": i["fileName"],
            "result": "No"
            })

print(result_greeting)