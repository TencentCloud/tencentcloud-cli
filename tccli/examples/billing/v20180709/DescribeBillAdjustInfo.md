**Example 1: 获取账单异常调整信息**

根据月份获取账单异常调整信息

Input: 

```
tccli billing DescribeBillAdjustInfo --cli-unfold-argument  \
    --Month 2023-09
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AdjustAmount": 2346.28,
                "AdjustCompletionTime": "2024-10-21 17:50:46",
                "AdjustNum": "20230906159081",
                "AdjustType": "manualAdjustment",
                "Month": "2023-09",
                "PayerUin": "909619400"
            },
            {
                "AdjustAmount": 5318.81,
                "AdjustCompletionTime": "2024-10-21 17:44:14",
                "AdjustNum": "20230909111993",
                "AdjustType": "manualAdjustment",
                "Month": "2023-09",
                "PayerUin": "909619400"
            }
        ],
        "RequestId": "7fd119c4-8f8b-4355-b365-6df62b7d6660",
        "Total": 2
    }
}
```

