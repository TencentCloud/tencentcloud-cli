**Example 1: 示例1**



Input: 

```
tccli csip DescribeIaCFileOverview --cli-unfold-argument  \
    --StartTime 2026-04-01T00:00:00+08:00 \
    --EndTime 2026-04-07T23:59:59+08:00 \
    --MemberId mem-a6df317cb6a8c424
```

Output: 
```
{
    "Response": {
        "RiskFile": [
            {
                "Key": 3,
                "Value": 90
            }
        ],
        "TotalFile": 92,
        "RequestId": "f7617bd3-6c2d-4ef2-8351-e4a2cd3c63d9"
    }
}
```

