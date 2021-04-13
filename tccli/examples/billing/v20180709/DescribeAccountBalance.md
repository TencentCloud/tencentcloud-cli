**Example 1: 获取账户余额示例**



Input: 

```
tccli billing DescribeAccountBalance --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Uin": "90961",
        "RealBalance": 9647442,
        "CashAccountBalance": 1299806668,
        "IncomeIntoAccountBalance": 0,
        "PresentAccountBalance": 209512,
        "FreezeAmount": 1290368738,
        "OweAmount": 0,
        "RequestId": "1323",
        "IsAllowArrears": true,
        "IsCreditLimited": true,
        "Balance": -6188426,
        "CreditAmount": 200,
        "CreditBalance": -6188226,
        "RealCreditBalance": -6188226
    }
}
```

