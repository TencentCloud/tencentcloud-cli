**Example 1: 获取防护概览趋势图**



Input: 

```
tccli antiddos DescribeOverviewCCTrend --cli-unfold-argument  \
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
        "Count": 1,
        "Data": [
            1234
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

