**Example 1: CreateOpenBankSubMerchantRateConfigure**



Input: 

```
tccli cpdp CreateOpenBankSubMerchantRateConfigure --cli-unfold-argument  \
    --ChannelRegistrationNo R123456 \
    --OutProductFeeNo P123456 \
    --ChannelMerchantId CM1234567 \
    --ChannelSubMerchantId CM456789 \
    --ChannelName HELIPAY \
    --PayType SDK \
    --PayChannel WXPAY \
    --FeeMode SINGLE \
    --FeeValue 24 \
    --MinFee 1 \
    --MaxFee 2 \
    --NotifyUrl http://xxx.com \
    --FeeRangeList.0.RangeStartValue 1 \
    --FeeRangeList.0.MaxFee 1 \
    --FeeRangeList.0.RangeFeeMode SINGLE \
    --FeeRangeList.0.RangeEndValue 1 \
    --FeeRangeList.0.MinFee 1 \
    --FeeRangeList.0.CardType DEBIT \
    --FeeRangeList.0.FeeValue 1
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "DealStatus": "SUCCESS",
            "DealMessage": "success",
            "ChannelProductFeeNo": "R1234567"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

