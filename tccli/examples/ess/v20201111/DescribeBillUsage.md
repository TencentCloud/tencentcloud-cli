**Example 1: 查询企业版合同套餐使用**

获取指定企业套餐使用汇总信息

Input: 

```
tccli ess DescribeBillUsage --cli-unfold-argument  \
    --StartTime 20240901 \
    --EndTime 20240930 \
    --QuotaType CloudEnterprise \
    --Operator.UserId yDxoQxxxxxxxxxxxxxxxxxx1h2hnnR
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

