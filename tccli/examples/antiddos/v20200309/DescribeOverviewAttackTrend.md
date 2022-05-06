**Example 1: 拉取防护概览攻击趋势**



Input: 

```
tccli antiddos DescribeOverviewAttackTrend --cli-unfold-argument  \
    --Type ddos \
    --Dimension attackcount \
    --Period 86400 \
    --StartTime '2020-02-01 12:04:12' \
    --EndTime '2020-02-03 18:03:23'
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Type": "ddos",
        "StartTime": "2020-02-01 12:04:12",
        "EndTime": "2020-02-03 18:03:23",
        "Period": 86400,
        "Data": [
            0,
            0
        ],
        "Count": 2
    }
}
```

