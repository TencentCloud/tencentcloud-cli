**Example 1: DescribeRechargeRecords异常回参**

请求异常的情况

Input: 

```
tccli iotvideo DescribeRechargeRecords --cli-unfold-argument  \
    --Limit 0 \
    --AccountType 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "AccountType": 1,
        "Records": null
    }
}
```

**Example 2: DescribeRechargeRecords正常回参**

正常请求的情况

Input: 

```
tccli iotvideo DescribeRechargeRecords --cli-unfold-argument  \
    --Limit 0 \
    --AccountType 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e",
        "AccountType": 1,
        "Records": [
            {
                "WaterId": 919,
                "BalanceBeforeRecharge": 10367808782,
                "OperateTime": 1602764840
            },
            {
                "WaterId": 920,
                "BalanceBeforeRecharge": 10367807918,
                "OperateTime": 1602765531
            }
        ]
    }
}
```

