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

