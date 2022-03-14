**Example 1: 云企付-查询联行号**

余额查询示例

Input: 

```
tccli cpdp QueryOpenBankBankBranchList --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelName TENPAY \
    --PaymentMethod OPENBANK_PAYMENT \
    --BankBranchName 工商银行 \
    --BankAbbreviation ICBC \
    --PageNumber.Count 50 \
    --PageNumber.Index 1
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "Count": 1
        }
    }
}
```

