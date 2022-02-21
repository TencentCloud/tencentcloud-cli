**Example 1: CreateOpenBankExternalSubMerchantRegistration**



Input: 

```
tccli cpdp CreateOpenBankExternalSubMerchantRegistration --cli-unfold-argument  \
    --BusinessLicenseNumber 12345678 \
    --ChannelMerchantId 12345678 \
    --ChannelName TENPAY \
    --LegalName 测试 \
    --OutRegistrationNo 202102181612 \
    --OutSubMerchantId sub_test_20220218 \
    --OutSubMerchantName 测试 \
    --OutSubMerchantShortName 测试 \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "RegistrationStatus": "SUCCESS",
            "RegistrationMessage": "success",
            "ChannelRegistrationNo": "R1234567",
            "ChannelSubMerchantId": "CM12345678",
            "ExternalReturnData": null
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

