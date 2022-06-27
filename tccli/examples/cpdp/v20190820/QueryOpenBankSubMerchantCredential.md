**Example 1: 正常返回**



Input: 

```
tccli cpdp QueryOpenBankSubMerchantCredential --cli-unfold-argument  \
    --ChannelMerchantId 123456 \
    --ChannelSubMerchantId 1234567 \
    --ChannelName HELIPAY \
    --OutApplyId R6152221530716200192
```

Output: 
```
{
    "Response": {
        "RequestId": "948948503842433243",
        "Result": {
            "UploadStatus": "SUCCESS",
            "UploadMessage": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

