**Example 1: CreateBatchPayment**



Input: 

```
tccli cpdp CreateBatchPayment --cli-unfold-argument  \
    --RecipientList.0.OrderId xx \
    --RecipientList.0.Remark xx \
    --RecipientList.0.TransferAmount 0 \
    --RecipientList.0.AnchorName xx \
    --RecipientList.0.Uid xx \
    --RecipientList.0.AnchorId xx \
    --RecipientList.0.ReqReserved xx \
    --NotifyUrl xx \
    --TransferType 0 \
    --ReqReserved xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "BatchId": "xx",
            "BatchInfoList": [
                {
                    "OrderId": "xx",
                    "Status": 0,
                    "AgentId": "xx",
                    "TradeSerialNo": "xx",
                    "AgentName": "xx",
                    "StatusDesc": "xx"
                }
            ]
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

