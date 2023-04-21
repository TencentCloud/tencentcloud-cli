**Example 1: 获取防护概览DDoS攻击流量带宽和攻击包速率数据**

当Business可以不传，统计所有Business为 基础防护 + 高防ip + 高防包 的和

Input: 

```
tccli antiddos DescribeOverviewDDoSTrend --cli-unfold-argument  \
    --Business bgp \
    --Period 0 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id bgp-00000001 \
    --MetricName bps
```

Output: 
```
{
    "Response": {
        "RequestId": "cb39db80-b483-4139-a00e-1177ed011579",
        "Count": 1,
        "Data": [
            12234
        ]
    }
}
```

