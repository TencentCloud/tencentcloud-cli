**Example 1: QueryBatchPaymentResult**



Input: 

```
tccli cpdp QueryBatchPaymentResult --cli-unfold-argument  \
    --BatchId xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "Remark": "xx",
            "TransferType": 0,
            "TransferInfoList": [
                {
                    "OrderId": "xx",
                    "Status": 0,
                    "TransferAmount": 0,
                    "StatusDesc": "SUCCESS",
                    "AgentName": "xx",
                    "AgentId": "xx"
                }
            ],
            "BatchId": "xx",
            "TotalCount": 0,
            "TotalAmount": 0,
            "ReqReserved": "xx"
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

