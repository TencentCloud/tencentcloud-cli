**Example 1: 正常返回**



Input: 

```
tccli cpdp CreateOnlineOpenBankSingleSubMerchant --cli-unfold-argument  \
    --ChannelMerchantId 12345678 \
    --ChannelName TENPAY \
    --OutRegistrationNo 202102181612 \
    --ChannelSubMerchantId CM9889877444 \
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

