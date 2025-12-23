**Example 1: 查余额用例返回验证**

查余额返回临时额度验证

Input: 

```
tccli billing DescribeAccountBalance --cli-unfold-argument  \
    --TempCredit True
```

Output: 
```
{
    "Response": {
        "Balance": 0,
        "CashAccountBalance": 0,
        "CreditAmount": 10000000000,
        "CreditBalance": 10000000000,
        "FreezeAmount": 0,
        "IncomeIntoAccountBalance": 0,
        "IsAllowArrears": true,
        "IsCreditLimited": true,
        "OweAmount": 0,
        "PresentAccountBalance": 0,
        "RealBalance": 0,
        "RealCreditBalance": 10000000000,
        "TempAmountInfoList": [
            {
                "EndTime": "2026-11-16 00:00:00",
                "StartTime": "2025-11-01 00:00:00",
                "TempAmount": 200000,
                "Uin": "600000561284"
            }
        ],
        "TempCredit": 0,
        "Uin": 600000561284,
        "RequestId": "8590441d-6e17-4afe-8ca4-f75cec86e290"
    }
}
```

