**Example 1: 云企付-查询支持银行列表**

云企付-查询支持银行列表

Input: 

```
tccli cpdp QueryOpenBankSupportBankList --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelName TENPAY \
    --PaymentMethod OPENBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {}
    }
}
```

