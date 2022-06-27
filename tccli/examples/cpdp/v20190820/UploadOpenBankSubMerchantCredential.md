**Example 1: 正常返回**



Input: 

```
tccli cpdp UploadOpenBankSubMerchantCredential --cli-unfold-argument  \
    --ChannelMerchantId 123456 \
    --ChannelSubMerchantId 1234567 \
    --ChannelName HELIPAY \
    --OutApplyId R6152221530716200192 \
    --CredentialType 011 \
    --FileType jpg \
    --CredentialUrl http://xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "948948503842433243",
        "Result": {
            "UploadStatus": "SUCCESS",
            "UploadMessage": null,
            "ChannelApplyId": "CID6181264040260xxxxx"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

