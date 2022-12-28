**Example 1: 修改收款用户资金账号信息**



Input: 

```
tccli cpdp ModifyFlexFundingAccount --cli-unfold-argument  \
    --PayeeId 1529657731805986816 \
    --FundingAccountBindSerialNo 1529657731805986816 \
    --FundingAccountType PINGAN_BANK \
    --FundingAccountName 张三 \
    --FundingAccountNo 632xxxxxxxx123 \
    --BankBranchName 中国平安银行xx支行 \
    --PhoneNo 134xxx1234
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": null,
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

