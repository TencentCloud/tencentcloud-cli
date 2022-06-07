**Example 1: 提现**



Input: 

```
tccli cpdp ApplyFlexPayment --cli-unfold-argument  \
    --Remark 字符串 \
    --FundingAccountInfo.FundingAccountType 字符串 \
    --FundingAccountInfo.FundingAccountNo 字符串 \
    --FundingAccountInfo.FundingAccountBindSerialNo 字符串 \
    --AmountBeforeTax 字符串 \
    --OutOrderId 字符串 \
    --IncomeType 字符串 \
    --PayeeId 字符串
```

Output: 
```
{
    "Response": {
        "ErrCode": "COMMON.INVALID_PARAMETER",
        "ErrMessage": "参数错误:收入类型不规范, 可选范围[LABOR, OCCASION],",
        "Result": null,
        "RequestId": "55e276c9-2c82-4777-b141-a0d4fc6ab475"
    }
}
```

