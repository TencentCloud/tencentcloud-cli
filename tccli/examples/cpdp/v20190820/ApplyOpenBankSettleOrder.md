**Example 1: 正常返回**



Input: 

```
tccli cpdp ApplyOpenBankSettleOrder --cli-unfold-argument  \
    --ChannelMerchantId CM635846524835979264 \
    --ChannelName HELIPAY \
    --ChannelSubMerchantId CM615222155219103744 \
    --OutSettleId test21212328671312312120361 \
    --SettleAmount 5000
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "Result": null,
        "ErrCode": "COMMON.SYSTEM_DISABLED",
        "ErrMessage": ""
    }
}
```

**Example 2: 商户信息不存在**



Input: 

```
tccli cpdp ApplyOpenBankSettleOrder --cli-unfold-argument  \
    --Remark 字符串 \
    --SettleDetail 字符串 \
    --NotifyUrl 字符串 \
    --ChannelMerchantId CM635846524835979264 \
    --Environment 字符串 \
    --SettleAmount 5000 \
    --ChannelSubMerchantId CM615222155219103744 \
    --OutSettleId test2121232867131231212221 \
    --ExternalSettleData 字符串 \
    --ChannelName HELIPAY
```

Output: 
```
{
    "Response": {
        "RequestId": "3c3f9260-16f5-4728-b9f6-07d9a031fa7d",
        "Result": null,
        "ErrCode": "MERCHANT.INVALID_PARAMETER",
        "ErrMessage": "渠道商户信息不存在，请检查参数是否正确"
    }
}
```

