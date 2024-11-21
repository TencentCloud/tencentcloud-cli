**Example 1: 查询本地镜像风险概览**



Input: 

```
tccli tcss DescribeImageRiskSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RiskCnt": [
            {
                "Cnt": 1,
                "Level": "HIGH"
            }
        ],
        "VulnerabilityCnt": [
            {
                "Cnt": 1,
                "Level": "HIGH"
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
        "MalwareVirusCnt": [
            {
                "Cnt": 1,
                "Level": "HIGH"
            }
        ]
    }
}
```

