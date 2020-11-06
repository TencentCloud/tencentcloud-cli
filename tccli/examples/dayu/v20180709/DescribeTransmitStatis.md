**Example 1: 获取业务转发统计数据**



Input: 

```
tccli dayu DescribeTransmitStatis --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000x7 \
    --Period 300 \
    --StartTime '2018-08-28 07:15:00' \
    --EndTime '2018-08-28 10:05:00' \
    --MetricName traffic
```

Output: 
```
{
    "Response": {
        "InDataList": [
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
        "OutDataList": [
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
        "MetricName": "traffic",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

