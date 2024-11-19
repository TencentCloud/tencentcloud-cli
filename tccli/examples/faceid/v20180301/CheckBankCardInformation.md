**Example 1: 银行卡基础信息查询成功示例**



Input: 

```
tccli faceid CheckBankCardInformation --cli-unfold-argument  \
    --BankCard 6225768888888888
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "查询成功",
        "AccountBank": "招商银行信用卡",
        "AccountType": 2,
        "RequestId": "8695c53f-776f-4ff5-a66d-84e67b352d20"
    }
}
```

**Example 2: 银行卡基础信息查询失败示例**



Input: 

```
tccli faceid CheckBankCardInformation --cli-unfold-argument  \
    --BankCard 6225768888888888
```

Output: 
```
{
    "Response": {
        "AccountBank": "",
        "AccountType": -1,
        "Description": "未查到信息",
        "RequestId": "bd41a241-0e50-4337-999e-0687d56a34c8",
        "Result": "-1"
    }
}
```

