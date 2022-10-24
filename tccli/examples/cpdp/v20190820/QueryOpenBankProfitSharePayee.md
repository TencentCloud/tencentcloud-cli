**Example 1: 正常返回**



Input: 

```
tccli cpdp QueryOpenBankProfitSharePayee --cli-unfold-argument  \
    --ChannelMerchantId CM635846524835979264 \
    --ChannelSubMerchantId CM615222155219103744 \
    --AccountId test2222 \
    --AccountNo  \
    --Currency USD \
    --Environment sandbox
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

**Example 2: 系统未知异常**



Input: 

```
tccli cpdp QueryOpenBankProfitSharePayee --cli-unfold-argument  \
    --AccountNo 字符串 \
    --ChannelMerchantId 字符串 \
    --Environment 字符串 \
    --Currency 字符串 \
    --ChannelSubMerchantId 字符串 \
    --AccountId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "8a70f9f5-a90a-4bd8-85d9-8d7eabba7783",
        "Result": null,
        "ErrCode": "FailedOperation.SystemError",
        "ErrMessage": "系统未知异常"
    }
}
```

