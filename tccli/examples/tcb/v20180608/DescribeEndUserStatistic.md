**Example 1: DescribeEndUserStatistic**



Input: 

```
tccli tcb DescribeEndUserStatistic --cli-unfold-argument  \
    --EnvId envid
```

Output: 
```
{
    "Response": {
        "TotalCount": 19800,
        "PlatformStatistics": [
            {
                "Platform": "WECHAT-OPEN",
                "Count": 9900,
                "UpdateTime": "2020-02-02 20:13:14"
            },
            {
                "Platform": "ANONYMOUS",
                "Count": 9900,
                "UpdateTime": "2020-02-02 20:13:14"
            }
        ],
        "RequestId": "046cacfd-af90-4355-ac92-f56954bd1831"
    }
}
```

