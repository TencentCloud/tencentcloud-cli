**Example 1: 商户新增正常返回**

正确输入返回的场景

Input: 

```
tccli cpdp CreatePayMerchant --cli-unfold-argument  \
    --ChannelCheckFlag 0 \
    --ChannelMerchantNo 1023459381 \
    --PlatformCode 2928394059 \
    --MerchantName 测试商户
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "MerchantAppId": "1c6f41570498301d85fc4589a5435b54"
    }
}
```

