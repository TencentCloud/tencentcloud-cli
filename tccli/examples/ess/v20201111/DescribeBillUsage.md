**Example 1: 查询企业版合同套餐使用**



Input: 

```
tccli ess DescribeBillUsage --cli-unfold-argument  \
    --StartTime 20240901 \
    --EndTime 20240930 \
    --QuotaType CloudEnterprise
```

Output: 
```
{
    "Response": {
        "RequestId": "s1729129053894358080",
        "SubOrgSummary": [],
        "Summary": [
            {
                "Available": 9967,
                "QuotaType": "CloudEnterprise",
                "Total": 412505,
                "Used": 32
            }
        ]
    }
}
```

