**Example 1: CreateSinglePayment**



Input: 

```
tccli cpdp CreateSinglePayment --cli-unfold-argument  \
    --OrderId xx \
    --Remark xx \
    --TransferAmount 1 \
    --AnchorId xx \
    --TransferType 1 \
    --NotifyUrl xx \
    --Uid xx \
    --AnchorName xx \
    --ReqReserved xx
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "TradeSerialNo": "xx"
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

