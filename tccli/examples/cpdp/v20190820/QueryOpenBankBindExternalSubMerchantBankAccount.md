**Example 1: QueryOpenBankBindExternalSubMerchantBankAccount**



Input: 

```
tccli cpdp QueryOpenBankBindExternalSubMerchantBankAccount --cli-unfold-argument  \
    --ChannelApplyId AID12345678 \
    --ChannelMerchantId CM12345678 \
    --ChannelSubMerchantId CM12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "d69a4d94-c402-40c6-94da-70b6f32a3c0c",
        "Result": {
            "ChannelApplyId": "AID12345678",
            "BindStatus": "SUCCESS",
            "BindMessage": "success",
            "BindSerialNo": "",
            "ExternalSubMerchantBankAccountReturnData": "{\"AccountBank\":\"COMM\",\"AccountNumberLastFour\":\"\",\"AccountType\":\"COLLECT_MONEY\",\"BankBranchId\":\"12345678\"}"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

