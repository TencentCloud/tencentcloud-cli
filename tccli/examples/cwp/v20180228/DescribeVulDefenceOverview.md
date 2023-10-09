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
            "DefendCounts": 0,
            "DefendHostCount": [
                0
            ],
            "ExceptionCount": [
                0
            ],
            "Date": [
                "xx"
            ],
            "AttackCounts": [
                0
            ]
        },
        "RequestId": "xx"
    }
}
```

