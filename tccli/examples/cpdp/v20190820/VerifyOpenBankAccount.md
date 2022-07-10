**Example 1: 打款验证成功**



Input: 

```
tccli cpdp VerifyOpenBankAccount --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelName TENPAY \
    --NotifyUrl http://127.0.0.1/pay/notify \
    --PayeeInfo.PayeeId test00002 \
    --PayeeInfo.PayeeName test00002 \
    --PayeeInfo.BankAccountNumber xx \
    --PayeeInfo.BindSerialNo 1212121323 \
    --PayeeInfo.BankBranchId xx \
    --PayeeInfo.BankBranchName xx \
    --PayeeInfo.AccountType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "订单提交成功",
        "Result": ""
    }
}
```

**Example 2: 调用打款验证失败**



Input: 

```
tccli cpdp VerifyOpenBankAccount --cli-unfold-argument  \
    --PayeeInfo.BankAccountNumber 字符串 \
    --PayeeInfo.BindSerialNo 1002030191514840205164 \
    --PayeeInfo.BankBranchId 字符串 \
    --PayeeInfo.BankBranchName 字符串 \
    --PayeeInfo.PayeeName 字符串 \
    --PayeeInfo.AccountType 字符串 \
    --PayeeInfo.PayeeId CM618130426611634176 \
    --ChannelName TENPAY \
    --ChannelMerchantId CM584693967762206720 \
    --NotifyUrl 字符
```

Output: 
```
{
    "Response": {
        "RequestId": "e6728d43-3418-4142-875e-ee60c1cce9c7",
        "Result": null,
        "ErrCode": "COMMON.SYSTEM_ERROR",
        "ErrMessage": "系统未知异常"
    }
}
```

