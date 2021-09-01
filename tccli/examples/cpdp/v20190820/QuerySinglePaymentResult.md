**Example 1: QuerySinglePaymentResult**



Input: 

```
tccli cpdp QuerySinglePaymentResult --cli-unfold-argument  \
    --OrderId xx \
    --TransferType 0 \
    --TradeSerialNo xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "OrderId": "xx",
            "Remark": "xx",
            "AgentId": "xx",
            "TradeSerialNo": "xx",
            "AgentName": "xx",
            "TradeStatus": 0
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

