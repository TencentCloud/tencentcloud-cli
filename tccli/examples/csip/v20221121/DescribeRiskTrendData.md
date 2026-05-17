**Example 1: 查看风险趋势图**



Input: 

```
tccli csip DescribeRiskTrendData --cli-unfold-argument  \
    --LastDays 14
```

Output: 
```
{
    "Response": {
        "CosRiskTrendData": [
            {
                "CurrentDateStr": "2024-01-31",
                "RiskDataSet": [
                    {
                        "PolicyType": 1,
                        "PolicyTypeName": "公共读取权限风险",
                        "PolicyCount": 15
                    }
                ]
            }
        ],
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

