**Example 1: BindOpenBankExternalSubMerchantBankAccount**



Input: 

```
tccli cpdp BindOpenBankExternalSubMerchantBankAccount --cli-unfold-argument  \
    --ChannelMerchantId CM12345678 \
    --ChannelName TENPAY \
    --ChannelSubMerchantId CM12345678 \
    --ExternalSubMerchantBindBankAccountData {"AccountBank":"COMM","AccountName":"测试","AccountNumber":"12345678","AccountType":"COLLECT_MONEY","BankBranchId":"12345678"} \
    --OutApplyId 202102181633 \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "93888c91-f4cd-45d0-9bb5-71ad1ee06fb1",
        "Result": {
            "ChannelApplyId": "AID580433254176370688",
            "BindStatus": "SUCCESS",
            "BindMessage": "success",
            "BindSerialNo": null,
            "ExternalSubMerchantBankAccountReturnData": "{}"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

