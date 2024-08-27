data = [{
    "fileName": "",
    "agentChannel": 1,
    "time_load_info": 0.004248142242431641,
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
    "askTotalAmount": {
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
    "criterias_order": []
}]


result_amount = []

for i in data:
    slot_PaymentAmount = i['askPaymentAmount']['slots']
    slot_TotalAmount = i['askTotalAmount']['slots']
    if 'amount' in slot_PaymentAmount and 'customer_confirm_word' in slot_PaymentAmount:
        result_amount.append({
            "case": "1",
            "file_name": i["fileName"],
            "result": "Yes"
        })
        break
    elif 'amt_credit_limit_word' in slot_TotalAmount and 'amt_credit_limit' in slot_TotalAmount:
        result_amount.append({
            "case": "2",
            "file_name": i["fileName"],
            "result": "Yes"
        })
        break
    elif 'amt_credit_limit_word' in slot_TotalAmount or 'amt_credit_limit' in slot_TotalAmount:
        result_amount.append({
            "case": "3",
            "file_name": i["fileName"],
            "result": "partially"
        })
        break
    else:
        result_amount.append({
            "case": "4",
            "file_name": i["fileName"],
            "result": "No"
        })
print(f"kết quả: {result_amount}")