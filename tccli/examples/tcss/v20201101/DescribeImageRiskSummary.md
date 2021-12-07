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
                "Level": "xx"
            }
        ],
        "VulnerabilityCnt": [
            {
                "Cnt": 1,
                "Level": "xx"
            }
        ],
        "RequestId": "xx",
        "MalwareVirusCnt": [
            {
                "Cnt": 1,
                "Level": "xx"
            }
        ]
    }
}
```

