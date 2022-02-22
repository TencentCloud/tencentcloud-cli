**Example 1: CreateOpenBankMerchant**



Input: 

```
tccli cpdp CreateOpenBankMerchant --cli-unfold-argument  \
    --ChannelName TENPAY \
    --ExternalMerchantInfo {"PlatformCode":"12345678","PlatformName":"平台名称","PlatformPublicKey":"PlatformPublicKey","PlatformPrivateKey":"PlatformPrivateKey","PlatformCertSerialNo":"12345678","ThirdPublicKey":"ThirdPublicKey","ThirdCertSerialNo":"12345678"} \
    --OutMerchantDescription 测试 \
    --OutMerchantId test_20220218 \
    --OutMerchantName 测试 \
    --OutMerchantShortName 测试
```

Output: 
```
{
    "Response": {
        "RequestId": "85515359-a2ca-4f57-b782-62ed91fa2a6d",
        "Result": {
            "ChannelMerchantId": "CM12345678"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

