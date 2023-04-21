**Example 1: 获取防护概览趋势图**

当Business可以不传，统计所有Business为 基础防护 + 高防ip + 高防包 的和

Input: 

```
tccli antiddos DescribeOverviewCCTrend --cli-unfold-argument  \
    --Period 0 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --MetricName bps
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Data": [
            1234
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

