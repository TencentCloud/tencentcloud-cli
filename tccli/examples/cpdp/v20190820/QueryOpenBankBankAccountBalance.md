**Example 1: 余额查询示例**

余额查询示例

Input: 

```
tccli cpdp QueryOpenBankBankAccountBalance --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelSubMerchantId sub0001 \
    --ChannelName TENPAY \
    --PaymentMethod OPENBANK_PAYMENT \
    --BindSerialNo 123243556
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "TotalBalance": 500,
            "YesterdayBalance": 300
        }
    }
}
```

**Example 2: 查询异常示例**



Input: 

```
tccli cpdp QueryOpenBankBankAccountBalance --cli-unfold-argument  \
    --BindSerialNo 1123 \
    --ChannelMerchantId 123 \
    --Environment sandbox \
    --ChannelSubMerchantId sub123456 \
    --ChannelName TENPAY \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "f26233a4-9f61-4d4b-9279-8a8fa137861f",
        "Result": null,
        "ErrCode": "COMMON.SYSTEM_ERROR",
        "ErrMessage": "系统未知异常"
    }
}
```

