**Example 1: 获取漏洞防御概览信息**



Input: 

```
tccli cwp DescribeVulDefenceOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Overview": {
            "Enable": 0,
            "DefendHostCount": 0,
            "ExceptionCount": 0,
            "AttackCounts": [
                0
            ],
            "DefendCounts": [
                0
            ],
            "Date": [
                "2020-10-01"
            ]
        },
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

