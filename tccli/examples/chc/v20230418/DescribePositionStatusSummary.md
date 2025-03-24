**Example 1: 获取机位数据汇总**



Input: 

```
tccli chc DescribePositionStatusSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "54c5a2de-513a-4d98-93c8-c0a682364495",
        "StatusCountSet": [
            {
                "Count": 7442,
                "PositionStatus": 0
            },
            {
                "Count": 29447,
                "PositionStatus": 1
            },
            {
                "Count": 313,
                "PositionStatus": 2
            },
            {
                "Count": 3,
                "PositionStatus": 3
            },
            {
                "Count": 0,
                "PositionStatus": 4
            }
        ],
        "Total": 37205
    }
}
```

