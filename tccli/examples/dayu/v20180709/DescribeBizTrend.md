**Example 1: 获取业务流量曲线**



Input: 

```
tccli dayu DescribeBizTrend --cli-unfold-argument  \
    --Domain xx \
    --Statistics xx \
    --Business xx \
    --ProtoInfo.0.Protocol xx \
    --ProtoInfo.0.Port 1 \
    --Period 1 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id xx \
    --MetricName xx
```

Output: 
```
{
    "Response": {
        "DataList": [
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236,
            236
        ],
        "MetricName": "intraffic",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

