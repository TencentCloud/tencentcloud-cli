**Example 1: 正常示例**



Input: 

```
tccli cpdp CreateOpenBankSingleSubMerchant --cli-unfold-argument  \
    --ChannelMerchantId 12345678 \
    --OutSubMerchantId sub_test_20220218 \
    --OutSubMerchantName 测试 \
    --OutSubMerchantShortName 测试
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "ChannelSubMerchantId": "CM12345678"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

