**Example 1: QueryOpenBankUnbindExternalSubMerchantBankAccount**



Input: 

```
tccli cpdp QueryOpenBankUnbindExternalSubMerchantBankAccount --cli-unfold-argument  \
    --ChannelApplyId AID12345678 \
    --ChannelMerchantId CM12345678 \
    --ChannelSubMerchantId CM12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "b8a55ef5-05c0-4e90-981f-e5117a6f8918",
        "Result": {
            "ChannelApplyId": "AID12345678",
            "UnbindStatus": "SUCCESS",
            "UnbindMessage": "success"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

