**Example 1: QueryOpenBankSubMerchantRateConfigure**



Input: 

```
tccli cpdp QueryOpenBankSubMerchantRateConfigure --cli-unfold-argument  \
    --ChannelMerchantId CM123456 \
    --ChannelSubMerchantId CM345678 \
    --ChannelRegistrationNo R123456 \
    --ChannelName HELIPAY \
    --ChannelProductFeeNo P345678
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "DealStatus": "SUCCESS",
            "DealMessage": "success"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

