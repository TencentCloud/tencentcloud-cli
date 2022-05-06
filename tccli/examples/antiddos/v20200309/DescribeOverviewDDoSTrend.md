**Example 1: 获取防护概览DDoS攻击流量带宽和攻击包速率数据**



Input: 

```
tccli antiddos DescribeOverviewDDoSTrend --cli-unfold-argument  \
    --Business xx \
    --Period 0 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id xx \
    --MetricName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Count": 1,
        "Data": [
            1234
        ]
    }
}
```

