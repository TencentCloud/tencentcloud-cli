**Example 1: 查询账户收支明细**



Input: 

```
tccli billing DescribeBillList --cli-unfold-argument  \
    --StartTime '2019-07-31 00:00:00'\
    --EndTime '2020-07-31 00:00:00'\
    --Offset 0\
    --Limit 1\
    --PayType all\
    --SubPayType all\
    --WithZeroAmount 1
```

Output: 
```
{
    "Response": {
        "Total": 39,
        "ReturnAmount": 9667,
        "DeductAmount": -7057155,
        "RechargeAmount": 2247483647,
        "BlockAmount": -5130854,
        "UnblockAmount": 10000,
        "TransactionList": [
            {
                "OperationTime": "2020-07-08 15:52:30.941",
                "ActionType": "deduct",
                "PayChannel": "用户余额",
                "OperationInfo": "OCR文字识别-广州-07月按月结算扣费",
                "Amount": -45,
                "Balance": 1951932174,
                "BillId": "20200708000000005009170242661921",
                "Cash": 1957274510,
                "Incentive": 0,
                "Freezing": 5342336,
                "DeductMode": "hourm"
            }
        ],
        "RequestId": "d40b48bf-6755-4128-910b-b54f8b9df6c3"
    }
}
```
