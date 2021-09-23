**Example 1: 查询执行器执行记录**



Input: 

```
tccli tat DescribeInvokerRecords --cli-unfold-argument  \
    --InvokerIds ivk-b7s3qa5l \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "0398dcea-b3de-4ec9-8e78-976191e0a94f",
        "TotalCount": 1443,
        "InvokerRecordSet": [
            {
                "InvokerId": "ivk-b7s3qa5l",
                "Reason": "start an invocation at scheduled time.",
                "InvocationId": "inv-l9l4orf1",
                "Result": "SUCCESS",
                "InvokeTime": "2021-09-06T09:33:05Z"
            },
            {
                "InvokerId": "ivk-b7s3qa5l",
                "Reason": "start an invocation at scheduled time.",
                "InvocationId": "inv-7ojgezbd",
                "Result": "SUCCESS",
                "InvokeTime": "2021-09-06T09:30:05Z"
            }
        ]
    }
}
```

