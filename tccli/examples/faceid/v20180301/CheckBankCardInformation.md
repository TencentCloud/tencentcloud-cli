**Example 1: 查询成功**

查询成功

Input: 

```
tccli faceid CheckBankCardInformation --cli-unfold-argument  \
    --BankCard xxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "查询成功",
        "AccountBank": "中国工商银行",
        "AccountType": 1,
        "RequestId": "8695c53f-776f-4ff5-a66d-84e67b352d20"
    }
}
```

