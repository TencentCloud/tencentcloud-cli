**Example 1: QueryOpenBankExternalSubMerchantRegistration**



Input: 

```
tccli cpdp QueryOpenBankExternalSubMerchantRegistration --cli-unfold-argument  \
    --ChannelMerchantId CM12345678 \
    --ChannelRegistrationNo R12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "68359316-3032-4f5d-91b6-c628eb2ba378",
        "Result": {
            "RegistrationStatus": "SUCCESS",
            "RegistrationMessage": "success",
            "ChannelRegistrationNo": "R12345678",
            "ChannelSubMerchantId": "CM12345678",
            "OutSubMerchantName": "测试",
            "ChannelName": "TENPAY",
            "PaymentMethod": "EBANK_PAYMENT",
            "BusinessLicenseNumber": "12345678",
            "LegalName": "测试",
            "ExternalReturnData": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

