**Example 1: QueryTransferResult**



Input: 

```
tccli cpdp QueryTransferResult --cli-unfold-argument  \
    --OrderId xx \
    --MerchantId xx \
    --TransferType 1 \
    --TradeSerialNo xx \
    --MerchantAppId xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "OrderId": "xx",
            "Remark": "xx",
            "TradeStatus": 0,
            "TradeSerialNo": "xx"
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

