**Example 1: QueryOpenBankExternalSubMerchantBankAccount**



Input: 

```
tccli cpdp QueryOpenBankExternalSubMerchantBankAccount --cli-unfold-argument  \
    --ChannelMerchantId CM12345678 \
    --ChannelName TENPAY \
    --ChannelSubMerchantId CM12345678 \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "be5be48b-3ae6-4619-98a5-6e7235b73b5f",
        "Result": {
            "AccountList": [
                {
                    "AccountBank": "COMM",
                    "BindSerialNo": "12345678",
                    "AccountType": "COLLECT_MONEY",
                    "BankBranchId": "12345678",
                    "AccountNumberLastFour": "4940"
                }
            ]
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

