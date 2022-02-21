**Example 1: UnbindOpenBankExternalSubMerchantBankAccount**



Input: 

```
tccli cpdp UnbindOpenBankExternalSubMerchantBankAccount --cli-unfold-argument  \
    --BindSerialNo 1234567 \
    --ChannelMerchantId CM12345678 \
    --ChannelName TENPAY \
    --ChannelSubMerchantId CM12345678 \
    --OutApplyId 202102181646 \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "89d31240-a4c9-45c2-9273-e7c58b62a847",
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

