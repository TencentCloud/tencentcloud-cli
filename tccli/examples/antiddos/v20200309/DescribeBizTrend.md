**Example 1: 获取高防IP业务流量曲线**

获取高防IP业务流量曲线

Input: 

```
tccli antiddos DescribeBizTrend --cli-unfold-argument  \
    --Domain test.com \
    --Statistics avg \
    --Business bgpip \
    --ProtoInfo.0.Protocol TCP \
    --ProtoInfo.0.Port 1 \
    --Period 1 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id bgpip-00000001 \
    --BusinessType domain \
    --MetricName qps
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
        "MaxData": 236,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

