**Example 1: 退款成功**

退款成功

Input: 

```
tccli cpdp RefundOpenBankOrder --cli-unfold-argument  \
    --Remark xx \
    --RefundAmount 0 \
    --ChannelOrderId xx \
    --NotifyUrl xx \
    --OutRefundId xx \
    --RefundReason xx \
    --ChannelMerchantId xx \
    --OutOrderId xx \
    --ExternalRefundData xx
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "ChannelOrderId": "xx",
            "RefundAmount": 0,
            "OutRefundId": "xx",
            "OutOrderId": "xx",
            "ChannelRefundId": "xx",
            "RefundMessage": "xx"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 2: 订单不存在**



Input: 

```
tccli cpdp RefundOpenBankOrder --cli-unfold-argument  \
    --Remark 字符串 \
    --ChannelOrderId 字符串 \
    --RefundAmount 1 \
    --NotifyUrl 字符串 \
    --OutRefundId 字符串 \
    --RefundReason 字符串 \
    --ChannelMerchantId 字符串 \
    --OutOrderId 字符串 \
    --ExternalRefundData 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "46d39578-875e-47d6-b4a7-4f2895cbbaf2",
        "Result": null,
        "ErrCode": "ORDER.RECORD_NOT_EXIST",
        "ErrMessage": "该笔订单字符串不存在"
    }
}
```

